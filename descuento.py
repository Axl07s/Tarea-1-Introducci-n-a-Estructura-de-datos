# 8. Cálculo de descuento con validación
# Axel Molineros

precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento (0-100): "))

if 0 <= descuento <= 100:
    precio_final = precio * (1 - descuento / 100)
    print(f"Precio final: {precio_final:.2f}")
else:
    print("El descuento debe estar entre 0 y 100.")
