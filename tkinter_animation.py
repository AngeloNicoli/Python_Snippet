import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("60 FPS Canvas Update")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Create a circle
        self.circle = self.canvas.create_oval(50, 50, 100, 100, fill="blue")
        self.dx = 5  # Movement in x-direction

        self.update_frame()

    def update_frame(self):
        # Move the circle
        
        self.canvas.move(self.circle, self.dx, 0)
        self.canvas.configure(bg = "black")
        # Bounce off the walls
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if x2 >= 800 or x1 <= 0:
            self.dx = -self.dx

        # Schedule next frame (16 ms ≈ 60 FPS)
        self.root.after(16, self.update_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
