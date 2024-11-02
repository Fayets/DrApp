import reflex as rx

def titulo():
    return rx.heading("Historia Clínica", size="9", color="green", text_align="center", text_justify="center",margin_bottom="2em")

def datos_paciente():
    return rx.card(
        rx.vstack(
            rx.heading("Datos del Paciente", size="7", color="green", margin_bottom="1em", text_align="center"),
            patient_info("Nombre", "Facundo"),
            patient_info("Apellido", "Folledo"),
            patient_info("Fecha de Nacimiento", "2002-06-11"),
            patient_info("Documento", "44200029"),
            patient_info("Obra Social", "OSDE"),
            spacing="1em",
        ),
        padding="1.5em",
        color=("black"),
        bg="white",
        border="1px solid",
        border_color="green",
        border_radius="lg",
        box_shadow="md",
        width="100%",
        max_width="18rem",
    )

def patient_info(label, value):
    return rx.vstack(
        rx.text(label, size="6", font_weight="medium", color="green"),
        rx.text(value, color="black"),
        align_items="start",
        spacing="0.25em",
    )

def seccion_derecha(titulo, contenido):
    return rx.card(
        rx.vstack(
            rx.heading(titulo, size="lg", color="green", margin_bottom="0.5em"),
            rx.text(contenido, color="black"),
            align_items="start",
        ),
        padding="1em",
        bg="white",
        border="1px solid",
        border_color="green",
        border_radius="lg",
        box_shadow="sm",
        _hover={"box_shadow": "md"},
        transition="box-shadow 0.3s",
        width="100%",
    )

@rx.page(route="/hclinica/44200029", title="Historia Clínica")
def historia_clinica2():
    return rx.center(
        rx.card(
            rx.vstack(
                titulo(),
                rx.hstack(
                    datos_paciente(),
                    rx.vstack(
                        seccion_derecha("Alergias", "Alergia al Polvo"),
                        seccion_derecha("Condiciones", "Arritmia, Problema Cardiaco"),
                        seccion_derecha("Observaciones", "Paciente Inestable, presenta ritmo cardiaco bajo"),
                        seccion_derecha("Prescripciones", "Amiodarona 500mg"),
                        spacing="1.5em",
                        width="100%",
                    ),
                    spacing="2em",
                    align_items="flex-start",
                    width="100%",
                ),
                spacing="0.1em",
            ),
            padding="2em",
            bg="white",
            border_radius="lg",
            box_shadow="lg",
            width="100%",
            max_width="4xl",
        ),
        padding="1em",
        min_height="100vh",
        bg="gray.50",
    )