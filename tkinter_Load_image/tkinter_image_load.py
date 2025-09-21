import tkinter as tk

# Crea la finestra principale
root = tk.Tk()

# Crea un canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Carica e ridimensiona l'immagine
triangle_image = tk.PhotoImage(file="images/Triangle.png")
triangle_resized = triangle_image.subsample(4, 4)

for i in range(4):
    for j in range(4):
        canvas.create_image((i*100)+50, (j*100)+50, image=triangle_resized)
        
# Posiziona l'immagine al centro del canvas (x=200, y=200)
canvas.create_image(200, 200, image=triangle_resized)

# Serve per mantenere un riferimento all'immagine
canvas.image = triangle_resized

# Avvia il loop della GUI
root.mainloop()
