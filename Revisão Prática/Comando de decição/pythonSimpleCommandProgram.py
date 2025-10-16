# Comandos de Decisão em Python
try:
    num1 = int(input("Digite um número inteiro (positivo, negativo ou zero): "))
except ValueError:
    print("Erro: Entrada inválida.")
    exit()

print("\n--- Classificação (Python) ---")

# Comandos de Decisão: if, elif (else if), else
if num1 > 0:
    print(f"O número {num1} é POSITIVO.")
elif num1 < 0: # elif é o equivalente a 'else if'
    print(f"O número {num1} é NEGATIVO.")
else:
    print(f"O número {num1} é ZERO.")