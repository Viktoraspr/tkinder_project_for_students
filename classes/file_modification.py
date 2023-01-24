import os
from constants.zen_of_python import THIS_DATA


class FileModification:
    def __init__(self):
        self.file_name = 'zen_of_python.txt'

    def load_data_from_file(self):
        with open(self.file_name, 'r') as file:
            file_data = file.read()
        return file_data.split()

    def create_txt_file(self, data: str = THIS_DATA):
        with open(self.file_name, 'w') as file:
            file.write(data)

    def find_words_by_symbols(self, symbols: str):
        data_list: list = self.load_data_from_file()
        words_list = []

        for word in data_list:
            if all([symbol in word.lower() for symbol in symbols]):
                words_list.append(word)

        return words_list

    def append_words(self, words: str):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(f'\n{words}')

    def delete_data_from_file(self):
        with open(self.file_name, 'r+') as file:
            file.truncate(0)

    def find_words_with_letters_and_length_of_word(self, symbol: str, length: int = None):
        words = self.load_data_from_file()
        result = []
        for word in words:
            if symbol in word.lower():
                if length in [None, len(word.strip(',.!'))]:
                    result.append(word.lower().strip(',.!'))
        return result

    def delete_file(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        else:
            print(f"File {self.file_name} doesn't exists.")
