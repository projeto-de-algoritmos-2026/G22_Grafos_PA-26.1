import tkinter as tk
from main import executar

def iniciar_interface():
    root = tk.Tk()
    root.title("Planejador de Viagens")

    btn = tk.Button(root, text="Calcular Rota", command=executar)
    btn.pack(pady=20)

    root.mainloop()