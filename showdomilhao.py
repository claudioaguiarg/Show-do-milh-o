import random
from time import sleep

import pygame

perguntas = ['1','2','3','4','5']
i = 's'
p = 0

pygame.init()

pygame.mixer.music.load('sounds/abertura.mp3')
pygame.mixer.music.play()
input('vc escuta?s')

#-------Sistema de perguntas---------#
while (i == 's' or i == 'S'):
    rodada=(random.choice(perguntas))
    print(rodada)
    print(i)
    if rodada == '1':
        print('Saldo: R${}'.format(p))
        print('Qual bicho transmite Doença de Chagas?')
        print('A) Pulga\nB) Barebeiro\nC) Barata\nD) Abelha')
        r=input('Digite a letra da resposta: ')
        if r == 'B' or r == 'b':
            p = p + 1
            print('Você Acertou!')
            print('Saldo: R${}'.format(p))
        else:
            print('VocÊ errou!')
            print('Saldo: R${}'.format(p))
        i = (input('vc quer continuar?'))
        perguntas.remove('1')

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
