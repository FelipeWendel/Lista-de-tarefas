class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.descricao} - {status}"

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        try:
            del self.tarefas[indice]
        except IndexError:
            print("Índice inválido")

    def marcar_tarefa_concluida(self, indice):
        try:
            self.tarefas[indice].marcar_concluida()
        except IndexError:
            print("Índice inválido")

    def imprimir_lista(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i+1}. {tarefa}")

def main():
    lista_de_tarefas = ListaDeTarefas()

    while True:
        print("\nOpções:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Imprimir lista de tarefas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            lista_de_tarefas.adicionar_tarefa(descricao)
        elif opcao == "2":
            indice = int(input("Digite o índice da tarefa a remover: ")) - 1
            lista_de_tarefas.remover_tarefa(indice)
        elif opcao == "3":
            indice = int(input("Digite o índice da tarefa a marcar como concluída: ")) - 1
            lista_de_tarefas.marcar_tarefa_concluida(indice)
        elif opcao == "4":
            lista_de_tarefas.imprimir_lista()
        elif opcao == "5":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()