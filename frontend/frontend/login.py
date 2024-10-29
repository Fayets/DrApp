import reflex as rx

class LoginState(rx.State):
    username: str = ""
    password: str = ""
    error_message: str = ""

@rx.page(route="/", title="Inicio de Sesión")
def login() -> rx.Component:
    return rx.box(
        # Contenedor exterior principal
        rx.box(
            # Logo y título
            rx.flex(
                rx.image(src="/logo.png", width="50px", height="50px"),
                justify_content="center",
                align_items="center",
                display="flex",
            ),
            rx.box(
                rx.text("Drapp", font_size="2.8rem", font_weight="bold", color="#333", mt="1.5rem"),
                rx.text("Gestión de Historias Clínicas", color="#666", font_size="1.0rem", mt="0.25rem", mb="5rem"),
                padding="1rem",
                direction="column",
                align_items="center",
                justify_content="center",
            ),
            # Cuadro de credenciales
            rx.box(
                rx.text("Correo electrónico", color="#333", font_size="0.9rem"),
                rx.input(
                    placeholder="Correo electrónico",
                    on_change=LoginState.set_username,
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
                    on_change=LoginState.set_password,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.spacer(1),
                rx.button(
                    "Iniciar sesión",
                    type="submit",
                   # on_click=LoginState.verificar,
                    bg="#333",
                    color="white",
                    width="100%",
                    padding="0.5rem",
                    border_radius="0.3rem",
                    mt="1rem",
                    _hover={"bg": "#555"},
                    box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",  # Aumentar sombra del botón
                ),
                rx.spacer(1),
                rx.button(
                    "Registrate",
                    type="submit",
                    on_click=rx.redirect("/register"),
                    bg="#333",
                    color="white",
                    width="100%",
                    padding="0.5rem",
                    border_radius="0.3rem",
                    mt="1rem",
                    _hover={"bg": "#555"},
                    box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",  # Aumentar sombra del botón
                ),
                # Mensaje de error
                rx.cond(LoginState.error_message != "", 
                        rx.text(LoginState.error_message, color="red", mt="0.5rem")),
                padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.5)",
                border_radius="0.5rem",
                width="22rem",
                box_shadow="0 12px 24px rgba(0, 0, 0, 0.2)",  # Aumentar sombra del cuadro de credenciales
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