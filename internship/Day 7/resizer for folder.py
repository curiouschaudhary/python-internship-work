import os
from tkinter import Tk, filedialog, Label, Entry, Button, StringVar, IntVar, messagebox
from PIL import Image

# === Image Resize Logic ===
def resize_images(input_folder, output_folder, width, height, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            try:
                img_path = os.path.join(input_folder, filename)
                with Image.open(img_path) as img:
                    resized_img = img.resize((width, height))
                    base_name = os.path.splitext(filename)[0]
                    output_file = f"{base_name}.{output_format.lower()}"
                    output_path = os.path.join(output_folder, output_file)
                    resized_img.save(output_path, output_format.upper())
                    count += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return count

# === GUI Function ===
def start_resize():
    in_folder = input_folder.get()
    out_folder = output_folder.get()
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

    count = resize_images(in_folder, out_folder, w, h, fmt)
    messagebox.showinfo("Success", f"✅ {count} image(s) resized and saved to {out_folder}")

# === Folder Selectors ===
def browse_input():
    path = filedialog.askdirectory()
    input_folder.set(path)

def browse_output():
    path = filedialog.askdirectory()
    output_folder.set(path)

# === GUI Window ===
app = Tk()
app.title("🖼️ Batch Image Resizer Tool")
app.geometry("400x300")
app.resizable(False, False)

# === State Variables ===
input_folder = StringVar()
output_folder = StringVar()
width = IntVar(value=800)
height = IntVar(value=800)
output_format = StringVar(value="PNG")

# === GUI Layout ===
Label(app, text="Input Folder").pack()
Entry(app, textvariable=input_folder, width=40).pack()
Button(app, text="Browse", command=browse_input).pack(pady=5)

Label(app, text="Output Folder").pack()
Entry(app, textvariable=output_folder, width=40).pack()
Button(app, text="Browse", command=browse_output).pack(pady=5)

Label(app, text="Width").pack()
Entry(app, textvariable=width).pack()

Label(app, text="Height").pack()
Entry(app, textvariable=height).pack()

Label(app, text="Output Format (PNG/JPEG/WEBP)").pack()
Entry(app, textvariable=output_format).pack()

Button(app, text="Start Resizing", command=start_resize, bg="#4CAF50", fg="white").pack(pady=10)

# === Run App ===
app.mainloop()
