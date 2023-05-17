#Nuestro diccinario inicial
from email import iterators
import itertools
from pickletools import read_uint1
import random
import re
import pandas as pd


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

limite_mochila = 1250
cantidad_iteraciones = 10
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
vitamicaC_requerido = 70





#Parametros que se usaran
def main(cantidad_iteraciones, diccionario, limite_mochila,posiblidad_cruza,posibiliada_mutacion_individuo,posivilidad_mutacion_gen,energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,limite_poblacion):
    
    resultado_menores= []
    #Genera las combinaciones que digita el usuario
    def combinaciones_posibles(diccionario):
            #id = list(diccionario) #Se obtienen los id del diccionario
        id = [clave for clave in diccionario if isinstance(clave, int)]
        resultado_combinaciones = []
        for i in range(10):
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

        #Emparejamiento de las comninaciones
        def emparejamiento_poblacion (resultado_combinacione,):
            parejas_generadas = [] # Arreglo donde se guardaran todas las parejas generadas
            parejas_generadas  = list(itertools.combinations(resultado_combinacione,2))
            return parejas_generadas
        resutado_emparejamiento = emparejamiento_poblacion(resultado_combinaciones)
        print("Combinacion: ",resutado_emparejamiento)
        print(" ")

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
                    numero_aleatorio = random.randint(1, 10)
                    if numero_aleatorio <= posivilidad_mutacion_gen:
                        nueva_posicion = random.randint(0, len(subarreglo_lista)-1)
                        # Intercambiar los elementos de las posiciones actuales y nuevas en la lista
                        subarreglo_lista[i], subarreglo_lista[nueva_posicion] = subarreglo_lista[nueva_posicion], subarreglo_lista[i]
                subarreglo_tupla = tuple(subarreglo_lista)  # Convertir la lista modificada en una tupla
                resultado_mutacion_individuo[resultado_mutacion_individuo.index(subarreglo)] = subarreglo_tupla
            return resultado_mutacion_individuo
        resultado_gen_cambio_posicion = posbilidad_gen_cambio_posicion(resultado_mutacion_individuo,posivilidad_mutacion_gen)
        #print("mutacion del gen",resultado_gen_cambio_posicion)
        #print(" ")

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
                energia_resultado = valores[0] - energia
                proteina_resultado = valores[1] - proteina
                grasa_resultado = valores[2] - grasa
                calcio_resultado = valores[3] - calcio
                hierro_resultado = valores[4] - hierro
                vitaminaA_resultado = valores[5] - vitaminaA
                tiamina_resultado = valores[6] - tiamina
                riboflavina_resultado = valores[7] - riboflavina
                niacina_resultado = valores[8] - niacina
                foloto_resultado = valores[9] - foloto
                vitaminac_resultado = valores[10] - vitaminaC
                resultado_dif.append((energia_resultado,proteina_resultado,grasa_resultado,calcio_resultado,hierro_resultado,vitaminaA_resultado,tiamina_resultado,riboflavina_resultado,niacina_resultado,foloto_resultado,vitaminac_resultado,elementos[11]))
            return(resultado_dif)
        resultado_diferencia = diferencia(energia,proteina,grasa,calcio,hierro,vitaminaA,tiamina,riboflavina,niacina,foloto,vitaminaC,resultado_suma_valores)
        #print("diferencia individual",resultado_diferencia)
        #print(" ")

        #se suma todo para sacar la diferencia absoluta
        def diferencia_absoluta(resultado):
            resultado_absoluta= []

            for elemento in resultado:
                suma_elementos = sum(elemento[:11])
                resultado_absoluta.append((suma_elementos,elemento[11],))
            return resultado_absoluta
        resultado_diferencia_absoltuta = diferencia_absoluta(resultado_diferencia)
        #print("Direfencia absoluta",resultado_diferencia_absoltuta)
        #print(" ")

        #ordenamiento de meno a mayor y se guarda el resultado menor
        def ordenamiento(diferencia_absoluta):
            resultado_ordenado = sorted(diferencia_absoluta, key=lambda x: x[0])
            elemento_menor = resultado_ordenado[0]
            resultado_menores.append(elemento_menor)
            return resultado_menores
        resultado_ordenamiento = ordenamiento(resultado_diferencia_absoltuta)
        print(resultado_ordenamiento)
        #
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
        print("============================================")
    print(resultado_menores)



main(cantidad_iteraciones,diccionario,limite_mochila,posiblidad_cruza,posibiliada_muta_individuo,posivilidad_mutacion_gen,energia_requerido,protenia_requerido,grasa_requerido,calcio_requerido,hierro_requerido,vitaminaA_requerido,tiamina_requerido,riboflavina_requerido,niacina_requerido,foloto_requerido,vitamicaC_requerido,limite_poblacion)
