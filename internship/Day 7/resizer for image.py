import os
from tkinter import Tk, filedialog, Label, Entry, Button, StringVar, IntVar, messagebox
from PIL import Image

# === Resize Logic for Single Image ===
def resize_image(image_path, output_folder, width, height, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with Image.open(image_path) as img:
            resized_img = img.resize((width, height))

            base_name = os.path.splitext(os.path.basename(image_path))[0]
            output_filename = f"{base_name}_resized.{output_format.lower()}"
            output_path = os.path.join(output_folder, output_filename)

            resized_img.save(output_path, output_format.upper())
            return output_path
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# === Start Resize on Button Click ===
def start_resize():
    path = image_path.get()
    folder = output_folder.get()

    if not path or not folder:
        messagebox.showerror("Missing Input", "Please select both image and output folder.")
        return

    try:
        w = int(width.get())
        h = int(height.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Width and Height must be numbers.")
        return

    fmt = output_format.get().upper()
    if fmt not in ["PNG", "JPEG", "WEBP"]:
        messagebox.showerror("Format Error", "Supported formats: PNG, JPEG, WEBP")
        return

    result = resize_image(path, folder, w, h, fmt)
    if result:
        messagebox.showinfo("Success", f"Image saved at:\n{result}")
    else:
        messagebox.showerror("Error", "Something went wrong.")

# === File/Folder Browsers ===
def browse_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")])
    image_path.set(path)

def browse_output():
    path = filedialog.askdirectory()
    output_folder.set(path)

# === GUI Setup ===
app = Tk()
app.title("🖼️ Single Image Resizer Tool")
app.geometry("400x320")
app.resizable(False, False)

# === State Variables ===
image_path = StringVar()
output_folder = StringVar()
width = IntVar(value=800)
height = IntVar(value=800)
output_format = StringVar(value="PNG")

# === GUI Layout ===
Label(app, text="Select Image").pack()
Entry(app, textvariable=image_path, width=40).pack()
Button(app, text="Browse", command=browse_image).pack(pady=5)

Label(app, text="Output Folder").pack()
Entry(app, textvariable=output_folder, width=40).pack()
Button(app, text="Browse", command=browse_output).pack(pady=5)

Label(app, text="Width").pack()
Entry(app, textvariable=width).pack()

Label(app, text="Height").pack()
Entry(app, textvariable=height).pack()

Label(app, text="Output Format (PNG/JPEG/WEBP)").pack()
Entry(app, textvariable=output_format).pack()

Button(app, text="Resize Image", command=start_resize, bg="#4CAF50", fg="white").pack(pady=10)

# === Run GUI ===
app.mainloop()
