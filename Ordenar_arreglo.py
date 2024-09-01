
#Realizamos la matriz
matriz = [
    [33, 44, 24],
    [38, 29, 6],
    [52, 10, 30]
]

print(f'Esta es la matriz sin ordenar {matriz}')

for n in range(len(matriz)): #Este es bucle que tomara cada fila como un arreglo
    for j in range(len(matriz[n])): #Este bucle y el de abajo serviran para comprar los elementos
        for f in range(len(matriz[n]) -1):
            if matriz[j][f] > matriz[j][f+1]: #Esta comparación para evaluar si es menor o mayor
                #Algoritmo para intercambiar los números en caso de cumplir la condición
                aux = matriz[j][f]
                matriz[j][f] = matriz[j][f+1]
                matriz[j][f + 1] = aux


print(f'Esta es la matriz ordenada {matriz}.')
