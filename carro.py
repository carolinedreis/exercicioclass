class Carro: # classe define objeto
    def __init__(self, propietario,modelo, cor, placa, preco,marca):
        self.propietario=propietario
        self.modelo=modelo
        self.cor=cor
        self.placa=placa      # referencias
        self.preco=preco
        self.marca=marca

    def __str__(self): # itens orientados a objeto/ funçao que retorna o valor
        return f"Ola, {self.propietario} , seu carro é o {self.modelo}, {self.cor} ,{self.placa} , {self.preco}, {self.marca}"

meu_carro = Carro(  # funçoes que retornam o valor
    # parametros
    propietario= 'Ana',
    modelo='Toro',
    cor= 'Vermelho',
    placa='ETJ 1234',
    preco=50000,
    marca='Fiat',
)
print(meu_carro)

salario= 2000