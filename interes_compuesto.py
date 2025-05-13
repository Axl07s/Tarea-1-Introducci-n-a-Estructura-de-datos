# 6. Calcular interés compuesto
# Axel Molineros

capital = float(input("Capital inicial: "))
tasa = float(input("Tasa de interés anual (en %): "))
años = int(input("Número de años: "))

monto = capital * (1 + tasa / 100) ** años
print(f"Monto final con interés compuesto: {monto:.2f}")
