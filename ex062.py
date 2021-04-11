# Progressão Aritmética V3

print('Gerador de P.A')
print('='*20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da P.A: '))

#Variáveis
termo = primeiro
cont = 1
total = 0
mais = 10

#Solução
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA. . .')
    mais = int(input('Digite quantos termos ainda quer mostrar: '))

print('A contagem foi finalizada com {} termos nos total'.format(total))
