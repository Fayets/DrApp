import reflex as rx
import httpx
from datetime import date

class RegisterPatientState(rx.State):
    nombre: str = ""
    apellido: str = ""
    dni: str = ""
    fecha_nacimiento: str = ""
    obrasocial: str = ""
    medico_id: int = 0
    error_message: str = ""
    success_message: str = ""

    def set_nombre(self, value: str):
        self.nombre = value

    def set_apellido(self, value: str):
        self.apellido = value

    def set_dni(self, value: str):
        self.dni = value

    def set_fecha_nacimiento(self, value: str):  # Mantener como str para el input de tipo date
        self.fecha_nacimiento = value

    def set_obrasocial(self, value: str):
        self.obrasocial = value

    def set_medico_id(self, value: str):  # Cambiado a str para recibir del input
        self.medico_id = int(value) if value.isdigit() else 0  # Convertir a int si es válido

    async def registrar_paciente(self):
        url = "http://127.0.0.1:8002/paciente/create"  # Asegúrate que esta URL sea la correcta

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    json={
                        "nombre": self.nombre,
                        "apellido": self.apellido,
                        "dni": self.dni,
                        "fecha_nacimiento": self.fecha_nacimiento,
                        "obrasocial": self.obrasocial,
                        "medico_id": self.medico_id,
                    }
                )
                response.raise_for_status()  # Esto lanzará una excepción si hay un error en la respuesta
                self.success_message = "Paciente registrado exitosamente."
                self.error_message = ""
                # Limpiar campos después del registro exitoso
                self.nombre = ""
                self.apellido = ""
                self.dni = ""
                self.fecha_nacimiento = ""
                self.obrasocial = ""
                self.medico_id = 0

        except httpx.HTTPStatusError as e:
            self.error_message = f"Error al registrarse: {e.response.text}"
        except Exception as e:
            self.error_message = f"Ocurrió un error: {str(e)}"

@rx.page(route="/registrarpaciente", title="Registro de Paciente")
def registrar_paciente():
    return rx.box(
        rx.vstack(
            # Logo y título
            rx.image(src="/logo.png", width="70px", height="70px", mt="2vh"),
            rx.text("Registro de Paciente", color="#666", font_size="1rem", mb="2vh"),
            
            # Formulario
            rx.box(
                rx.hstack(
                    # Columna izquierda
                    rx.vstack(
                        rx.text("Nombre", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_nombre,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                        rx.text("Apellido", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_apellido,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                        rx.text("DNI", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_dni,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                    ),
                    # Columna derecha
                    rx.vstack(
                        rx.text("Fecha de Nacimiento", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            type_="date",
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_fecha_nacimiento,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                        rx.text("Médico a Cargo (ID)", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            type_="text",
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_medico_id,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                        rx.text("Obra Social", color="#333", font_size="0.8rem", align_self="center"),
                        rx.input(
                            border="none",
                            border_bottom="1px solid #ccc",
                            padding="0.5rem",
                            margin_bottom="1vh",
                            bg="white",
                            color="black",
                            on_change=RegisterPatientState.set_obrasocial,
                            _focus={"border_bottom": "2px solid #3182ce"},
                        ),
                        width="48%",
                        align_items="stretch",
                    ),
                    width="100%",
                    justify_content="space-between",
                    align_items="flex-center",
                ),
                rx.spacer("1"),
                rx.button(
                    "Registrar Paciente",
                    on_click=RegisterPatientState.registrar_paciente,
                    bg="#333",
                    color="white",
                    width="100%",
                    padding="0.5rem",
                    border_radius="0.3rem",
                    mt="2vh",
                    _hover={"bg": "#555"},
                    box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",
                ),
                padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.5)",
                border_radius="0.5rem",
                width="90%",
                max_width="600px",
                box_shadow="0 12px 24px rgba(0, 0, 0, 0.2)",
                bg="rgba(255, 255, 255, 0.3)",
                backdrop_filter="blur(10px)",
            ),
            # Mensaje de éxito
            rx.cond(
                RegisterPatientState.success_message != "",
                rx.text(RegisterPatientState.success_message, color="green", font_size="1rem"),
            ),
            # Mensaje de error
            rx.cond(
                RegisterPatientState.error_message != "",
                rx.text(RegisterPatientState.error_message, color="red", font_size="1rem"),
            ),
            spacing="0.5rem",
            width="100%",
            max_width="650px",
            justify_content="center",
            align_items="center",
        ),
        height="100vh",
        width="100%",
        bg="#F5F5DC",
        display="flex",
        justify_content="center",
        align_items="center",
    )

def index():
    return rx.center(
        registrar_paciente(),
        width="100%",
        height="100vh",
    )
