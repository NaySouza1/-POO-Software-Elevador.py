# Instruções do exercício: Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.
# A classe Elevador também possui os seguintes métodos:
# Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo". Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".
# Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".
# Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".
# Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".

class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self, destino):
        if self.atualAndar < self.totalAndar and self.atualAndar < destino:
            self.atualAndar = destino
            print("Subindo para o andar", self.atualAndar)
        elif self.atualAndar >= self.totalAndar:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
        else:
            print("Você já está no andar desejado.")

    def Descer(self, destino):
        if self.atualAndar > 0 and self.atualAndar > destino:
            self.atualAndar = destino
            print("Descendo para o andar", self.atualAndar)
        elif self.atualAndar <= 0:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
        else:
            print("Você já está no andar desejado.")

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa. Total de pessoas:", self.atualCapacidade)
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa. Total de pessoas:", self.atualCapacidade)
        else:
            print("NÃO TEM NINGUÉM")


def menu():
    print("\n--- Opções do Elevador ---")
    print("1. Subir")
    print("2. Descer")
    print("3. Entrar")
    print("4. Sair")
    print("0. Sair do programa")
    opcao = input("Escolha uma opção: ")

    return opcao


totalCapacidade = int(input("Digite a capacidade total do elevador: "))
totalAndar = int(input("Digite o total de andares do prédio: "))


elevador = Elevador(totalCapacidade, totalAndar)
opcao = menu()

while opcao != "0":
    if opcao == "1":
        destino = int(input("Para qual andar deseja subir? "))
        elevador.Subir(destino)
    elif opcao == "2":
        destino = int(input("Para qual andar deseja descer? "))
        elevador.Descer(destino)
    elif opcao == "3":
        elevador.Entrar()
    elif opcao == "4":
        elevador.Sair()
    else:
        print("Opção inválida. Tente novamente.")

    opcao = menu()
