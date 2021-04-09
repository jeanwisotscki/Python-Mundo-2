# Bibliotecas
from time import sleep
from random import choice

# Cabeçalho
print('''Escolha seu lance
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

# Solução
lance = int(input('Digite seu lance: '))

if lance == 1:
    lance = 'PEDRA'

elif lance == 2:
    lance = 'PAPEL'

elif lance == 3:
    lance = 'TESOURA'

sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(lista)

print('-=-'*10)
print('Computador jogou {}'.format(comp))
print('Você jogou {}'.format(lance))
print('-=-'*10)

if comp == lance:
    print('EMPATE')

elif comp == 'PEDRA' and lance == 'TESOURA':
    print('COMPUTADOR VENCEU')

elif comp == 'TESOURA' and lance == 'PEDRA':
    print('VOCÊ VENCEU')

elif comp == 'PAPEL' and lance == 'PEDRA':
    print('COMPUTADOR VENCEU')

elif comp == 'PEDRA' and lance == 'PAPEL':
    print('VOCÊ VENCEU')

elif comp == 'TESOURA' and lance == 'PAPEL':
    print('COMPUTADOR VENCEU')

elif comp == 'PAPEL' and lance == 'TESOURA':
    print('VOCÊ VENCEU')

else:
    print('\033[:31m============ LANCE INVÁLIDO ============')
