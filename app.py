import mysql.connector

# Configurações da conexão

host = "sistema88.ddns.net"
port = 50505
database = "DB88"
username = input("Seu usuario: ")
password = input("Sua senha: ")

connection = mysql.connector.connect(
    host=host,
    port=port,
    database=database,
    user=username,
    password=password
)


while True:
    menu = {
    1:"Registrar venda",
    2:"Verificar estoque",
    3:"Registrar compra",
    4:"Atualizar dados",
    5:"Analisar históricos",
    6:"Sair"
    }

    for foo, bar in menu.items():
        print(f"[{foo}] {bar}")

    foo = int(input("O que você quer fazer? : "))

    if foo == 1:

        ask = input("Registrar cliente Primeiro? (s/n):")
        if ask == "s":

            cliente = []
            venda = []
            itens_venda = []

            # inputando dados do cliente
            cliente.append(input("Nome: "))
            cliente.append(input("Bairro: "))
            cliente.append(input("Sexo: "))
            cliente.append(input("Contato: "))
            cliente.append(input("Captação: "))

            # inputando dados da venda
           #venda.append(id_cliente)
            venda.append(input("Data: "))
            venda.append(input("Hora: "))
            venda.append(input("Canal de aquisição: "))
            venda.append(input("Forma de recebimento: "))
            venda.append(input("Valor faturado: "))
            venda.append(input("Taxa de entrega: "))

            # inputando os dados de cada item na venda
            while True:
                item = []
                item.append("SKU: ")
                item.append("Quantidade: ")
                item.append("Preço unitário: ")
                item.append("Taxa de entrega: ")
                itens_venda.append(item)

                ask = input("Registrar +1 item? (s/n): ")
                if ask == "s":
                    pass
                break

            # estabelecendo conexão com o banco de dados
            # escrevendo no banco de dados

            # atualizando o estoque

        if ask == "n":

            venda = []
            itens_venda = []

            # inputando dados da venda
            venda.append(input("id_cliente: "))
            venda.append(input("Data: "))
            venda.append(input("Hora: "))
            venda.append(input("Canal de aquisição: "))
            venda.append(input("Forma de recebimento: "))
            venda.append(input("Valor faturado: "))
            venda.append(input("Taxa de entrega: "))

            # inputando os dados de cada item na venda
            while True:
                item = []
                item.append("SKU: ")
                item.append("Quantidade: ")
                item.append("Preço unitário: ")
                item.append("Taxa de entrega: ")
                itens_venda.append(item)

                ask = input("Registrar +1 item? (s/n): ")
                if ask == "s":
                    pass
                break

            # escrevendo no banco de dados

            # atualizando o estoque

    if foo == 2:
        # Consultar o estoque
        print("essa etapa está em desenvolvimento!")

    if foo == 3:
        ask = input("Registrar produto(s) primeiro? (s/n):")
        if ask == "s":

            produtos = []
            compra = []
            itens_compra = []

            # inputando dados do(s) produto(s)
            while True:
                produto = []
                produto.append("Marca: ")
                produto.append("Modelo: ")
                produto.append("Categoria: ")
                produto.append("Variação: ")
                produtos.append(produto)

                ask = input("Registrar +1 item? (s/n): ")
                if ask == "s":
                    pass
                break

            # inputando dados da compra
            compra.append(input("App: "))
            compra.append(input("Conta: "))
            compra.append(input("Forma de pagamento: "))
            compra.append(input("Data da compra: "))
            compra.append(input("Data da entrega: "))
            compra.append(input("Custo base: "))
            compra.append(input("Frete: "))
            compra.append(input("Impostos: "))
            compra.append(input("Custo final: "))

            # inputando os dados de cada item na compra
            while True:
                item = []
                item.append("SKU: ")
                item.append("Fornecedor: ")
                item.append("Cód. de rastreio: ")
                item.append("Status: ")
                item.append("Quantidade: ")
                item.append("Custo-base unitário: ")
                itens_compra.append(item)

                ask = input("Registrar +1 item? (s/n): ")
                if ask == "s":
                    pass
                break

            # escrevendo no banco de dados

            # atualizando o estoque

        if ask == "n":

            # inputando dados da compra
            compra.append(input("App: "))
            compra.append(input("Conta: "))
            compra.append(input("Forma de pagamento: "))
            compra.append(input("Data da compra: "))
            compra.append(input("Data da entrega: "))
            compra.append(input("Custo base: "))
            compra.append(input("Frete: "))
            compra.append(input("Impostos: "))
            compra.append(input("Custo final: "))

            # inputando os dados de cada item na compra
            while True:
                item = []
                item.append("SKU: ")
                item.append("Fornecedor: ")
                item.append("Cód. de rastreio: ")
                item.append("Status: ")
                item.append("Quantidade: ")
                item.append("Custo-base unitário: ")
                itens_compra.append(item)

                ask = input("Registrar +1 item? (s/n): ")
                if ask == "s":
                    pass
                break

            # escrevendo no banco de dados

            # atualizando o estoque

    elif foo == 4:
        print("essa etapa está em desenvolvimento!")

    elif foo == 5:
        print("essa etapa está em desenvolvimento!")

    else:
        print("o número caractere digitado não se refere a nenhuma das opções, tente novamente")
        # volta para o início

# Fecha a conexão
connection.close()