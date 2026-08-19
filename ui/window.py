import tkinter as tk

from ui.menu import create_menu


def create_window():
    window = tk.Tk()
    window.title("TextEditor")
    window.geometry("800x600")

    textArea = tk.Text(window)
    textArea.pack(fill="both", expand=True)

    window.current_file = None

    menu_bar = create_menu(window, textArea)

    window.config(menu=menu_bar)

    return window