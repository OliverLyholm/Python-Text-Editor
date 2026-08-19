import tkinter as tk

from ui.menu import create_menu


def create_window():
    window = tk.Tk()
    window.title("TextEditor")
    window.geometry("800x600")

    text_area = tk.Text(window)
    text_area.pack(fill="both", expand=True)

    menu_bar = create_menu(window, text_area)

    window.config(menu=menu_bar)

    return window