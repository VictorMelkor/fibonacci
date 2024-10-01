# Programa para verificar se um número faz parte da sequência de fibonacci
import os

n1 = 0
n2 = 1
n = 0


os.system('cls')
print('-'*50)
print('VERIFICADOR FIBONACCI'.center(50))
print('-'*50)

num = int(input('Digite o número que quer verificar: '))
print()

if num == n1 or num == n2:
    print('Esse número faz parte da Sequência de Finabocci')
else:
    while n <= num:
        n = n1 + n2
        n1 = n2
        n2 = n
        if n == num:
            print('Esse número FAZ parte da Sequência de Fibonacci')
            break
    if n != num:
        print('Esse número NÃO faz parte da Sequência de Fibonacci')

print()        
print('-'*50)
print('Essa é a sequência de fibonacci até o 15ª termo: ')
n1 = 0
n2 = 1


for c in range(1,16):
    print(n1, end=' ')
    n = n1 + n2
    n1 = n2
    n2 = n
print()
print('-'*50)
