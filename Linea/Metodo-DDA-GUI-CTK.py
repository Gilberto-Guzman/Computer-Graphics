import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Establecer el modo de apariencia y el tema de color predeterminado
customtkinter.set_appearance_mode(
    "System"
)  # Modos: "System" (estándar), "Dark" (oscuro), "Light" (claro)
customtkinter.set_default_color_theme(
    "green"
)  # Temas: "blue" (estándar), "green" (verde), "dark-blue" (azul oscuro)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.title("Método DDA")
        self.geometry(f"{1100}x{580}")
        self.resizable(False, False)

        # Centrar la ventana en la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 1100) / 2)
        y = int((screen_height - 580) / 2)
        self.geometry(f"+{x}+{y}")

        # Crear etiqueta "Método DDA"
        self.label_metodo_dda = customtkinter.CTkLabel(
            master=self,
            text="Método DDA",
            font=customtkinter.CTkFont(size=36, weight="bold"),
            anchor="w",
        )
        self.label_metodo_dda.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew"
        )

        # Crear etiquetas y entradas para X1, X2, Y1, Y2
        self.label_x1 = customtkinter.CTkLabel(
            master=self,
            text="X1",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_x1.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_x1 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_x1.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.entry_x1.insert(0, "20")  # Establecer el valor inicial para X1

        self.label_x2 = customtkinter.CTkLabel(
            master=self,
            text="X2",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_x2.grid(row=3, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_x2 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_x2.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.entry_x2.insert(0, "60")  # Establecer el valor inicial para X2

        self.label_y1 = customtkinter.CTkLabel(
            master=self,
            text="Y1",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_y1.grid(row=1, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_y1 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_y1.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
        self.entry_y1.insert(0, "20")  # Establecer el valor inicial para Y1

        self.label_y2 = customtkinter.CTkLabel(
            master=self,
            text="Y2",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_y2.grid(row=3, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_y2 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_y2.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")
        self.entry_y2.insert(0, "50")  # Establecer el valor inicial para Y2

        # Crear botón "Mostrar"
        self.button_mostrar = customtkinter.CTkButton(
            self,
            text="Mostrar",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.funcion_mostrar,
        )
        self.button_mostrar.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

        # Crear botón "Limpiar"
        self.button_limpiar = customtkinter.CTkButton(
            self,
            text="Limpiar",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.funcion_limpiar,
        )
        self.button_limpiar.grid(row=5, column=1, padx=20, pady=10, sticky="nsew")

        # Crear tabla
        style = ttk.Style(self)
        style.configure("Treeview.Heading", font=("Arial", 16, "bold"))
        style.configure("Treeview", font=("Arial", 14))
        self.tabla_resultante = ttk.Treeview(self, columns=("X", "Y"), show="headings")
        self.tabla_resultante.heading("X", text="X")
        self.tabla_resultante.heading("Y", text="Y")
        self.tabla_resultante.grid(
            row=8, column=0, columnspan=2, padx=20, pady=10, sticky="nsew"
        )

        # Crear gráfico de resultados
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=7, rowspan=9)

    # Función para manejar el evento de clic del botón "Mostrar"
    def funcion_mostrar(self):
        # Obtener valores de las entradas
        X1 = float(self.entry_x1.get())
        Y1 = float(self.entry_y1.get())
        X2 = float(self.entry_x2.get())
        Y2 = float(self.entry_y2.get())

        if ((X2 - X1) != 0):
            M = round((Y2 - Y1) / (X2 - X1), 2)
            self.label_resultado_pendiente = customtkinter.CTkLabel(
                master=self,
                text=f"Valor de M = {M}",
                font=customtkinter.CTkFont(size=20, weight="bold"),
            )
            self.label_resultado_pendiente.grid(
                row=6, column=0, columnspan=2, padx=20, pady=0, sticky="nsew"
            )

            DX = abs(X1 - X2)
            DY = abs(Y1 - Y2)
            Numero_De_Pasos = int(max(DX, DY))
            Incremento_En_X = DX / Numero_De_Pasos
            Incremento_En_Y = DY / Numero_De_Pasos

            X = float(X1)
            Y = float(Y1)

            # Ajustar el incremento según el signo de la pendiente
            Incremento_En_X *= 1 if X2 >= X1 else -1
            Incremento_En_Y *= 1 if Y2 >= Y1 else -1
        else:
            self.label_resultado_pendiente = customtkinter.CTkLabel(
                master=self,
                text=f"Valor de M = Error",
                font=customtkinter.CTkFont(size=20, weight="bold"),
            )
            self.label_resultado_pendiente.grid(
                row=6, column=0, columnspan=2, padx=20, pady=0, sticky="nsew"
            )
            M = 0
            DX = 0
            DY = abs(Y1 - Y2)
            Numero_De_Pasos = int(max(DX, DY))
            Incremento_En_X = DX / Numero_De_Pasos
            Incremento_En_Y = DY / Numero_De_Pasos

            X = float(X1)
            Y = float(Y1)

            # Ajustar el incremento según el signo de la pendiente
            Incremento_En_X *= 1 if X2 >= X1 else -1
            Incremento_En_Y *= 1 if Y2 >= Y1 else -1

        direccion = ""
        if M == 0:
            direccion = "Línea horizontal"
        elif Y1 < Y2:
            direccion += "De arriba a abajo"
        elif Y1 > Y2:
            direccion += "De abajo a arriba"

        direccion += " y "

        if X1 < X2:
            direccion += "de izquierda a derecha"
        elif X1 > X2:
            direccion += "de derecha a izquierda"
        
        # Mostrar la dirección
        self.label_resultado_direccion = customtkinter.CTkLabel(
            master=self,
            text=direccion,
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_resultado_direccion.grid(
            row=7, column=0, columnspan=2, padx=20, pady=0, sticky="nsew"
        )

        Coordenadas_En_X = []
        Coordenadas_En_Y = []

        for i in range(Numero_De_Pasos):
            Coordenadas_En_X.append(round(X, 2))
            Coordenadas_En_Y.append(round(Y, 2))
            X = X + Incremento_En_X
            Y = Y + Incremento_En_Y

        # Limpiar la tabla
        self.tabla_resultante.delete(*self.tabla_resultante.get_children())

        # Insertar valores en la tabla
        for i in range(Numero_De_Pasos):
            self.tabla_resultante.insert(
                "", "end", values=(Coordenadas_En_X[i], Coordenadas_En_Y[i])
            )

        # Limpiar el gráfico
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=7, rowspan=9)

        # Graficar la línea en el gráfico
        ax.clear()
        ax.plot(
            [0],
            0,
            linestyle="-",
            color="white",
            marker="o",
            markersize=5,
            markerfacecolor="white",
        )
        ax.plot(
            Coordenadas_En_X,
            Coordenadas_En_Y,
            linestyle="-",
            color="blue",
            marker="o",
            markersize=5,
            markerfacecolor="red",
        )
        ax.plot(
            [60],
            60,
            linestyle="-",
            color="white",
            marker="o",
            markersize=5,
            markerfacecolor="white",
        )
        canvas.draw()

    # Función para manejar el evento de clic del botón "Limpiar"
    def funcion_limpiar(self):
        self.entry_x1.delete(0, tk.END)
        self.entry_x2.delete(0, tk.END)
        self.entry_y1.delete(0, tk.END)
        self.entry_y2.delete(0, tk.END)
        self.label_resultado_pendiente.destroy()
        self.label_resultado_direccion.destroy()
        self.tabla_resultante.delete(*self.tabla_resultante.get_children())
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=7, rowspan=9)


if __name__ == "__main__":
    app = App()
    app.mainloop()
