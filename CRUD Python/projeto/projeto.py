import uuid
import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'agilstore.json')

estoque = []

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return []

def salvar_dados(dados):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

def adicionar_produto():
    if len(estoque) >= 100:
        print("Erro: O estoque está cheio!")
        input("\nPressione Enter para voltar ao menu principal...")
        return

    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    codigo_id = str(uuid.uuid4().hex[:4])

    produto = {
        "codigo": codigo_id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
    }

    estoque.append(produto)
    salvar_dados(estoque)
    print(f"O produto com ID: {codigo_id} foi adicionado!")
    input("\nPressione Enter para voltar ao menu principal...")

def excluir_produto():
    codigo = input("Digite o código do produto a ser removido: ")

    produto = next((p for p in estoque if p["codigo"] == codigo), None)
    if not produto:
        print("Produto não encontrado!")
        input("\nPressione Enter para voltar ao menu principal...")
        return

    print("\nProduto encontrado:")
    print(
        f"ID: {produto['codigo']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | "
        f"Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
    )

    confirmacao = input("\nTem certeza de que deseja remover este produto? (s/n): ").strip().lower()
    if confirmacao in 'Nn':
        print("Ação cancelada. Nenhum produto foi removido.")
        input("\nPressione Enter para voltar ao menu principal...")
        return

    estoque.remove(produto)
    salvar_dados(estoque)
    print("O produto foi removido do estoque com sucesso!")
    input("\nPressione Enter para voltar ao menu principal...")

def listar_produtos():
    os.system("cls")
    if not estoque:
        print("O estoque está vazio.")
        input("\nPressione Enter para voltar ao menu principal...")
        return

    print("\nProdutos no estoque:")
    for produto in estoque:
        print(
            f"ID: {produto['codigo']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | "
            f"Preço: {produto['preco']:.2f} | Quantidade em estoque: {produto['quantidade']}"
        )
    input("\nPressione Enter para voltar ao menu principal...")

def atualizar_produto():
    codigo = input("Digite o código do produto que deseja atualizar: ")

    produto = next((p for p in estoque if p["codigo"] == codigo), None)
    if not produto:
        print("Produto não encontrado!")
        input("\nPressione Enter para voltar ao menu principal...")
        return

    print("\nProduto encontrado:")
    print(
        f"ID: {produto['codigo']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | "
        f"Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
    )

    print("\nSelecione os campos que deseja atualizar:")
    print("[1] Nome")
    print("[2] Categoria")
    print("[3] Preço")
    print("[4] Quantidade")
    print("[5] Cancelar")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        novo_nome = input("Digite o novo nome do produto: ").strip()
        if novo_nome:
            produto["nome"] = novo_nome
            print("Nome atualizado com sucesso!")
        else:
            print("Erro: O nome não pode estar vazio!")
    elif opcao == 2:
        nova_categoria = input("Digite a nova categoria do produto: ").strip()
        if nova_categoria:
            produto["categoria"] = nova_categoria
            print("Categoria atualizada com sucesso!")
        else:
            print("Erro: A categoria não pode estar vazia!")
    elif opcao == 3:
        try:
            novo_preco = float(input("Digite o novo preço do produto: "))
            if novo_preco >= 0:
                produto["preco"] = novo_preco
                print("Preço atualizado com sucesso!")
            else:
                print("Erro: O preço não pode ser negativo!")
        except ValueError:
            print("Erro: Valor inválido para o preço!")
    elif opcao == 4:
        try:
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            if nova_quantidade >= 0:
                produto["quantidade"] = nova_quantidade
                print("Quantidade atualizada com sucesso!")
            else:
                print("Erro: A quantidade não pode ser negativa!")
        except ValueError:
            print("Erro: Valor inválido para a quantidade!")
    elif opcao == 5:
        print("Atualização cancelada.")
    else:
        print("Opção inválida!")

    salvar_dados(estoque)
    input("\nPressione Enter para voltar ao menu principal...")

def buscar_produto():
    while True:
        busca = input("Digite o ID ou nome do produto que deseja buscar: ").strip().lower()

        if len(busca) == 4:
            for produto in estoque:
                if produto["codigo"] == busca:
                    print(
                        f"ID: {produto['codigo']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | "
                        f"Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
                    )
                    input("\nPressione Enter para voltar ao menu principal...")
                    return
            print("Produto não encontrado! Tente novamente.")

        else:
            encontrados = [produto for produto in estoque if busca in produto["nome"].lower()]
            if encontrados:
                for produto in encontrados:
                    print(
                        f"ID: {produto['codigo']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | "
                        f"Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
                    )
                input("\nPressione Enter para voltar ao menu principal...")
                return
            else:
                print("Produto não encontrado! Tente novamente.")

def exibir_menu():
    print("\n   --- AgilStore ---")
    print("[1] Adicionar produto")
    print("[2] Listar produtos")
    print("[3] Atualizar produto")
    print("[4] Excluir produto")
    print("[5] Buscar produto")
    print("[6] Sair")

def opcoes():
    global estoque
    estoque = carregar_dados()

    while True:
        exibir_menu()
        opcao = int(input("Selecione uma das opções: "))

        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            excluir_produto()
        elif opcao == 5:
            buscar_produto()
        elif opcao == 6:
            print("Obrigado por usar o AgilStore!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    opcoes()
