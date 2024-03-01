class Veículos:
    def __init__(self, marca, ano, preço):
        self.marca = marca
        self.ano = ano
        self.preço = preço
    def info(self):
        return f"Marca: {self.marca} \nAno: {self.ano} \nPreço: R${self.preço}"
class Carro (Veículos):
    def __init__(self, marca, ano, preço, modelo, potencia):
        self.modelo = modelo
        self.potencia = potencia
        super().__init__(marca, ano, preço)
    def info(self):
        return super().info()+ f"\nModelo: {self.modelo} \nPotência: {self.potencia} cavalos"
class Moto (Veículos):
    def __init__(self, marca, ano, preço, cilindradas):
        self.cilindradas = cilindradas
        super().__init__(marca, ano, preço)
    
    def info(self):
        return super().info() + f"\nCilindradas: {self.cilindradas} cm³"
Batmovel = Carro("Chevrolet", 1968, 14700.54, "HB20", 76)
Vespa = Moto("Hyundai", 2012, 10500.87, 56)
print(Batmovel.info())
print(Vespa.info())