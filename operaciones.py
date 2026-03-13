# Programa de operaciones básicas en Python

# Pedir al usuario dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Evitar división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre 0"

# Mostrar resultados
print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
