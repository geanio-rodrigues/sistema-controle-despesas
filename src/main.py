from datetime import datetime
from models.categoria import Categoria
from models.receita import Receita
from models.despesa import Despesa
from models.orcamento_mensal import OrcamentoMensal


categorias = []
orcamento = OrcamentoMensal(mes=datetime.now().month, ano=datetime.now().year)


def escolher_categoria(tipo):
    filtradas = [c for c in categorias if c.tipo == tipo]

    if not filtradas:
        print("Nenhuma categoria cadastrada para esse tipo.")
        return None
    
    for i, cat in enumerate(filtradas, start=1):
        print(f"{i} - {cat.nome}")
    
    escolha = int(input("Escolha a categoria: "))
    return filtradas[escolha - 1]


def cadastrar_categoria():
    nome = input("Nome da categoria: ")
    tipo = input("Tipo (RECEITA ou DESPESA): ").upper()

    limite = None
    if tipo == "DESPESA":
        limite = float(input("Limite mensal (ou 0 para sem limite): "))
        if limite == 0:
            limite = None

    categoria = Categoria(nome, tipo, limite)
    categorias.append(categoria)
    print("Categoria cadastrada com sucesso!")


def adicionar_receita():
    valor = float(input("Valor da receita: "))
    descricao = input("Descrição: ")
    forma_pagamento = input("Forma de pagamento: ")

    categoria = escolher_categoria("RECEITA")
    if not categoria:
        return
    
    receita = Receita(
        id=len(orcamento.lista_lancamentos) + 1,
        valor=valor,
        data=datetime.now().date(),
        descricao=descricao,
        forma_pagamento=forma_pagamento
    )

    orcamento.adicionar_lancamento(receita)
    print("Receita adicionada!")


def adicionar_despesa():
    valor = float(input("Valor da despesa: "))
    descricao = input("Descrição: ")
    forma_pagamento = input("Forma de pagamento: ")

    categoria = escolher_categoria("DESPESA")
    if not categoria:
        return

    despesa = Despesa(
        id=len(orcamento.lista_lancamentos) + 1,
        valor=valor,
        data=datetime.now().date(),
        descricao=descricao,
        categoria=categoria,
        forma_pagamento=forma_pagamento
    )

    orcamento.adicionar_lancamento(despesa)
    print("✅ Despesa adicionada!")


def listar_categorias():
    if not categorias:
        print("⚠️ Nenhuma categoria cadastrada.")
        return

    for cat in categorias:
        print(cat)


def mostrar_resumo():
    print("\n📊 RESUMO MENSAL")
    print(f"Total de receitas: R$ {orcamento.total_receitas:.2f}")
    print(f"Total de despesas: R$ {orcamento.total_despesas:.2f}")
    print(f"Saldo disponível: R$ {orcamento.saldo_consolidado:.2f}")


# MENU PRINCIPAL
def menu():
    while True:
        print("\n===== SISTEMA DE CONTROLE DE DESPESAS =====")
        print("1 - Cadastrar categoria")
        print("2 - Listar categorias")
        print("3 - Adicionar receita")
        print("4 - Adicionar despesa")
        print("5 - Ver resumo mensal")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_categoria()
        elif opcao == "2":
            listar_categorias()
        elif opcao == "3":
            adicionar_receita()
        elif opcao == "4":
            adicionar_despesa()
        elif opcao == "5":
            mostrar_resumo()
        elif opcao == "0":
            print("👋 Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    menu()