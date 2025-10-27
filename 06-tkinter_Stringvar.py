import tkinter as tk

# --- 1. DEFINIÇÃO DA FUNÇÃO DE AÇÃO ---
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

root =  tk.Tk()
root.title("Programa com StringVar")

# --- 3. CRIAÇÃO DA VARIÁVEL DE CONTROLE ---

nome_var = tk.StringVar()
# Opcional: Podemos definir um valor inicial para a variável 
nome_var.set("Seu Nome Aqui")  #parecido com placeholder do html

# --- 4. CRIAÇÃO E POSICIONAMENTO DOS WIDGETS (USANDO GRID) ---
# Usamos o grid do passo anterior para manter a organização

# 4.1. Rótulo de instrução

rotulo_instrucao = tk.Label(root, text="Digite seu nome:")
rotulo_instrucao.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# 4.2. Campo de Entrada de Texto (Entry)
# ATENÇÃO: Ligamos a StringVar ao Entry usando 'textvariable'
campo_nome = tk.Entry(root, width=30, textvariable=nome_var)
campo_nome.grid(row=0, column=1, padx=10, pady=10, sticky="WE")

# 4.3. Botão
botao_saudar = tk.Button(root, text="saudar utilizador (StringVar)", command=saudar_utilizador)
botao_saudar.grid(row=1, columnspan=2, padx=10, pady=10, sticky="WE")

# 4.4. Rótulo de Output (Label)

rotulo_saudacao = tk.Label(root, text="Aguardando dados da StringVar..", fg="darkblue")
rotulo_saudacao.grid(row=2, columnspan=2, padx=10, pady=10)


# 5. Configuração extra do Grid (Responsividade)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
print("Programa finalizado")

# Segmento do Código,Documentação
# nome_var = tk.StringVar(),"Criação da Variável de Controle: Cria uma variável especial do Tkinter que é feita para guardar strings (texto). Ela é um objeto, e não uma string Python simples."


# "nome_var.set(""..."")",Definir Valor: É o método usado para escrever (dar um valor) na variável de controle. Este valor aparecerá no widget ligado.

# "campo_nome = tk.Entry(..., textvariable=nome_var)","Ligação: O parâmetro textvariable conecta o Entry à variável nome_var. A partir deste momento, o widget e a variável mantêm-se sincronizados."

# nome_var.get(),"Obter Valor: É o método usado para ler o valor atual contido na variável de controle, devolvendo-o como uma string Python padrão."

# Outras Variáveis,"Existem outras: tk.IntVar() para números inteiros, tk.DoubleVar() para números decimais, e tk.BooleanVar() para valores True/False."