from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('='*36)
    print('''Escolha uma das opções abaixo
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('='*36)
        print('O resultado de {} + {} é {}'.format(n1, n2, soma))
        sleep(1)

    elif opcao == 2:
        produto = n1 * n2
        print('=' * 36)
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
        sleep(1)

    elif opcao == 3:
        if n1 > n2:
            maior = n1

        else:
            maior = n2

        print('=' * 36)
        print('O maior valor entre {} e {} é {}'.format(n1 , n2, maior))
        sleep(1)

    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizando. . .')
        sleep(1)

    else:
        print('Opção inválida, digite uma opção válida.')
    sleep(1)

print('Programa finalizado com sucesso!')
