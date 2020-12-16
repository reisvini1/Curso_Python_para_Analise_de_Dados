<<<<<<< HEAD
import csv

# Escrita de arquivos com o csv
with open('arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55, 93, 76))
    writer.writerow((62, 14, 86))

# Leitura de arquivos com o csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print("Número de colunas:", len(x))
        print(x)

# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

=======
import csv

# Escrita de arquivos com o csv
with open('arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55, 93, 76))
    writer.writerow((62, 14, 86))

# Leitura de arquivos com o csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print("Número de colunas:", len(x))
        print(x)

# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

>>>>>>> f3ab38b7f6a4913e0f50db94c3423ad719f0c85c
print(dados)