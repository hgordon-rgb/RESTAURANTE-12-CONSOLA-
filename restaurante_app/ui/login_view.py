import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginView(tk.Frame):

    def __init__(self, master, on_login):
        super().__init__(master)

        self.on_login = on_login

        # ==================================
        # CONTENEDOR CENTRADO
        # ==================================

        contenedor = tk.Frame(self)
        contenedor.place(
            relx=0.5,
            rely=0.45,
            anchor="center"
        )

        # ==================================
        # LOGO
        # ==================================

        imagen_logo = Image.open(
            "assets/logo.png"
        )

        imagen_logo = imagen_logo.resize(
            (300, 200)
        )

        self.logo = ImageTk.PhotoImage(
            imagen_logo
        )

        tk.Label(
            contenedor,
            image=self.logo
        ).pack(pady=10)

        # ==================================
        # TITULO
        # ==================================

        tk.Label(
            contenedor,
            text="INICIO DE SESIÓN",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        # ==================================
        # ICONO USUARIO
        # ==================================

        imagen_usuario = Image.open(
            "assets/usuario.png"
        )

        imagen_usuario = imagen_usuario.resize(
            (32, 32)
        )

        self.icono_usuario = ImageTk.PhotoImage(
            imagen_usuario
        )

        frame_usuario = tk.Frame(
            contenedor
        )

        frame_usuario.pack(
            pady=5
        )

        tk.Label(
            frame_usuario,
            image=self.icono_usuario
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            frame_usuario,
            text="Usuario",
            font=("Arial", 14)
        ).pack(side="left")

        self.txt_usuario = tk.Entry(
            contenedor,
            font=("Arial", 14),
            width=30
        )

        self.txt_usuario.pack(
            ipady=8,
            pady=5
        )

        # ==================================
        # ICONO CONTRASEÑA
        # ==================================

        imagen_password = Image.open(
            "assets/contraseña.png"
        )

        imagen_password = imagen_password.resize(
            (32, 32)
        )

        self.icono_password = ImageTk.PhotoImage(
            imagen_password
        )

        frame_password = tk.Frame(
            contenedor
        )

        frame_password.pack(
            pady=5
        )

        tk.Label(
            frame_password,
            image=self.icono_password
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            frame_password,
            text="Contraseña",
            font=("Arial", 14)
        ).pack(side="left")

        self.txt_password = tk.Entry(
            contenedor,
            show="*",
            font=("Arial", 14),
            width=30
        )

        self.txt_password.pack(
            ipady=8,
            pady=5
        )

        # ==================================
        # BOTÓN INGRESAR
        # ==================================

        tk.Button(
            contenedor,
            text="Ingresar",
            font=("Arial", 14, "bold"),
            width=15,
            height=2,
            bg="#1976D2",
            fg="white",
            command=self.validar
        ).pack(
            pady=20
        )

    def validar(self):

        usuario = self.txt_usuario.get()
        password = self.txt_password.get()

        if usuario == "admin" and password == "1234":

            self.on_login()

        else:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )