import flet as ft


def main(page: ft.Page):
    page.title = "Mi Chat App"
    page.window.width = 600
    page.window.height = 800
    page.theme_mode = ft.ThemeMode.DARK # SYSTEM DARK LIGHT
    page.bgcolor = ft.Colors.DEEP_ORANGE
    page.padding = 30
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Campo de texto para ingresar el nombre
    name_input = ft.TextField(
        hint_text="Enter your name",
        expand=True,
        # 1. Color del texto que escribe el usuario
        color=ft.Colors.WHITE,
        # 2. Color de fondo del campo de texto
        bgcolor=ft.Colors.BLUE_GREY_900,
        # 3. (Opcional) Color del texto de pista/placeholder
        hint_style=ft.TextStyle(color=ft.Colors.GREY_400),
        # 4. (Opcional) Color del borde al seleccionar
        border=ft.Border.all(2, ft.Colors.BLUE_400),
    )

    # Función que se ejecuta al presionar el botón
    def join_chat_click(e):
        name = name_input.value.strip() if name_input.value else ""     # Recibe la entrada del TextField name_input

        # Validación simple
        if not name:
            name_input.error_text = "Please enter a valid name"
            page.update()
            return

        # Si pasa la validación, limpiamos el mensaje de error previo
        name_input.error_text = None
        page.update()

        # Limpiamos la pantalla actual
        page.clean()

        # Mostramos la nueva pantalla de bienvenida/chat
        page.add(
            ft.SafeArea(
                content=ft.Container(
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                    border=ft.Border.all(2, ft.Colors.BLUE_400),
                    # La Column va DENTRO del Container
                    content=ft.Column(
                        controls=[
                            ft.Text(f"Welcome to the chat, {name}!", size=24, weight=ft.FontWeight.BOLD),
                            ft.Text("Chat interface goes here..."),
                        ]
                    ),
                )
            )
        )

    # Botón configurado con el evento on_click
    join_button = ft.Button("Join chat", on_click=join_chat_click)

    # Vista inicial
    page.add(
        ft.SafeArea(
            content=ft.Container(
                margin=ft.Margin(left=20, top=10, right=20, bottom=10),
                width=480,
                height=400,
                padding=20,
                bgcolor=ft.Colors.PURPLE,
                border=ft.Border.all(width=2, color=ft.Colors.LIME),
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.BLACK_54,  # Nota: Es BLACK54 sin guion bajo entre BLACK y 54
                    offset=ft.Offset(0, 4),
                ),
                # Usamos Column para apilar el título arriba y los controles abajo
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente el contenido dentro de la caja
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente
                    spacing=20,  # Espacio de 20px entre el título y la fila
                    controls=[
                        # 1. El nuevo texto del título
                        ft.Text(
                            "Título de la App",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                            margin=ft.Margin(left=20, top=0, right=20, bottom=30),
                        ),
                        # 2. La fila con el campo de texto y el botón
                        ft.Row(
                            controls=[
                                name_input,
                                join_button,
                            ]
                        ),
                    ],
                ),
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)