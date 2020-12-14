import os

texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."

arq = open(os.path.join('arquivos/cientista.txt'), 'w')
for palavra in texto.split():
    arq.write(palavra+' ')
arq.close()

arq =open('arquivos/cientista.txt', 'r')
conteudo = arq.read()
arq.close()

print(conteudo)

with open('arquivos/cientista.txt', 'r') as arq:
    conteudo = arq.read()
print(len(conteudo))
print(conteudo)

with open('arquivos/cientista.txt', 'w') as arq:
    arq.write(texto[:21])
    arq.write("\n")
    arq.write(texto[:23])

arq = open('arquivos/cientista.txt', 'r')
conteudo = arq.read()
arq.close()

print(texto)