class Funcionario :
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario= salario

    def __str__(self):
        return f"ola {self.nome}, voce foi cadastrdo com sucesso em nosso sistema"

    def aumento(self,valor):
        return  self.salario + valor
meu_funcionario = Funcionario (
    nome= 'julia',
    email= 'julia@hotmail.com',
    rg= 49993246875,
    idade= 25,
    salario= 2000
)
print(meu_funcionario)
print(meu_funcionario.aumento(500))