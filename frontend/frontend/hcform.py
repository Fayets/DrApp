import reflex as rx

class FormState(rx.State):
    nombre: str = ""
    apellido: str = ""
    edad: str = ""
    dni: str = ""
    direccion: str = ""
    telefono: str = ""
    email: str = ""
    alergias: str = ""
    condiciones: str = ""
    observaciones: str = ""
    prescripciones_medicas: str = ""
    error_message: str = ""
    success_message: str = ""

    def set_nombre(self, value: str):
        self.nombre = value

    def set_apellido(self, value: str):
        self.apellido = value

    def set_edad(self, value: str):
        self.edad = value

    def set_dni(self, value: str):
        self.dni = value

    def set_direccion(self, value: str):
        self.direccion = value

    def set_telefono(self, value: str):
        self.telefono = value

    def set_email(self, value: str):
        self.email = value

    def set_alergias(self, value: str):
        self.alergias = value

    def set_condiciones(self, value: str):
        self.condiciones = value

    def set_observaciones(self, value: str):
        self.observaciones = value

    def set_prescripciones_medicas(self, value: str):
        self.prescripciones_medicas = value

class SelectState(rx.State):
    value: str = "apple"

    def change_value(self, value: str):
        """Change the select value var."""
        self.value = value
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

@rx.page(route="/hcform", title="Historia Clínica")
def form() -> rx.Component:
    return rx.box(
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
            
            
            bg=rx.color("green", 2),
            padding="1em",
            width="100%",
        ),
rx.box(
        # Contenedor exterior principal
        rx.box(
            # Título
            rx.text("Historia Clínica", font_size="2.5rem", font_weight="bold", color="#333", mt="1.5rem"),
            rx.spacer(1),
            # Cuadro del formulario
            rx.vstack(
                # Contenedor de datos personales
                rx.box(
                    rx.text("Asignar HC a Paciente", font_size="1", font_weight="bold", color="#333", mt="0.5rem"),
                    rx.text("DNI", color="#333", font_size="0.9rem"),
                    rx.input(
                        placeholder="Dni",
                        on_change=FormState.set_dni,
                        aling=("center"),
                        justify=("center"),
                        padding="0.5rem",
                        border_radius="0.3rem",
                        border="1px solid #ccc",
                        focus_border_color="#333",
                        background_color="#f9f9f9",
                        style={"color": "#000"}
                    ),
                    padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.3)",
                border_radius="0.5rem",
                width="18rem",
                box_shadow="0 12px 24px rgba(0, 0, 0, 0.2)",
                bg="rgba(255, 255, 255, 0.3)",
                mt="1.5rem",
                margin="auto",
                ),
                # Contenedor de condiciones y alergias
                rx.box(
                    rx.text("Alergias y Condiciones", font_size="1.5rem", font_weight="bold", color="#333", mt="0.5rem"),
                    rx.text("Alergias", color="#333", font_size="0.9rem"),
                    rx.input(
                        placeholder="Alergias",
                        on_change=FormState.set_alergias,
                        padding="0.5rem",
                        border_radius="0.3rem",
                        border="1px solid #ccc",
                        focus_border_color="#333",
                        background_color="#f9f9f9",
                        style={"color": "#000"}
                    ),
                    rx.text("Condiciones", color="#333", font_size="0.9rem", mt="0.5rem"),
                    rx.input(
                        placeholder="Condiciones",
                        on_change=FormState.set_condiciones,
                        padding="0.5rem",
                        border_radius="0.3rem",
                        border="1px solid #ccc",
                        focus_border_color="#333",
                        background_color="#f9f9f9",
                        style={"color": "#000"}
                    ),
                    rx.text("Observaciones", color="#333", font_size="0.9rem", mt="0.5rem"),
                    rx.input(
                        placeholder="Observaciones",
                        on_change=FormState.set_observaciones,
                        padding="0.5rem",
                        border_radius="0.3rem",
                        border="1px solid #ccc",
                        focus_border_color="#333",
                        background_color="#f9f9f9",
                        style={"color": "#000"}
                    ),
                    rx.text("Prescripciones Médicas", color="#333", font_size="0.9rem", mt="0.5rem"),
                    rx.input(
                        placeholder="Prescripciones Médicas",
                        on_change=FormState.set_prescripciones_medicas,
                        padding="0.5rem",
                        border_radius="0.3rem",
                        border="1px solid #ccc",
                        focus_border_color="#333",
                        background_color="#f9f9f9",
                        style={"color": "#000"}
                    ),
                    padding="1rem",
                    border="1px solid rgba(128, 128, 128, 0.5)",
                    border_radius="0.5rem",
                    bg="rgba(255, 255, 255, 0.3)",
                ),
                rx.button(
                "Enviar",
                type="submit",
                   
                   bg="#333",
                   color="white",
                   width="100%",
                   padding="0.5rem",
                   border_radius="0.3rem",
                   mt="1rem",
                   _hover={"bg": "#555"},
                   box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",
                #on_click=submit_form,
            ),
                # Espaciado
                rx.spacer(1),
                padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.3)",
                border_radius="0.5rem",
                width="22rem",
                box_shadow="0 12px 24px rgba(0, 0, 0, 0.2)",
                bg="rgba(255, 255, 255, 0.3)",
                mt="1.5rem",
                margin="auto",
                
            ),
            
            direction="column",
            align_items="center",
            justify_content="center",
            gap="1.5rem",
            text_align="center",
            border="1px solid rgba(128, 128, 128, 0.2)",
            border_radius="0.5rem",
            padding="2rem",
            bg="#f4f4f4",
        ),
        # Contenedor para el botón y el mensaje de error
                   
            direction="row",
            align_items="center",
            justify_content="center",
            margin="auto",  # Centrando el contenido
            gap="0.5rem",  # Espacio entre el mensaje y el botón
            padding="1rem",
        )
        
    
    ),