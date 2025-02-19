class Pessoa:
    nome = ""
    idade = 0
    peso = 0.0
    altura = 0.0

def envelhecer(self, aumentar_idade):
    self.idade += 6
    if self.idade <21:
        self.altura += 0.5

def engordar(self, aumentar_peso):
    self.peso += 4

def emagrecer(self, perder_peso):
    self.peso -= 3
    
def crescer(self, aumentar_altura):
    self.altura += 2

if __name__=="__main__":
    individuo=Pessoa()
    individuo.nome="Luisito"
    individuo.idade=15 
    individuo.altura=1.70
    individuo.peso=70

    print(f"Nome: {individuo.nome}")
    print(f"Idade: {individuo.idade} anos")
    print(f"Peso: {individuo.peso}kg")
    print(f"Altura: {individuo.altura}m")
    print(f"")
   