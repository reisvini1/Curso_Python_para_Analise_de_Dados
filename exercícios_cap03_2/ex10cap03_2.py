<<<<<<< HEAD
# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"

import pandas as pd
file_name = "binary.csv"

def teste(file_name):
    ts = pd.read_csv(file_name)
    print(ts.describe())

=======
# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"

import pandas as pd
file_name = "binary.csv"

def teste(file_name):
    ts = pd.read_csv(file_name)
    print(ts.describe())

>>>>>>> f3ab38b7f6a4913e0f50db94c3423ad719f0c85c
teste(file_name)