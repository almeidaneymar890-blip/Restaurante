import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurantes = []

print("""
███╗░░██╗███████╗██╗░░░██╗███╗░░░███╗░█████╗░██████╗░███████╗░██████╗
████╗░██║██╔════╝╚██╗░██╔╝████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝
██╔██╗██║█████╗░░░╚████╔╝░██╔████╔██║███████║██████╔╝█████╗░░╚█████╗░
██║╚████║██╔══╝░░░░╚██╔╝░░██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝░░░╚═══██╗
██║░╚███║███████╗░░░██║░░░██║░╚═╝░██║██║░░██║██║░░██║███████╗██████╔╝
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░ """)

def menu():
    while True:
        print("\n" + "="*30) 
        print("1. Cadastrar restaurante")
        print("2. Listar restaurantes")
        print("3. Alternar estado do restaurante")
        print("4. Adicionar avaliação")
        print("5. Adicionar item ao cardápio")
        print("6. Exibir cardápio")
        print("7. Sair")
        print("="*30)
    
        try:
            opcao = int(input('Escolha uma opção: '))
            
            if opcao == 1:
                cadastrar_restaurante()
            elif opcao == 2:
                listar_restaurantes()
            elif opcao == 3:
                alternar_estado_restaurante()
            elif opcao == 4:
                adicionar_avaliacao()
            elif opcao == 5:
                adicionar_item_cardapio()
            elif opcao == 6:
                exibir_cardapio()
            elif opcao == 7:
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida! Escolha um número de 1 a 7.")
        except ValueError:
            print("Por favor, digite apenas números.")

def cadastrar_restaurante():
    print("\n" + "="*30)
    print("CADASTRAR NOVO RESTAURANTE")
    print("="*30)

    nome = input("Digite o nome do restaurante: ").strip()
    categoria = input("Digite a categoria (ex: Italiana, Japonesa): ").strip()
    
    if nome and categoria:
    
        novo_restaurante = {
            "nome": nome,
            "categoria": categoria,
            "ativo": False,
            "avaliacoes": [],
            "cardapio": []
        }
        restaurantes.append(novo_restaurante)
        print(f"Restaurante '{nome}' cadastrado com sucesso!")
    else:
        print("Nome e categoria não podem ser vazios.")

def listar_restaurantes():
    print("\n=== LISTA DE RESTAURANTES ===")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
        return False
    
    for i, r in enumerate(restaurantes, 1):
        status = "Ativo" if r["ativo"] else "Inativo"
        
        if r["avaliacoes"]:
            media = sum(r["avaliacoes"]) / len(r["avaliacoes"])
            media_str = f" {media:.1f}"
        else:
            media_str = "Sem avaliações"
            
        print(f"{i}. {r['nome']} ({r['categoria']}) - [{status}] - {media_str}")
    return True

def alternar_estado_restaurante():
    if not listar_restaurantes():
        return
    try:
        idx = int(input("\nDigite o número para alterar o status: ")) - 1
        if 0 <= idx < len(restaurantes):
            
            restaurantes[idx]["ativo"] = not restaurantes[idx]["ativo"]
            status_atual = "Ativo" if restaurantes[idx]["ativo"] else "Inativo"
            print(f"Status alterado para [{status_atual}] com sucesso!")
        else:
            print("Restaurante não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def adicionar_avaliacao():
    if not listar_restaurantes():
        return
    try:
        idx = int(input("\nNúmero do restaurante a avaliar: ")) - 1
        if 0 <= idx < len(restaurantes):
            nota = int(input("Nota (1 a 5): "))
            if 1 <= nota <= 5:
                restaurantes[idx]["avaliacoes"].append(nota)
                print("Avaliação adicionada!")
            else:
                print("Nota deve ser entre 1 e 5.")
        else:
            print("Restaurante não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def adicionar_item_cardapio():
    if not listar_restaurantes():
        return
    try:
        idx = int(input("\nNúmero do restaurante para o cardápio: ")) - 1
        if 0 <= idx < len(restaurantes):
            print("1. Prato\n2. Bebida")
            tipo = int(input("Escolha o tipo de item: "))
            
            nome_item = input("Nome do item: ")
            preco = float(input("Preço: R$ "))
            
            if tipo == 1:
                descricao = input("Descrição do prato: ")
                item = {"tipo": "Prato", "nome": nome_item, "preco": preco, "detalhe": descricao}
            elif tipo == 2:
                tamanho = input("Tamanho da bebida (ex: 350ml): ")
                item = {"tipo": "Bebida", "nome": nome_item, "preco": preco, "detalhe": tamanho}
            else:
                print("Tipo inválido.")
                return
                
            restaurantes[idx]["cardapio"].append(item)
            print("Item adicionado ao cardápio!")
        else:
            print("Restaurante não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def exibir_cardapio():
    if not listar_restaurantes():
        return
    try:
        idx = int(input("\nNúmero do restaurante para exibir: ")) - 1
        if 0 <= idx < len(restaurantes):
            r = restaurantes[idx]
            print(f"\n=== CARDÁPIO DO RESTAURANTE: {r['nome'].upper()} ===")
            
            if not r["cardapio"]:
                print("Cardápio ainda está vazio.")
                return
                
            for item in r["cardapio"]:
                if item["tipo"] == Prato:
                    print(f" {item['nome']} - R$ {item['preco']:.2f} | Descrição: {item['detalhe']}")
                elif item["tipo"] == Bebida:
                    print(f" {item['nome']} - R$ {item['preco']:.2f} | Tamanho: {item['detalhe']}")
        else:
            print("Restaurante não encontrado.")
    except ValueError:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
