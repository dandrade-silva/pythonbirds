# Classe é a base para Orientação a Objetos
# De acordo com a PEP8, as classes devem começar com letras maiusculas
# Exemplos: carros = Carros ou classe carro = ClasseCarro

class Pessoa:
    # Método é uma função que pertence há uma classe, portanto, está sempre ligada a classe.
    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
