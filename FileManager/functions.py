import tkinter as tk
from tkinter import filedialog

# Open File Funtion
def open_file(window, textArea):
    filePath = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filePath:
        return

    with open(filePath, "r") as file:
        contents = file.read()

    textArea.delete("1.0", tk.END)
    textArea.insert("1.0", contents)

    window.current_file = filePath

# save file as function
def SaveAsFile(window, textArea):
        filePath = filedialog.asksaveasfilename(
        title="Save As",
        filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        
        if not filePath:
            return
        
        saveFile(filePath, textArea)

        
        window.current_file = filePath

# save file data function
def saveFile(filePath, textArea):
    contents = textArea.get("1.0", tk.END)

    with open(filePath, "w") as file:
         file.write(contents)

# save function
def save(window, textArea):
     if window.current_file is None:
          SaveAsFile(window, textArea)
          return
     saveFile(window.current_file, textArea)
     