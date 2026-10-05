class Usuario:

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        rol
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(datos):
        return Usuario(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"],
            datos.get("rol", "Cliente")
        )