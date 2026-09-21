import flet as ft


def main(page: ft.Page):
    page.title="Expand Proportional 1 3 1"
    page.add(
        ft.SafeArea(
            content=ft.Container(
                width=500,
                padding=10,
                border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                border_radius=10,
                # Usamos Column para apilar el Título y la Row verticalmente
                content=ft.Column(
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        # 1. Título principal
                        ft.Text(
                            "Mi Título Principal",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_GREY_500,
                        ),
                        # 2. Fila con los bloques proporcionales
                        ft.Row(
                            spacing=8,
                            controls=[
                                ft.Container(
                                    expand=1,
                                    height=60,
                                    bgcolor=ft.Colors.CYAN_300,
                                    alignment=ft.Alignment.CENTER,
                                    border_radius=8,
                                    content=ft.Text(
                                        "1",
                                        color=ft.Colors.GREY_700,
                                        size=20,
                                        weight=ft.FontWeight.BOLD),
                                ),
                                ft.Container(
                                    expand=3,
                                    height=60,
                                    bgcolor=ft.Colors.AMBER_300,
                                    alignment=ft.Alignment.CENTER,
                                    border_radius=8,
                                    content=ft.Text(
                                        "3",
                                        color=ft.Colors.GREY_800,
                                        size=20,
                                        weight=ft.FontWeight.BOLD),
                                ),
                                ft.Container(
                                    expand=1,
                                    height=60,
                                    bgcolor=ft.Colors.PINK_200,
                                    alignment=ft.Alignment.CENTER,
                                    border_radius=8,
                                    content=ft.Text(
                                        "1",
                                        color=ft.Colors.GREY_900,
                                        size=20,
                                        weight=ft.FontWeight.BOLD),
                                ),
                            ],
                        ),
                        # 1. Título principal
                        ft.Text(
                            "Mi Título secundario",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_GREY_500,
                        ),
                    ],
                ),
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)