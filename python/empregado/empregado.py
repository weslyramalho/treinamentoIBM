class Empregado:
    def __init__(self, nome, salario, fone):
        self.nome = nome
        self.salario = salario
        self.fone = fone
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_nome(self):
        return self._nome
    
    def set_salario(self, salario):
        self._salario = salario
    
    def get_salario(self):
        return self._salario
    
    def set_fone(self, fone):
        self._fone=fone
    
    def get_fone(self):
        return self._fone
    
