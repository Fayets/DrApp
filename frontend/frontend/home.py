import reflex as rx

@rx.page(route="/home", title="Bienvenidos!")
def home():
    return rx.box(
        rx.vstack(
            # Navegación
            rx.box(
                rx.hstack(
                    rx.link("Inicio", href="/home", color="gray.700", _hover={"color": "blue.500", "text_decoration": "none"}),
                    rx.link("Pacientes", href="/pacientes", color="gray.700", _hover={"color": "blue.500", "text_decoration": "none"}),
                    rx.link("Reportes", href="/reportes", color="gray.700", _hover={"color": "blue.500", "text_decoration": "none"}),
                    rx.link("Contacto", href="/contacto", color="gray.700", _hover={"color": "blue.500", "text_decoration": "none"}),
                    spacing="2em",
                    align="center",
                    justify="center",
                ),
                bg="white",
                w="100%",
                p="4",
                size="2",
                border_bottom="1px solid",
                border_color="white",
                position="sticky",
                top="0",
                z_index="1",
            ),

            # Contenido principal con mejor espaciado
            rx.box(
                rx.vstack(
                    rx.image(
                        src="/logo.png",
                        alt="DrApp Logo",
                        width="150px",
                        height="150px",
                    ),
                    rx.spacer(1),
                    rx.heading(
                        "Bienvenido a DrApp",
                        size="xl",
                        color="black",
                        weight="bold",
                        #font_weight="semibold",
                        mt="4",
                    ),
                    rx.text(
                        "Tu solución para el manejo eficiente de registros médicos.",
                        color="gray",
                        font_size="md",
                        text_align="center",
                        mt="4",
                        mb="6",
                    ),
                    rx.button(
                        "Registrar un Paciente",
                        bg="#333",
                        color="white",
                        size="lg",
                        px="8",
                        py="4",
                        border_radius="md",
                        _hover={
                            "bg": "blue.600",
                            "transform": "translateY(-1px)",
                            "shadow": "md",
                        },
                        mt="4",
                    ),
                    spacing="4",
                    align="center",
                    py="12",
                ),
                bg="white",
                w="100%",
                max_w="800px",
                mx="auto",
                border_radius="lg",
                shadow="sm",
                height="auto",
                my="auto",
                display="flex",
                align_items="center",
                justify_content="center",
            ),

            # Footer
            rx.box(
                rx.text(
                    "© 2024 DrApp. Todos los derechos reservados.",
                    color="#333",
                    size="3",
                    text_align="center",
                ),
                py="4",
                bg="white",
                border_top="1px solid",
                border_color="white",
                w="100%",
                mt="auto",  # Empuja el footer hacia abajo
            ),

            spacing="0",
            align="stretch",
            w="100%",
            height="100vh",
            bg="white",
            flex="1",
            display="flex",
            flex_direction="column",
            justify_content="space-between",
        ),
        w="100%",
        min_h="100vh",
        bg="white",
        position="relative",
        overflow_y="auto",
        overflow_x="hidden",
    )