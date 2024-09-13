matriz_temperatura=[
    [
        ['Piñas'],
        ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        [[30, 29, 26, 25, 28, 27, 23],
         [30, 26, 24, 28, 26, 26, 24],
         [31, 27, 26, 25, 24, 27, 28],
         [29, 28, 27, 26, 23, 28, 30]]
    ],
    [
        ['Portovelo'],
        ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        [[30, 29, 33, 32, 34, 27, 33],
         [33, 28, 29, 30, 30, 30, 32],
         [31, 28, 30, 30, 29, 29, 32],
         [32, 27, 33, 29, 28, 28, 35]]
    ],
    [
        ['Zaruma'],
        ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        [[30, 28, 26, 27, 28, 27, 23],
         [33, 27, 25, 28, 24, 30, 33],
         [32, 28, 26, 26, 26, 29, 30],
         [31, 29, 28, 27, 25, 29, 29]]
    ]
]

for ciudad in range(len(matriz_temperatura)):
    for indice in range(len(matriz_temperatura[ciudad])):
        for elemento in range(len(matriz_temperatura[ciudad][indice])):
            

