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
if (Cantidad < 2):
    print(f'Total valor a pagar: {Valor_Total}')
elif Cantidad >= 2 or Cantidad < 5:
    print(f'Total valor a pagar: {Valor_Descuento1}')
elif Cantidad < 10 or Cantidad >= 5:
    print(f'Total valor a pagar: {Valor_Descuento2}')
elif Cantidad >= 10:
    print(f'Total valor a pagar: {Valor_Descuento3}')

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
