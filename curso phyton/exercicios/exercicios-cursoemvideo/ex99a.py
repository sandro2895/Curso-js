def maior(*num):
    maior = max(num)
    ler = len(num)
    print('=-=' * 20)
    print('Analisando valores passados...')
    if num[0] > 0:
        for cont in num:
            print(cont, end=' ')
        print(f'foram informados {ler} valores ao todo.')
        print(f'O maior valor foi {maior}.')
    else:
        del num
        print(f'Foram informados {ler} valores ao todo')
        print(f'O maior valor foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
