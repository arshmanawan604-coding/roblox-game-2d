import tkinter as tk
from tkinter import messagebox

class Roblox2DGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 2D Sandbox (Roblox Style)")
        self.root.geometry("800x600")
        
        # Game Grid Variables
        self.grid_size = 40
        self.current_material = "brown" # Default block color
        self.blocks = {}
        
        # Sidebar for controls
        self.sidebar = tk.Frame(root, width=150, bg="#2c3e50")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Game Canvas
        self.canvas = tk.Canvas(root, bg="#87CEEB", width=650, height=600) # Sky Blue background
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # UI Buttons for Materials
        tk.Label(self.sidebar, text="SELECT BLOCK", fg="white", bg="#2c3e50", font=("Arial", 12, "bold")).pack(pady=10)
        
        materials = [("Dirt (Brown)", "brown"), ("Grass (Green)", "green"), ("Stone (Gray)", "gray"), ("Brick (Red)", "red")]
        for text, color in materials:
            btn = tk.Button(self.sidebar, text=text, bg=color, fg="white", width=12, command=lambda c=color: self.set_material(c))
            btn.pack(pady=5)
            
        # Instruction Label
        instructions = "\n\nCONTROLS:\nLeft Click: Place\nRight Click: Delete\n"
        tk.Label(self.sidebar, text=instructions, fg="lightgray", bg="#2c3e50", justify=tk.LEFT).pack(pady=20)

        # Bind Mouse Events
        self.canvas.bind("<Button-1>", self.place_block)
        self.canvas.bind("<Button-3>", self.delete_block)

    def set_material(self, color):
        self.current_material = color

    def place_block(self, event):
        # Snap to grid
        x = (event.x // self.grid_size) * self.grid_size
        y = (event.y // self.grid_size) * self.grid_size
        
        # Check if block already exists
        if (x, y) not in self.blocks:
            rect_id = self.canvas.create_rectangle(x, y, x + self.grid_size, y + self.grid_size, fill=self.current_material, outline="black")
            self.blocks[(x, y)] = rect_id

    def delete_block(self, event):
        # Snap to grid
        x = (event.x // self.grid_size) * self.grid_size
        y = (event.y // self.grid_size) * self.grid_size
        
        # Remove block if exists
        if (x, y) in self.blocks:
            self.canvas.delete(self.blocks[(x, y)])
            del self.blocks[(x, y)]

if __name__ == "__main__":
    root = tk.Tk()
    game = Roblox2DGame(root)
    root.mainloop()

