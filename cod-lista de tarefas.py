tarefas = []

while true: 
    print("1. Adicionar tarefa")
    print("2. ver tarefas")
    print("3. Sair")

opcao = input("Escolha uma opção:")
if opcao == "1":
    tarefa = input("digite a tarefa:")
    tarefas.append(tarefa)
print("tarefa adicionada!")

elif opcao == "2":
     print("\n===== tarefas =====")
    for tarefa in tarefas:
    print("-", tarefa)

elif opcao == "3":
     print("encerrando programa...")
    break

else: 
    print("opção inválida.")

