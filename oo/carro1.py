"""
Voce deve criar uma classe de carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direcao

O motor tera a responsabilidade de controlar a velocidade.
Ele oferece os seguites atributos:
1) Atributo de dado velicidade
2) Metodo acelerar, que devera incrementar a velocidade de uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A Direcao tera a responsabilidade de controlar a direcao. Ela oferece os seguintes atributos:
1) Valor de direcao com valores possiveis: Norte, Sul, Leste, Oeste.
2) Metodo girar_a_direita
3)Metodo girar_a_esquerda

  N
O   L
  S
    Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
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
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
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
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
"""


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return  self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'


class Direcao:
    rotacao_a_direita_dct={NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct={NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor=self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor=self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)






