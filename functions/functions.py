import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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
    window.hasUnsavedchanges = False
    textArea.edit_modified(False)

# save file as function
def saveAsFile(window, textArea):
        filePath = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        
        if not filePath:
            return False
        
        saved = saveFile(filePath, textArea, window)

        if saved:
            window.current_file = filePath
            return True
        
        return False

# save file data function
def saveFile(filePath, textArea, window):
    contents = textArea.get("1.0", tk.END)

    with open(filePath, "w") as file:
         file.write(contents)

    window.hasUnsavedChanges= False

    return True

# save function
def save(window, textArea):
     if window.current_file is None:
          saveAsFile(window, textArea)
          return
     
     saveFile(window.current_file, textArea, window)

     return True

# unsaved changes function
def textChanged(textArea, window):
     window.hasUnsavedChanges = True

     textArea.edit_modified(False)


# check unsaved changes on close function
def closeApp(window, textArea):
     
     if not window.hasUnsavedChanges:
          window.destroy()
          return

     answer = messagebox.askyesnocancel(
          "Unsaved Changes Detected",
          "You have unsaved changes. Would you like to save before closing?"
     )

     if answer is True:
          saved = save(window, textArea)

          if saved: 
               window.destroy()
     elif answer is False:
          window.destroy()

# create new File function
def newFile(window, textArea):
     
     if not window.hasUnsavedChanges:
          textArea.delete("1.0", tk.END)
          window.current_file = None
          return

     answer = messagebox.askyesnocancel(
          "Unsaved Changes Detected",
          "You have unsaved changes. Would you like to save before closing?"
     )

     if answer is True:
          saved = save(window, textArea)

          if not saved: 
               return
          
     elif answer is None:
          return

     textArea.delete("1.0", tk.END)
     window.hasUnsavedChanges = False
     textArea.edit_modified(False)
     window.current_file = None


     
     