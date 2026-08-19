import tkinter as tk

from FileManager.functions import (
    open_file,
    save,
    saveFile,
    SaveAsFile
)


def create_menu(window, textArea):
    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)

    file_menu.add_command(
        label="New"
    )

    file_menu.add_command(
        label="Open",
        command=lambda: open_file(window, textArea)
    )

    file_menu.add_command(
        label="Save",
        command=lambda: save(window, textArea)
    )

    file_menu.add_command(
        label="Save As",
        command=lambda: saveAsFile(window, textArea)
    )

    menu_bar.add_cascade(
        label="File",
        menu=file_menu
    )

    return menu_bar