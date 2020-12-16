# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

varpessoa = True
class Pessoa:
    print("Bem vindo ao cadastro de pessoas no sistema!\n")

    def __init__(self, nome, cidade, telefone, email):
        print("\nCadastro realizado\n")
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def prints(self):
        print("Seu nome é: %s" %(self.nome))
        print("%s mora em: %s" %(self.nome, self.cidade))
        print("Seu email: %s" %(self.email))
        print("Seu telefone: %d" %(self.telefone))

pessoa1 = Pessoa((str(input("Digite seu nome: "))), str(input("Digite sua cidade: ")), int(input("Digite seu telefone: ")), str(input("Digite seu email: ")))
pessoa1.prints()