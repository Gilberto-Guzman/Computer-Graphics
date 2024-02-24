import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Set appearance mode and default color theme
customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "green"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Método DDA")
        self.geometry(f"{1100}x{580}")
        self.resizable(False, False)

        # Center window on screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 1100) / 2)
        y = int((screen_height - 580) / 2)
        self.geometry(f"+{x}+{y}")

        # Create labels and entries for X1, X2, Y1, Y2
        self.label_x1 = customtkinter.CTkLabel(
            master=self,
            text="X1",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_x1.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_x1 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_x1.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.entry_x1.insert(0, "20")  # Set initial value for X1

        self.label_x2 = customtkinter.CTkLabel(
            master=self,
            text="X2",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_x2.grid(row=3, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_x2 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_x2.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.entry_x2.insert(0, "60")  # Set initial value for X2

        self.label_y1 = customtkinter.CTkLabel(
            master=self,
            text="Y1",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_y1.grid(row=1, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_y1 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_y1.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
        self.entry_y1.insert(0, "20")  # Set initial value for Y1

        self.label_y2 = customtkinter.CTkLabel(
            master=self,
            text="Y2",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            anchor="w",
        )
        self.label_y2.grid(row=3, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_y2 = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry_y2.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")
        self.entry_y2.insert(0, "50")  # Set initial value for Y2

        # Create "Mostrar" button
        self.button_mostrar = customtkinter.CTkButton(
            self,
            text="Mostrar",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.funcion_mostrar,
        )
        self.button_mostrar.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

        # Create "Limpiar" button
        self.button_limpiar = customtkinter.CTkButton(
            self,
            text="Limpiar",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.funcion_limpiar,
        )
        self.button_limpiar.grid(row=5, column=1, padx=20, pady=10, sticky="nsew")

        # Create table
        style = ttk.Style(self)
        style.configure("Treeview.Heading", font=("Arial", 16, "bold"))
        style.configure("Treeview", font=("Arial", 14))
        self.tabla_resultante = ttk.Treeview(self, columns=("X", "Y"), show="headings")
        self.tabla_resultante.heading("X", text="X")
        self.tabla_resultante.heading("Y", text="Y")
        self.tabla_resultante.grid(
            row=8, column=0, columnspan=2, padx=20, pady=10, sticky="nsew"
        )

        # Create result graph
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=7, rowspan=9)

    # Function to handle "Mostrar" button click event
    def funcion_mostrar(self):
        # Get values from entries
        X1 = float(self.entry_x1.get())
        Y1 = float(self.entry_y1.get())
        X2 = float(self.entry_x2.get())
        Y2 = float(self.entry_y2.get())

        # Calculate slope
        M = round((Y2 - Y1) / (X2 - X1), 2)

        # Display slope value
        self.label_resultado = customtkinter.CTkLabel(
            master=self,
            text=f"Valor de M = {M}",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_resultado.grid(
            row=6, column=0, columnspan=2, padx=20, pady=0, sticky="nsew"
        )

        # Determine direction
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

        # Display direction
        self.label_resultado = customtkinter.CTkLabel(
            master=self,
            text=direccion,
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_resultado.grid(
            row=7, column=0, columnspan=2, padx=20, pady=0, sticky="nsew"
        )

        # Calculate coordinates using DDA algorithm
        DX = abs(X1 - X2)
        DY = abs(Y1 - Y2)
        Numero_De_Pasos = int(max(DX, DY))
        Incremento_En_X = DX / Numero_De_Pasos
        Incremento_En_Y = DY / Numero_De_Pasos

        X = float(X1)
        Y = float(Y1)

        Incremento_En_X *= 1 if X2 >= X1 else -1
        Incremento_En_Y *= 1 if Y2 >= Y1 else -1

        Coordenadas_En_X = []
        Coordenadas_En_Y = []

        for i in range(Numero_De_Pasos):
            Coordenadas_En_X.append(round(X, 2))
            Coordenadas_En_Y.append(round(Y, 2))
            X = X + Incremento_En_X
            Y = Y + Incremento_En_Y

        # Clear the table
        self.tabla_resultante.delete(*self.tabla_resultante.get_children())

        # Insert values into the table
        for i in range(Numero_De_Pasos):
            self.tabla_resultante.insert(
                "", "end", values=(Coordenadas_En_X[i], Coordenadas_En_Y[i])
            )

        # Clear the graph
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=7, rowspan=9)

        # Plot the line on the graph
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

    # Function to handle "Limpiar" button click event
    def funcion_limpiar(self):
        self.entry_x1.delete(0, tk.END)
        self.entry_x2.delete(0, tk.END)
        self.entry_y1.delete(0, tk.END)
        self.entry_y2.delete(0, tk.END)
        self.label_resultado.destroy()
        self.tabla_resultante.delete(*self.tabla_resultante.get_children())


if __name__ == "__main__":
    app = App()
    app.mainloop()
