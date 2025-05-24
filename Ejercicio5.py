# 5. Conversión de millas a kilómetros y metros
# Axel Molineros

millas = float(input("Ingrese la cantidad de millas: "))
kilometros = millas * 1.60934
metros = kilometros * 1000

print(f"{millas} millas = {kilometros:.3f} km = {metros:.2f} m")
