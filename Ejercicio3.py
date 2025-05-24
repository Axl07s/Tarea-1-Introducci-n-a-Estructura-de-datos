# 3. Perímetro y área de un rectángulo
# Axel Molineros

largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

if largo > 0 and ancho > 0:
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")
else:
    print("Ambos valores deben ser positivos.")
