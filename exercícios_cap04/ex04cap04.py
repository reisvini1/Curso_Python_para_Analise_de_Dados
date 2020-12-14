# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def quad():
    quad = [x**2 for x in lista]
    print(quad)

def cub():
    cub = [x**3 for x in lista]
    print(cub)

quad()
cub()