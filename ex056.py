# Variavéis
soma_idade = 0
media_idade = 0
idade_homem = 0
nome_homem = 0
total_mulheres = 0

for pessoas in range(1, 5):

    print('------ {}ª PESSOA ------'.format(pessoas))
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade

    if pessoas == 1 and sexo in 'Mm':
        idade_homem = idade
        nome_homem = nome

    if sexo in 'Mm' and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome

    if sexo in 'Ff' and idade <20:
        total_mulheres += 1

media_idade = soma_idade / 4

print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_homem, idade_homem))
print('Ao todo são {} mulheres com menos de 20 anos de idade.'.format(total_mulheres))
