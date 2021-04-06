# Bibliotecas
from time import sleep

# Cabeçalho
print('-=-'*8, end=''), print(' L O J A S  T E M D E T U D O ', end=''), print('-=-'*8)

valor = float(input('Qual o valor das compras? R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA EM DINHEIRO
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
opc = int(input('Digite a opção desejada: '))

sleep(0.3)
print('\033[:34mPROCESSANDO. . .\033[m')
sleep(1)

# Variavéis
des10 = valor*10/100
des5 = valor*5/100
juros = valor*20/100

# Solução
while opc > 4 or opc < 1:
    sleep(1)
    print('\033[:31m======== OPÇÃO INVÁLIDA ========\033[m')
    print('Digite uma das opções abaixo')
    print('''FORMAS DE PAGAMENTO:
[ 1 ] À VISTA DINHEIRO
[ 2 ] À VISTA CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')

    opc = int(input('Digite a opção desejada: '))
    sleep(0.3)
    print('\033[:34mPROCESSANDO. . .\033[m')
    sleep(1)

if opc == 1:
    print('''Para pagamentos à vista em dinheiro você recebe 10% de desconto! 
Portanto, a sua compra de \033[:34mR${:.2f}\033[m vai ficar por \033[:32mR${:.2f}\033[m'''.format(valor, valor-des10))

elif opc == 2:
    print('''Para pagamentos à vista com cartão você recebe 5% de desconto! 
Portanto, a sua compra de \033[:34mR${:.2f}\033[m vai ficar por \033[:32mR${:.2f}\033[m'''.format(valor, valor-des5))

elif opc == 3:
    print('Para pagamentos em até 2x no cartão suas compras não recebem juros. Aproveite!')

elif opc == 4:
    parc = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, (valor+juros)/parc))
    print(f'Sua compra de \033[:34mR${valor:.2f}\033[m vai custar \033[:33mR${valor+juros:.2f}\033[m no total.')
