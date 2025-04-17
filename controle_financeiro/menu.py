from salvar_json import carregar_transacoes
from salvar_json import salvar_transacoes

def exibir_menu():

    print("\n------------Tabela Financeira------------")
    print("1 - Adicionar Transação")
    print("2 - Listar Transações")
    print("3 - Filtros de transações")
    print("0 - Sair")

def adicionar_receita():
    tipo = input("Qual o tipo de entrada (Receita ou Despesa): ").strip().lower()
    valor = float(input("Digite o valor que deseja salvar: "))
    categoria = input("Digite a categoria (ex: Alimentação, Transporte...): ").strip()
    descricao = input("Digite a descrição da entrada: ").strip()
    data = input("Data (formato YYYY-MM-DD): ").strip()

    transacao = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": data
    }

    salvar_transacoes(transacao)
    print("Transação salva com sucesso!")

def listar_transacoes():
    transacoes = carregar_transacoes()
    if not transacoes:
        print("Não existe nenhuma transação cadastrada ainda!")
        return
    
    print("\n------------Lista de Transações------------")
    for i, t in enumerate(transacoes, start=1):
        print(f"{i}. [{t['data']}] {t['tipo'].capitalize()} - {t['categoria']}: R${t['valor']} | {t['descricao']}")

def menu_filtros():

    print("\n------------Escolha a operação para a verificação------------")
    print("1 - Mês atual")
    print("2 - Mês específico")
    print("3 - De um mês até hoje")
    print("4 - Ano completo")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_transacoes_mes_atual()
    elif opcao == "2":
        mes_especifico()
    elif opcao == "3":
        mes_hoje
    elif opcao == "4":
        ano_completo()
    else:
        print("Escolha inválida, tente novamente")

def mostrar_transacoes_mes_atual():
    transacoes = mes_atual()

    if not transacoes:
        print("Nenhuma transação encontrada para este mês.")
        return
    
    print("\n------------Transações do mês atual------------")
    for i, t in enumerate(transacoes, start=1):
        print(f"{i}. [{t['data']}] {t['tipo'].capitalize()} - {t['categoria']}: R${t['valor']} | {t['descricao']}")

def executar():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            listar_transacoes()
        elif opcao == "3":
            menu_filtros()
        elif opcao == "0":
            print("Finalizando...")
            break
        else:
            print("Escolha inválida, tente novamente.")

if __name__ == "__main__":
    executar()