def programa_historico_navegacao():
    # Pilha para armazenar URLs visitadas (LIFO: Volta para a última)
    historico = [] 
    
    print("--- 🌐 Navegador LIFO: Histórico Web Simulado ---")

    while True:
        print("\n--- Ações do Navegador ---")
        print("1 - Visitar Nova Página (PUSH)")
        print("2 - Voltar à Página Anterior (POP)")
        print("3 - Ver Página Atual (PEEK)")
        print("4 - Mostrar Histórico Completo")
        print("5 - Sair do Navegador")
        print("----------------------------\n")

        try:
            opcao = input("Escolha uma opção (1-5): ")
            print()

            if opcao == '1':
                url = input("URL para visitar (ex: google.com): ").strip()
                if url:
                    historico.append(url)
                    print(f"✅ Navegando para: **{url}**")
                else:
                    print("⚠️ URL inválida.")

            elif opcao == '2':
                # Verifica se há páginas para voltar
                if historico:
                    pagina_atual = historico.pop()
                    print(f"⬅️ Voltando... Saímos de **{pagina_atual}**.")
                    
                    if historico:
                        print(f"   Agora você está em: {historico[-1]}")
                    else:
                        print("   Histórico zerado. Você está no início de tudo.")
                else:
                    print("🚫 O histórico está vazio. Não há para onde voltar.")

            elif opcao == '3':
                if historico:
                    pagina_atual = historico[-1] 
                    print(f"📍 Sua página atual é: **{pagina_atual}**")
                else:
                    print("⚠️ Histórico vazio. Visite uma página primeiro (Opção 1).")

            elif opcao == '4':
                print("📋 Histórico de Navegação (Página atual no topo):")
                if historico:
                    for i, page in enumerate(historico):
                        print(f"   [{i + 1}] {page}")
                    print(f"\nTotal de páginas no histórico: {len(historico)}")
                else:
                    print("🚫 O histórico de navegação está vazio.")

            elif opcao == '5':
                print("👋 Encerrando o navegador LIFO. Fui!")
                break

            else:
                print("❌ Opção inválida. Por favor, escolha um número entre 1 e 5.")

        except:
            print("🚨 Erro inesperado. Tente novamente.")
            
# --- CHAMADA ATIVA PARA O ONECOMPILER ---
programa_historico_navegacao()