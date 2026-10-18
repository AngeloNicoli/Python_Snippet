import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Formula ricavata dai dati osservati (fit quadratico su 22 battaglie, SP 1-325.3)
A, B, C = 10.00357207, 968.13646747, -956.88942779

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "personaggi_sparking_zero.json")


def exp_cumulativa(sp: float) -> float:
    return A * sp**2 + B * sp + C


def formatta(n: float) -> str:
    return f"{n:,.0f}".replace(",", ".")


def carica_personaggi() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def salva_personaggi(dati: dict) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


class ExpCalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Sparking Zero - Calcolatore EXP")
        root.geometry("820x680")
        root.resizable(False, False)
        root.configure(bg="#1c2b1f")

        self.personaggi = carica_personaggi()

        self._build_header()
        self._build_personaggio_area()
        self._build_input_area()
        self._build_result_area()
        self._build_table()
        self._popola_tabella()
        self._aggiorna_combobox()

    # ---------- UI sections ----------

    def _build_header(self):
        header = tk.Frame(self.root, bg="#2e7d4f", height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(
            header,
            text="Sparking Zero — Calcolatore EXP / SP",
            font=("Segoe UI", 18, "bold"),
            bg="#2e7d4f",
            fg="white",
        ).pack(pady=12)

    def _build_personaggio_area(self):
        frame = tk.Frame(self.root, bg="#1c2b1f", pady=10)
        frame.pack(fill="x", padx=24)

        tk.Label(
            frame,
            text="Personaggio:",
            font=("Segoe UI", 12),
            bg="#1c2b1f",
            fg="white",
        ).grid(row=0, column=0, sticky="w")

        self.personaggio_var = tk.StringVar()
        self.combo = ttk.Combobox(
            frame,
            textvariable=self.personaggio_var,
            font=("Segoe UI", 12),
            width=22,
            state="normal",
        )
        self.combo.grid(row=0, column=1, padx=10)
        self.combo.bind("<<ComboboxSelected>>", lambda e: self._carica())

        tk.Button(
            frame,
            text="Carica",
            font=("Segoe UI", 10, "bold"),
            bg="#4a90d9",
            fg="white",
            relief="flat",
            padx=10,
            pady=4,
            command=self._carica,
        ).grid(row=0, column=2, padx=4)

        tk.Button(
            frame,
            text="Salva",
            font=("Segoe UI", 10, "bold"),
            bg="#8bc34a",
            fg="#1c2b1f",
            relief="flat",
            padx=10,
            pady=4,
            command=self._salva,
        ).grid(row=0, column=3, padx=4)

        tk.Button(
            frame,
            text="Elimina",
            font=("Segoe UI", 10, "bold"),
            bg="#c0392b",
            fg="white",
            relief="flat",
            padx=10,
            pady=4,
            command=self._elimina,
        ).grid(row=0, column=4, padx=4)

    def _build_input_area(self):
        frame = tk.Frame(self.root, bg="#1c2b1f", pady=6)
        frame.pack(fill="x", padx=24)

        tk.Label(
            frame,
            text="Livello (SP):",
            font=("Segoe UI", 12),
            bg="#1c2b1f",
            fg="white",
        ).grid(row=0, column=0, sticky="w")

        self.sp_var = tk.StringVar()
        entry = tk.Entry(
            frame,
            textvariable=self.sp_var,
            font=("Segoe UI", 12),
            width=12,
            justify="center",
        )
        entry.grid(row=0, column=1, padx=10)
        entry.bind("<Return>", lambda e: self._calcola())

        calc_btn = tk.Button(
            frame,
            text="Calcola",
            font=("Segoe UI", 11, "bold"),
            bg="#8bc34a",
            fg="#1c2b1f",
            activebackground="#a4d96c",
            relief="flat",
            padx=14,
            pady=4,
            command=self._calcola,
        )
        calc_btn.grid(row=0, column=2, padx=10)

    def _build_result_area(self):
        self.result_frame = tk.Frame(self.root, bg="#243626", height=70)
        self.result_frame.pack(fill="x", padx=24, pady=(0, 16))
        self.result_frame.pack_propagate(False)

        self.result_label = tk.Label(
            self.result_frame,
            text="Scegli o inserisci un personaggio, un livello, e premi Calcola",
            font=("Segoe UI", 13, "bold"),
            bg="#243626",
            fg="#c5e1a5",
            wraplength=760,
            justify="left",
        )
        self.result_label.pack(pady=14, padx=12, anchor="w")

    def _build_table(self):
        tk.Label(
            self.root,
            text="Valori significativi (EXP cumulativa stimata)",
            font=("Segoe UI", 11, "bold"),
            bg="#1c2b1f",
            fg="white",
        ).pack(anchor="w", padx=24)

        table_frame = tk.Frame(self.root, bg="#1c2b1f")
        table_frame.pack(fill="both", expand=True, padx=24, pady=(6, 16))

        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#f5f5f5",
            fieldbackground="#f5f5f5",
            foreground="#1c2b1f",
            rowheight=24,
            font=("Segoe UI", 10),
        )
        style.configure(
            "Treeview.Heading",
            background="#8bc34a",
            foreground="#1c2b1f",
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Treeview", background=[("selected", "#aed581")])

        columns = ("sp", "exp_cum", "exp_intervallo")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=12
        )
        self.tree.heading("sp", text="SP")
        self.tree.heading("exp_cum", text="EXP cumulativa")
        self.tree.heading("exp_intervallo", text="EXP nell'intervallo")
        self.tree.column("sp", width=100, anchor="center")
        self.tree.column("exp_cum", width=220, anchor="e")
        self.tree.column("exp_intervallo", width=220, anchor="e")

        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ---------- Logic ----------

    def _popola_tabella(self):
        milestones = list(range(50, 1001, 50))
        prev = 0.0
        for sp in milestones:
            cum = exp_cumulativa(sp)
            delta = cum - prev
            self.tree.insert(
                "", "end", values=(sp, formatta(cum), formatta(delta))
            )
            prev = cum

    def _aggiorna_combobox(self):
        nomi = sorted(self.personaggi.keys())
        self.combo["values"] = nomi

    def _calcola(self):
        testo = self.sp_var.get().strip().replace(",", ".")
        if not testo:
            messagebox.showwarning("Attenzione", "Inserisci un valore di SP.")
            return
        try:
            sp = float(testo)
        except ValueError:
            messagebox.showerror(
                "Valore non valido", "Inserisci un numero valido per il livello SP."
            )
            return

        if sp < 0:
            messagebox.showerror("Valore non valido", "Il livello SP non può essere negativo.")
            return

        nome = self.personaggio_var.get().strip()
        cum = max(exp_cumulativa(sp), 0)
        prefisso = f"{nome} — " if nome else ""
        self.result_label.config(
            text=(
                f"{prefisso}Livello SP {sp:g}  →  EXP cumulativa stimata: {formatta(cum)}\n"
                f"(formula: EXP = {A:.2f}·SP² + {B:.2f}·SP {C:+.2f})"
            )
        )

    def _salva(self):
        nome = self.personaggio_var.get().strip()
        if not nome:
            messagebox.showwarning("Attenzione", "Inserisci il nome del personaggio da salvare.")
            return

        testo = self.sp_var.get().strip().replace(",", ".")
        if not testo:
            messagebox.showwarning("Attenzione", "Inserisci un livello SP da salvare.")
            return
        try:
            sp = float(testo)
        except ValueError:
            messagebox.showerror(
                "Valore non valido", "Inserisci un numero valido per il livello SP."
            )
            return

        self.personaggi[nome] = {"sp": sp}
        salva_personaggi(self.personaggi)
        self._aggiorna_combobox()
        messagebox.showinfo("Salvato", f"Personaggio '{nome}' salvato con livello SP {sp:g}.")

    def _carica(self):
        nome = self.personaggio_var.get().strip()
        if nome not in self.personaggi:
            messagebox.showwarning("Attenzione", f"Nessun personaggio salvato chiamato '{nome}'.")
            return

        sp = self.personaggi[nome].get("sp", 0)
        self.sp_var.set(f"{sp:g}")
        self._calcola()

    def _elimina(self):
        nome = self.personaggio_var.get().strip()
        if nome not in self.personaggi:
            messagebox.showwarning("Attenzione", f"Nessun personaggio salvato chiamato '{nome}'.")
            return

        if not messagebox.askyesno("Conferma", f"Eliminare il personaggio '{nome}'?"):
            return

        del self.personaggi[nome]
        salva_personaggi(self.personaggi)
        self._aggiorna_combobox()
        self.personaggio_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpCalculatorApp(root)
    root.mainloop()
