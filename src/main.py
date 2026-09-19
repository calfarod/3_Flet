import flet as ft


def main(page: ft.Page):
    # Agregamos key="counter" para identificarlo unívocamente en las pruebas
    counter = ft.Text("0", size=50, data=0, key="counter")

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)
        page.update()  # Aseguramos la actualización de la página

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)