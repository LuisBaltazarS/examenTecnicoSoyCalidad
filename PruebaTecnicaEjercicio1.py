# Se tiene una matriz nxn de enteros, crear una funci´on que
# retorne un arreglo cuyo primer elemento es la cantidad de
# n´umeros que aparecen solo una vez y cuyo segundo elemento
# la cantidad de t´erminos repetidos.
# Ejemplos
# [[2, 2], [2, 2]] - [0, 1]
# [[2, 1, 3], [4, 5, 2], [6, 6, 6]] - [4, 2]

def ejercicio1(matriz): 

    valores_sin_repeticiones = []
    valores_completos = []

    # Recorrer la matriz para crear una lista con todos los valores que contienen, sin repeticiones y tambien agregamos otra lista para tomar todos los valores

    # Obtenemos las listas
    for a in matriz:
        # Obtenemos los valores de la listas
        for b in a: 
            # Agregamos los valores a la lista "valores_sin_repeticiones"
            valores_sin_repeticiones.append(b)
            # Agregamos todos los valores a la lista "valores_completos"
            valores_completos.append(b)

    # Borramos valores duplicados de la lista "valores_sin_repeticiones"
    valores_sin_repeticiones = list(set(valores_sin_repeticiones))

    # Creamos las variables requeridas
    repiten_una_vez = 0
    repiten_mas_de_dos = 0

    # Recorremos la lista "valores_sin_repeticiones"
    for i in valores_sin_repeticiones: 
        # Usamos count para verificar cuanto se repite cada elemento en la lista "valores_completos"
        cant = valores_completos.count(i)
        
        # Armamos la logica para obtener lo que se requiere
        if( cant == 1 ): 
            repiten_una_vez += 1
        elif( cant >= 2):
            repiten_mas_de_dos += 1

    return [ repiten_una_vez, repiten_mas_de_dos ]

matriz = [ 
    [2, 1, 3], 
    [4, 5, 2],
    [6, 6, 6] 
]

print(ejercicio1(matriz))