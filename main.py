import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab


def get_image_from_clipboard():
    try:
        # Try to get the image from the clipboard
        img = ImageGrab.grabclipboard()

        # Check if the clipboard contains an image
        if isinstance(img, Image.Image):
            width, height = img.size

            # If you want to process the image, you can do it here
            # Example: Print the top-left pixel's RGB value
            for y in range(height):
                for x in range(width):
                    r, g, b = img.getpixel((x, y))
                    #img.putpixel((x,y), (255,255,255))
                    if r == 0 and b == 0 and g == 0:
                        img.putpixel((x, y), (255, 0, 0))
            #print(f"Top-left pixel RGB: ({r}, {g}, {b})")
            img.show()

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
