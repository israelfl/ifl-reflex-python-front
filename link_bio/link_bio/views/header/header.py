import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
      rx.avatar(fallback="Ifl Developer", size="xl"),
      rx.text("@ifldeveloper"),
      rx.text("HOLA MI NOMBRE ES ISRAEL FALCÓN")
    )