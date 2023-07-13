# Classe é a base para Orientação a Objetos
# De acordo com a PEP8, as classes devem começar com letras maiusculas
# Exemplos: carros = Carros ou classe carro = ClasseCarro

class Pessoa:
    # Atributo especial. Ele é executado quando você construi o objeto
    # Ele é conhecido também como método construtor
    def __init__(self, nome=None, idade=30):
        self.nome = nome
        self.idade = idade

    # Método é uma função que pertence há uma classe, portanto, está sempre ligada a classe.

    def cumprimentar(self):  # Atributo da classe
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Miguel')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Danilo'
    print(p.nome)
    print(p.idade)
