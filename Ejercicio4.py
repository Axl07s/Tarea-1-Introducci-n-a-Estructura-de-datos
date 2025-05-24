# 4. Potencia de un número con opción de repetir
# Axel Molineros

while True:
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"{base} ^ {exponente} = {resultado:.2f}")
    
    repetir = input("¿Deseas hacer otro cálculo nuevamente? (si/no): ").lower()
    if repetir != 'si':
        break
