import collections
import random
import time

def sistema_fila_impressao():
    # Usamos deque para a fila de documentos
    fila_impressao = collections.deque()
    contador_documentos = 1

    print("--- 🖨️ Sistema de Fila de Impressão ---")

    while True:
        print("\n--- Opções do Sistema de Impressão ---")
        print("1 - Enviar novo documento para impressão")
        print("2 - Processar (imprimir) próximo documento")
        print("3 - Ver status da fila de impressão")
        print("4 - Sair")
        print("--------------------------------------\n")

        try:
            opcao = input("Escolha uma opção (1-4): ")
            print()

            if opcao == '1':
                # 1 - Enviar novo documento
                nome_doc = input("Nome do documento (Deixe em branco para nome padrão): ").strip()
                if not nome_doc:
                    nome_doc = f"Documento_N_{contador_documentos}"

                prioridade = random.choice(["Normal", "Alta"])
                
                documento = {
                    "id": contador_documentos,
                    "nome": nome_doc,
                    "paginas": random.randint(1, 50),
                    "prioridade": prioridade
                }
                
                # Adiciona o documento ao final da fila
                fila_impressao.append(documento)
                print(f"✅ Documento '{documento['nome']}' ({documento['paginas']} páginas) enviado para a fila.")
                contador_documentos += 1

            elif opcao == '2':
                # 2 - Processar próximo documento
                if fila_impressao:
                    # Remove o primeiro documento da fila (FIFO)
                    doc_para_imprimir = fila_impressao.popleft()
                    
                    print(f"⏳ Processando documento: **{doc_para_imprimir['nome']}**...")
                    # Simula o tempo de impressão (tempo base 0.5s + 0.1s por página)
                    tempo_impressao = 0.5 + (doc_para_imprimir['paginas'] / 10)
                    # Limita o tempo para não ser muito longo (máximo 3 segundos)
                    time.sleep(min(3, tempo_impressao)) 

                    print(f"🎉 Impressão concluída: **{doc_para_imprimir['nome']}**.")
                else:
                    print("✋ A fila de impressão está vazia. Nenhum documento pendente.")

            elif opcao == '3':
                # 3 - Ver status da fila
                print("📋 Documentos na Fila de Impressão (Próximo a ser impresso no topo):")
                if fila_impressao:
                    for i, doc in enumerate(fila_impressao, 1):
                        print(f"   {i}. {doc['nome']} (Págs: {doc['paginas']}, Prioridade: {doc['prioridade']})")
                    print(f"\nTotal de documentos pendentes: {len(fila_impressao)}")
                else:
                    print("   *** A fila de impressão está livre! ***")

            elif opcao == '4':
                # 4 - Sair
                print("👋 Encerrando o Sistema de Fila de Impressão.")
                break

            else:
                print("❌ Opção inválida. Por favor, escolha um número entre 1 e 4.")

        except ValueError:
            print("❌ Entrada inválida. Por favor, digite apenas o número da opção.")
        except KeyboardInterrupt:
            print("\n👋 Programa interrompido pelo usuário. Encerrando.")
            break

# ----------------------------------------------------
# CHAMADA PARA INICIAR O PROGRAMA NO ONECOMPILER
# ----------------------------------------------------
sistema_fila_impressao()