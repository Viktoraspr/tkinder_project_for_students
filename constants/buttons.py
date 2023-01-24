from dataclasses import dataclass
from typing import Any

from classes.file_modification import FileModification

file_modification = FileModification()

WIDTH = 25


@dataclass()
class ButtonDataclass:
    text: str = 'Describe the button'
    width: int = WIDTH
    command: Any = None
    row: int = 0
    column: int = 0
    fg: str = 'red'


BUTTON_CREATE_FILE = ButtonDataclass(
    text='Create file',
    command=file_modification.create_txt_file,
    row=0,
    column=0,
)

BUTTON_DELETE_FILE = ButtonDataclass(
    text='Delete file',
    command=file_modification.delete_file,
    row=10,
    fg='black',
    width=10
)


BUTTON_FIND_WORDS_BY_SIMBOLS = ButtonDataclass(
    text='Find word by file',
)