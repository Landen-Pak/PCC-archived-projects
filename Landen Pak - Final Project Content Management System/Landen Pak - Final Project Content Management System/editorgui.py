import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import databackend
import htmlgenerator

class editorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Webpage Editor")

        self.frame = ttk.Frame(self.root, padding = 5)
        self.frame.pack()

        self.data = databackend.getJsonData()

        # Row 1
        self.titleDisplay = ttk.Label(self.frame, text=self.data["title"], font=('Calibre', 10))
        self.titleDisplay.grid(row=0, column=0, padx=10, pady=10)

        self.editButton = ttk.Button(self.frame, text= 'Edit', state='normal', command=self.editText)
        self.editButton.grid(row=0, column=1, padx=10, pady=10)

        # Row 2
        self.contentDisplay = ttk.Label(self.frame, text=self.data["content"], font=('Calibre', 10))
        self.contentDisplay.grid(row=1, column=0, padx=10, pady=10)

        self.saveButton = ttk.Button(self.frame, text= 'Save', state='disabled', command=self.saveText)
        self.saveButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10)


    # Function for editing text - hides display GUI and enables entry boxes
    def editText(self):
        self.saveButton.config(state='normal')
        self.editButton.config(state='disabled')
        self.titleDisplay.grid_remove()
        self.contentDisplay.grid_remove()

        # Row 1
        self.titleEntry = tk.Text(self.frame, wrap='word', height=2, width=50)
        self.titleEntry.insert(tk.END, self.data["title"])
        self.titleEntry.grid(row=0, column=0, padx=10, pady=10)

        # Row 2
        self.contentEntry = tk.Text(self.frame, wrap='word', height=5, width=50)
        self.contentEntry.insert(tk.END, self.data["content"])
        self.contentEntry.grid(row=1, column=0,padx=10, pady=10)


    # Function for saving text - hides entry GUI and enables display for title and content
    def saveText(self):
        self.saveButton.config(state='disabled')
        self.editButton.config(state='normal')
        self.titleEntry.grid_remove()
        self.contentEntry.grid_remove()

        # retrieve data
        self.newTitle = self.titleEntry.get(1.0, tk.END).strip()
        self.newContent = self.contentEntry.get(1.0, tk.END).strip()

        # update GUI
        self.titleDisplay.config(text=self.newTitle)
        self.contentDisplay.config(text=self.newContent)
        self.titleDisplay.grid()
        self.contentDisplay.grid()

        # update json
        databackend.setJsonData(self.newTitle, self.newContent)
        self.data = databackend.getJsonData()

        # update html
        htmlgenerator.generateHTML(self.newTitle, self.newContent)

if __name__ == "__main__":
    root = ThemedTk(theme="radiance") 
    app = editorGUI(root)
    root.mainloop()