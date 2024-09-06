class Estudante:
    def __init__(self, nome, notas=None):
        self.nome = nome
        # Se notas não for fornecido, inicializar com notas zeradas para 4 bimestres
        self.notas = notas if notas is not None else [0.0] * 4
    
    def atualizar_nota(self, bimestre, nota):
        """Atualiza a nota de um bimestre específico (1 a 4)"""
        if 1 <= bimestre <= 4:
            if 0 <= nota <= 10:
                self.notas[bimestre - 1] = nota
            else:
                print("Nota deve estar entre 0 e 10.")
        else:
            print("Número do bimestre deve estar entre 1 e 4.")
    
    def calcularMedia(self):
        """Calcula a média das notas dos quatro bimestres."""
        return sum(self.notas) / len(self.notas)

class TesteEstudante:
    def __init__(self):
        # Criação de um estudante para teste
        self.estudante = Estudante(nome="Maria", notas=[7.5, 8.0, 6.5, 9.0])
    
    def executar_teste(self):
        print(f"Nome: {self.estudante.nome}")
        print(f"Notas: {self.estudante.notas}")
        print(f"Média das notas: {self.estudante.calcularMedia():.2f}")
        
        # Atualizar notas e calcular a nova média
        self.estudante.atualizar_nota(2, 9.5)  # Atualiza a nota do 2º bimestre
        self.estudante.atualizar_nota(4, 8.5)  # Atualiza a nota do 4º bimestre
        print("Após atualizar notas:")
        print(f"Notas: {self.estudante.notas}")
        print(f"Média das notas: {self.estudante.calcularMedia():.2f}")

# Executar o teste
if __name__ == "__main__":
    teste = TesteEstudante()
    teste.executar_teste()
