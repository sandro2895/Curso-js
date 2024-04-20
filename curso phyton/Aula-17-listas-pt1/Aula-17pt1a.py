num = [1, 2, 3, 4]
num[2] = 2
num.insert(4, 9)
#del num[0]
#num.pop()
#num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não tem o valor 5')
print(num)
print(F'Essa lista tem {len(num)} elementos')


