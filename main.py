import tkinter as tk
from tkinter import ttk
import pandas as pd

def leer_datos_desde_excel():
    # Leer el archivo Excel
    df = pd.read_excel('datasetalimentos.xlsx')

    # Eliminar la columna 'Unnamed: 0'
    df = df.drop(columns=['Unnamed: 0'])

    # Crear un diccionario para guardar los datos
    diccionario = {}

    # Rellenar el diccionario con los datos del DataFrame
    for idx, row in df.iterrows():
        if idx < 2:
            # Clave como string para las dos primeras filas
            clave = str(row[0])
        else:
            # Clave como número sucesivo para las filas restantes
            clave = idx - 1

        diccionario[clave] = row.tolist()

    return diccionario

def crear_tabla(datos):
    root = tk.Tk()
    root.title("Tabla de datos")

    tabla = ttk.Treeview(root)
    tabla["columns"] = list(datos.keys())

    # Configurar encabezados de columna
    for columna in tabla["columns"]:
        tabla.heading(columna, text=columna)

    # Agregar filas de datos
    for clave, fila in datos.items():
        tabla.insert("", "end", text=clave, values=fila)

    tabla.pack()

    # Funciones para los botones
    def accion_boton1():
        print("Se presionó el Botón 1")

    def accion_boton2():
        print("Se presionó el Botón 2")

    def accion_boton3():
        print("Se presionó el Botón 3")

    # Frame para los botones
    frame_botones = tk.Frame(root)
    frame_botones.pack()

    # Botones
    boton1 = tk.Button(frame_botones, text="Botón 1", command=accion_boton1)
    boton1.pack(side="left")

    boton2 = tk.Button(frame_botones, text="Botón 2", command=accion_boton2)
    boton2.pack(side="left")

    boton3 = tk.Button(frame_botones, text="Botón 3", command=accion_boton3)
    boton3.pack(side="left")

    root.mainloop()

# Leer datos desde el archivo Excel
datos_excel = leer_datos_desde_excel()

# Crear la tabla con los datos leídos y los botones
crear_tabla(datos_excel)
