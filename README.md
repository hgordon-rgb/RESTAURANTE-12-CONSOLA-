# RESTAURANTE-12-CONSOLA-

# Sistema Restaurante – Semana 16

## Autor

Gordon Ortega Henri Daniel

---

## Descripción General

Aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO), persistencia de datos mediante archivos JSON e interfaz gráfica con Tkinter.

El sistema permite realizar el inicio de sesión, gestionar productos y usuarios mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar), almacenar información de manera permanente en archivos JSON y administrar usuarios según roles definidos.

---

## Tecnologías Utilizadas

- Python 3
- Tkinter
- ttk
- JSON
- Programación Orientada a Objetos (POO)
- Colecciones de Python
  - Listas
  - Diccionarios
  - Conjuntos

---

## Estructura del Proyecto

```text
restaurante_app/
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
├── assets/
│   ├── logo.png
│   └── icono.ico
│
└── main.py
