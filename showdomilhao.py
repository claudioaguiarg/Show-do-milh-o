import random
from time import sleep

perguntas = ['1','2','3','4','5']
i = 's'
p = 0

while (i == 's' or i == 'S'):
    rodada=(random.choice(perguntas))
    print(rodada)
    print(i)
    if rodada == '1':
        print('Saldo: R${}'.format(p))
        i = (input('vc quer parra?'))
        perguntas.remove('1')
        p = p + 1

    if rodada == '2':
        print('Saldo: R${}'.format(p))
        i = (input('tem verteza'))
        perguntas.remove('2')
        p = p + 1


    if rodada == '3':
        print('Saldo: R${}'.format(p))
        i = (input('tem verteza'))
        perguntas.remove('3')
        p = p + 1

    if rodada == '4':
        print('Saldo: R${}'.format(p))
        i = (input('tem verteza'))
        perguntas.remove('4')
        p = p + 1

    if rodada == '5':
        print('Saldo: R${}'.format(p))
        i = (input('tem verteza'))
        perguntas.remove('5')
        p = p + 1

    if p == 5:
        print('Saldo: R${}'.format(p))
        exit()

    i = input('deseja continuar?')
