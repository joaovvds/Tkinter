import tkinter as tk

root = tk.Tk()
root.title("Programa com Label")
root.geometry("400x200")

# --- 2. CRIAÇÃO DO WIDGET LABEL ---

# Passo A: Criar o objeto Label
# Parâmetros:
# - master/parent (primeiro): Onde este widget deve ser colocado (root)
# - text: O texto que será exibido

rotulo_saudacao = tk.Label(root, text="olá Programador! Tkinter é fixe")

# --- 3. GERENCIAMENTO DE LAYOUT (TORNAR VISÍVEL) ---

# Passo B: Posicionar o Label usando o gerenciador de layout 'pack'
# O pack é o mais simples: ele "empacota" o widget no centro ou numa lateral

rotulo_saudacao.pack(pady=20)# 'pady=20' adiciona 20px de espaço vertical acima e abaixo do widget

root.mainloop()
print("programa finalizado")
