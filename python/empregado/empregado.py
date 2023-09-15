class Empregado:
    def __init__(self, nome, salario, fone):
        self._nome = nome
        self._salario = salario
        self._fone = fone
    
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


subContrato1 = Terceirizado("Roberto Flores Morales", 123456789, 88888888,"Coca-Cola")
subContrato2 = Terceirizado("Ana Mora Cruz", 223446789, 77777777, "Pepsi")

print("\n\tSubcontratos:")
print("\n***EMPREGADO 1 ***")
print("Nome: " + subContrato1.get_nome() + 
      "\nSalario: " + str(subContrato1.get_salario()) +
      "\nfone: " + str(subContrato1.get_fone()) + 
      "\nResponsável: "+ subContrato1.get_responsavel())

print("\n***EMPREGADO 2 ***")
print("Nome: " + subContrato2.get_nome() + 
      "\nSalario: " + str(subContrato2.get_salario()) +
      "\nfone: " + str(subContrato2.get_fone()) + 
      "\nResponsável: "+ subContrato2.get_responsavel())

indeterm1 = Indeterminado("Roberto Rojas Salazar", 434565432, 22222222, 4, 350000, 1)
indeterm2 = Indeterminado("Rebeca Suárez Tapia", 897456274, 33445533, 7, 510000, 2)

print("\n*** Empregado por tempo inteterminado ***")
print("\n\tIndeterminado:")
print("\n***EPREGADO 1 ***")
print("Nome: " + indeterm1.get_nome() + 
      "\nSalario: " + str(indeterm1.get_salario()) +
      "\nfone: " + str(indeterm1.get_fone()) + 
      "\nRegistro: "+ str(indeterm1.get_registro()) +
      "\nCategoria: " + str(indeterm1.get_categoria()) +
      "\nSalario Total: " + str(indeterm1.calcularSalarioTotal()))

print("\n\tIndeterminado:")
print("\n***EPREGADO 2 ***")
print("Nome: " + indeterm1.get_nome() + 
      "\nSalario: " + str(indeterm2.get_salario()) +
      "\nfone: " + str(indeterm2.get_fone()) + 
      "\nRegistro: "+ str(indeterm2.get_registro()) +
      "\nCategoria: " + str(indeterm2.get_categoria()) +
      "\nSalario Total: " + str(indeterm2.calcularSalarioTotal()))


    
    
