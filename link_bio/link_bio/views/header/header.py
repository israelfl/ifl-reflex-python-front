import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Brais Moure",
                    size="7",
                    src="/avatar.jpg",
                    radius="full",
                    color="#F1F2F4",
                    bg="#171F26",
                    padding="2px",
                    border=f"4px solid #14A1F0"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Brais Moure",
                    size="6"
                ),
                rx.text(
                    "@mouredev",
                    margin_top="0px !important",
                    color="#14A1F0"
                ),
                spacing="0px !important",
            ),
            align="end",
            spacing="0"
        ),
        width="100%",
        spacing="6",
        align_items="center"
    )
