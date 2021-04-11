# Tratando valores

#Variáveis
cont = soma = 0

#Solução
print('[DIGITE 999 PARA PARAR]')
n = int(input('Digite um número: '))

while n != 999:
    soma += n
    cont += 1
    print('[DIGITE 999 PARA PARAR]')
    n = int(input('Digite um número: '))

print('você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
