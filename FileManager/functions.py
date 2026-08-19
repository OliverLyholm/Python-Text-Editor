import tkinter as tk
from tkinter import filedialog


def open_file(text_area):
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    with open(file_path, "r") as file:
        contents = file.read()

    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", contents)