# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

lis = []
x = 4

while x <= 20:
    x+=1
    if x % 2 == 0:
        lis.append(x)
print(lis)