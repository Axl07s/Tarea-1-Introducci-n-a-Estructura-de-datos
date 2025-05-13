# 2. Conversión de temperatura (Celsius a Fahrenheit o Fahrenheit a Celsius)
# Axel Molineros

opcion = input("Convertir en Celsius a Fahrenheit escribe C, o Fahrenheit a Celsius escribe F: ").upper()

if opcion == 'C':
    celsius = float(input("Ingrese temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C = {fahrenheit:.2f} °F")
elif opcion == 'F':
    fahrenheit = float(input("Ingrese temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} °F = {celsius:.2f} °C")
else:
    print("Opción inválida.")
