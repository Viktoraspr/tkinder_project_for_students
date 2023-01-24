from dataclasses import dataclass

@dataclass()
class EntryDataclass:
    row: int = 0
    column: int = 0


ENTRY_FIND_WORDS_BY_SIMBOLS = EntryDataclass()
