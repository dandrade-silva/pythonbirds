"""
Você deve criar uma classe Carro que vai possuir dois atributos compostos por 
outras duas classes:
    1) Motor
    2) Direcao

O Motor terá a responsabilidade de controlar a velocidade. 
Ele ofecere os seguintes atributos:
    1) Atributo de dado: velocidade
    2) Método acelerar: deverá incrementar a velocidade de uma unidade
    3) Método frear: deverá decrementar a velocidade em duas unidades

A Direcao terá a responsabilidade de controlar a direção.
Ele ofecere os seguintes atributos:
    1) Atributo de dado: direcao, com os valores possíveis: Norte, Sul, Lest, Oeste.
    2) Método girar_a_direita
    2) Método girar_a_esquerda

    N
  O   L
    S

    Exemplo:
    # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_direita(self):
        coordenadas = {
            'Norte': 'Leste',
            'Leste': 'Sul',
            'Sul': 'Oeste',
            'Oeste': 'Norte'
        }

        self.valor = coordenadas[self.valor]

    def girar_a_esquerda(self):
        coordenadas = {
            'Norte': 'Oeste',
            'Oeste': 'Sul',
            'Sul': 'Leste',
            'Leste': 'Norte'
        }

        self.valor = coordenadas[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
