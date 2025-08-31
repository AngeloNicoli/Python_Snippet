import tkinter as tk
from tkinter import messagebox

def calcola_forza():
    try:
        massa = float(entry_massa.get())
        accelerazione = float(entry_accelerazione.get())
        forza = massa * accelerazione
        label_risultato.config(text=f"Forza = {forza:.2f} N")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori numerici validi.")

def cancella_campi():
    entry_massa.delete(0, tk.END)
    entry_accelerazione.delete(0, tk.END)
    label_risultato.config(text="Forza = ? N")

# Crea la finestra principale
finestra = tk.Tk()
finestra.title("Secondo Principio della Dinamica")

# Etichetta e input per la massa
tk.Label(finestra, text="Massa (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_massa = tk.Entry(finestra)
entry_massa.grid(row=0, column=1)

# Etichetta e input per l'accelerazione
tk.Label(finestra, text="Accelerazione (m/s²):").grid(row=1, column=0, padx=10, pady=10)
entry_accelerazione = tk.Entry(finestra)
entry_accelerazione.grid(row=1, column=1)

# Pulsante per calcolare la forza
btn_calcola = tk.Button(finestra, text="Calcola Forza", command=calcola_forza)
btn_calcola.grid(row=2, column=0, padx=10, pady=10)

# Pulsante per cancellare i campi
btn_cancella = tk.Button(finestra, text="Cancella", command=cancella_campi)
btn_cancella.grid(row=2, column=1, padx=10, pady=10)

# Etichetta per mostrare il risultato
label_risultato = tk.Label(finestra, text="Forza = ? N", font=("Arial", 14))
label_risultato.grid(row=3, column=0, columnspan=2, pady=10)

# Avvia l'interfaccia grafica
finestra.mainloop()