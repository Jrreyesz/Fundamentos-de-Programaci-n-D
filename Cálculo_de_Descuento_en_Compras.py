
def calcular_descuento(total_c, po_desc=20): #Creamos la función con un parámetro predeterminado
    desc = ((total_c * po_desc)/100) #Calculamos el descuento
    pre_desc = total_c - desc #Aplicamos el descuento al total
    print(f'El total real de su compra es {total_c:.2f}. Pero, por el descuento pagará {pre_desc:.2f}, un total de {desc:.2f} dólares de descuento.') #Imprimimos el resultado
    return

calcular_descuento(356.2) #Llamamos a la función sin darle el segundo parámetro

calcular_descuento(123.89, 30) #Llamamos a la función dándole los dos parámetros