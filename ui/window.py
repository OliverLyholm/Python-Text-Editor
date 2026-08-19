import tkinter as tk

from ui.menu import create_menu
from functions.functions import (
    textChanged,
    closeApp,
    save,
    saveAsFile,
    open_file,
    newFile
)

#Function that creates the shortcuts
def shortcutSetup(window, textArea):
    window.bind(
        "<Control-s>",
        lambda event: save(window, textArea)
    )

    window.bind(
        "<Control-Alt-s>",
        lambda event: saveAsFile(window, textArea)
    )

    window.bind(
        "<Control-o>",
        lambda event: open_file(window, textArea)
    )

    window.bind(
        "<Control-n>",
        lambda event: newFile(window, textArea)
    )


def create_window():
    window = tk.Tk()
    window.title("TextEditor")
    window.geometry("800x600")

    textArea = tk.Text(window)
    textArea.pack(fill="both", expand=True)

    window.current_file = None
    window.hasUnsavedChanges = False

    textArea.bind(
        "<<Modified>>",
        lambda event: textChanged(textArea, window)
    )

    menu_bar = create_menu(window, textArea)

    window.config(menu=menu_bar)

    window.protocol(
        "WM_DELETE_WINDOW",
        lambda: closeApp(window, textArea)
    )

    shortcutSetup(window, textArea)

    return window