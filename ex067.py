###################################################
#            TABUADA v3.0 com while True:         #
###################################################

'''
    Exercício Python 67: Faça um programa que mostre
    a tabuada de vários números, um de cada vez, para
    cada valor digitado pelo usuário. O programa será
    interrompido quando o número solicitado for
    negativo ou igual á 0.
'''

# Solução
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('~'*42)

    if n <= 0:
        msg = 'PROGRAMA ENCERRADO'
        print(f'{msg:^42}')
        print('x' * 42)
        break

    for c in range(1, 11):
        res = n * c
        print(f'{n} x {c} = {res}')

    print('~'*42)
