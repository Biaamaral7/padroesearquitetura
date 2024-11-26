import datetime

agendamentos = []

def adicionar_agendamento(data, hora, aluno, professor, descricao):
    agendamento = {
        "data": data,
        "hora": hora,
        "aluno": aluno,
        "professor": professor,
        "descricao": descricao
    }
    agendamentos.append(agendamento)
    print(f"Agendamento do aluno {aluno} para {data} às {hora} com professor {professor} adicionado com sucesso!")

def listar_agendamentos():
    if not agendamentos:
        print("Não há agendamentos no sistema.")
    else:
        for agendamento in agendamentos:
            print(f"{agendamento['data']} às {agendamento['hora']} com professor {agendamento['professor']} - aluno {agendamento['aluno']} - {agendamento['descricao']}")

def remover_agendamento(data, hora, aluno="", professor=""):
    for agendamento in agendamentos[:]:  
        if agendamento["aluno"] == aluno and agendamento["professor"] == professor and agendamento["data"] == data and agendamento["hora"] == hora:
            agendamentos.remove(agendamento)
            print(f"Agendamento do aluno {aluno} para {data} às {hora} com professor {professor} removido com sucesso!")
            return
    print(f"Não foi encontrado agendamento do aluno {aluno} para {data} às {hora} com professor {professor}.")

def menu():
    while True:
        print("\nSistema de Agendamento")
        print("1 - Adicionar agendamento")
        print("2 - Listar agendamentos")
        print("3 - Remover agendamento")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            aluno = input("Dgite o nome do aluno que deseja agendar: ")
            professor = input("Digite o nome do professor: ")
            data = input("Digite a data do agendamento (AAAA-MM-DD): ")
            hora = input("Digite a hora do agendamento (HH:MM): ")
            descricao = input("Digite a descrição do agendamento: ")
            adicionar_agendamento(data, hora, aluno, professor, descricao)
        
        elif opcao == "2":
            listar_agendamentos()
        
        elif opcao == "3":
            aluno = input("Digite o nome do aluno para remover o agendamento: ")
            professor = input("Digite o nome do professor para remover o agendamento: ")
            data = input("Digite a data do agendamento (AAAA-MM-DD) para remover o agendamento: ")
            hora = input("Digite a hora do agendamento (HH:MM) para remover o agendamento: ")
            remover_agendamento(data, hora, aluno, professor)
        
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
