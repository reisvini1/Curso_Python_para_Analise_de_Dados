# Este método vai inicializar cada objeto criado a partir desta classe
# O nome deste método é __init__
# (self) é uma referência a cada atributo de um objeto criado a partir desta classe
# Criando a classe livro com parâmetros no método construtor
class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe")

    # Atributos de cada objeto criado a partir desta classe.
    # O self indica que estes são atributos dos objetos

    def imprime(self):
        print("Este é o livro %s e ISBN %d" %(self.titulo, self.isbn))

# Criando um objeto de classe a partir da classe Livro()
Livro1 = Livro("O monge e o executivo", 9988888)

Livro1.imprime()

class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        print("Construtor chamado para criar um objeto desta classe")

# Criando um objeto a partir da classe Cachorro()
Rex = Cachorro(raca='Labrador')
Golias = Cachorro(raca='Huskie')

print(Rex.raca)
print(Golias.raca)