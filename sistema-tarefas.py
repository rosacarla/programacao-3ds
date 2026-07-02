# --- ENTRADA DE DADOS ---
# Solicita ao usuário a quantidade de tarefas e converte para inteiro
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []

# Laço para capturar o nome de cada tarefa
for i in range(qtd_tarefas):
    nome = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome)

# --- PROCESSAMENTO DOS DADOS ---
banco_dados_tarefas = []

# Percorre a lista usando enumerate iniciando em 1
for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    # Lógica de progressão de prazos: tarefa 1 = 2 dias, tarefa 2 = 4 dias, etc.
    prazo_dias = id_tarefa * 2
    status = "Pendente"
    
    # Armazena os dados estruturados em uma tupla
    banco_dados_tarefas.append((id_tarefa, nome_tarefa, prazo_dias, status))

# --- SAÍDA DE DADOS (RESUMO) ---
print("\n--- RESUMO DO SISTEMA ---")

# Percorre o banco de dados utilizando o desempacotamento de tuplas
for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

print("-" * 25)
# Exibe a quantidade total de tarefas processadas usando len()
print(f"Total de tarefas gerenciadas: {len(banco_dados_tarefas)}")
