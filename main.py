import tkinter as tk

window = tk.Tk()
window.title("TextEditor")
window.geometry("800x600")

menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar, tearoff=0)

fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As")
fileMenu.add_command(label="Exit")

menuBar.add_cascade(label="File", menu=fileMenu)

window.config(menu=menuBar)


window.mainloop()