# 1. Área y perímetro de un círculo
# Axel Molineros

import math

radio = float(input("Ingrese el radio del círculo: "))
if radio > 0:
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")
else:
    print("El radio debe ser un número positivo.")
