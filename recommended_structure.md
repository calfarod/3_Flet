# Estructura Recomendada

3 Flet/
├── .gitignore
├── recommended_structure.md        # Árbol organizador de archivos
├── pyproject.toml
├── README.md
└── src/
    ├── __init__.py
    ├── main.py                     # Selector o menú principal para lanzar las apps
    ├── assets/                     # Recursos compartidos (imágenes, fuentes, iconos)
    │   └── icon.png
    ├── shared/                     # Componentes y estilos reutilizables
    │   ├── __init__.py
    ├── app_01_contador/            # Practica 1: Conceptos básicos
    │   ├── __init__.py
    │   └── app.py
    ├── app_02_todo_list/           # Práctica 2: Listas y estado
    │   ├── __init__.py
    │   └── app.py
    └── app_03_dashboard/           # Práctica 3: Layouts avanzados
        ├── __init__.py
        ├── app.py
        └── components/