import flet as ft

def main(page: ft.Page):
    page.title = "Carta de Colores Flet"
    page.scroll = ft.ScrollMode.AUTO

    # Lista de nombres de colores
    color_names = [
        "RED", "PINK", "PURPLE", "DEEP_PURPLE", "INDIGO", "BLUE",
        "LIGHT_BLUE", "CYAN", "TEAL", "GREEN", "LIGHT_GREEN", "LIME",
        "YELLOW", "AMBER", "ORANGE", "DEEP_ORANGE", "BROWN", "BLUE_GREY"
    ]

    grid = ft.GridView(expand=True, max_extent=160, child_aspect_ratio=2.5)

    for name in color_names:
        # Obtiene la constante dinámicamente
        color_val = getattr(ft.Colors, name)
        grid.controls.append(
            ft.Container(
                content=ft.Text(name, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                bgcolor=color_val,
                alignment=ft.Alignment(0, 0),
                border_radius=8,
                padding=5,
            )
        )

    page.add(
        ft.Text("Muestra de Colores Material", size=20, weight=ft.FontWeight.BOLD),
        grid
    )

if __name__ == "__main__":
    ft.run(main)