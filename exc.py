import heapq
import random

fila_de_prioridades = []

def adicionar_paciente(fila, nome, idade, gravidade):
    paciente = (gravidade, nome, idade)
    heapq.heappush(fila, paciente)

def atender_proximo_paciente(fila):
    if not fila:
        print("Não há pacientes na fila.")
        return None
    paciente = heapq.heappop(fila)
    return paciente

def visualizar_fila(fila):
    print("Pacientes na fila de prioridades:")
    for gravidade, nome, idade in fila:
        print(f"Nome: {nome}, Idade: {idade}, Gravidade: {gravidade}")

def proximo_paciente(fila):
    if not fila:
        print("Não há pacientes na fila.")
        return None
    paciente = fila[0]
    return paciente

historico_ultimos_pacientes = []


def listar_ultimos_pacientes():
    if not historico_ultimos_pacientes:
        print("Nenhum paciente foi atendido recentemente.")
    else:
        print("Últimos 5 pacientes atendidos:")
        for i, paciente in enumerate(historico_ultimos_pacientes, 1):
            gravidade, nome, idade = paciente
            print(f"{i}. Nome: {nome}, Idade: {idade}, Gravidade: {gravidade}")

def gerar_simulacao(fila):
    nomes = ["Ana", "Carlos", "Helena", "Maria", "Clara"]
    for _ in range(10):
        nome = random.choice(nomes)
        idade = random.randint(18, 70)
        gravidade = random.randint(1, 10)
        adicionar_paciente(fila, nome, idade, gravidade)

def jogo_pronto_socorro():
    print("Bem-vindo ao Pronto-Socorro Médico!")
    while True:
        print("\nOpções:")
        print("1. Adicionar paciente")
        print("2. Atender próximo paciente")
        print("3. Visualizar fila de pacientes")
        print("4. Mostrar próximo paciente na fila")
        print("5. Listar últimos 5 pacientes atendidos")
        print("6. Gerar simulação de pacientes aleatórios")
        print("7. Sair do jogo")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            gravidade = int(input("Gravidade do paciente: "))
            adicionar_paciente(fila_de_prioridades, nome, idade, gravidade)
        elif opcao == "2":
            paciente = atender_proximo_paciente(fila_de_prioridades)
            if paciente:
                print(f"Atendendo o paciente: Nome: {paciente[1]}, Idade: {paciente[2]}, Gravidade: {paciente[0]}")
                historico_ultimos_pacientes.append(paciente)
                if len(historico_ultimos_pacientes) > 5:
                    historico_ultimos_pacientes.pop(0)
        elif opcao == "3":
            visualizar_fila(fila_de_prioridades)
        elif opcao == "4":
            paciente = proximo_paciente(fila_de_prioridades)
            if paciente:
                print(f"Próximo paciente na fila: Nome: {paciente[1]}, Idade: {paciente[2]}, Gravidade: {paciente[0]}")
        elif opcao == "5":
            listar_ultimos_pacientes()
        elif opcao == "6":
            gerar_simulacao(fila_de_prioridades)
            print("Simulação gerada com sucesso.")
        elif opcao == "7":
            print("Obrigado por jogar o Pronto-Socorro Médico!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    jogo_pronto_socorro()
