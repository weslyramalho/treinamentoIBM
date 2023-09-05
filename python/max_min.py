lista = [1, 3, 5, 6, 0, 20, 7, 8, 9, 10, 14, 100, 258, 584]

def maxmin(l):
    return max(l), min(l)

maximo, minimo = maxmin(lista)

print('O maior valor é: {}'.format(maximo))
print('O menor valor é: {}'.format(minimo))
