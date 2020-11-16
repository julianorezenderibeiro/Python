import tkinter as tk
from classes import Aplicacao

root = tk.Tk()
root.title("Compactador de Arquivos")
# root.iconbitmap(default="icone.ico")
root.iconbitmap()
root.geometry("600x500")
root.resizable(width=False, height=False)
Aplicacao(root)
root.mainloop()
