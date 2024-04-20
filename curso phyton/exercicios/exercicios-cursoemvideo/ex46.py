import time

cor = {'nada': '\033[m',
       'red': '\033[31m',
       'blue': '\033[34m',
       'green': '\033[32m',
       'yellow': '\033[33m',
       'purple': '\033[35m'}
for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)
print('BUM{}!{}{}!{}{}!{}{}!{}{}!{}'
      .format(cor['blue'], cor['nada'], cor['green'], cor['nada'], cor['yellow'], cor['nada'],
              cor['purple'], cor['nada'], cor['red'], cor['nada']))
