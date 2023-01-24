from tkinter import Button
from classes.file_modification import FileModification
from constants.buttons import ButtonDataclass

file_modification = FileModification()


class ButtonFieldSimple:
    def __init__(self, master, button: ButtonDataclass):
        self.button = Button(master, text=button.text, fg=button.fg, width=button.width)
        self.button.grid(row=button.row, column=0)


    # def __init__(self, master, button: ButtonDataclass):
        # self.button = Button(master, text=button.text, width=button.width, command=button.command)
        # self.button.grid(row=button.row, column=button.column)
