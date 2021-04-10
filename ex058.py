# ================== JOGO DA ADIVINHAÇÃO ======================

# Bibliotecas
from random import choice # Faz a escolha aleatória
from time import sleep # Faz o delay nas escritas exibidas no console

# Variavéis
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resposta = choice(lista)
tentativas = 1

# Cabeçalho
print('\033[:1m -=-'*20)
print('\033[:35m           Vou pensar em um número entre 0 e 10. Tente adivinhar. . .')
print('\033[:1m -=-'*20)
num = int(input('Digite o seu palpite: '))
print('\033[:34mPROCESSANDO. . .\033[m')
sleep(1.3)

# Solução
while num != resposta:

    if resposta > num:
        print('\033[:32mUm pouco mais. . .\033[m')

    if resposta < num:
        print('\033[:32mUm pouco menos. . .\033[m')

    if num > 10:
        print('\033[:31mNÚMERO INVÁLIDO!\033[m Digite um número entre 0 e 10.\033[m')

    num = int(input('\033[mDigite novamente: \033[m'))
    print('\033[:34mPROCESSANDO. . .\033[m')
    sleep(1)
    tentativas += 1

print('\033[:32mVOCE ACERTOU!\033[m Você usou \033[:34m{}\033[m palpites para acertar.'.format(tentativas))
