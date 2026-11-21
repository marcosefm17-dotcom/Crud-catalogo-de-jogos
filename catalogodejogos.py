catalogo = []

while True:
    print("\n=== CATÁLOGO DE JOGOS ===")
    print("1 - Cadastrar jogo (Create)")
    print("2 - Listar jogos (Read)")
    print("3 - Atualizar jogo (Update)")
    print("4 - Excluir jogo (Delete)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n--- Novo Cadastro ---")
        titulo = input("Título do jogo: ").strip()
        if titulo == "":
            print("Erro: O título do jogo não pode ficar em branco!")
            continue

        try:
            ano = int(input("Ano de lançamento (ex: 2023): ").strip())
            if ano < 1970 or ano > 2026:
                print("Erro: Digite um ano válido entre 1970 e 2026!")
                continue
        except ValueError:
            print("Erro: O ano deve ser um número inteiro (ex: 2020)!")
            continue

        try:
            nota = float(input("Nota do jogo (0 a 10): ").strip())
            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10!")
                continue
        except ValueError:
            print("Erro: A nota deve ser um número (ex: 8.5)!")
            continue

        novo_jogo = {
            "titulo": titulo,
            "ano": ano,
            "nota": nota
        }
        catalogo.append(novo_jogo)
        print(f"Sucesso! '{titulo}' foi adicionado ao catálogo.")

    elif opcao == "2":
        print("\n--- Jogos Cadastrados ---")
        if len(catalogo) == 0:
            print("Nenhum jogo cadastrado no momento.")
        else:
            for i, jogo in enumerate(catalogo):
                print(f"{i + 1}. {jogo['titulo']} ({jogo['ano']}) - Nota: {jogo['nota']}")

    elif opcao == "3":
        print("\n--- Atualizar Jogo ---")
        if len(catalogo) == 0:
            print("Nenhum jogo cadastrado para atualizar.")
        else:
            for i, jogo in enumerate(catalogo):
                print(f"{i + 1}. {jogo['titulo']} ({jogo['ano']}) - Nota: {jogo['nota']}")

            try:
                indice = int(input("\nDigite o número do jogo que deseja atualizar: ").strip()) - 1
                if indice < 0 or indice >= len(catalogo):
                    print("Erro: Jogo não encontrado! Escolha um número da lista.")
                    continue

                jogo_selecionado = catalogo[indice]
                print(f"Atualizando: {jogo_selecionado['titulo']}")

                novo_titulo = input("Novo título: ").strip()
                if novo_titulo == "":
                    print("Erro: O título não pode ficar em branco!")
                    continue

                novo_ano = int(input("Novo ano (1970 a 2026): ").strip())
                if novo_ano < 1970 or novo_ano > 2026:
                    print("Erro: Ano inválido!")
                    continue

                nova_nota = float(input("Nova nota (0 a 10): ").strip())
                if nova_nota < 0 or nova_nota > 10:
                    print("Erro: Nota inválida!")
                    continue

                catalogo[indice]["titulo"] = novo_titulo
                catalogo[indice]["ano"] = novo_ano
                catalogo[indice]["nota"] = nova_nota
                print("Jogo atualizado com sucesso!")

            except ValueError:
                print("Erro: Digite apenas números válidos!")

    elif opcao == "4":
        print("\n--- Excluir Jogo ---")
        if len(catalogo) == 0:
            print("Nenhum jogo cadastrado para excluir.")
        else:
            for i, jogo in enumerate(catalogo):
                print(f"{i + 1}. {jogo['titulo']} ({jogo['ano']}) - Nota: {jogo['nota']}")

            try:
                indice = int(input("\nDigite o número do jogo que deseja excluir: ").strip()) - 1
                if indice < 0 or indice >= len(catalogo):
                    print("Erro: Jogo não encontrado! Escolha um número da lista.")
                    continue

                jogo_removido = catalogo.pop(indice)
                print(f"Sucesso! '{jogo_removido['titulo']}' foi removido do catálogo.")

            except ValueError:
                print("Erro: Digite apenas o número do jogo!")

    elif opcao == "0":
        print("Encerrando o Catálogo de Jogos. Até mais!")
        break

    else:
        print("Opção inválida! Digite um número de 0 a 4.")
