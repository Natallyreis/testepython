class Elevador:
    def __init__(self, andarAtual=0, portaAberta=False, peso=0.0):
        self.andarAtual = andarAtual
        self.portaAberta = portaAberta
        self.peso = peso
    
    def subir(self, andarDesejado):
        """Subir para o andar desejado se a porta estiver fechada."""
        if not self.portaAberta:
            if andarDesejado > self.andarAtual:
                print(f"Subindo de {self.andarAtual} para {andarDesejado}.")
                self.andarAtual = andarDesejado
            else:
                print("O andar desejado deve ser maior que o andar atual.")
        else:
            print("Não é possível subir com a porta aberta.")
    
    def descer(self, andarDesejado):
        """Descer para o andar desejado se a porta estiver fechada."""
        if not self.portaAberta:
            if andarDesejado < self.andarAtual:
                print(f"Descendo de {self.andarAtual} para {andarDesejado}.")
                self.andarAtual = andarDesejado
            else:
                print("O andar desejado deve ser menor que o andar atual.")
        else:
            print("Não é possível descer com a porta aberta.")

    def abrir_porta(self):
        """Abrir a porta do elevador."""
        self.portaAberta = True
        print("Porta do elevador aberta.")
    
    def fechar_porta(self):
        """Fechar a porta do elevador."""
        self.portaAberta = False
        print("Porta do elevador fechada.")

class TesteElevador:
    def __init__(self):
        # Criação de um elevador para teste
        self.elevador = Elevador()
    
    def executar_teste(self):
        print(f"Andar atual: {self.elevador.andarAtual}")
        print(f"Porta aberta: {self.elevador.portaAberta}")
        print(f"Peso: {self.elevador.peso}")
        
        # Testar abrir e fechar a porta
        self.elevador.abrir_porta()
        self.elevador.subir(5)  # Não deve funcionar porque a porta está aberta
        self.elevador.fechar_porta()
        
        # Testar subir e descer
        self.elevador.subir(5)
        self.elevador.descer(2)
        
        # Testar descer até o andar atual
        self.elevador.descer(5)  # Não deve funcionar porque não pode descer mais

# Executar o teste
if __name__ == "__main__":
    teste = TesteElevador()
    teste.executar_teste()
