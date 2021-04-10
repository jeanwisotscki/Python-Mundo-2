# Bibliotecas
from datetime import date

# Cabeçalho e Variavéis
maior = 0
menor = 0
atual = date.today().year

# Solução
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc

    if idade >= 18:
        maior += 1
        
    elif idade < 18:
        menor += 1

print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade.'''.format(maior, menor))
