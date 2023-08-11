import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab


def get_image_from_clipboard():
    try:
        # Try to get the image from the clipboard
        img = ImageGrab.grabclipboard()

        # Check if the clipboard contains an image
        if isinstance(img, Image.Image):
            # Display the image (for demonstration purposes)
            img.show()

            # If you want to process the image, you can do it here
            # Example: Print the top-left pixel's RGB value
            r, g, b = img.getpixel((0, 0))
            print(f"Top-left pixel RGB: ({r}, {g}, {b})")

        else:
            messagebox.showerror("Error", "No image found in clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve image from clipboard. Error: {e}")


# Create the main window
root = tk.Tk()
root.title("Get Image from Clipboard")

# Create a button to fetch the image from clipboard
btn = tk.Button(root, text="Paste Image from Clipboard", command=get_image_from_clipboard)
btn.pack(pady=20)

root.mainloop()
