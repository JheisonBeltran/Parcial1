# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:01:27 2021

@author: Jbeltrant
"""
# PARCIAL #1

# EJERCICIO 1
Valor = float(input('Digite el precio de las manzanas: '))
Cantidad = float(input('Digite el número de kilos a comprar: '))
Valor_Total = Valor * Cantidad
Descuento1 = Valor_Total * 0.10
Valor_Descuento1 = Valor_Total - Descuento1
Descuento2 = Valor_Total * 0.15
Valor_Descuento2 = Valor_Total - Descuento2
Descuento3 = Valor_Total * 0.20
Valor_Descuento3 = Valor_Total - Descuento3
print("El valor a pagar es: ")
if Cantidad >= 0 and Cantidad < 2:
    print("0")
if Cantidad >= 2 and Cantidad < 5:
    print(Valor_Descuento1)
if Cantidad >= 5 and Cantidad < 10:
    print(Valor_Descuento2)
if Cantidad >= 10:
    print(Valor_Descuento3)

# EJERCICIO 2
Valor_abanico = float(input('Digite el precio de los abanicos a comprar: '))
Cantidad = float(input('Digite la cantidad de abanicos: '))
Clave = (input('Digite su clave de descuento: '))
Total = Valor_abanico * Cantidad
if Clave == '010':
    Descuento1 = Total - (Total * 0.20)
    print(f'Total valor a pagar con descuento es: {Descuento1}')
elif Clave == '020':
    Descuento2 = Total - (Total * 0.40)
    print(f'Total valor a pagar con descuento es: {Descuento2}')
elif Clave == '030':
    Descuento3 = Total - (Total * 0.55)
    print(f'Total valor a pagar con descuento es: {Descuento3}')
elif Clave == '040':
    Descuento4 = Total - (Total * 0.75)
    print(f'Total valor a pagar con descuento es: {Descuento4}')

# EJERCICIO 3
Valor = int(input('Digite el precio del aparato a comprar  : '))
Marca = input('Digite la marca del aparato: ')
if Valor >= 4000 and Marca.lower() == 'nosy':
    Total_Descuento = Valor - (Valor * 0.20) - (Valor * 0.10)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.30)
    print(f' Total: {Total_IVA}')
elif Valor >= 4000:
    Total_Descuento = Valor - (Valor * 0.20)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.30)
    print(f' Total: {Total_IVA}')
elif Marca.lower() == 'nosy':
    Total_Descuento = Valor - (Valor * 0.10)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.30)
    print(f' Total: {Total_IVA}')
else:
    print(f' Total: {Valor}')

# EJERCICIO 4
Num_Hectareas = int(input('Ingrese el número de hectáreas del bosque : '))
if Num_Hectareas > 5:
    Pino = float(Num_Hectareas * 0.80)
    Oyamel = float(Num_Hectareas * 0.15)
    Cedro = float(Num_Hectareas * 0.05)
    print('Se Deben sembrar')
    print(f'Hectáreas de pinos: {Pino}')
    print(f'Hectáreas de  oyamel: {Oyamel}')
    print(f'Hectáreas de cedro: {Cedro}')
elif Num_Hectareas <= 5:
    Pino = float(Num_Hectareas * 0.45)
    Oyamel = float(Num_Hectareas * 0.25)
    Cedro = float(Num_Hectareas * 0.30)
    print('Se Deben sembrar')
    print(f'Hectáreas de pinos: {Pino}')
    print(f'Hectáreas de  oyamel: {Oyamel}')
    print(f'Hectáreas de cedro: {Cedro}')

# EJERCICIO 5
Recoletar_n1 = float(input('Digite el primer número : '))
Recoletar_n2 = float(input('Digite el primer número : '))
Recoletar_n3 = float(input('Digite el primer número : '))
if Recoletar_n1 > Recoletar_n2 and Recoletar_n1 > Recoletar_n3:
    print(f'El mayor numero es el : {Recoletar_n1}')
elif Recoletar_n2 > Recoletar_n1 and Recoletar_n2 > Recoletar_n3:
    print(f'El mayor numero es el : {Recoletar_n2}')
elif Recoletar_n3 > Recoletar_n1 and Recoletar_n3 > Recoletar_n2:
    print(f'El mayor numero es el : {Recoletar_n3}')
