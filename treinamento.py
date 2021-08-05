# ex054
'''class QuadradoPerfeito:
    def __init__(self, tamanho_altura=4, tamanho_largura=5):
        self.tamanho_altura = tamanho_altura
        self.tamanho_largura = tamanho_largura

    def calcular_area(self):
        return self.tamanho_largura * self.tamanho_altura


quadrado_primeiro = QuadradoPerfeito()
quadrado_segundo = QuadradoPerfeito(6, 7)

print(quadrado_primeiro.tamanho_altura, quadrado_primeiro.calcular_area())
print(quadrado_segundo.tamanho_altura, quadrado_segundo.calcular_area())'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

p1 = Pessoa('João', 40, 85.0, 1.80)
print(p1.nome, p1.idade, p1.peso, p1.altura)








