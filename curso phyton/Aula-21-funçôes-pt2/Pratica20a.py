#def fatorial(num=0):
  #  f = 1
   # for c in range(num, 0, -1):
   #     f *= c
    #return f


#f1 = fatorial(5)
#f2 = fatorial(2)
#f3 = fatorial(3)
#print(f'Fatoriais: 5=[{f1}] 2=[{f2}] 3=[{f3}]')

def parouimpar(p=0):
    if p % 2 == 0:
        return True
    else:
        return False


pi = int(input('Digite um número: '))
res = parouimpar(pi)
print(f'{res}')
