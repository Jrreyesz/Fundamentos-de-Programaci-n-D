#Realizamos la matriz
matriz = [
    [1, 40, 24],
    [3, 29, 16],
    [50, 8, 33]
]

#Le pedimos al usuario que ingrese el valor que desea buscar
find_element = int(input('¿Qué elemento desea buscar? '))


for i in range(len(matriz)): #Este for recorrera las filas
    for j in range(len(matriz[i])): #Este for recorrera las columnas
        if matriz[i][j] == find_element: #Evaluamos cada elemento de la matriz para ver si coincide con el numero ingresado
            print(f'El elemento {find_element} se encuentra en la fila {i} columna {j}')
            break #Si el número coincide se termina el ciclo
        elif len(matriz)-1 == i and j == 2 and matriz[i][j] != find_element: #Condición para evaluar si no se encontró el número
            print("El elemento no ha sido encontrado.")
            break
