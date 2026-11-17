#uma loja está realizando uma campanha de desconto e precisa automatizar o calculo do valor final das compras. desenvolva um programa em python que percorra 5 vendas utilizando a estrutura for. para cada venda, o programa devera solicitar
#o valor da compra e verificar as seguites condições: compras a partir de R$ 200,00 recebem 10% de desconto; Compras abaixo de R$ 200,00 não recebem desconto; O programa devera calcular o desconto e apresentar o valor final da compra
# ao termino de cinco venda
for venda in range(5):
    valor = float(input('\nqual o valor da compra? '))

    if valor >= 200:
        desconto = valor * 0.10
    else:
        desconto = 0
    

    valor_final = valor - desconto

    print(f'desconto de R$: {desconto}')
    print(f'total a pagar de R$: {valor_final}')