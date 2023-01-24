from dataclasses import dataclass

WIDTH = 15


@dataclass()
class LabelDataclass:
    text: str = 'Describe the text'
    row: int = 0
    column: int = 0
    width: int = WIDTH


LABEL_FIND_WORDS_BY_SIMBOLS = LabelDataclass(
    text='Find words by symbols',
    row=1,
    column=0,
)
