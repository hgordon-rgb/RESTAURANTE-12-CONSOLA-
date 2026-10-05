# Sistema Restaurante – Semana 16

## Autor

Gordon Ortega Henri Daniel

---

# Descripción del Proyecto

Sistema desarrollado en Python utilizando Programación Orientada a Objetos (POO), persistencia de datos mediante archivos JSON e interfaz gráfica desarrollada con Tkinter.

La aplicación permite administrar productos y usuarios mediante operaciones CRUD, almacenar información de forma permanente en archivos JSON y utilizar eventos gráficos para mejorar la interacción con el usuario.

---

# Objetivo de la Semana 16

Implementar una gestión completa de usuarios utilizando eventos de Tkinter, manteniendo la arquitectura modular del proyecto y utilizando persistencia de datos mediante archivos JSON.

---

# Tecnologías Utilizadas

- Python 3
- Tkinter
- ttk
- JSON
- Programación Orientada a Objetos
- Pillow (Procesamiento de imágenes)
- Listas
- Diccionarios
- Conjuntos

---

# Estructura del Proyecto

```text
restaurante_app/
│
├── assets/
│   ├── logo.png
│   ├── usuario.png
│   └── contraseña.png
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
