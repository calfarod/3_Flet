import flet as ft  # 1. Asegurar la importación al inicio


def main(page: ft.Page):
    page.title = "Visualizador de Paletas Flet"
    page.scroll = ft.ScrollMode.AUTO

    palettes = [
        "RED",
        "PINK",
        "PURPLE",
        "DEEP_PURPLE",
        "INDIGO",
        "BLUE",
        "LIGHT_BLUE",
        "CYAN",
        "TEAL",
        "GREEN",
        "LIGHT_GREEN",
        "LIME",
        "YELLOW",
        "AMBER",
        "ORANGE",
        "DEEP_ORANGE",
        "BROWN",
        "BLUE_GREY",
        "GREY",
        "BLUE",
    ]

    shades = [
        "50",
        "100",
        "150",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "A100",
        "A200",
        "A400",
        "A700",
        "A800",
        "A900",
    ]

    grid_palette = ft.GridView(
        max_extent=160,
        child_aspect_ratio=2.5,
        spacing=8,
        run_spacing=8,
    )

    def load_palette(palette_name: str):
        grid_palette.controls.clear()

        base_color_val = getattr(ft.Colors, palette_name, None)
        if base_color_val:
            grid_palette.controls.append(
                ft.Container(
                    content=ft.Text(
                        f"{palette_name} (Base)",
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor=base_color_val,
                    alignment=ft.Alignment(0, 0),
                    border_radius=8,
                    padding=5,
                )
            )

        for shade in shades:
            full_name = f"{palette_name}_{shade}"
            color_val = getattr(ft.Colors, full_name, None)

            if color_val:
                text_color = (
                    ft.Colors.BLACK
                    if shade in ["50", "100", "200", "A100"]
                    else ft.Colors.WHITE
                )

                grid_palette.controls.append(
                    ft.Container(
                        content=ft.Text(
                            full_name,
                            color=text_color,
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor=color_val,
                        alignment=ft.Alignment(0, 0),
                        border_radius=8,
                        padding=5,
                    )
                )

    def on_palette_change(e):
        selected_palette = dropdown.value
        load_palette(selected_palette)
        page.update()

    # 2. El Dropdown DEBE declararse dentro de main()
    dropdown = ft.Dropdown(
        label="Selecciona una paleta de color",
        value="BLUE_GREY",
        options=[ft.dropdown.Option(p) for p in palettes],
        on_select=on_palette_change,
        width=300,
    )

    load_palette("BLUE_GREY")

    page.add(
        ft.Text(
            "Explorador de Paletas de Color",
            size=22,
            weight=ft.FontWeight.BOLD,
        ),
        dropdown,
        ft.Divider(height=20, thickness=1),
        grid_palette,
    )


if __name__ == "__main__":
    ft.run(main)