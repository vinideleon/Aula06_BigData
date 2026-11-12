#desenvolva um programa que solicite o valor de um ingresso e permita ao usuario escolher o tipo de entrada.
#as opções disponiveis são: 1- inteira (sem desconto); 2- meia entrada (50% de desconto); 3- promoção(30% de desconto);
#de acordo com as opções escolhida, o programa deve calcular e exibir o valor final do ingresso. caso o usuario informe
#uma opção invalida, o programa deve exibir uma mensagem informando o erro.

ingresso = float(input('informe o valor do ingresso: '))

print('''
[1] - inteira (sem desconto)
[2] - meia entrada (50% de desconto)
[3] - promoção (30% de desconto)
''')

desconto = 0
opcao = int(input('informe a opção desejada: '))

match opcao:
    case 1:
        print('Sem desconto')
    case 2:
        print('50% de desconto')
        desconto = ingresso * 0.50
    case 3:
        print('30% de desconto')
        desconto = ingresso * 0.30
    case _:
        print('ERRO')

if opcao in [1 , 2 , 3 ]:
    valor_final = ingresso - desconto
    print(f'o valor do seu ingresso é {ingresso}.\no valor do seu desconto é {desconto}.\no valor total é {valor_final}. ')
else:
    print('escolha uma das opções acima: ')