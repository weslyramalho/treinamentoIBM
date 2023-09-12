from empregado.empregado import Empregado


class Efetivo(Empregado):
    def __init__(self, nome, salario, fone, registro, salarioBase, duracao_contrato):
        super().__init__(nome, salario, fone)
        
        self._registro = registro
        self._salarioBase = salarioBase
        self._duracao_contrato = duracao_contrato

    def set_registro(self, registro):
        self._registro = registro

    def get_registro(self):
        return self._registro
    
    def set_salarioBase(self, salarioBase):
        self._salarioBase

    def get_slarioBase(self):
        return self._salarioBase
    
    def set_duracaoContrato(self, duracao_contrato):
        self._duracao_contrato = duracao_contrato
    
    def get_duracaoContrato(self):
        return self._duracao_contrato
    
    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)
    
