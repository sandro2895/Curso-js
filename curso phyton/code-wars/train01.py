def descending_order(num):
    s = str(num).strip()
    s2 = sorted(s, reverse=True)
    s3 = ''
    for cont in s2:
        s3 += cont

    return print(s3)


descending_order(123)



#def descending_order(num):
    #return print(int(''.join(sorted(list(str(num)), reverse=True))))

