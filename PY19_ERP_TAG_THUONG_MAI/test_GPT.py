import tkinter as tk
from PIL import Image, ImageTk

class FrameWithImage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Frame with Image in Top Right Corner")
        self.geometry("600x400")  # Set a fixed size for the window

        # Create a Frame
        self.frame = tk.Frame(self, bg="#f4f4f9", width=600, height=400)
        self.frame.pack(fill="both", expand=True)

        # Load image using Pillow
        self.image = Image.open("your_image.jpg")  # Replace with your image path

        # Resize the image if necessary
        self.image = self.image.resize((100, 100))  # Resize to fit better

        # Convert image to PhotoImage
        self.photo_image = ImageTk.PhotoImage(self.image)

        # Create a label to hold the image
        self.image_label = tk.Label(self.frame, image=self.photo_image, bg="#f4f4f9")
        self.image_label.pack(side="top", anchor="ne", padx=10, pady=10)  # Top-right corner

        # Example label to show content in the frame
        self.example_label = tk.Label(self.frame, text="This is some content in the frame", font=("Helvetica", 12), bg="#f4f4f9")
        self.example_label.pack(pady=50)  # Some padding to show how it works alongside the image

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = FrameWithImage()
    app.run()
