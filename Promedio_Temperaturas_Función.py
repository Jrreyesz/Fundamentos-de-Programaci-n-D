matr_temp = [#Ciudad
    [#Semanas
        [30, 26, 28, 35, 29, 30, 27],#Dias
        [30, 28, 29, 35, 29, 30, 27],
        [30, 28, 28, 33, 29, 30, 22],
        [30, 26, 27, 35, 28, 30, 25]
    ],
    [
        [30, 26, 26, 34, 29, 31, 27],
        [26, 31, 28, 33, 29, 32, 23],
        [32, 29, 29, 29, 29, 30, 24],
        [30, 26, 28, 33, 33, 34, 27]
    ],
    [
        [30, 26, 28, 33, 33, 35, 23],
        [32, 26, 28, 22, 29, 26, 27],
        [28, 26, 29, 28, 29, 30, 26],
        [30, 26, 28, 35, 29, 35, 27]
    ]
]

def temp_prom_ciud(temperaturas, ciudad, semana): #Definimos la función
    suma = 0 #Variable para sumar las temperaturas
    for dia in range(len(temperaturas[ciudad][semana])):
        suma += temperaturas[ciudad][semana][dia] #Sumamanos las temperaturas con la variable

    promedio = suma/len(temperaturas[ciudad][semana]) #Calculamos el promedio

    return promedio

promed_fin = temp_prom_ciud(matr_temp, 0, 0) #Llamamos a la función
print(f'El promedio de la ciudad en esa semana es de {promed_fin:.2f}')
