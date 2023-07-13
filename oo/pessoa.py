# Classe é a base para Orientação a Objetos
# De acordo com a PEP8, as classes devem começar com letras maiusculas
# Exemplos: carros = Carros ou classe carro = ClasseCarro

class Pessoa:
    olhos = 2  # Atributo default / Atributo de classe

    def __init__(self, *filhos, nome=None, idade=30):
        # Atributo especial. Ele é executado quando você construi o objeto.
        # Ele também é conhecido como método construtor
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):  # Método da classe
        # Método é uma função que pertence há uma classe.
        return f'Olá {id(self)}'


if __name__ == '__main__':
    miguel = Pessoa(nome='Miguel', idade=4)
    danilo = Pessoa(miguel, nome='Danilo', idade=30)
    print(Pessoa.cumprimentar(danilo))
    print(id(danilo))
    print(danilo.cumprimentar())
    print(danilo.nome)
    print(danilo.idade)
    for filho in danilo.filhos:
        print(filho.nome)
    danilo.sobrenome = 'Silva'  # Atributo Dinâmico: Não é uma boa prática!
    print(danilo.sobrenome)
    del danilo.sobrenome
    danilo.olhos = 1
    # __dict__: contém um dicionário com os atributos da instância
    print(danilo.__dict__)
    print(miguel.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(danilo.olhos)
    print(miguel.olhos)
    print(id(Pessoa.olhos), id(danilo.olhos), id(miguel.olhos))
