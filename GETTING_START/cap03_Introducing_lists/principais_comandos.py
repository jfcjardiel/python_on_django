bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#adicionar elemento ao final da lista
bicycles.append('oi')
print(bicycles)

#adicionar elemento em uma posição específica
bicycles.insert(2, 'nova')
print(bicycles)

#deletar elemento de uma lista
del bicycles[2]
print(bicycles)

#deletar último elemento da lista mas utilizá-lo (acho que é mais otimizado)
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

popped_in_any_position = bicycles.pop(0)
print(bicycles)
print(popped_in_any_position)

#deletar elemento pelo seu valor
lista = ['lista1', 'lista2', 'lista', 'lista', 'lista6']
print(lista)
lista.remove('lista')
print(lista)

#organizar os elementos
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

sorted(lista) #para não precisar alterar a lista

#achar o tamanho da lista
len(lista)
lista[-1] #exibe o último elemento da lista


