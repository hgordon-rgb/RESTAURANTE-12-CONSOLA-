from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self):

        self.productos = []
        self.usuarios = []

        self.indice_productos = {}
        self.indice_usuarios = {}

        self.codigos_productos = set()

    def reconstruir_indices(self):

        self.indice_productos = {}
        self.indice_usuarios = {}

        self.codigos_productos = set()

        for producto in self.productos:

            self.indice_productos[
                producto.codigo
            ] = producto

            self.codigos_productos.add(
                producto.codigo
            )

        for usuario in self.usuarios:

            self.indice_usuarios[
                usuario.identificacion
            ] = usuario

    # ==================================
    # PRODUCTOS
    # ==================================

    def registrar_producto(self, producto):

        if producto.codigo in self.codigos_productos:
            return False

        self.productos.append(producto)

        self.indice_productos[
            producto.codigo
        ] = producto

        self.codigos_productos.add(
            producto.codigo
        )

        return True

    def buscar_producto(self, codigo):

        return self.indice_productos.get(
            codigo
        )

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):

        producto = self.buscar_producto(
            codigo
        )

        if producto:

            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            producto.stock = stock

            return True

        return False

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(
            codigo
        )

        if producto:

            self.productos.remove(producto)

            del self.indice_productos[
                codigo
            ]

            self.codigos_productos.remove(
                codigo
            )

            return True

        return False

    def listar_productos(self):

        return self.productos

    # ==================================
    # USUARIOS
    # ==================================

    def listar_usuarios(self):

        return self.usuarios

    def registrar_usuario(self, usuario):

        if usuario.identificacion in self.indice_usuarios:
            return False

        self.usuarios.append(usuario)

        self.indice_usuarios[
            usuario.identificacion
        ] = usuario

        return True

    def buscar_usuario(
        self,
        identificacion
    ):

        return self.indice_usuarios.get(
            identificacion
        )

    def actualizar_usuario(
        self,
        identificacion,
        nombre,
        correo,
        rol
    ):

        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario:

            usuario.nombre = nombre
            usuario.correo = correo
            usuario.rol = rol

            return True

        return False

    def eliminar_usuario(
        self,
        identificacion
    ):

        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario:

            self.usuarios.remove(usuario)

            del self.indice_usuarios[
                identificacion
            ]

            return True

        return False