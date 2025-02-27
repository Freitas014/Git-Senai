import tkinter as tk

janela = tk.Tk()

janela.title("O REI")

mensagem = tk.Label(text = "Os mistérios da vida", fg ='white', bg = '#0000EE', width = 50, height = 10)
mensagem.pack()

mensagem2 = tk.Label(text = "São encontrados nele")
mensagem2.pack()

moeda = tk.Entry()
moeda.pack()

janela.mainloop()