# Comandos de Repetição em Python
try:
    num1 = int(input("Digite um número inteiro (limite de repetição, ex: 5): "))
except ValueError:
    print("Erro: Entrada inválida.")
    exit()

print("\n--- Loop 'for' (Contagem de 1 a N) ---")
# 'range(1, num1 + 1)' gera números de 1 até num1
for i in range(1, num1 + 1):
    print(i, end=" ")
print() # Quebra de linha

print("\n--- Loop 'while' (Contagem Regressiva) ---")
contador = num1
while contador >= 1:
    print(contador, end=" ")
    contador -= 1 # Decremento
print()