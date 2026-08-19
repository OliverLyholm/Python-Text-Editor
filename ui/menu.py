import tkinter as tk

from FileManager.functions import open_file


def create_menu(window, text_area):
    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)

    file_menu.add_command(label="New")
    file_menu.add_command(
        label="Open",
        command=lambda: open_file(text_area)
    )
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As")

    menu_bar.add_cascade(
        label="File",
        menu=file_menu
    )

    return menu_bar