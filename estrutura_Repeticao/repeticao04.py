pais_a = 80000
pais_b = 200000
anos = 0

print('População Pais A: ', pais_a, '\nPopulação Pais B: ', pais_b)

while pais_a <= pais_b:
    pais_a *= 1.03
    pais_b *= 1.015
    anos += 1

    print('\n Ano: ', anos)
    print('População Pais A: ', pais_a, '\nPopulação Pais B: ', pais_b)

print('Numero de anos para igualar ou ultrapassar a População: ', anos)