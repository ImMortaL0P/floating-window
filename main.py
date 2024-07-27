import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk  # Ensure Pillow is installed

class FloatingTab:
    def __init__(self, root):
        self.root = root
        self.root.title("Floating Tab")
        self.root.geometry("150x100")
        self.root.attributes("-topmost", True)  # Keep window on top
        self.root.attributes("-alpha", 0.85)  # Set window opacity
        self.root.overrideredirect(True)  # Remove window decorations

        # Load and set icon
        self.icon_image = Image.open("privacy.png")  # Replace with your icon path
        self.icon_image = self.icon_image.resize((20, 20), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(self.icon_image)

        self.drag_frame = tk.Frame(root, bg="gray", height=30)
        self.drag_frame.pack(fill=tk.X)
        
        self.icon_label = tk.Label(self.drag_frame, image=self.icon, bg="gray")
        self.icon_label.pack(side=tk.LEFT, padx=5)

        self.title_label = tk.Label(self.drag_frame, text="Move Me", bg="gray", fg="white", font=("Arial", 12))
        self.title_label.pack(side=tk.LEFT, padx=5)

        self.button = tk.Button(root, text="Launch App", command=self.launch_app, font=("Arial", 12), bg="blue", fg="white")
        self.button.pack(fill=tk.BOTH, expand=True)

        # Bind dragging functionality to the drag_frame
        self.drag_frame.bind("<ButtonPress-1>", self.start_move)
        self.drag_frame.bind("<ButtonRelease-1>", self.stop_move)
        self.drag_frame.bind("<B1-Motion>", self.do_move)

    def launch_app(self):
        try:
            subprocess.Popen(["notepad.exe"])  # Change this to your target application
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch application: {e}")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.x
        y = self.root.winfo_pointery() - self.y
        self.root.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FloatingTab(root)
    root.mainloop()
