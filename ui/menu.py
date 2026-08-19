import tkinter as tk

from functions.functions import (
    open_file,
    save,
    saveFile,
    saveAsFile,
    newFile
)


def create_menu(window, textArea):
    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)

    file_menu.add_command(
        label="New",
        command=lambda: newFile(window, textArea),
        accelerator="Ctrl+N"
    )

    file_menu.add_command(
        label="Open",
        command=lambda: open_file(window, textArea),
        accelerator="Ctrl+O"
    )

    file_menu.add_command(
        label="Save",
        command=lambda: save(window, textArea),
        accelerator="Ctrl+S"
    )

    file_menu.add_command(
        label="Save As",
        command=lambda: saveAsFile(window, textArea),
        accelerator="Ctrl+Alt+S"
    )

    menu_bar.add_cascade(
        label="File",
        menu=file_menu
    )

    return menu_bar