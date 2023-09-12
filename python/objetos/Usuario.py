class Usuario():
    nome = "Angel"
    idade = 47
    login = "admin"
    senha = "1234"
    email = "angel@angel.com"
    fone = 0000000

    def __init__(self):
        self.nome
        self.idade
        self.login
        self.senha
        self.email
        self.fone

    def imprimeUsuarios(self):
        print(f'Dados dos usuarios: \n'
              f'Nome: {self.nome}\n'
              f'Idade: {self.idade}\n'
              f'login: {self.login}\n'
              f'senha: {self.senha}\n'
              f'email: {self.email}\n'
              f'fone: {self.fone}')
    
    def entrarIdade(self):
        idadeinput = int(input("Entre com a idade entre 18 - 100: "))
        if 18 < idadeinput < 100:
            self.idade = idadeinput
            print("Idade cadastrada com sucesso")
            return ""
        else:
            print("Idade introduzida incorretamente")
            self.entrarIdade
            return ""
        
    def imprimeIdade(self):
        print("A idade do usuario é: ", self.idade, "anos")
        return ""