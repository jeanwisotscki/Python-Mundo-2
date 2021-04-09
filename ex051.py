# Progressão Aritmética

print('='*25)
print(' 10 TERMOS DE UMA P.A ')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao

for cont in range(termo, decimo + razao, razao):
    print(cont, end=' → ')
    
print('Acabou...')
