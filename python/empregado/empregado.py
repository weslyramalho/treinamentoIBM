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
        self._salarioBase = salarioBase

    def get_slarioBase(self):
        return self._salarioBase
    
    def set_duracaoContrato(self, duracao_contrato):
        self._duracao_contrato = duracao_contrato
    
    def get_duracaoContrato(self):
        return self._duracao_contrato
    
    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)
    
    class Indeterminado(Empregado):
        def __init__(self, nome, salario, fone, registro, salarioBase, categoria):
            super().__init__(nome, salario, fone)
            self._registro = registro
            self._salarioBase = salarioBase
            self._categoria = categoria

        def set_registro(self, registro):
          self._registro = registro

        def get_registro(self):
             return self._registro

        def set_salarioBase(self, salarioBase):
            self._salarioBase = salarioBase

        def get_slarioBase(self):
             return self._salarioBase
        
        def set_categoria(self, categoria):
            self._categoria = categoria

        def get_categoria(self):
            return self._categoria
        
        def calcularSalarioTotal(self):
            if self._categoria == 1:
                return self._salarioBase + (self._salarioBase * 0.03)
            elif self._categoria == 2:
                return self._salarioBase + (self._salarioBase * 0.05)
            elif self._categoria == 3:
                return self._salarioBase + (self._salarioBase * 0.08)
            else: 
                return self._salarioBase

class Terceirizado(Empregado):
    def __init__(self, nome, salario, fone, responsavel):
        super().__init__(nome, salario, fone)
        self._responsavel = responsavel

    def set_responsavel(self, responsavel):
        self._responsavel = responsavel
    
    def get_responsavel(self):
        return self._responsavel
        
    
    
