# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def function(x):
    list = []
    list.append(x)
    print(list)

def function2(q, y, z, w):
    list = []
    list.extend((q, y, z, w))
    print(list)


function(3)
function2(4, 3, 2, 1)
