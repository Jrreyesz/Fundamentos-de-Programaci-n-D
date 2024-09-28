#Creamos el diccionario
informacion_personal = {
    'nombre': 'Jinsonp Romario Reyes Zambrano',
    'edad': 26,
    'ciudad': 'Piñas',
    'altura' : 1.82,
    'peso' : '140 Kg',
    'nacionalidad' : 'Ecuatoriana'
}

print(informacion_personal.get('ciudad')) #Acceso a el valor de la clave ciudad
informacion_personal['ciudad'] = 'Cuenca' #Cambiando el valor de la clave ciudad
print(informacion_personal.get('ciudad')) #Acceso a el valor de la clave ciudad

informacion_personal['profesión'] = 'Estudiante' #Agregando una nueva clave-valor
print(informacion_personal.get('profesión'))

if 'telefono' in informacion_personal.keys(): #Condicional para verificar si la clave teléfono esta en el diccionario
    print(informacion_personal['telefono'])
else:
    informacion_personal['telefono'] = 2970236 #Creamos la clave teléfono en caso de que no exista

print(informacion_personal['telefono'])

del informacion_personal['edad'] #Eliminamos la clave edad


print(informacion_personal) #Imprimimos el diccionario modificado

