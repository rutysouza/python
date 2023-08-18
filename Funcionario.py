class Funcionario:
    def __init__(self, nome, cpf, salario, senha):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.senha = senha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf      

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario 

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha 


    def Cadastro(self): 
        nome = input("Digite o seu nome: ")
        cpf = input("Digite o seu cpf: ")
        salario = input("Digite o seu salario: ")
        senha = input("Digite uma senha: ")

        print("--------------------------")
        print("--- INFORMACOES CADASTRADAS ---")
        print("nome: ", nome)
        print("cpf: ", cpf)
        print("salario: ", salario)
        print("senha: ******")
        print("----------------------")
                  

    def Autentica(self):
        print("---LOGIN ---")
        senha = input("Digite a sua senha:")

        if (senha == self.senha):
            print("Funcionario autenticado no sistema!")
        else:
            print("Funcionario nao logado!")

        print("--------------------------")

    def Informacoes_Funcionario(self):
        print("--- INFORMACOES ---")   
        print("nome:", self.nome) 
        print("cpf:", self.cpf)
        print("salario:", self.salario)
        print("--------------------------")

    def Bonificacao(self):
        reajunte = float
        print("Calculando benificacao...")
        reajunte = self._salario * 0.10
        print("Salario reajustado: ", self.salario)
         

     


