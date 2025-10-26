import tkinter as tk

# --- 1. DEFINIÇÃO DA FUNÇÃO DE AÇÃO ---
# Esta função será chamada sempre que o botão for clicado.

def mudar_saudacao():
    # Para que a função possa alterar o nosso Label, precisamos de o referenciar.
    # Usamos o método 'config' (ou 'configure') para mudar as propriedades de um widget.
    rotulo.config(text="O botão foi clicado! haha :)")

# --- 2. CONFIGURAÇÃO DA JANELA ---
root = tk.Tk()
root.title("Programa com botão")
root.geometry("500x250")

rotulo = tk.Label(root, text="Clique no botão abaixo :p")
rotulo.pack(pady=20)

# O Botão
# - text: o que aparece escrito no botão
# - command: MUITO IMPORTANTE! Liga a função 'mudar_saudacao' ao evento de clique.
#   Note que NÃO usamos parênteses na função (não é 'mudar_saudacao()').
#   Passamos apenas a referência da função.
botao_clicar = tk.Button(text="Clicar em min", command=mudar_saudacao)

# --- 4. GERENCIAMENTO DE LAYOUT (TORNAR VISÍVEL) ---
botao_clicar.pack(pady=10)

root.mainloop()
print("Programa Finalizado!")