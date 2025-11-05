import tkinter as tk
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

       
        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=10)

        # Brush setup
        self.brush_color = "black"
        self.brush_size = 4

       
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.last_x = None
        self.last_y = None

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y,
                                    fill=self.brush_color, width=self.brush_size)
            self.draw.line((self.last_x, self.last_y, x, y),
                           fill=self.brush_color, width=self.brush_size)
        self.last_x, self.last_y = x, y

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        filename = "digit1.png"
        resized = self.image.resize((28, 28), Image.LANCZOS)  # High-quality downscaling
        resized.save(filename)
        print(f"Saved resized image as {filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
