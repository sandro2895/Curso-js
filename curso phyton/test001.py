def maxi(h):
    print(max(h), end=' ... ')


def mini(l):
    print(min(l))
    print()


print('# high_and_low')
num1 = "1 2 3 4 5"
print(num1)
num2 = num1.replace(' ', '')
num3 = [int(num2[0]), int(num2[1]), int(num2[2]), int(num2[3]), int(num2[4])]
maxi(num2)
mini(num2)
num4 = "1 2 -3 4 5"
num5 = num4.replace(' ', '')
num6 = [int(num5[0]), int(num5[1]), int(num5[3]), int(num5[4]), int(num5[5])]
num7 = [num6[0], num6[1], -num6[2], num6[3], num6[4]]
print(num4)
maxi(num7)
mini(num7)
num9 = "1 9 3 4 -5"
num10 = num9.replace(' ', '')
num11 = [int(num10[0]), int(num10[1]), int(num10[2]), int(num10[3]), int(num10[5])]
num12 = [num11[0], num11[1], num11[2], num11[3], -num11[4]]
print(num9)
maxi(num12)
mini(num12)




