class Veiculo:
    def __init__(self, cor, rodas):
        self.cor = cor
        self.rodas = rodas
    
    def __str__(self):
        return 'cor: ' + self.cor + 'rodas: ' + str(self.rodas)
    
class Carro(Veiculo):
    def __init__(self, cor, rodas, velocidade):
        super().__init__(cor, rodas)
        self.velocidade = velocidade

        def __str__(self):
            return super().__str__() + ', Velocidade (km/hr): ' + str(self.velocidade)
        
class Bicicleta(Veiculo):
    def __init__(self, cor, rodas, tipo):
        super().__init__(cor, rodas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', tipo: ' + str(self.tipo)
    

viculo = Veiculo('verde', 4)
carrOO = Carro("AZUL", 4, 200)
bike = Bicicleta("branca", 2, "monto bike")