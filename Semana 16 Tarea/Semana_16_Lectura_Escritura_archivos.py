#Abrimos el archivo
archivo = open('my_notes.txt', 'r')

print(archivo.readline()) #Leemos cada línea del archivo
print(archivo.readline())
print(archivo.readline())

archivo.seek(0)  #Ubicamos la posición del archivo en 0
ar_list = archivo.readlines() #Creamos una lista de las lineas
print(ar_list)

archivo.close() # Cerramos el archivo

with open('my_notes_2.txt', 'w') as archivo: #Utilizamos write para escribir
    archivo.write('Mañana salgo a comprar la comida\nEstaré muy ocupado el  fin de semana')
    archivo.close()