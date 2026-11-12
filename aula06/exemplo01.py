#uma loja oferece diferentes descontos de acordo com a forma de pagamento escolhida pelo cliente. crie um algoritmo
#que solicite o valor da compra,apresente as opções de pagamento e permita que o cliente escolha uma delas.
#pix oferece 12% de desconto; debito 8% de desconto; credito oferece 5% de desconto; dinheiro oferece 15% de desconto.

valor = float(input('valor da venda: '))

print('''
[1] - Pix (12% de desconto)
[2] - debito (8% de desconto)
[3] - credito (5% de desconto)
[4] - dinheiro (15% de desconto)
''')

operacao = True
desconto = 0
opcao = int(input('informe a opção escolhida: '))

match opcao:
    case 1:
        print('----- PIX -----') 
        desconto = valor * 0.12
    case 2:
        print('----- DEBITO -----') 
        desconto = valor * 0.08
    case 3:
        print('----- CREDITO -----')
        desconto = valor * 0.05 
    case 4:
        print('----- Dinheiro -----') 
        desconto = valor * 0.15
    case _:
        operacao == False
        print('Invalido')

if opcao in [1, 2, 3, 4]:
#if operacao == True:
#if desconto != 0:
    valor_final = valor - desconto
    print(f'preço: {valor}')
    print(f'desconto: {desconto}')
    print(f'total a pagar: {valor_final}')

else:
    print('Por favor, escolha uma das opções acima: ')
