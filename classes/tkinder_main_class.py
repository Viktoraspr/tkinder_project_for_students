from classes.buttons import ButtonFieldSimple
from classes.entries import ENTRY_FIND_WORDS_BY_SIMBOLS
from classes.find_words_by_symbols import FindWordsBySymbols
from classes.program_settings import ProgramSettings
from classes.file_modification import FileModification
from constants.buttons import BUTTON_CREATE_FILE, BUTTON_DELETE_FILE, BUTTON_FIND_WORDS_BY_SIMBOLS
from constants.labels import LABEL_FIND_WORDS_BY_SIMBOLS

file_modification = FileModification()


class TkinderManager(ProgramSettings):
    def __init__(self, master):
        super().__init__(master)
        self.button_create_file = ButtonFieldSimple(master=master, button=BUTTON_CREATE_FILE)
        self.find_words_by_symbols = FindWordsBySymbols(master,
                                                        button=BUTTON_FIND_WORDS_BY_SIMBOLS,
                                                        entry=ENTRY_FIND_WORDS_BY_SIMBOLS,
                                                        label=LABEL_FIND_WORDS_BY_SIMBOLS)
        self.button_delete_file = ButtonFieldSimple(master=master, button=BUTTON_DELETE_FILE)



        master.bind("<Escape>", lambda event: master.destroy())

