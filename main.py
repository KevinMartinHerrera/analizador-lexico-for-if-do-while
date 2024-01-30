
from scanner import Scanner
import tkinter as tk
from tkinter import scrolledtext

def analyze_input():
    input_text = input_text_widget.get("1.0", tk.END).strip()
    s = Scanner(input_text)
    tokens = s.scanAll()
    result_text_widget.delete("1.0", tk.END)
    for token in tokens:
        result_text_widget.insert(tk.END, f"{token}\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Analizador Léxico")
root.geometry("500x600")  # Tamaño inicial de la ventana

# Crear y configurar widgets
input_label = tk.Label(root, text="Ingresa el código:", font=("Helvetica", 14))
input_label.pack(pady=10)

input_text_widget = scrolledtext.ScrolledText(root, width=40, height=10, font=("Helvetica", 12))
input_text_widget.pack(pady=10)

analyze_button = tk.Button(root, text="Analizar", command=analyze_input)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="Resultados:", font=("Helvetica", 14))
result_label.pack(pady=10)

result_text_widget = scrolledtext.ScrolledText(root, width=50, height=10, font=("Helvetica", 12))
result_text_widget.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()
