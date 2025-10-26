# 1. Importação da biblioteca Tkinter
# Usamos 'as tk' para facilitar a escrita do código (é um apelido)
import tkinter as tk

# 1. Importação da biblioteca Tkinter
# Usamos 'as tk' para facilitar a escrita do código (é um apelido)
root = tk.Tk()

# Opcional: Definir um título para a janela
root.title("Meu app")

root.l
# Opcional: Definir o tamanho inicial da janela (largura x altura)
root.geometry("600x400")

# 3. Execução: Iniciar o loop principal
# Esta linha é crucial! Ela coloca a janela na tela e espera por eventos
root.mainloop()

# O código após o mainloop() só será executado quando a janela for fechada
print("Programa finalizado.")

