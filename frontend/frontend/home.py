import reflex as rx
import httpx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.button(
        rx.text(text, size="4", weight="medium"),
        href=url,
        variant="ghost",  # Modo ghost
        color="white",  # Color del texto
        size="md",  # Tamaño del botón
        padding="1rem",  # Espaciado interno
        _hover={
            "bg": "blue.500",  # Fondo en hover
            "color": "white",  # Color del texto en hover
            "transform": "translateY(-1px)",  # Efecto de elevación
            "box_shadow": "md",  # Sombra en hover
        },
        _active={
            "bg": "blue.600",  # Fondo en activo
            "color": "white",  # Color del texto en activo
        },
    )

class DeletePatientState(rx.State):
    dni: str = ""
    error_message: str = ""
    success_message: str = ""

    def set_dni(self, value: str):
        self.dni = value

    async def dni_delete(self):
        url = f"http://127.0.0.1:8002/paciente/delete/{self.dni}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url)
                response.raise_for_status()  # Lanza una excepción si la respuesta tiene un error
                self.success_message = "Paciente borrado exitosamente."
                self.error_message = ""
                self.dni = ""  # Limpiar campo DNI después del borrado exitoso

        except httpx.HTTPStatusError as e:
            self.error_message = f"Error al borrar el paciente: {e.response.text}"
        except Exception as e:
            self.error_message = f"Ocurrió un error: {str(e)}"

#---------------------------------------------------------------------------------------------------#

class State(rx.State):
    dni: str = ""
    error_message: str = ""
    success_message: str = ""
    patient_data: dict = None  # Estado para almacenar los datos del paciente

    def set_dni(self, value: str):
        self.dni = value

    def set_patient_data(self, data: dict):
        self.patient_data = data

    def set_success_message(self, message: str):
        self.success_message = message

    def set_error_message(self, message: str):
        self.error_message = message

    def buscar_historia_clinica(self):
        url = f"http://127.0.0.1:8002/historiaclinica/get/{self.dni}"
        try:
            with httpx.AsyncClient() as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                #HcViewState.set_patient_data(data)  # Actualiza el estado de HcView
                self.success_message = "Historia clínica obtenida exitosamente."
                self.error_message = ""
                return rx.redirect("/hcview")
        except httpx.HTTPStatusError as e:
            self.error_message = f"Error al obtener la historia clínica: {e.response.text}"
        except Exception as e:
            self.error_message = f"Ocurrió un error: {str(e)}"

@rx.page(route="/home", title="Bienvenidos!")
def home():
    return rx.box(
        # Encabezado con barra de navegación
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.image(src="/logo.png", width="50px", height="50px"),
                    rx.heading("DrApp", size="7", weight="bold"),
                    rx.hstack(
                        rx.menu.separator(),
                        navbar_link("INICIO", "/"),
                        navbar_link("PACIENTES", "/#"),
                        navbar_link("HISTORIAS CLINICAS", "/#"),
                        justify="center",
                        spacing="5",
                        width="75%",  # Ajusta este valor según sea necesario
                    ),
                    width="100%",
                    justify="space-between",
                    align_items="center",
                    padding_x="4",
                ),
            ),
            bg=rx.color("green", 2),
            padding="1em",
            width="100%",
        ),

        # Main Content
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.image(
                        src="/logo.png",
                        alt="DrApp Logo",
                        width="130px",
                        height="130px",
                    ),
                    rx.text(
                        "_________",
                        color="black",
                        text_decoration="underline",
                    ),
                    rx.spacer(height="1em"),
                    rx.heading(
                        "Bienvenido a DrApp",
                        size="xl",
                        color="black",
                        font_weight="bold",
                        margin_top="4",
                    ),
                    rx.text(
                        "Tu solución para el manejo eficiente de registros médicos.",
                        color="gray",
                        font_size="md",
                        text_align="center",
                        margin_top="4",
                        margin_bottom="6",
                    ),
                    rx.text(
                        "_________",
                        color="black",
                        text_decoration="underline",
                    ),
                    rx.spacer(1),
                    
                    # Contenedor para los botones
                    rx.vstack(
                        # Botones en la parte superior
                        rx.hstack(
                            rx.button(
                                "Registrar un Paciente",
                                on_click=lambda: rx.redirect("/registrarpaciente"),
                                bg="#17970d",
                                color="white",
                                size="lg",
                                width="200px",  # Ancho fijo
                                padding="1rem",
                                border_radius="md",
                                _hover={
                                    "bg": "blue.600",
                                    "transform": "translateY(-1px)",
                                    "box_shadow": "md",
                                },
                            ),
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button(
                                        "Borrar Paciente",
                                        bg="#970d0d",
                                        color="white", 
                                        size="lg",
                                        width="200px",
                                        padding="1rem",
                                        border_radius="md",
                                        _hover={
                                            "bg": "red.600",
                                            "transform": "translateY(-1px)", 
                                            "box_shadow": "md",
                                        },
                                    ),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Borrar"),
                                    rx.alert_dialog.description(
                                        "Ingrese el DNI del paciente a eliminar"
                                    ),
                                    rx.form.root(
                                        rx.input(
                                            placeholder="Ingrese DNI",
                                            name="dni",
                                            value=DeletePatientState.dni,  # Enlaza el valor del estado
                                            on_change=DeletePatientState.set_dni  # Actualiza el estado al escribir
                                        ),
                                        rx.flex(
                                            rx.alert_dialog.cancel(
                                                rx.button("Cancelar"),
                                            ),
                                            rx.alert_dialog.action(
                                                rx.button(
                                                    "Borrar", 
                                                    color_scheme="red", 
                                                    on_click=DeletePatientState.dni_delete  # Llama a la función de borrado
                                                ),
                                            ),
                                            spacing="3",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        
                        # Espaciado entre grupos de botones
                        rx.spacer(height="2em"),

                        # Botones en la parte inferior
                        rx.hstack(
                            rx.button(
                                "Registrar Historia Clinica",
                                bg="#2894d6 ",
                                on_click=lambda: rx.redirect("/hcform"),
                                color="white",
                                size="lg",
                                width="200px",  # Ancho fijo
                                padding="1rem",
                                border_radius="md",
                                _hover={
                                    "bg": "orange.600",
                                    "transform": "translateY(-1px)",
                                    "box_shadow": "md",
                                },
                           ),
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button(
                                        "Buscar Historia Clinica",
                                        bg="#d8d329",
                                        color="white",
                                        size="lg",
                                        width="200px",
                                        padding="1rem",
                                        border_radius="md",
                                        _hover={
                                            "bg": "orange.600",
                                            "transform": "translateY(-1px)",
                                            "box_shadow": "md",
                                        },
                                    ),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Buscar Historia Clinica"),
                                    rx.alert_dialog.description(
                                        "Ingrese el DNI del paciente"
                                    ),
                                    rx.form.root(
                                        rx.input(
                                            placeholder="Ingrese DNI",
                                            name="dni",
                                            value=State.dni,
                                            on_change=State.set_dni
                                        ),
                                        rx.flex(
                                            rx.alert_dialog.cancel(
                                                rx.button("Cancelar"),
                                            ),
                                            rx.alert_dialog.action(
                                                rx.button(
                                                    "Buscar",
                                                    color_scheme="green",
                                                    on_click=lambda: rx.redirect(f"/hclinica/{State.dni}"),
                                                ),
                                            ),
                                            spacing="3",
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        spacing="4",
                        align="center",
                    ),
                    
                    spacing="4",
                    align="center",
                    padding_y="12",
                ),
                bg="white",
                w="100%",
                max_width="800px",
                margin_x="auto",
                border_radius="lg",
                box_shadow="sm",
                height="auto",
                margin_y="auto",
                display="flex",
                align_items="center",
                justify_content="center",
            ),

            # Footer
            rx.box(
                rx.text(
                    "© 2024 DrApp. Todos los derechos reservados.",
                    bg="#",
                    color="#121B17",
                    font_size="sm",
                    text_align="center",
                ),
                padding_y="4",
                bg="white",
                border_top="1px solid",
                border_color="gray.200",
                w="100%",
                margin_top="auto",
            ),

            spacing="0",
            align="stretch",
            width="100%",
            height="87vh",
            bg="white",
            flex="1",
            display="flex",
            flex_direction="column",
            justify_content="space-between",
        ),
        width="100%",
        min_height="100vh",
        bg="white",
        position="relative",
        overflow_y="auto",
        overflow_x="hidden",
    )