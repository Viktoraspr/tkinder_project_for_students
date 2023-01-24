from tkinter import Label
from classes.file_modification import FileModification
from constants.labels import LabelDataclass

file_modification = FileModification()


class LabelsFieldSimple:

    def __init__(self, master, label: LabelDataclass):
        self.label = Label(master, text=label.text, width=label.width)
        self.label.grid(row=label.row, column=label.column)
