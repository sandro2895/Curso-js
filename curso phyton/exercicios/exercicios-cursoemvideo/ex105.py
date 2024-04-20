def notas(*n, sit=False):
    """
     -> Função para analisar várias notas, situação opcional.
     :param n: Uma ou mais notas de aluno(aceita várias)
     :param sit: Valor opcional, indicando ou não a situação do aluno
     :return: dicionário com várias informações sobre o aluno

    """
    meds = {}
    soma = 0
    somador = 0
    medias = ''
    for cont in n:
        somador += cont
        soma += 1
    meds["total"] = soma
    meds["maior"] = max(n)
    meds["menor"] = min(n)
    media = somador / soma
    meds["média"] = media
    if media < 6:
        medias = 'RUIM'
    if 7 > media >= 6:
        medias = 'RAZOÁVEL'
    if media >= 7:
        medias = 'BOA'

    if sit:
        meds["situação"] = medias
    return meds


resp = notas(5.5, 6, 10, 6.5, sit=True)
print(resp)
help(notas)
