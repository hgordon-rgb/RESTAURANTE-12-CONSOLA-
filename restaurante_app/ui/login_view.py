import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):

    def __init__(self, master, on_login):
        super().__init__(master)

        self.on_login = on_login

        tk.Label(
            self,
            text="INICIO DE SESIÓN",
            font=("Arial", 28, "bold")
        ).pack(pady=40)

        tk.Label(self, 
                 text="Usuario",
                 font=("Arial", 14)
        ).pack(pady=10)

        self.txt_usuario = tk.Entry(
            self,
            font=("Arial", 14),
            width=30
        )            
        self.txt_usuario.pack(ipady=8)

        tk.Label(self, 
                text="Contraseña",
                font=("Arial", 14)
                ).pack(pady=10)

        self.txt_password = tk.Entry(
            self,
            font=("Arial", 14),
            width=30
        )
        self.txt_password.pack(ipady=8)

        tk.Button(
            self,
            text="Ingresar",
            font=("Arial", 14),
            width=15,
            height=2,
            command=self.validar
        ).pack(pady=10)

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