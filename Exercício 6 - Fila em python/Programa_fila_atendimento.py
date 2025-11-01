import collections
import time # Usado para criar um pequeno delay visual no atendimento

def menu_fila_atendimento():
    # Usamos collections.deque para maior eficiência em operações de fila (FIFO)
    fila = collections.deque()

    while True:
        print("\n--- Fila de Atendimento ---")
        print("1 - Adicionar pessoa à fila")
        print("2 - Atender pessoa")
        print("3 - Mostrar fila")
        print("4 - Sair")
        print("---------------------------\n")

        try:
            # No OneCompiler, a entrada (input) é interativa no console de saída
            opcao = input("Escolha uma opção (1-4): ")
            print()

            if opcao == '1':
                # 1 - Adicionar pessoa à fila
                nome = input("Informe o nome da pessoa para adicionar à fila: ").strip()
                if nome:
                    # Adiciona ao final da fila (FIFO)
                    fila.append(nome)
                    print(f"✅ '{nome}' foi adicionado(a) à fila.")
                else:
                    print("⚠️ O nome não pode ser vazio. Tente novamente.")

            elif opcao == '2':
                # 2 - Atender pessoa
                if fila:
                    # Remove a primeira pessoa da fila (FIFO)
                    pessoa_atendida = fila.popleft()
                    print(f"➡️ Atendimento em andamento...")
                    time.sleep(0.5) 
                    print(f"🎉 **{pessoa_atendida}** foi atendido(a).")
                else:
                    print("✋ A fila está vazia. Não há ninguém para atender.")

            elif opcao == '3':
                # 3 - Mostrar fila
                print("📋 Status atual da Fila:")
                if fila:
                    for i, pessoa in enumerate(fila, 1):
                        print(f"   {i}. {pessoa}")
                    print(f"\nTotal de pessoas na fila: {len(fila)}")
                else:
                    print("   *** A fila está vazia no momento. ***")

            elif opcao == '4':
                # 4 - Sair
                print("👋 Encerrando o programa da Fila de Atendimento. Até mais!")
                break

            else:
                print("❌ Opção inválida. Por favor, escolha um número entre 1 e 4.")

        except ValueError:
            print("❌ Entrada inválida. Por favor, digite apenas o número da opção.")
        except KeyboardInterrupt:
            # Captura Ctrl+C, comum em ambientes interativos
            print("\n👋 Programa interrompido pelo usuário. Encerrando.")
            break

# ----------------------------------------------------
# CHAMADA PARA INICIAR O PROGRAMA NO ONECOMPILER
# ----------------------------------------------------
menu_fila_atendimento()