import tkinter as tk

root =  tk.Tk()
nome_var = tk.StringVar(value="Digite aqui...") # Definimos o valor inicial


def saudar_utilizador():

    # Passo A: Obter o valor diretamente da StringVar
    # Muito mais limpo e direto!
    nome_digitado = nome_var.get()

    # Passo B: Criar a mensagem personalizada
    if nome_digitado:
        mensagem = f"Olá, {nome_digitado}! Usando StringVar para dados."
    else:
        mensagem = "Digite o seu nome e teste a StringVar!"

    # Passo C: Atualizar o Label (rótulo) com a nova mensagem
    rotulo_saudacao.config(text=mensagem)


# --- 2. CONFIGURAÇÃO DA JANELA ---

root.title("Programa Estruturado com Frames")

# --- 3. CRIAÇÃO DOS FRAMES (OS NOSSOS RECIPIENTES) ---

# Frame 1: Recipiente para o input (Label e Entry)
frame_input = tk.Frame(root, padx=10, pady=10, relief=tk.GROOVE, bd=2) # 'relief' e 'bd' dão uma borda visual ao Frame
frame_input.pack(pady=10) # Organizamos o Frame na janela principal com pack()


# Frame 2: Recipiente para a ação e output (Button e Label)
frame_acao = tk.Frame(root, padx=10, pady=10)
frame_acao.pack(pady=10)# Organizamos o segundo Frame com pack()

# --- 4. WIDGETS DENTRO DO frame_input (USANDO GRID) ---

# Atenção: O primeiro argumento agora é 'frame_input', não mais 'root'
rotulo_instrução = tk.Label(frame_input, text="Nome:")
rotulo_instrução.grid(row=0, column=0, padx=10, pady=10, sticky="WE")

campo_nome = tk.Entry(frame_input, width=30, textvariable=nome_var)
campo_nome.grid(row=0, column=1, padx=5, sticky="W")

# Fazemos a coluna do Entry expandir dentro do frame_input
frame_input.grid_columnconfigure(1, weight=1)

# --- 5. WIDGETS DENTRO DO frame_acao (USANDO GRID) ---
# Atenção: O primeiro argumento agora é 'frame_acao'
botao_saudar = tk.Button(frame_acao, text="executar ação", command=saudar_utilizador)
botao_saudar.grid(row=1, column=0, columnspan=2, pady=5, sticky="WE")

rotulo_saudacao = tk.Label(frame_acao, text="Interface organizada com sucesso ")
rotulo_saudacao.grid(row=2, column=0, columnspan=2, pady=5)


root.mainloop()
print("Programa finalizado")