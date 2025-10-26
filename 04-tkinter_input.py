import tkinter as tk

# --- 1. DEFINIÇÃO DA FUNÇÃO DE AÇÃO (Lê o input e atualiza o output) ---
# Esta função será chamada quando o botão for clicado.

def saudar_utilizador():
    # Passo A: Obter o texto do widget Entry
    # O método .get() lê o que está digitado no campo.
    nome_digitado = campo_nome.get()

    # Passo B: Criar a mensagem personalizada
    if (nome_digitado):
        # Se o utilizador digitou algo
        mensagem = f"Olá, {nome_digitado}! Bem vindo ao Tkinter."
        rotulo_saudacao.config(text="Nome digitado com Sucesso", fg="green") #implementei isso rs :p
    else: 
        mensagem = "Por favor, digite seu nome para ser saudado!"
        rotulo_saudacao.config(text="Vocé não digitou seu nome", fg="red")
    # Passo C: Atualizar o Label (rótulo) com a nova mensagem
    rotulo.config(text=mensagem)


# --- 2. CONFIGURAÇÃO DA JANELA ---
root = tk.Tk()
root.title("Programa com Input")
root.geometry("400x300")

# --- 3. CRIAÇÃO DOS WIDGETS ---
# 3.1. Rótulo de instrução (Label)
rotulo = tk.Label(root, text="Digite seu nome abaixo!")
rotulo.pack(pady=(20, 5)) # padding de 20px no topo, 5px em baixo

# 3.2. Campo de Entrada de Texto (Entry)
# Armazenamos o objeto 'Entry' na variável 'campo_nome' para podermos usar o .get() nele.
campo_nome = tk.Entry(root, width=40)
campo_nome.pack(pady=5)

# 3.3. Botão
# O 'command' continua a apontar para a nossa função
tk.Button(root, text="Saudar", command=saudar_utilizador).pack(pady=10)


# 3.4. Rótulo de Output (Label)
# Inicialmente com uma mensagem de espera.
rotulo_saudacao = tk.Label(root, text="Aguardando seu nome...", fg="blue") # 'fg' muda a cor do texto
rotulo_saudacao.pack(pady=15)

root.mainloop()
print("programa finalizado!")
