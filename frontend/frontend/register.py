import reflex as rx
import httpx

class RegisterState(rx.State):
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    dni: str = ""
    esp: str = ""
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""

    async def registrar(self):
        # Validar que las contraseñas coincidan
        if self.password != self.confirm_password:
            self.error_message = "Las contraseñas no coinciden."
            return
        
        # URL del backend
        url = "http://localhost:8001/register"  # Cambia esto según tu configuración

        # Hacer la solicitud POST
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={
                        "nombre": self.nombre,
                        "apellido": self.apellido,
                        "email": self.email,
                        "dni": self.dni,
                        "especialidad": self.esp,
                        "password": self.password,
                    }
                )
                response.raise_for_status()  # Lanza un error si la respuesta es un error
                # Redirigir al inicio de sesión si el registro es exitoso
                rx.redirect("/login")
            except httpx.HTTPStatusError as e:
                # Manejo de errores específico basado en el código de estado HTTP
                self.error_message = f"Error al registrarse: {e.response.text}"
            except Exception as e:
                # Manejo de errores generales
                self.error_message = f"Ocurrió un error: {str(e)}"

app = rx.App()

@rx.page(route="/register", title="Registro")
def register() -> rx.Component:
    return rx.box(
        # Contenedor exterior principal
        rx.box(
            # Título
            rx.text("Bienvenido!", font_size="2.8rem", font_weight="bold", color="#333", mt="1.5rem"),
            rx.spacer(1),
            # Cuadro de registro
            rx.box(
                rx.text("Nombre", color="#333", font_size="0.9rem"),
                rx.input(
                    placeholder="Nombre",
                    on_change=RegisterState.set_nombre,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Apellido", color="#333", font_size="0.9rem"),
                rx.input(
                    placeholder="Apellido",
                    on_change=RegisterState.set_apellido,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Correo electrónico", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    placeholder="Correo electrónico",
                    on_change=RegisterState.set_email,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("DNI", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    placeholder="DNI",
                    on_change=RegisterState.set_dni,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Especialidad", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    placeholder="Especialidad",
                    on_change=RegisterState.set_esp,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Contraseña", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    type="password",
                    placeholder="Contraseña",
                    on_change=RegisterState.set_password,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Confirmar Contraseña", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    type="password",
                    placeholder="Confirmar Contraseña",
                    on_change=RegisterState.set_confirm_password,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.spacer(1),
                rx.button(
                    "Registrar",
                    on_click=RegisterState.registrar,
                    bg="#333",
                    color="white",
                    width="100%",
                    padding="0.5rem",
                    border_radius="0.3rem",
                    mt="1rem",
                    _hover={"bg": "#555"},
                    box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",
                ),
                # Mensaje de error
                rx.cond(RegisterState.error_message != "", 
                        rx.text(RegisterState.error_message, color="red", mt="0.5rem")),
                padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.5)",
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
            border="1px solid rgba(128, 128, 128, 0.3)",
            border_radius="0.5rem",
            bg="rgba(128, 128, 128, 0.1)",
            width="30rem",
            padding="2rem",
        ),
        height="100vh",
        justify_content="center",
        align_items="center",
        display="flex",
        bg="#F5F5DC",
    )

if __name__ == "__main__":
    app.run()
