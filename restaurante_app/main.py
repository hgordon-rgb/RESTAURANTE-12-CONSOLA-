import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class App:

    def __init__(self, root):

        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("1400x900")

        archivo = ArchivoServicio("datos/productos.json")

        self.restaurante = RestauranteServicio()

        # Cargar datos
        self.restaurante.productos = archivo.cargar_productos()
        self.restaurante.usuarios = archivo.cargar_usuarios()

        print("Productos cargados:", len(self.restaurante.productos))
        print("Usuarios cargados:", len(self.restaurante.usuarios))

        self.restaurante.reconstruir_indices()

        self.frame_actual = None

        self.mostrar_login()

    def limpiar(self):
        if self.frame_actual:
            self.frame_actual.destroy()

    def mostrar_login(self):

        self.limpiar()

        self.frame_actual = LoginView(
            self.root,
            self.mostrar_main
        )

        self.frame_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_main(self):

        self.limpiar()

        self.frame_actual = MainView(
            self.root,
            self.restaurante,
            self.mostrar_login
        )

        self.frame_actual.pack(
            fill="both",
            expand=True
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()