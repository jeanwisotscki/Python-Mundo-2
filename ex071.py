'''
    Exercício Python 071: Crie um programa que simule o funcionamento
     de um caixa eletrônico. No início, pergunte ao usuário qual será
     o valor a ser sacado (número inteiro) e o programa vai informar
     quantas cédulas de cada valor serão entregues. OBS:

    considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

# Cabeçalho
print('='*30)
print("{:^30}".format("CAIXA ELETRÔNICO"))
print('='*30)

# Solução
saque = int(input('Digite o valor do saque: '))
total = saque # Montante total que será decomposto
nota = 50 # Tirar 50 reais do montante
totalnotas = 0

while True:
    if total >= nota:
        total -= nota
        totalnotas += 1

    else:
        if totalnotas > 0:
            print('Total de {} notas de R$ {}' .format(totalnotas, nota))

        if nota == 50:
            nota = 20

        elif nota == 20:
            nota = 10

        elif nota == 10:
            nota = 1

        totalnotas = 0

        if total == 0:
            break
            
print('~'*30)
print('{:-^30}'.format(' BANCO BOX '))
print('~'*30)