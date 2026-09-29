#Imprime o cardápio para primeira leitura do usuário
def mostrar_cardapio():
    print("\n     CARDÁPIO     ")
    print("1 - Hambúrguer ........ R$ 15,00")
    print("2 - Pizza ............. R$ 25,00")
    print("3 - Refrigerante ...... R$  6,00")
    print("4 - Batata Frita ...... R$ 10,00")
    print("5 - Sorvete ........... R$  8,00")
    print("0 - Finalizar pedido")

#Verifica o código escolhido pelo usuário e retorna com o preço do produto
def obter_preco(codigo):
    if codigo == 1:
        return 15
    elif codigo == 2:
        return 25
    elif codigo == 3:
        return 6
    elif codigo == 4:
        return 10
    elif codigo == 5:
        return 8
    else:
        return 0

#Verifica o código escolhido pelo usuário e retorna com o nome do produto
def obter_nome_produto(codigo):
    if codigo == 1:
        return "Hambúrguer"
    elif codigo == 2:
        return "Pizza"
    elif codigo == 3:
        return "Refrigerante"
    elif codigo == 4:
        return "Batata Frita"
    elif codigo == 5:
        return "Sorvete"
    else:
        return "Desconhecido"

#Calcula o desconto com base no valor total do pedido
def calcular_desconto(total):
    if total < 50:
        percentual = 0
    elif total < 100:
        percentual = 5
    else:
        percentual = 10

    valor_desconto = total * percentual / 100
    valor_final = total - valor_desconto

    return percentual, valor_desconto, valor_final

#Imprime o cabeçalho do sistema e solicita o nome do cliente
print("     SISTEMA DE PEDIDOS     ")
nome = input("Digite o nome do cliente: ")
#define as variáveis para o total do pedido e a quantidade de itens
total = 0
itens = 0
#Loop principal do sistema de pedidos
while True:
    mostrar_cardapio()
#Recebe o código do produto para incluir no pedido
    try:
        codigo = int(input("\nEscolha um produto: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if codigo == 0:
        break
#Exibe erro ao código do produto não cadastrado e retorna a opção de escolha
    if codigo < 1 or codigo > 5:
        print("Produto inválido!")
        continue
#Recebe a quantidade do item solicitado
    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if quantidade <= 0:
        print("Quantidade inválida!")
        continue

    preco = obter_preco(codigo)
    produto = obter_nome_produto(codigo)

    subtotal = preco * quantidade

    total += subtotal
    itens += quantidade
#Exibe o último produto adicionado ao pedido
    print(f"\nProduto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Subtotal: R$ {subtotal:.2f}")
#Exibe quantidade de produtos no pedido e o valor total acumulado até o momento
    print("\n--- RESUMO PARCIAL ---")
    print(f"Itens acumulados: {itens}")
    print(f"Total acumulado: R$ {total:.2f}")

percentual, valor_desconto, valor_final = calcular_desconto(total)
#Exibe opções de pagamento
print("\n     PAGAMENTO     ")
print("1 - Dinheiro")
print("2 - PIX")
print("3 - Cartão")
#loop para garantir que o usuário escolha uma forma de pagamento válida
while True:
    try:
        pagamento = int(input("Escolha a forma de pagamento: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if pagamento == 1:
        forma_pagamento = "Dinheiro"
        break
    elif pagamento == 2:
        forma_pagamento = "PIX"
        break
    elif pagamento == 3:
        forma_pagamento = "Cartão"
        break
    else:
        print("Opção inválida! Tente novamente.")
#Exibe o resumo final do pedido como uma nota fiscal, incluindo o nome do cliente, quantidade total de itens, valor original, desconto aplicado, valor do desconto, valor final e forma de pagamento
print("\n     RESUMO DO PEDIDO     ")
print(f"Cliente: {nome}")
print(f"Quantidade total de itens: {itens}")
print(f"Valor original: R$ {total:.2f}")
print(f"Desconto aplicado: {percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
#Agradecimento formal pela compra
print("\nA equipe da Pizzaria e Hamburgueria Requintados agradece sua preferência!")