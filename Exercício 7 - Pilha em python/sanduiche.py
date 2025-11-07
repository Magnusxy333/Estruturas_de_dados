def programa_sanduiche_pilha():
    # A lista do Python funciona como uma Pilha: append (PUSH), pop (POP).
    sanduiche = []
    
    # O Pão de baixo é a base (primeiro item).
    sanduiche.append("🍞 Pão de Baixo (Base)")

    print("--- 🥪 Montador de Sanduíche (Pilha/LIFO) ---")
    print(f"✅ Base do sanduíche pronta: '{sanduiche[0]}'")

    while True:
        print("\n--- Menu do Sanduíche ---")
        print("1 - Adicionar ingrediente (PUSH)")
        print("2 - Remover ingrediente do topo (POP)")
        print("3 - Ver último ingrediente adicionado (PEEK)")
        print("4 - Mostrar sanduíche completo")
        print("5 - Finalizar pedido")
        print("-------------------------\n")

        try:
            opcao = input("Escolha uma opção (1-5): ")
            print()

            if opcao == '1':
                ingrediente = input("Nome do ingrediente para adicionar ao topo: ").strip()
                if ingrediente:
                    sanduiche.append(ingrediente)
                    print(f"✅ '{ingrediente}' adicionado ao topo do sanduíche!")
                else:
                    print("⚠️ O nome do ingrediente não pode ser vazio.")

            elif opcao == '2':
                # Verifica se há algo além da 'Base' (Pão de Baixo)
                if len(sanduiche) > 1: 
                    ingrediente_removido = sanduiche.pop()
                    print(f"🗑️ **{ingrediente_removido}** removido do topo. Ufa!")
                elif len(sanduiche) == 1 and sanduiche[0] == "🍞 Pão de Baixo (Base)":
                    print("✋ Você só pode remover o pão de cima. O sanduíche está no pão de baixo!")
                else:
                    print("🚫 O sanduíche está vazio. Adicione um pão, pelo menos.")

            elif opcao == '3':
                if len(sanduiche) > 1:
                    topo = sanduiche[-1]
                    print(f"👀 Ingrediente no topo (o próximo a ser mordido): **{topo}**")
                else:
                    print("⚠️ O sanduíche está na base. Hora de rechear!")

            elif opcao == '4':
                print("📋 Ordem do Sanduíche (da base para o topo):")
                if len(sanduiche) > 0:
                    for i, item in enumerate(sanduiche):
                        if i == 0:
                            print(f"  --> BASE: {item}")
                        elif i == len(sanduiche) - 1:
                            print(f"  --> TOPO: **{item}**")
                        else:
                            print(f"  --| Camada {i}: {item}")
                    print(f"\nTotal de camadas: {len(sanduiche)}.")
                else:
                    print("🚫 O sanduíche está completamente vazio. Cadê a fome?")

            elif opcao == '5':
                print("\n🎉 Pedido finalizado! Bom apetite!")
                break

            else:
                print("❌ Opção inválida. Escolha um número entre 1 e 5.")

        except:
            print("🚨 Erro inesperado. Tente novamente.")
            
# --- CHAMADA ATIVA PARA O ONECOMPILER ---
programa_sanduiche_pilha()