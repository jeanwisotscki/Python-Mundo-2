'''
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e
    qual foi o maior e o menor valores lidos. O programa deve
    perguntar ao usuário se ele quer ou não continuar a digitar
    valores.
'''

# Variáveis
menor = 999999999 # Mais a frente no curso, isso será corrigido
maior = 0
media = 0
cont = 0

# Solução
while True:
    num = int(input('Digite um número inteiro maior que "0": '))

    cont += 1
    media += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    res = input('Quer continuar? [S/N] ').strip().upper()[0]

    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()[0]

    if res == 'N':
        break

print(f'A média dos valores digitados é: {media/cont:.2f}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
