# 9. Conversión de horas a días, horas, minutos y segundos
# Axel Molineros

total_horas = int(input("Ingrese la cantidad de horas: "))
dias = total_horas // 24
horas_restantes = total_horas % 24
minutos = total_horas * 60
segundos = total_horas * 3600

print(f"{total_horas} horas = {dias} días, {horas_restantes} horas")
print(f"También equivale a {minutos} minutos o {segundos} segundos")
