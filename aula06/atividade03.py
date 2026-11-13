#uma loja está realizando uma campanha de desconto e precisa automatizar o calculo do valor final das compras. desenvolva um programa em python que percorra 5 vendas utilizando a estrutura for. para cada venda, o programa devera solicitar
#o valor da compra e verificar as seguites condições: compras a partir de R$ 200,00 recebem 10% de desconto; Compras abaixo de R$ 200,00 não recebem desconto; O programa devera calcular o desconto e apresentar o valor final da compra
# ao termino de cinco venda

compra = float(input('qual o valor? '))

for i in range(5):
    match compra:
        case compra if compra >=200:
            desconto = compra * 0.10
            valor_final = compra - desconto
            print(f'o valor da sua compra é: {compra} você tem direito a 10% de desconto e o valor total da sua compra é: \n{valor_final}')
            case compra if compra < 200:
                print(f'o valor da sua compra é: {compra} você não tem direito a desconto.')
