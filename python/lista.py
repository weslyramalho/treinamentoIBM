miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1, 2]]
l3 = [22, True, "una lista", [1, 2]]

print(type(miLista))

print(miLista[:]) #IMPRIMIR TODOS ELEMENTOS DA LISTA
print(miLista[:1]) #IMPRIME O PRIMEIRO ELEMENTO DA LISTA
print(miLista[:-1]) #IMPRIME TODOS ELEMENTOS DA LISTA, EXCETO O ULTIMO ELEMENTO

print(miLista==miLista2) # comparar se listas são iguais
print(l3==miLista2) # comparar se listas são iguais
print(miLista in miLista2) # comparar se listas são iguais
print(miLista is miLista2) # comparar se listas são iguais

print(l3[0:2])#imprime itens que estão entre a posição 0 e 2