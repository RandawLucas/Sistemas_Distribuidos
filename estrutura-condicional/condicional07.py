numero1 = int(input('Digite o valor 1: '))
numero2 = int(input('Digite o valor 2: '))
numero3 = int(input('Digite o valor 3: '))
maior = 0
menor = 0
if (numero1 >= numero2 and numero1 >= numero3):
    maior = numero1
    print('maior número: ',maior)
elif((numero2 > numero1 and numero2 > numero3)):
    maior = numero2
    print('maior número: ',maior)
else:
    maior = numero3
    print('maior número: ',maior)

if (numero1 <= numero2 and numero1 <= numero3):
    menor = numero1
    print('menor número: ',menor)
elif((numero2 < numero1 and numero2 < numero3)):
    menor = numero2
    print('menor número: ',menor)
else:
    menor = numero3
    print('menor número: ',menor)