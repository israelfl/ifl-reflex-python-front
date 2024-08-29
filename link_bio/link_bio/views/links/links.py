import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://google.es"),
        link_button("Youtube", "https://google.es"),
        width="100%",
        align_items="center",
    )
