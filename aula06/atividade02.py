#digite o numero, na saida tem que aparecer o dobro, o triple e o quadrado desse numero.

# num = float(input('indique um numero: '))

# dobro = num * 2
# triplo = num * 3
# quadrado = num * num
#quadrado tambem pode ser representado com ** 2, ao cubo ** 3 

#print(f'o seu numero a4o dobro é {dobro}\no seu numero triplo é {triplo} \no seu numero ao quadrado é {quadrado}')

#-------------------------------------------------------- // ------------------------------------- // --------------------------------------------------------------

#estrutura de repetição
#laço for
for i in range(3):
    print(f'\nRodada {i + 1}')
    num = float(input('indique um numero: '))
    dobro = num * 2
    triplo = num * 3
    quadrado = num * num
    print(f'o seu numero ao dobro é {dobro} \no seu numero triplo é {triplo} \no seu numero ao quadrado é {quadrado}')