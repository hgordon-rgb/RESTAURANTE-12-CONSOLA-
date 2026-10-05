import json

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(self, productos):

        try:
            datos = [
                producto.to_dict()
                for producto in productos
            ]

            with open(
                "datos/productos.json",
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:

            print(
                "No existen permisos para escribir el archivo."
            )

    def cargar_productos(self):

        try:

            with open(
                "datos/productos.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for item in datos:

                try:
                    producto = Producto.from_dict(item)
                    productos.append(producto)

                except KeyError:
                    print(
                        "Registro incompleto encontrado."
                    )

                except ValueError:
                    print(
                        "Registro inválido encontrado."
                    )

            return productos

        except FileNotFoundError:

            print(
                "Archivo no encontrado. Se inicia con lista vacía."
            )

            return []

        except json.JSONDecodeError:
            return []

    def guardar_usuarios(self, usuarios):

        try:

            datos = [
                usuario.to_dict()
                for usuario in usuarios
            ]

            with open(
                "datos/usuarios.json",
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:

            print(
                "No existen permisos para escribir usuarios."
            )

    def cargar_usuarios(self):

        try:

            with open(
                "datos/usuarios.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios = []

            for item in datos:

                try:
                    usuarios.append(
                        Usuario.from_dict(item)
                    )

                except KeyError:
                    print(
                        "Usuario incompleto encontrado."
                    )

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []