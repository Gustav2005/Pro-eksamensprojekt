import tkinter as tk


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        # Create canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Bind mouse button events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        # Keep track of the drawing state, the starting point of the current line,
        # the previous point, and the size of the tool
        self.drawing = False
        self.start_x = None
        self.start_y = None
        self.prev_x = None
        self.prev_y = None
        self.size = 2  # Default size

        # Add buttons for changing tools and size
        self.pencil_button = tk.Button(
            root, text="Pencil", command=self.use_pencil)
        self.pencil_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(
            root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        self.size_button = tk.Scale(
            root, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_button.pack(side=tk.LEFT)
        self.size_button.set(self.size)  # Set default size

        # Set default tool
        self.current_tool = "pencil"

    def start_draw(self, event):
        # Update the starting point and set drawing state to True
        self.start_x = event.x
        self.start_y = event.y
        self.drawing = True

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            # If it's not the first point
            if self.prev_x is not None and self.prev_y is not None:
                if self.current_tool == "pencil":
                    # Draw using the pencil tool
                    self.canvas.create_oval(
                        x - self.size, y - self.size, x + self.size, y + self.size, fill="black")
                    # Draw a line from the previous point to the current point
                    self.canvas.create_line(
                        self.prev_x, self.prev_y, x, y, fill="black", width=self.size * 2)
                elif self.current_tool == "eraser":
                    # Erase using the eraser tool
                    self.canvas.create_rectangle(
                        x - self.size, y - self.size, x + self.size, y + self.size, fill="white", outline="")
            # Update the previous point
            self.prev_x = x
            self.prev_y = y

    def stop_draw(self, event):
        # Reset the drawing state and previous point
        self.drawing = False
        self.prev_x = None
        self.prev_y = None

    def use_pencil(self):
        self.current_tool = "pencil"

    def use_eraser(self):
        self.current_tool = "eraser"

    def change_size(self, size):
        self.size = int(size)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
