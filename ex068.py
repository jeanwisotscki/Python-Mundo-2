###################################################
#          PAR OU ÍMPAR COM while True:           #
###################################################

'''
    Exercício Python 68: Faça um programa que jogue
    par ou ímpar com o computador. O jogo só será
    interrompido quando o jogador perder, mostrando
    o total de vitórias consecutivas que ele
    conquistou no final do jogo.
'''

# Bibliotecas
from random import randint

# Cabeçalho
print('-=-'*15)
print('           VAMOS JOGAR PAR OU ÍMPAR ')
print('-=-'*15)

# Variavéis
vitorias = 0

# Solução
while True:
    jogador = int(input('Digite um valor: '))

    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '

    while tipo not in 'PI':
        tipo = input('Par ou ìmpar? [P/I] ').strip().upper()[0]

    print(f'voce jogou {jogador} e o computador {comp}, totalizando {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1

        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1

        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente. . .')
print(f'GAME OVER! Você venceu {vitorias} vezes')
