# Colhendo dados:
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

# Solução
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos a cima \033[:32mPODEM FORMAR\033[m  um triângulo!')
    if n1 == n2 == n3:
        print('Do tipo: \033[:34mEQUILÁTERO\033[m')
    elif n1 != n2 != n3 != n1:
        print('Do tipo: \033[:34mESCALENO\033[m')
    else:
        print('Do tipo: \033[:34mISÓCELES\033[m')
else:
    print('Esses segmentos \033[:31mNÃO PODEM FORMAR\033[m um triângulo!')
