import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width="560px",
                width="100%",
                margin_y="2em",
                padding="2em",
                align_items="center",
            )
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)
