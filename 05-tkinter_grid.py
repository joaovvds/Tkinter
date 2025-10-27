import tkinter as tk

def saudar_utilizador():
    nome_digitado = campo_nome.get()

    if (nome_digitado):
        mensagem = f"Olá, {nome_digitado}! Bem vindo ao Tkinter."
        rotulo_saudacao.config(text="Nome digitado com Sucesso", fg="green")
    else: 
        mensagem = "Por favor, digite seu nome para ser saudado!"
        rotulo_saudacao.config(text="Você não digitou seu nome", fg="red")
    
    rotulo_output.config(text=mensagem)
    
root = tk.Tk()
root.title("Tkinter com Grid layout")
# Não definiremos um tamanho fixo (geometry) para ver o grid em ação!

# --- 3. CRIAÇÃO E POSICIONAMENTO DOS WIDGETS COM GRID ---

# 3.1. Rótulo de instrução (Label)
rotulo_instrucao = tk.Label(text="Digite seu nome:")

# row=0: primeira linha
# column=0: primeira coluna
# sticky="W": anexa o widget ao lado Oeste (West/Esquerda) da célula
rotulo_instrucao.grid(row=0, column=0, padx=10, pady=10, sticky="W")


# 3.2 Campo de Entrada de Texto (Entry)
campo_nome = tk.Entry(root, width=30)

# row=0: primeira linha (ao lado do rótulo)
# column=1: segunda coluna
# sticky="WE": anexa o widget aos lados Oeste e Este, fazendo-o preencher a largura da coluna
campo_nome.grid(row=0, column=1, padx=10, pady=10, sticky="WE")

# 3.2.9 Rótulo de Output (Label)
rotulo_output = tk.Label(root, text="") #saida output para o nome
rotulo_output.grid(row=2, columnspan=2, padx=10, pady=10)

# 3.3. Botão
botao_saudar = tk.Button(root, text="Saudar utilizador", command=saudar_utilizador)

# row=1: segunda linha
# columnspan=2: faz com que o botão ocupe 2 colunas (coluna 0 e coluna 1)
# sticky="WE": faz o botão preencher toda a largura das duas colunas
botao_saudar.grid(row=1, columnspan=2)


# 3.4. Rótulo de Output (Label)
rotulo_saudacao = tk.Label(root, text="Aguardando nome...", fg="darkgreen")

# row=2: terceira linha
# columnspan=2: também ocupa as 2 colunas
rotulo_saudacao.grid(row=3, columnspan=3, padx=10, pady=10)


# 4. Configuração extra do Grid (Melhorando a responsividade)
# Faz com que a coluna 1 se expanda quando a janela é redimensionada
root.grid_columnconfigure(1, weight=1)

root.mainloop()
print("Programa finalizado.")

# Segmento do Código,Documentação:
# "widget.grid(row=R, column=C)",Posicionamento Principal: Define que o widget será colocado na linha R (onde 0 é a primeira linha) e na coluna C (onde 0 é a primeira coluna).


# "padx=10, pady=10","Padding (Espaçamento): Adiciona 10 pixels de espaço externo (horizontal e verticalmente, respetivamente) fora do widget, ajudando a separá-lo dos outros elementos."

# "sticky=""W""","Ancoragem: Diz ao widget para se ""colar"" ao lado Oeste (Esquerdo) da sua célula no grid. N (Norte/Topo), S (Sul/Fundo), E (Este/Direita)."

# "sticky=""WE""","Esticar Horizontalmente: Faz o widget esticar-se para preencher toda a largura da célula (ou das células, se usar columnspan)."

# columnspan=2,"Abranger Colunas: Permite que um widget se espalhe por várias colunas (neste caso, 2), como a mesclagem de células numa folha de cálculo."

# "root.grid_columnconfigure(1, weight=1)","Responsividade: Avançado, mas poderoso! Diz ao Tkinter para dar à Coluna 1 um ""peso"" de 1. Quando a janela é redimensionada, toda a largura extra disponível é alocada para colunas com peso (aquela com o maior peso recebe mais), fazendo os widgets dentro delas (como o Entry) expandirem-se."