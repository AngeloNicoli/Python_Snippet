dati = [
    ["Nome", "Età", "Città"],
    ["Luca", 25, "Milano"],
    ["Anna", 30, "Roma"],
    ["Marco", 22, "Torino"]
]

# Larghezze massime delle colonne
larghezze = [max(len(str(riga[i])) for riga in dati) for i in range(len(dati[0]))]

# Funzione per stampare una riga
def stampa_riga(riga):
    print("| " + " | ".join(str(val).ljust(larghezze[i]) for i, val in enumerate(riga)) + " |")

# Stampa la tabella
print("-" * (sum(larghezze) + len(larghezze)*3 + 1))
for i, riga in enumerate(dati):
    stampa_riga(riga)
    if i == 0:
        print("-" * (sum(larghezze) + len(larghezze)*3 + 1))
print("-" * (sum(larghezze) + len(larghezze)*3 + 1))
