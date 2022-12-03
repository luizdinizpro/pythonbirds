class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    luiz = Pessoa(nome='Luiz')
    rose = Pessoa(luiz, nome='rose')
    print(Pessoa.cumprimentar(rose))
    print(id(rose))
    print(rose.cumprimentar())
    print(rose.nome)
    print(rose.idade)
    for filho in rose.filhos:
        print(filho.nome)
    rose.sobrenome = 'Diniz'
    del rose.filhos
    rose.olhos = 1
    del  rose.olhos
    print(rose.sobrenome)
    print(luiz.__dict__)
    print(rose.__dict__)
    Pessoa.olhos = 3
    print(rose.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(luiz.olhos), id(rose.olhos))





