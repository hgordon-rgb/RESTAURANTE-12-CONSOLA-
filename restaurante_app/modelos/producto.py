class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ):
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        self.stock -= cantidad

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(datos):
        return Producto(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["stock"]
        )

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )