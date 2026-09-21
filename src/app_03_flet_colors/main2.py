import flet as ft


def main(page: ft.Page):
    page.title = "Comparador: Roles de Tema vs. Sombras (Shades)"
    page.scroll = ft.ScrollMode.AUTO
    # Tema inicial
    page.theme_mode = ft.ThemeMode.LIGHT

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
        "GREY",
        "BLUE_GREY",
    ]

    shades = [
        "50",
        "100",
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
    ]

    semantic_roles = [
        "PRIMARY",
        "ON_PRIMARY",
        "SECONDARY",
        "ON_SECONDARY",
        "TERTIARY",
        "ON_TERTIARY",
        "SURFACE",
        "ON_SURFACE",
        "ERROR",
        "ON_ERROR",
    ]

    # Contenedores para la grilla de comparación
    grid_semantic = ft.GridView(
        max_extent=160, child_aspect_ratio=2.2, spacing=8, run_spacing=8
    )
    grid_shades = ft.GridView(
        max_extent=160, child_aspect_ratio=2.2, spacing=8, run_spacing=8
    )

    def load_comparison(palette_name: str):
        grid_semantic.controls.clear()
        grid_shades.controls.clear()

        # 1. Columna/Sección de Roles Semánticos del Tema
        for role in semantic_roles:
            color_val = getattr(ft.Colors, role, None)
            if color_val:
                text_color = (
                    ft.Colors.WHITE if "ON_" not in role else ft.Colors.BLACK
                )
                grid_semantic.controls.append(
                    ft.Container(
                        content=ft.Text(
                            role,
                            color=text_color,
                            weight=ft.FontWeight.BOLD,
                            size=11,
                        ),
                        bgcolor=color_val,
                        alignment=ft.Alignment(0, 0),
                        border_radius=8,
                        padding=5,
                        border=ft.Border.all(
                            width=1, color=ft.Colors.OUTLINE_VARIANT
                        ),
                    )
                )

        # 2. Columna/Sección de Sombras (50 a 900)
        for shade in shades:
            full_name = f"{palette_name}_{shade}"
            color_val = getattr(ft.Colors, full_name, None)

            if color_val:
                text_color = (
                    ft.Colors.BLACK
                    if shade in ["50", "100", "200", "A100"]
                    else ft.Colors.WHITE
                )

                grid_shades.controls.append(
                    ft.Container(
                        content=ft.Text(
                            f"{shade}",
                            color=text_color,
                            weight=ft.FontWeight.BOLD,
                            size=12,
                        ),
                        bgcolor=color_val,
                        alignment=ft.Alignment(0, 0),
                        border_radius=8,
                        padding=5,
                    )
                )

    def on_palette_change(e):
        load_comparison(dropdown.value)
        page.update()

    # Función para alternar entre tema Claro y Oscuro
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_btn.icon = ft.Icons.DARK_MODE
            theme_btn.tooltip = "Cambiar a modo claro"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_btn.icon = ft.Icons.LIGHT_MODE
            theme_btn.tooltip = "Cambiar a modo oscuro"
        page.update()

    theme_btn = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        tooltip="Cambiar a modo oscuro",
        on_click=toggle_theme,
    )

    dropdown = ft.Dropdown(
        label="Selecciona paleta base (ej. PINK)",
        value="PINK",
        options=[ft.dropdown.Option(p) for p in palettes],
        on_select=on_palette_change,
        width=300,
    )

    load_comparison("PINK")

    page.add(
        ft.Row(
            [
                ft.Text(
                    "Comparador de Tema Semántico vs. Sombras Material",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                theme_btn,
            ],
            # Corregido: SPACE_BETWEEN en lugar de BETWEEN
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        dropdown,
        ft.Divider(height=20, thickness=1),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Roles de Tema (Global)",
                            weight=ft.FontWeight.BOLD,
                            size=16,
                        ),
                        grid_semantic,
                    ],
                    expand=True,
                ),
                ft.VerticalDivider(width=20),
                ft.Column(
                    [
                        ft.Text(
                            "Sombras de la Paleta (50-900)",
                            weight=ft.FontWeight.BOLD,
                            size=16,
                        ),
                        grid_shades,
                    ],
                    expand=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )


if __name__ == "__main__":
    ft.run(main)