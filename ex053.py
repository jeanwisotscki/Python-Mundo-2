frase = input('Escreva uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} fica assim {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um pálidromo!')
else:
    print('A frase não é um palíndromo')
