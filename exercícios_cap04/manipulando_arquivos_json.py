<<<<<<< HEAD
# Criando um dicionário
dic = {'nome': 'Guido van Rossum', 'linguagem': 'Python', 'similar': ['c', 'Modula-3', 'lisp'], 'users': 100000}

for k, v in dic.items():
    print(k, v)

# Importando o módulo Json
import json

# Convertendo o dicionário para um objeto Json
json.dumps(dic)

# Criando um arquivo Json
with open('arquivos/dados.json', 'w') as arquivos:
    arquivos.write(json.dumps(dic))

# Leitura de arquivos Json
with open('arquivos/dados.json', 'r') as arquivos:
    texto = arquivos.read()
    data = json.loads(texto)

print(data)
print(data['nome'])
'''
# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response[0])

print('Título', data['title'])
print('URL', data['url'])
print('Duração', data['duration'])
print('Número de visualizações', data['stats_number_of_plays'])
'''

# Copiando o conteúdo de um arquivo para outro
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
=======
# Criando um dicionário
dic = {'nome': 'Guido van Rossum', 'linguagem': 'Python', 'similar': ['c', 'Modula-3', 'lisp'], 'users': 100000}

for k, v in dic.items():
    print(k, v)

# Importando o módulo Json
import json

# Convertendo o dicionário para um objeto Json
json.dumps(dic)

# Criando um arquivo Json
with open('arquivos/dados.json', 'w') as arquivos:
    arquivos.write(json.dumps(dic))

# Leitura de arquivos Json
with open('arquivos/dados.json', 'r') as arquivos:
    texto = arquivos.read()
    data = json.loads(texto)

print(data)
print(data['nome'])
'''
# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response[0])

print('Título', data['title'])
print('URL', data['url'])
print('Duração', data['duration'])
print('Número de visualizações', data['stats_number_of_plays'])
'''

# Copiando o conteúdo de um arquivo para outro
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
>>>>>>> f3ab38b7f6a4913e0f50db94c3423ad719f0c85c
        outfile.write(text)