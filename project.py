import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    # Open the image
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if not image_path:
        return

    image = Image.open(image_path)

    # Add the watermark
    watermark_text = "Rehan's Image Watermark"
    watermark_font = ImageFont.truetype("arial.ttf", 36)
    watermark_color = (255, 255, 255, 128)  # RGBA color with transparency

    draw = ImageDraw.Draw(image)
    draw.text(
        (50, 50),
        text=watermark_text,
        font=watermark_font,
        fill=watermark_color,
    )

    # Save the watermarked image
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG Files", "*.png")]
    )

    if not save_path:
        return

    image.save(save_path)
    print("Watermark added and image saved successfully.")


# Create the main window
window = tk.Tk()
window.title("Image Watermarker")
window.geometry("100x100")

# Create a button to add watermark
add_watermark_button = tk.Button(window, text="Add Watermark", command=add_watermark)
add_watermark_button.pack(anchor="center", padx=10, pady=35)

# Start the Tkinter event loop
window.mainloop()
