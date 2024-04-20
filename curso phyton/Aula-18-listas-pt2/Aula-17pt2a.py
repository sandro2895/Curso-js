test = []
test.append('Doca')
test.append(28)
galera = []
galera.append(test[:])
test[0] = 'Maria'
test[1] = '22'
galera.append(test[:])
print(galera)

