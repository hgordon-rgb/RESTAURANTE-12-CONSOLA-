import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        on_logout
    ):
        super().__init__(master)

        self.restaurante = restaurante_servicio
        self.on_logout = on_logout

        self.archivo = ArchivoServicio(
            "datos/productos.json"
        )

        titulo = ttk.Label(
            self,
            text="SISTEMA RESTAURANTE",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=10)

        # =========================
        # FORMULARIO PRODUCTOS
        # =========================

        frame_formulario = ttk.LabelFrame(
            self,
            text="Gestión de Productos"
        )

        frame_formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            frame_formulario,
            text="Código:"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.codigo_entry = ttk.Entry(
            frame_formulario
        )
        self.codigo_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Nombre:"
        ).grid(row=1, column=0)

        self.nombre_entry = ttk.Entry(
            frame_formulario
        )
        self.nombre_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Categoría:"
        ).grid(row=2, column=0)

        self.categoria_entry = ttk.Entry(
            frame_formulario
        )
        self.categoria_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Precio:"
        ).grid(row=3, column=0)

        self.precio_entry = ttk.Entry(
            frame_formulario
        )
        self.precio_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_formulario,
            text="Stock:"
        ).grid(row=4, column=0)

        self.stock_entry = ttk.Entry(
            frame_formulario
        )
        self.stock_entry.grid(
            row=4,
            column=1,
            padx=5,
            pady=5
        )

        # =========================
        # BOTONES
        # =========================

        frame_botones = ttk.Frame(
            frame_formulario
        )

        frame_botones.grid(
            row=5,
            column=0,
            columnspan=4,
            pady=10
        )

        ttk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Buscar",
            command=self.buscar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=5
        )

        # =========================
        # PRODUCTOS
        # =========================

        frame_productos = ttk.LabelFrame(
            self,
            text="Productos Registrados"
        )

        frame_productos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        scrollbar = ttk.Scrollbar(
            frame_productos,
            orient="vertical"
        )

        self.tabla_productos = ttk.Treeview(
            frame_productos,
            columns=(
                "codigo",
                "nombre",
                "categoria",
                "precio",
                "stock"
            ),
            show="headings",
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(
            command=self.tabla_productos.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.pack(
            fill="both",
            expand=True
        )

        # =========================
        # USUARIOS
        # =========================

        frame_usuarios = ttk.LabelFrame(
            self,
            text="Usuarios"
        )

        frame_usuarios.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        self.tabla_usuarios = ttk.Treeview(
            frame_usuarios,
            columns=(
                "id",
                "nombre",
                "correo",
                "rol"
            ),
            show="headings",
            height=5
        )

        self.tabla_usuarios.heading(
            "id",
            text="Identificación"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.heading(
            "correo",
            text="Correo"
        )

        self.tabla_usuarios.heading(
            "rol",
            text="Rol"
        )
        
        self.tabla_usuarios.column(
            "id",
            width=120
        )
        
        self.tabla_usuarios.column(

            "nombre",
            width=180
        )
        
        self.tabla_usuarios.column(

            "correo",
            width=220
        )
        
        self.tabla_usuarios.column(
            "rol",
            width=120
        )
 

        self.tabla_usuarios.pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            self,
            text="Cerrar Sesión",
            command=self.on_logout
        ).pack(
            pady=10
        )

        self.cargar_productos()
        self.cargar_usuarios()

    # ==================================
    # UTILIDADES
    # ==================================

    def limpiar_campos(self):

        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.categoria_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)



    # ==================================
    # CARGAR TABLAS
    # ==================================

    def cargar_productos(self):

                for item in self.tabla_productos.get_children():
                    self.tabla_productos.delete(item)

                for producto in self.restaurante.productos:

                    self.tabla_productos.insert(
                        "",
                        tk.END,
                        values=(
                            producto.codigo,
                            producto.nombre,
                            producto.categoria,
                            producto.precio,
                            producto.stock
                        )
                    )

    def cargar_usuarios(self):

                for item in self.tabla_usuarios.get_children():
                    self.tabla_usuarios.delete(item)

                for usuario in self.restaurante.usuarios:

                    self.tabla_usuarios.insert(
                        "",
                        tk.END,
                        values=(
                            usuario.identificacion,
                            usuario.nombre,
                            usuario.correo,
                            usuario.rol
                        )
                )

        
# ==================================
# CRUD USUARIOS
# ==================================

    def registrar_usuario(self):

            from modelos.usuario import Usuario

            usuario = Usuario(
                self.id_usuario.get(),
                self.nombre_usuario.get(),
                self.correo_usuario.get(),
                self.cmb_rol.get()
            )

            if self.restaurante.registrar_usuario(
                usuario
            ):

                self.archivo.guardar_usuarios(
                    self.restaurante.usuarios
                )

                self.cargar_usuarios()
                self.limpiar_usuario()

                messagebox.showinfo(
                    "Correcto",
                    "Usuario registrado."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "La identificación ya existe."
                )


    def actualizar_usuario(self):

            actualizado = self.restaurante.actualizar_usuario(
                self.id_usuario.get(),
                self.nombre_usuario.get(),
                self.correo_usuario.get(),
                self.cmb_rol.get()
            )

            if actualizado:

                self.archivo.guardar_usuarios(
                    self.restaurante.usuarios
                )

                self.cargar_usuarios()

                messagebox.showinfo(
                    "Correcto",
                    "Usuario actualizado."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Usuario no encontrado."
                )


    def eliminar_usuario(self):

            eliminado = self.restaurante.eliminar_usuario(
                self.id_usuario.get()
            )

            if eliminado:

                self.archivo.guardar_usuarios(
                    self.restaurante.usuarios
                )

                self.cargar_usuarios()
                self.limpiar_usuario()

                messagebox.showinfo(
                    "Correcto",
                    "Usuario eliminado."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Usuario no encontrado."
                )


# ==================================
# EVENTOS USUARIOS
# ==================================

    def cambio_rol(self, event):

        print(
            "Rol:",
            self.cmb_rol.get()
        )


    def enter_usuario(self, event):

        self.registrar_usuario()


    def limpiar_usuario(self, event=None):

        self.id_usuario.delete(
            0,
            tk.END
        )

        self.nombre_usuario.delete(
            0,
            tk.END
        )

        self.correo_usuario.delete(
            0,
            tk.END
        )

        self.cmb_rol.set("")

        if hasattr(
            self,
            "tabla_usuarios"
        ):

            for item in self.tabla_usuarios.selection():

                self.tabla_usuarios.selection_remove(
                    item
                )


    def cargar_usuario(self, event):

        seleccion = self.tabla_usuarios.selection()

        if not seleccion:
            return

        item = self.tabla_usuarios.item(
            seleccion[0]
        )

        self.id_usuario.delete(0, tk.END)
        self.id_usuario.insert(
            0,
            item["values"][0]
        )

        self.nombre_usuario.delete(0, tk.END)
        self.nombre_usuario.insert(
            0,
            item["values"][1]
        )

        self.correo_usuario.delete(0, tk.END)
        self.correo_usuario.insert(
            0,
            item["values"][2]
        )

        self.cmb_rol.set(
            item["values"][3]
        )
        

    # ==================================
    # CRUD PRODUCTOS
    # ==================================

    def registrar_producto(self):

        try:

            producto = Producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                float(self.precio_entry.get()),
                int(self.stock_entry.get())
            )

            if self.restaurante.registrar_producto(
                producto
            ):

                self.archivo.guardar_productos(
                    self.restaurante.productos
                )

                self.cargar_productos()
                self.limpiar_campos()

                messagebox.showinfo(
                    "Éxito",
                    "Producto registrado correctamente."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Código duplicado."
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def buscar_producto(self):

        producto = self.restaurante.buscar_producto(
            self.codigo_entry.get()
        )

        if producto:

            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(
                0,
                producto.nombre
            )

            self.categoria_entry.delete(0, tk.END)
            self.categoria_entry.insert(
                0,
                producto.categoria
            )

            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(
                0,
                producto.precio
            )

            self.stock_entry.delete(0, tk.END)
            self.stock_entry.insert(
                0,
                producto.stock
            )

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

    def actualizar_producto(self):

        try:

            actualizado = self.restaurante.actualizar_producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                float(self.precio_entry.get()),
                int(self.stock_entry.get())
            )

            if actualizado:

                self.archivo.guardar_productos(
                    self.restaurante.productos
                )

                self.cargar_productos()

                messagebox.showinfo(
                    "Correcto",
                    "Producto actualizado."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Producto no encontrado."
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def eliminar_producto(self):

        eliminado = self.restaurante.eliminar_producto(
            self.codigo_entry.get()
        )

        if eliminado:

            self.archivo.guardar_productos(
                self.restaurante.productos
            )

            self.cargar_productos()
            self.limpiar_campos()

            messagebox.showinfo(
                "Correcto",
                "Producto eliminado."
            )

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )