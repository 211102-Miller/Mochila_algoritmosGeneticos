from xml.dom.xmlbuilder import DOMBuilderFilter
from tabulate import tabulate
from email import iterators
import itertools
from pickletools import read_uint1
import random
import re
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


"""diccionario = {
    '#': ['manzana',3,50,60],                           
    1 : ['manzana',3,50,60],
    2 : ['chocolate',40,0,50],
    3 : ['cocacola',120,597,60],
    4 : ['gancito',3,50,60],
    5 : ['limonada',15,599,600],
    6 : ['limonada',15,599,600],
    7 : ['limonada',15,599,600],

}
print(diccionario)"""


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
print(diccionario)

"""limite_mochila = 1250
cantidad_iteraciones = 5
posiblidad_cruza = 10
posibiliada_muta_individuo = 30
posivilidad_mutacion_gen = 2
limite_poblacion = 9

energia_requerido = 800 
protenia_requerido = 600
grasa_requerido = 100
calcio_requerido = 1000
hierro_requerido = 20
vitaminaA_requerido = 300
tiamina_requerido = 10
riboflavina_requerido = 10
niacina_requerido = 20
foloto_requerido= 120
vitamicaC_requerido = 70"""





#Parametros que se usaran
def main(cantidad_iteraciones, diccionario,posiblidad_cruza,posibiliada_mutacion_individuo,posivilidad_mutacion_gen,energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,limite_poblacion,Cantidad_individuos):
    
    resultado_menores= []
    resultado_mayores= []
    resultado_promedio = []


    #Genera las combinaciones que digita el usuario
    def combinaciones_posibles(diccionario):
            #id = list(diccionario) #Se obtienen los id del diccionario
        id = [clave for clave in diccionario if isinstance(clave, int)]
        resultado_combinaciones = []
        for i in range(Cantidad_individuos):
            muestra = random.sample(id,len(id))
            resultado_combinaciones.append(tuple(muestra))
        return resultado_combinaciones
    resultado_combinaciones = combinaciones_posibles(diccionario)
    print(resultado_combinaciones)

    #cantidad de generacions que se haran(iteraciones)
    for i in range(cantidad_iteraciones):
        
        #Genera todas las combinaciones posibles
        """def combinaciones_posibles(diccionario):
            id = list(diccionario) #Se obtienen los id del diccionario
            combinaciones = list(itertools.permutations(id))
            return combinaciones
        resultado_combinaciones = combinaciones_posibles(diccionario)
        print(resultado_combinaciones)"""

        print("a",resultado_combinaciones)

        #Emparejamiento de las comninaciones(parejas)
        def emparejamiento_poblacion (resultado_combinacione,):
            parejas_generadas = [] # Arreglo donde se guardaran todas las parejas generadas
            parejas_generadas  = list(itertools.combinations(resultado_combinacione,2))
            return parejas_generadas
        resutado_emparejamiento = emparejamiento_poblacion(resultado_combinaciones)
        #print("Combinacion: ",resutado_emparejamiento)
        #print(" ")

        #Parejas que cumplen con la posibilidad de cruza
        def posivili_mutacion_individuo(resutado_emparejamiento,posiblidad_cruza):
            aux_parejas =[]
            for parejas in resutado_emparejamiento:
                randow_cruza = random.randrange(0,50)
                if (randow_cruza <= posiblidad_cruza):
                    aux_parejas.append(parejas)
            return aux_parejas
        resultado_individuo = posivili_mutacion_individuo(resutado_emparejamiento,posiblidad_cruza)
        #print("parejas que cumplieron",resultado_individuo)
        #print(" ")

        #Cruza por pareja
        def cruza_metodo_puntofijo(individuo1, individuo2):
            punto_fijo = random.randint(1,len(individuo1)) # se genera el punto para hacer la cruza
            decendencia = [] #Arrelgo con los nuevos datos

            decendencia.append(individuo1[:punto_fijo] + individuo2[punto_fijo:]) 
            decendencia.append(individuo2[:punto_fijo] + individuo1[punto_fijo:])
            return tuple(decendencia)

        resultado_cruce = [elemento for individuo in resultado_individuo for elemento in cruza_metodo_puntofijo(individuo[0], individuo[1])] #se hace for para dividir las parejas
        #print("Cruza",resultado_cruce)
        #print(" ")

        #Reparacion de la cruza
        def reparamiento_cruza (resultado_cruce, diccionario):
            id = [clave for clave in diccionario if isinstance(clave, int)]
            ids = list(id)
            resultado_reparamiento= []

            for elemento in resultado_cruce:
                resultados_cruce = list(elemento)
                for i in range(len(resultados_cruce)-1,-1,-1):
                    if resultados_cruce[i] in resultados_cruce[:i] or resultados_cruce[i] in resultados_cruce[i+1:]:
                        for elemento in ids:
                            if elemento not in resultados_cruce:
                                resultados_cruce[i] = elemento
                                break
                resultado_reparamiento.append(tuple(resultados_cruce))
            return resultado_reparamiento
        resultado_reparamiento_cruza = reparamiento_cruza(resultado_cruce,diccionario)
        #print("Cruza reparada",resultado_reparamiento_cruza)
        #print(" ")

        #Se saca la posibilidad del individuo que tiene para mutar
        def posibilidad_muta_individuo(resultado_reparamiento_cruza,posibiliada_mutacion_individuo):
            aux_mutacion_individuo = []
            for individuo in resultado_reparamiento_cruza:
                randow_individuo = random.randrange(0, 50)
                if randow_individuo <= posibiliada_mutacion_individuo:
                    individuo_lista = list(individuo)
                    # Realizar las modificaciones necesarias en la lista individuo_lista
                    # ...
                    individuo_tupla = tuple(individuo_lista)
                    aux_mutacion_individuo.append(individuo_tupla)
            return aux_mutacion_individuo
        resultado_mutacion_individuo = posibilidad_muta_individuo(resultado_reparamiento_cruza,posibiliada_mutacion_individuo)
        #print("individuos mutacion individuo",resultado_mutacion_individuo)
        #print(" ")
        

        #Posilibidad de mutacion del gen y si cumple con la condicion se hace el metodo de cambio de posicion
        def posbilidad_gen_cambio_posicion (resultado_mutacion_individuo,posivilidad_mutacion_gen):
            for subarreglo in resultado_mutacion_individuo:
                subarreglo_lista = list(subarreglo)  # Convertir la tupla en una lista mutable
                for i in range(len(subarreglo_lista)):
                    numero_aleatorio = random.randint(1, 50)
                    if numero_aleatorio <= posivilidad_mutacion_gen:
                        nueva_posicion = random.randint(0, len(subarreglo_lista)-1)
                        # Intercambiar los elementos de las posiciones actuales y nuevas en la lista
                        subarreglo_lista[i], subarreglo_lista[nueva_posicion] = subarreglo_lista[nueva_posicion], subarreglo_lista[i]
                subarreglo_tupla = tuple(subarreglo_lista)  # Convertir la lista modificada en una tupla
                resultado_mutacion_individuo[resultado_mutacion_individuo.index(subarreglo)] = subarreglo_tupla
            return resultado_mutacion_individuo
        resultado_gen_cambio_posicion = posbilidad_gen_cambio_posicion(resultado_mutacion_individuo,posivilidad_mutacion_gen)
        print("mutacion del gen",resultado_gen_cambio_posicion)
        print(" ")

        #Se unen los arreglos inicales con los hijos
        def union_padres_hijos (resultado_gen_cambio_posicion,resultado_combinaciones):
            resultado_combinaciones.extend(resultado_gen_cambio_posicion)
            return resultado_combinaciones
        resultado_padres_hijos = union_padres_hijos(resultado_gen_cambio_posicion,resultado_combinaciones)
        #print("union del arreglo inicial con los hijos",resultado_padres_hijos)
        #print(" ")
        
        #Suma de de los valores de los primeros 30 atributos por individuo, tambien se pasa el individuo completo
        def suma_valores(diccionario,resultado_padres_hijos):
            resultado = []

            for tupla in resultado_padres_hijos:
                energia = 0
                proteinas = 0
                grasas = 0
                calcio = 0
                hierro = 0
                vitaminaA = 0
                tiamina = 0
                riboflavina = 0
                niacina = 0
                foloto = 0
                vitaminaC = 0
                elementos_iterados = ()
                for i,num in enumerate(tupla):
                    if i <29:
                        if num in diccionario:
                            energia += diccionario[num][2]
                            proteinas += diccionario[num][3]
                            grasas += diccionario[num][4]
                            calcio += diccionario[num][5]
                            hierro += diccionario[num][6]
                            vitaminaA += diccionario[num][7]
                            tiamina += diccionario[num][8]
                            riboflavina += diccionario[num][9]
                            niacina += diccionario[num][10]
                            foloto += diccionario[num][11]
                            vitaminaC += diccionario[num][12]
                    elementos_iterados +=(num,)
                resultado.append((energia,proteinas,grasas,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,elementos_iterados))
            return resultado
        resultado_suma_valores= suma_valores(diccionario,resultado_padres_hijos)
        #print("resultado de la suma",resultado_suma_valores)
        #print(" ")

        #Se saca la diferencia
        def diferencia (energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,resultado_suma_valores):
            resultado_dif = []
            for elementos in resultado_suma_valores:
                valores = elementos[:11]
                energia_resultado = (valores[0] - energia)/energia 
                proteina_resultado = (valores[1] - proteina)/proteina 
                grasa_resultado = (valores[2] - grasa)/ grasa
                calcio_resultado = (valores[3] - calcio)/calcio
                hierro_resultado = (valores[4] - hierro)/hierro
                vitaminaA_resultado = (valores[5] - vitaminaA)/vitaminaA
                tiamina_resultado = (valores[6] - tiamina)/tiamina
                riboflavina_resultado = (valores[7] - riboflavina)/riboflavina
                niacina_resultado = (valores[8] - niacina)/niacina
                foloto_resultado = (valores[9] - foloto)/foloto
                vitaminac_resultado = (valores[10] - vitaminaC)/ vitaminaC
                resultado_dif.append((energia_resultado,proteina_resultado,grasa_resultado,calcio_resultado,hierro_resultado,vitaminaA_resultado,tiamina_resultado,riboflavina_resultado,niacina_resultado,foloto_resultado,vitaminac_resultado,elementos[11]))
            return(resultado_dif)
        resultado_diferencia = diferencia(energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,resultado_suma_valores)
        print("diferencia individual",resultado_diferencia)
        print(" ")

        #se suma todo para sacar la diferencia absoluta
        def diferencia_absoluta(resultado):
            resultado_absoluta= []

            for elemento in resultado:
                suma_elementos = sum(elemento[:11])
                resultado_absoluta.append((suma_elementos,elemento[11],))
            return resultado_absoluta
        resultado_diferencia_absoltuta = diferencia_absoluta(resultado_diferencia)
        print("Direfencia absoluta",resultado_diferencia_absoltuta)
        print(" ")

        #ordenamiento de meno a mayor y se guarda el resultado menor
        def ordenamiento(diferencia_absoluta):
            resultado_ordenado = sorted(diferencia_absoluta, key=lambda x: x[0])
            elemento_menor = resultado_ordenado[0]
            resultado_menores.append(elemento_menor)
            return resultado_menores
        resultado_ordenamiento = ordenamiento(resultado_diferencia_absoltuta)
        print("ordenamiento",resultado_ordenamiento)

        #Ordenamiento de mayor a menor y se guarda el resultado mayor
        def ordenamiento_mayor(diferencia_absoluta):
            ordenado_mayor = sorted(diferencia_absoluta, key=lambda x: x[0], reverse=True)
            elemento_mayor = ordenado_mayor[0]
            resultado_mayores.append(elemento_mayor)
            return resultado_mayores
        resultado_ordenamiento_mayor = ordenamiento_mayor(resultado_diferencia_absoltuta)
        print("resultado ordenammiento mayor",resultado_ordenamiento_mayor)

        def promedio(diferencia_absoluta):
            suma = 0
            for elemento in diferencia_absoluta:
                if isinstance(elemento,tuple):
                    suma+= elemento[0]
            prome = suma / len(diferencia_absoluta)
            resultado_promedio.append(prome)
            return resultado_promedio
        resultadoo_promedio = promedio(resultado_diferencia_absoltuta)
        print(resultadoo_promedio)

        
        #elimina de forma alearotia conservando el individuo mas bajo que en este caso seria el mejor
        def poda_aleatoria(resultado_ordenamiento,resultado_padres_hijos):
            while len(resultado_padres_hijos) > limite_poblacion and resultado_ordenamiento:
                valor_no_eliminar = resultado_ordenamiento[-1][1]  # Obtener el último valor agregado en arreglo2[<indice>][1]

                if valor_no_eliminar in resultado_padres_hijos:
                    indice_eliminar = random.randint(0, len(resultado_padres_hijos) - 1)
                    
                    while resultado_padres_hijos[indice_eliminar] == valor_no_eliminar:
                        indice_eliminar = random.randint(0, len(resultado_padres_hijos) - 1)
                    
                    resultado_padres_hijos.pop(indice_eliminar)
            return resultado_padres_hijos
        resultado_poda = poda_aleatoria(resultado_ordenamiento,resultado_padres_hijos)
        print(resultado_poda)
        resultado_combinaciones = resultado_poda
        print(" ")
        print(resultado_menores)

        #se obtiene los datos de mi mejor individuo mi arreglo
        def mejores_datos (resultado_menores,diccionario,energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC):
            mejor_indivuo= resultado_menores[-1]
            #print(resultado_menores[-1])
            claves = mejor_indivuo[1]
            suma_absoluta = 0
            #print(clave)
            informacion= []
            sumas= []
            diferencia = []
            diferencia_absoluta = []
            requerido =[]
            energiaa = 0
            proteinass = 0
            grasass = 0
            calcioo = 0
            hierroo = 0
            vitaminaAA = 0
            tiaminaa = 0
            riboflavinaa = 0
            niacinaa = 0
            folotoo = 0
            vitaminaCC = 0
            for clave in claves[:29]:
                if clave in diccionario:
                    datos = diccionario[clave]
                    informacion.append((datos))
            for elemento in informacion:
                energiaa += elemento[2]
                proteinass += elemento[3]
                grasass += elemento[4]
                calcioo += elemento[5]
                hierroo += elemento[6]
                vitaminaAA += elemento[7]
                tiaminaa += elemento[8]
                riboflavinaa += elemento[9]
                niacinaa += elemento[10]
                folotoo += elemento[11]
                vitaminaCC += elemento[12]                
            sumas.append(["Total"," ",energiaa,proteinass,grasass,calcioo,hierroo,vitaminaAA,tiaminaa,riboflavinaa,niacinaa,folotoo,vitaminaCC])
            for elementos in sumas:
                energia_resultado = (elementos[2] - energia)/energia
                proteina_resultado = (elementos[3] - proteina)/proteina
                grasa_resultado = (elementos[4] - grasa)/grasa
                calcio_resultado = (elementos[5] - calcio)/calcio
                hierro_resultado = (elementos[6] - hierro)/hierro
                vitaminaA_resultado = (elementos[7] - vitaminaA)/vitaminaA
                tiamina_resultado = (elementos[8] - tiamina)/tiamina
                riboflavina_resultado = (elementos[9] - riboflavina)/riboflavina
                niacina_resultado = (elementos[10] - niacina)/niacina
                foloto_resultado = (elementos[11] - foloto)/foloto
                vitaminac_resultado = (elementos[12] - vitaminaC)/vitaminaC
            diferencia.append(["Diferencia","  ",energia_resultado,proteina_resultado,grasa_resultado,calcio_resultado,hierro_resultado,vitaminaA_resultado,tiamina_resultado,riboflavina_resultado,niacina_resultado,foloto_resultado,vitaminac_resultado])
            requerido.append(["Requerido","  ",energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC])
            #Se hace la suma de la diferencia absoluta
            suma_absoluta = sum(diferencia[0][2:])
            diferencia_absoluta.append(["Diferencia absoluta",suma_absoluta])
            print("todo",diferencia_absoluta)
            informacion.extend(sumas)
            informacion.extend(requerido)
            informacion.extend(diferencia)
            informacion.extend(diferencia_absoluta)
            print("aaaaaaaaaa",diferencia)
            return informacion
        resultado_mejores_datos = mejores_datos(resultado_menores,diccionario,energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC)
        print(resultado_mejores_datos)

        """def tabla_mejor_individuo(resultado_mejores_datos):
            print("sss")
        resultado_mejor_individuo = tabla_mejor_individuo(resultado_mejores_datos)"""
           
    def graficacion_resultados(resultado_menores,resultado_mejores_datos,resultado_mayores,resultado_promedio):

                    # Crear la ventana principal
            ventana = tk.Tk()
            ventana.geometry("1300x650")  
            ventana.title("Tabla de Datos")

            # Crear el árbol de datos
            tabla = ttk.Treeview(ventana)

            # Definir las columnas
            tabla['columns'] = ('Columna 1', 'Columna 2', 'Columna 3', 'Columna 4', 'Columna 5', 'Columna 6',
                                'Columna 7', 'Columna 8', 'Columna 9', 'Columna 10', 'Columna 11', 'Columna 12', 'Columna 13')

            # Formatear las columnas
            tabla.column('#0', width=0, stretch=tk.NO)
            tabla.column('Columna 1', width=180 )
            tabla.column('Columna 2', width=120)
            tabla.column('Columna 3', width=90, anchor=tk.CENTER)
            tabla.column('Columna 4', width=90, anchor=tk.CENTER)
            tabla.column('Columna 5', width=90, anchor=tk.CENTER)
            tabla.column('Columna 6', width=90, anchor=tk.CENTER)
            tabla.column('Columna 7', width=90, anchor=tk.CENTER)
            tabla.column('Columna 8', width=90, anchor=tk.CENTER)
            tabla.column('Columna 9', width=90, anchor=tk.CENTER)
            tabla.column('Columna 10', width=90, anchor=tk.CENTER)
            tabla.column('Columna 11', width=90, anchor=tk.CENTER)
            tabla.column('Columna 12', width=90, anchor=tk.CENTER)
            tabla.column('Columna 13', width=90, anchor=tk.CENTER)
            # Resto de las columnas...

            # Agregar encabezados de columna
            tabla.heading('#0', text='', anchor=tk.CENTER)
            tabla.heading('Columna 1', text='Alimentos', anchor=tk.CENTER)
            tabla.heading('Columna 2', text='Categoria', anchor=tk.CENTER)
            tabla.heading('Columna 3', text='Energia (kcal)', anchor=tk.CENTER)
            tabla.heading('Columna 4', text='Proteina (g)', anchor=tk.CENTER)
            tabla.heading('Columna 5', text='Grasa (g)', anchor=tk.CENTER)
            tabla.heading('Columna 6', text='Calcio (mg)', anchor=tk.CENTER)
            tabla.heading('Columna 7', text='Hierro (mg)', anchor=tk.CENTER)
            tabla.heading('Columna 8', text='VitaminaA (µg)', anchor=tk.CENTER)
            tabla.heading('Columna 9', text='Tiamana (mg)', anchor=tk.CENTER)
            tabla.heading('Columna 10', text='Riboflavina (mg)', anchor=tk.CENTER)
            tabla.heading('Columna 11', text='Niacina (mg)', anchor=tk.CENTER)
            tabla.heading('Columna 12', text='Foloto (µg)', anchor=tk.CENTER)
            tabla.heading('Columna 13', text='VitaminaC (mg)', anchor=tk.CENTER)
            # Resto de los encabezados...

            # Agregar filas de datos
            for i, row in enumerate(resultado_mejores_datos):
                tabla.insert(parent='', index='end', iid=i, text='', values=row)

            # Ajustar la tabla a la ventana
            tabla.pack(expand=True, fill=tk.BOTH)

            # Ejecutar el bucle principal de la ventana
            


        #Zona de grafiacion    
        #=========================================
            x = [9]
            y = [1.13]

            
            #plt.scatter(range(len(resultado_maximo)), resultado_maximo)
            #plt.scatter(range(len(resultado_maximo)), resultado_minimo)
            #plt.scatter(range(len(resultado_maximo)), resultado_promedio)
            #Para que solo grafiquemos la 1 pocicion de cada dato
            graficar_menores = []
            graficar_mayores = []


            for elementos in resultado_menores:
                graficar_menores.append(elementos[0])
            for elementos in resultado_mayores:
                graficar_mayores.append(elementos[0])

            fig, ax = plt.subplots()

            print("Resultados de las mejores generaciones",graficar_menores)
            
            ax.plot(graficar_menores, label=f'Menor {graficar_menores[-1]}',color='blue', )
            ax.plot(graficar_mayores, label=f'Mayor {graficar_mayores[-1]}',color='green', )
            ax.plot(resultado_promedio, label='Promedio',color='black', )
            
            ax.set_xlabel('Generaciones')
            ax.set_ylabel('Total')
            ax.set_xticks(range(len(graficar_menores)))
            ax.legend()

            plt.show()
            ventana.mainloop()
    graficacion_resultados(resultado_menores,resultado_mejores_datos,resultado_mayores,resultado_promedio)
    
    print("============================================")


# Crear la ventana principal
def datos_valores():
    Cantidad_individuos = int(Cantidad_de_individuos.get())
    cantidad_generaciones = int(iteraciones.get())
    limite_poblacion = int(poblacion_max.get())
    posibilidad_de_cruza = float(posi_cruza.get())
    posibilidad_de_mutacion_individuo = float(posi_individuo.get())
    posibilidad_de_mutacion_gen = float(posi_gen.get())
    
    energia_reque = float(reque_energia.get())
    proteina_reque = float(reque_proteina.get())
    grasa_reque = float(reque_grasa.get())
    calcio_reque = float(reque_calcio.get())
    hierro_reque = float(reque_hierro.get())
    vitaminaA_reque = float(reque_vitaminaA.get())
    tiamina_reque = float(reque_tiamina.get())
    riboflavina_reque = float(reque_riboflavina.get())
    niacina_reque = float(reque_niacina.get())
    foloto_reque = float(reque_foloto.get())
    vitaminaC_reque = float(reque_vitaminaC.get())

    main(cantidad_generaciones,diccionario,posibilidad_de_cruza,posibilidad_de_mutacion_individuo,posibilidad_de_mutacion_gen,energia_reque,proteina_reque,grasa_reque,calcio_reque,hierro_reque,vitaminaA_reque,tiamina_reque,riboflavina_reque,niacina_reque,foloto_reque,vitaminaC_reque,limite_poblacion,Cantidad_individuos)

    


root = tk.Tk()
root.configure(bg="gray")
root.title("Mochila")
root.geometry("900x800")

# Crear los labels
labe27 = tk.Label(root, text="Cantidad de individuos:",bg="grey")
label1 = tk.Label(root, text="Cantidad de iteraciones:",bg="grey")
label2 = tk.Label(root, text="Limite de poblacion",bg="grey")
label3 = tk.Label(root, text="Probabilidad de cruza:",bg="grey")
label4 = tk.Label(root, text="Probabilidad de mutacion del individuo:",bg="grey")
label5 = tk.Label(root, text="Probabilidad de mutacion del gen:",bg="grey")
label6 = tk.Label(root, text="Energia requerido:",bg="grey")
label7 = tk.Label(root, text="Proteina requerido:",bg="grey")
label8 = tk.Label(root, text="Grasa requerido:",bg="grey")
label9 = tk.Label(root, text="Calcio requerido:",bg="grey")
labe20 = tk.Label(root, text="Hierro requerido:",bg="grey")
labe21 = tk.Label(root, text="Vitamina A requerido:",bg="grey")
labe22 = tk.Label(root, text="Tiamina requerido:",bg="grey")
labe23 = tk.Label(root, text="Rivoflavina requerido:",bg="grey")
labe24 = tk.Label(root, text="Niacina requerido:",bg="grey")
labe25 = tk.Label(root, text="Folato requerido:",bg="grey")
labe26 = tk.Label(root, text="Vitamina C requerido:",bg="grey")

# Crear los entrys
Cantidad_de_individuos = tk.Entry(root, width = 50)
iteraciones = tk.Entry(root, width = 50)
poblacion_max = tk.Entry(root, width = 50)
posi_cruza = tk.Entry(root, width = 50)
posi_individuo = tk.Entry(root, width = 50)
posi_gen = tk.Entry(root, width = 50)

reque_energia = tk.Entry(root, width = 50)
reque_proteina = tk.Entry(root, width = 50)
reque_grasa = tk.Entry(root, width = 50)
reque_calcio = tk.Entry(root, width = 50)
reque_hierro = tk.Entry(root, width = 50)
reque_vitaminaA = tk.Entry(root, width = 50)
reque_tiamina = tk.Entry(root, width = 50)
reque_riboflavina = tk.Entry(root, width = 50)
reque_niacina = tk.Entry(root, width = 50)
reque_foloto = tk.Entry(root, width = 50)
reque_vitaminaC = tk.Entry(root, width = 50)

#precargar datos
iteraciones.insert(0,"20")
poblacion_max.insert(0,"9")
posi_cruza.insert(0,"35")
posi_individuo.insert(0,"35")
posi_gen.insert(0,"11")

reque_energia.insert(0,"6000")
reque_proteina.insert(0,"250")
reque_grasa.insert(0,"50")
reque_calcio.insert(0,"500")
reque_hierro.insert(0,"100")
reque_vitaminaA.insert(0,"2000")
reque_tiamina.insert(0,"50")
reque_riboflavina.insert(0,"30")
reque_niacina.insert(0,"50")
reque_foloto.insert(0,"300")
reque_vitaminaC.insert(0,"50")








# Crear un botón
buttonC = tk.Button(root, text="Confirmar", command = datos_valores)


# Acomodar el botón en la ventana utilizando grid
# Acomodar los labels y los entrys en una cuadrícula usando grid
label1.grid(row=0, column=0)
label1.config(font=("Arial", 20))
iteraciones.grid(row=0, column=1)

label2.grid(row=1, column=0)
label2.config(font=("Arial", 20))
poblacion_max.grid(row=1, column=1)

label3.grid(row=2, column=0)
label3.config(font=("Arial", 20))
posi_cruza.grid(row=2, column=1)

label4.grid(row=3, column=0)
label4.config(font=("Arial", 20))
posi_individuo.grid(row=3, column=1)

label5.grid(row=4, column=0)
label5.config(font=("Arial", 20))
posi_gen.grid(row=4, column=1)

label6.grid(row=5, column=0)
label6.config(font=("Arial", 20))
reque_energia.grid(row=5, column=1)

label7.grid(row=6, column=0)
label7.config(font=("Arial", 20))
reque_proteina.grid(row=6, column=1)

label8.grid(row=7, column=0)
label8.config(font=("Arial", 20))
reque_grasa.grid(row=7, column=1)

label9.grid(row=8, column=0)
label9.config(font=("Arial", 20))
reque_calcio.grid(row=8, column=1)

labe20.grid(row=9, column=0)
labe20.config(font=("Arial", 20))
reque_hierro.grid(row=9, column=1)

labe21.grid(row=10, column=0)
labe21.config(font=("Arial", 20))
reque_vitaminaA.grid(row=10, column=1)

labe22.grid(row=11, column=0)
labe22.config(font=("Arial", 20))
reque_tiamina.grid(row=11, column=1)

labe23.grid(row=12, column=0)
labe23.config(font=("Arial", 20))
reque_riboflavina.grid(row=12, column=1)

labe24.grid(row=13, column=0)
labe24.config(font=("Arial", 20))
reque_niacina.grid(row=13, column=1)

labe25.grid(row=14, column=0)
labe25.config(font=("Arial", 20))
reque_foloto.grid(row=14, column=1)

labe26.grid(row=15, column=0)
labe26.config(font=("Arial", 20))
reque_vitaminaC.grid(row=15, column=1)

labe27.grid(row=16, column=0)
labe27.config(font=("Arial", 20))
Cantidad_de_individuos.grid(row=16, column=1) 


buttonC.grid(row=17, column=0)

# Mostrar la ventana
root.mainloop()