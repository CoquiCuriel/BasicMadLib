# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:30:16 2022

@author: Ricardo Curiel
"""

nombre = input("Por favor, ingrese su nombre:")

color = input("¿Cual es su color preferido?")
animal = input("¿Cual es su animal preferido?")
actividad = input("¿Que actividad le gusta practicar?")
comida = input("¿Que le gusta cocinar?")

print(f"a {nombre}")
print(f"Le gusta el color {color}")
print("Su animal preferido es el" + animal)
print(f"Entre sus actividades preferidas está {actividad}")
print("Le gusta cocinar", comida)