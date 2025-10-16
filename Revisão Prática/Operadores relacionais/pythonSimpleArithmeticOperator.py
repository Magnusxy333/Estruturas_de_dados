print("Programa de Operadores Aritméticos em Python.")
CONSTANTE = 5 

try:
    num1 = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Entrada inválida.")
    exit() 

# Cálculos
soma = num1 + CONSTANTE
sub = num1 - CONSTANTE
mult = num1 * CONSTANTE
div = num1 / CONSTANTE
mod = num1 % CONSTANTE 

# Saída
print("\n--- Resultados (Python) ---")
print(f"Adição: {num1} + {CONSTANTE} = {soma}")
print(f"Subtração: {num1} - {CONSTANTE} = {sub}")
print(f"Multiplicação: {num1} * {CONSTANTE} = {mult}")
print(f"Divisão: {num1} / {CONSTANTE} = {div}")
print(f"Resto da Divisão (Módulo): {num1} % {CONSTANTE} = {mod}")