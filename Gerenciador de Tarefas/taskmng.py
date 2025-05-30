print("Gerenciador de tarefas")
print("Aqui você poderá adicionar, atualizar, listar tarefas pendentes ou concluídas e removê-las quando necessário.")

print("Digite:")
print("1. Adicionar uma tarefa (1)")
print("2. Atualizar uma tarefa (2)")
print("3. Remova uma tarefa (3)")
print("Caso queira apenas visualizar suas tarefas, digite um numero distinto (int).")
opt = int(input())

file_path = "tasks.txt"

match opt:
    case 1:
        texto = input("Adicione uma tarefa: ")
        if texto.isalnum():
            with open(file_path, "a") as file:
                file.write(f"[ ] {texto}\n")
        else:
            print("O nome da tarefa deve ser escrito apenas com letras e/ou numeros!")

    case 2:
        texto = input("Atualize uma tarefa: ")
        with open(file_path, "r") as file:
            tasks = file.readlines()

        with open(file_path, "w") as file:
            for task in tasks:
                if texto in task:
                    file.write(task.replace("[ ]", "[x]"))
                else:
                    file.write(task)

    case 3:
        texto = input("Remova uma tarefa: ")
        with open(file_path, "r") as file:
            tasks = file.readlines()
        
        with open(file_path, "w") as file:
            for task in tasks:
                if texto not in task:
                    file.write(task)
                    
with open(file_path, "r") as file:
    tasks = file.readlines()
    for task in tasks:
        print(task.replace("\n", " "))
