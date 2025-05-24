# 7. Cálculo del promedio de N nota
# Axel Molineros

notas = []
while True:
    entrada = input("Ingrese una nota y 'fin' cuando termines de ingresar todas las notas: ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except:
        print("Entrada inválida.")

if notas:
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
