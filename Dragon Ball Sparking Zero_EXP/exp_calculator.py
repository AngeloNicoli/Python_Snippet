import tkinter as tk
from tkinter import ttk, messagebox

# Formula ricavata dai dati osservati (fit quadratico su 22 battaglie, SP 1-325.3)
A, B, C = 10.00357207, 968.13646747, -956.88942779


def exp_cumulativa(sp: float) -> float:
    return A * sp**2 + B * sp + C


def formatta(n: float) -> str:
    return f"{n:,.0f}".replace(",", ".")


class ExpCalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Sparking Zero - Calcolatore EXP")
        root.geometry("800x600")
        root.resizable(False, False)
        root.configure(bg="#1c2b1f")

        self._build_header()
        self._build_input_area()
        self._build_result_area()
        self._build_table()
        self._popola_tabella()

    # ---------- UI sections ----------

    def _build_header(self):
        header = tk.Frame(self.root, bg="#2e7d4f", height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(
            header,
            text="GOKU — Calcolatore EXP / SP",
            font=("Segoe UI", 18, "bold"),
            bg="#2e7d4f",
            fg="white",
        ).pack(pady=12)

    def _build_input_area(self):
        frame = tk.Frame(self.root, bg="#1c2b1f", pady=16)
        frame.pack(fill="x", padx=24)

        tk.Label(
            frame,
            text="Inserisci il livello (SP):",
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
            text="Inserisci un livello e premi Calcola",
            font=("Segoe UI", 13, "bold"),
            bg="#243626",
            fg="#c5e1a5",
            wraplength=740,
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
            table_frame, columns=columns, show="headings", height=14
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

        cum = max(exp_cumulativa(sp), 0)
        self.result_label.config(
            text=(
                f"Livello SP {sp:g}  →  EXP cumulativa stimata: {formatta(cum)}\n"
                f"(formula: EXP = {A:.2f}·SP² + {B:.2f}·SP {C:+.2f})"
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpCalculatorApp(root)
    root.mainloop()
