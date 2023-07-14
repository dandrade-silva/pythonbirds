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
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'Nome da classe: {cls} - Olhos: {cls.olhos}'


class Homem(Pessoa):  # Herança simples
    def cumprimentar(self):

        return f'{super().cumprimentar()}. Aperto de mão!'


class Mutante(Pessoa):  # Herança simples
    olhos = 3  # Sobrescrita de Atributo de dados


if __name__ == '__main__':
    miguel = Mutante(nome='Miguel', idade=4)
    danilo = Homem(miguel, nome='Danilo', idade=30)
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
    print(Pessoa.olhos)
    print(danilo.olhos)
    print(miguel.olhos)
    print(id(Pessoa.olhos), id(danilo.olhos), id(miguel.olhos))
    print(Pessoa.metodo_estatico(), danilo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),
          danilo.nome_e_atributos_de_classe())
    pessoa = Pessoa()
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(danilo, Pessoa))
    print(isinstance(danilo, Homem))
    print(miguel.olhos)
    print(danilo.cumprimentar())
    print(miguel.cumprimentar())
