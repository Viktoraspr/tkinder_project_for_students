from tkinter import Label, Entry, Button
from classes.file_modification import FileModification

from classes.entries import EntryDataclass
from constants.buttons import ButtonDataclass
from constants.labels import LabelDataclass


class FindWordsBySymbols:

    def __init__(self, master, label: LabelDataclass, entry: EntryDataclass, button: ButtonDataclass):
        self.master = master

        self.label = Label(self.master, text=label.text)
        self.entry = Entry(self.master)
        self.button = Button(self.master, text=button.text, command=self.__find_word_by_symbol)
        self.result = Label(self.master, text='')
    #
        self.label.grid(row=label.row, column=label.column)
        self.entry.grid(row=label.row, column=label.column+1)
        self.button.grid(row=label.row, column=label.column+2)
        self.result.grid(row=label.row, column=label.column+3)

    def __find_word_by_symbol(self):
        value = self.entry.get()
        self.result['text'] = (FileModification().find_words_by_symbols(value))
