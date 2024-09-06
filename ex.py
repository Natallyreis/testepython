class Veiculo:
    def __init__(self, marca, modelo, cor, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
    
    def acelerar(self, incremento):
        """Aumenta a velocidade do veículo."""
        if incremento > 0:
            self.velocidade += incremento
            print(f"Veículo acelerado para {self.velocidade} km/h")
        else:
            print("Incremento deve ser positivo.")

    def frear(self, decremento):
        """Diminui a velocidade do veículo, sem permitir que a velocidade seja negativa."""
        if decremento > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"Veículo freado para {self.velocidade} km/h")
        else:
            print("Decremento deve ser positivo.")

class TesteVeiculo:
    def __init__(self):
        # Criação de um veículo para testar
        self.veiculo = Veiculo(marca="Chevrolet", modelo="Impala67", cor="Preto")

    def executar_teste(self):
        print(f"Marca: {self.veiculo.marca}")
        print(f"Modelo: {self.veiculo.modelo}")
        print(f"Cor: {self.veiculo.cor}")
        print(f"Velocidade inicial: {self.veiculo.velocidade} km/h")

        # Testando acelerar
        self.veiculo.acelerar(50)
        
        # Testando frear
        self.veiculo.frear(20)
        
        # Testando frear até zero
        self.veiculo.frear(40)

# Executar o teste
if __name__ == "__main__":
    teste = TesteVeiculo()
    teste.executar_teste()
