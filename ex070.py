####################################################
#     Estatísticas em produtos com while True:     #
####################################################

'''
    Exercício Python 70: Crie um programa que leia o
    nome e o preço de vários produtos. O programa
    deverá perguntar se o usuário vai continuar ou
    não. No final, mostre:

    A) qual é o total gasto na compra.

    B) quantos produtos custam mais de R$1000.

    C) qual é o nome do produto mais barato.
'''

# Cabeçalho
print('~'*35)
print('        LOJA BARATO LEGAL')
print('~'*35)

# Variavéis
cont = 0
m_barato = 0
soma = 0
n_barato = ' '
totmil = 0

# Solução
while True:
    nome = input('Nome do produto: ').strip().title()
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1

    if preco >= 1000:
        totmil += 1

    if cont == 1 or preco < m_barato:
        m_barato = preco
        n_barato = nome

    resp = input('Quer continuar: [S/N] ').lower().strip()[0]

    while resp not in 'sn':
        resp = input('Quer continuar: [S/N] ').lower().strip()[0]

    if resp == 'n':
        break

print(f'O valor total das suas compras é de R${soma:.2f}')
print(f'Foram registrados {totmil} produtos com o valor superior a R$1000,00')
print(f'O produto mais barato registrado foi {n_barato} custando R${m_barato:.2f}')
