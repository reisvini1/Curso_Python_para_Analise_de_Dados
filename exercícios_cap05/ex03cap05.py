# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone:
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3player(Smartphone):
    def __init__(self, capacidade, tamanho = 'Pequeno', interface = 'Led'):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def printmp3(self):
        print("Valores para o objeto criado: %s %s %s" %(self.tamanho, self.interface, self.capacidade))

ap = MP3player('128GB')
ap.printmp3()