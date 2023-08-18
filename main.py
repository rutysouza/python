from Funcionario import Funcionario
from gerente import Gerente
from Diretor import Diretor
from Secretario import Secretario
from Presidente import Presidente

func1 = Funcionario('Maria', '111.111.111.-11', '2500.00', '123456')
func1.Cadastro()
func1.Bonificacao


ger1 = Gerente('Jose', '222.222.222-22', '3500.00', '123456789', 10)
ger1.Cadastro()

ger1 = Diretor('Marcos', '333.333.333-33', '4500.00', '1234',)

ger1 = Secretario('Josafa', '333.333.333-33', '2000.00', '12345',)

ger1 = Presidente('Paulo', '555.555.555-55', '10000.00', '123467',)
