import tkinter as tk
from tkinter import Text, Entry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Valores fijos para la gráfica
X1 = 20
Y1 = 20
X2 = 60
Y2 = 50


# Función para calcular la pendiente y mostrar la gráfica
def calcular_mostrar():
    # Obtener valores de las entradas
    global X1, X2, Y1, Y2
    X1 = float(entry_x1.get())
    Y1 = float(entry_y1.get())

    X2 = float(entry_x2.get())
    Y2 = float(entry_y2.get())

    # Calcular la pendiente
    M = round((Y2 - Y1) / (X2 - X1), 2)
    label_resultado.config(text=f"Valor de M = {M}")

    # Algoritmo DDA
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

    Coordenadas_En_X = []
    Coordenadas_En_Y = []

    for i in range(Numero_De_Pasos):
        Coordenadas_En_X.append(round(X, 2))
        Coordenadas_En_Y.append(round(Y, 2))
        X = X + Incremento_En_X
        Y = Y + Incremento_En_Y

    # Tabla de valores obtenidos
    tabla_resultado_x.delete(1.0, tk.END)
    tabla_resultado_y.delete(1.0, tk.END)
    tabla_resultado_x.insert(tk.END, "X\n")
    tabla_resultado_y.insert(tk.END, "Y\n")
    for i in range(Numero_De_Pasos):
        tabla_resultado_x.insert(tk.END, f"{Coordenadas_En_X[i]}\n")
        tabla_resultado_y.insert(tk.END, f"{Coordenadas_En_Y[i]}\n")

    # Determinar dirección de la pendiente
    direccion = determinar_direccion(M, X1, X2, Y1, Y2)
    entry_direccion.delete(0, tk.END)
    entry_direccion.insert(0, f"{direccion} con una pendiente de {M}")

    # Gráfica resultante
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


# Función para determinar la dirección de la pendiente
def determinar_direccion(pendiente, x1, x2, y1, y2):
    direccion = ""

    if pendiente == 0:
        direccion = "Línea horizontal"
    elif y1 < y2:
        direccion += "De arriba a abajo"
    elif y1 > y2:
        direccion += "De abajo a arriba"

    direccion += " y "

    if x1 < x2:
        direccion += "de izquierda a derecha"
    elif x1 > x2:
        direccion += "de derecha a izquierda"

    return direccion


# Función para limpiar las entradas y resultados
def limpiar_datos():
    entry_x1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_y1.delete(0, tk.END)
    entry_y2.delete(0, tk.END)
    label_resultado.config(text="Valor de M = ")
    entry_direccion.delete(0, tk.END)
    tabla_resultado_x.delete(1.0, tk.END)
    tabla_resultado_y.delete(1.0, tk.END)
    ax.clear()
    canvas.draw()


# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Pendiente y Gráfica")

# Crear widgets
label_o = tk.Label(root, text=" ")
label_x1 = tk.Label(root, text="X1:")
entry_x1 = tk.Entry(root)
label_y1 = tk.Label(root, text="Y1:")
entry_y1 = tk.Entry(root)
label_x2 = tk.Label(root, text="X2:")
entry_x2 = tk.Entry(root)
label_y2 = tk.Label(root, text="Y2:")
entry_y2 = tk.Entry(root)

button_mostrar = tk.Button(root, text="Mostrar", command=calcular_mostrar)
button_limpiar = tk.Button(root, text="Limpiar Datos", command=limpiar_datos)

label_resultado = tk.Label(root, text="Valor de M = ")
entry_direccion = Entry(root, width=60)  # Ajustar el ancho del cuadro de texto

label_TX = tk.Label(root, text="X")
label_TY = tk.Label(root, text="Y")

tabla_resultado_x = Text(root, height=10, width=10)
tabla_resultado_y = Text(root, height=10, width=10)

# Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Organizar widgets en la interfaz
label_o.grid(row=0, column=0, columnspan=2, pady=10)
label_x1.grid(row=1, column=0)
entry_x1.grid(row=1, column=1)
label_y1.grid(row=1, column=2)
entry_y1.grid(row=1, column=3)
label_x2.grid(row=2, column=0)
entry_x2.grid(row=2, column=1)
label_y2.grid(row=2, column=2)
entry_y2.grid(row=2, column=3)

button_mostrar.grid(row=3, column=0, columnspan=2, pady=10)
button_limpiar.grid(row=3, column=2, columnspan=2, pady=10)
label_resultado.grid(row=4, column=0, columnspan=2)
entry_direccion.grid(row=5, column=0, columnspan=4, pady=10)
label_TX.grid(row=6, column=0)
label_TY.grid(row=6, column=1)

tabla_resultado_x.grid(row=8, column=0, columnspan=2)
tabla_resultado_y.grid(row=8, column=2, columnspan=2)

canvas_widget.grid(row=0, column=7, rowspan=9)  # Se ajustó la columna aquí

# Establecer valores iniciales
entry_x1.insert(0, str(X1))
entry_y1.insert(0, str(Y1))
entry_x2.insert(0, str(X2))
entry_y2.insert(0, str(Y2))

# Ejecutar la interfaz
root.mainloop()
