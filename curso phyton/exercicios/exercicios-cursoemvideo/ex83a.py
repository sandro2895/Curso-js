expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')' and len(pilha) > 0:
        pilha.pop()
    else:
        pilha.append(')')
        break
print(len(pilha))
if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida')
