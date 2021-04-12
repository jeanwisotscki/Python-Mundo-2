###################################################
#        Cadastro de dados com while True:        #
###################################################

'''
    Exercício Python 69: Crie um programa que leia
    a idade e o sexo de várias pessoas. A cada
    pessoa cadastrada, o programa deverá perguntar
    se o usuário quer ou não continuar. No final,
    mostre:

        A) quantas pessoas tem mais de 18 anos.

        B) quantos homens foram cadastrados.

        C) quantas mulheres tem menos de 20 anos.
'''

# Variavéis
total_mais18 = 0
total_homem = 0
mulheres_menos20 = 0

# Solução
while True:
    print('~'*30)
    print('     CADASTRO DE DADOS')
    print('~'*30)

    idade = int(input('Idade: '))

    if idade >= 18:
        total_mais18 += 1

    sexo = input('Sexo [M/F]: ').strip().upper()[0]

    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    if sexo == 'M':
            total_homem += 1

    elif sexo == 'F' and idade < 20:
            mulheres_menos20 += 1

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]

    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        print('============== FIM DO PROGRAMA ==============')
        print(f'Ao todo temos \033[34m{total_mais18}\033[m pessoas com mais de 18 anos.')
        print(f'Foram cadastrados um total de \033[34m{total_homem}\033[m homens.')
        print(f'E temos \033[34m{mulheres_menos20}\033[m mulheres com menos de 20 anos.')
        print('============== ~~~~~~~~~~~~~~~ ==============')
        break
