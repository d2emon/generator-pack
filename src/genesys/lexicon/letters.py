import random


class Letters:
    LETTERS = [chr(c) for c in range(ord('А'), ord('Я') + 1)]

    def __init__(self, letter_id=0):
        self.letter_id = letter_id

    def __iter__(self):
        return self

    def __next__(self):
        if self.letter_id is None:
            return self.random_letter()
        else:
            return self.LETTERS[self.letter_id]

    @classmethod
    def random_letter(cls, letters=None):
        letters = letters or cls.LETTERS
        return random.choice(letters) if len(letters) > 0 else None

    @property
    def max_articles(self):
        if self.letter_id is None:
            return None
        return len(self.LETTERS)

    @property
    def used_letters(self):
        if self.letter_id is None:
            return self.LETTERS
        if self.letter_id > 0:
            return self.LETTERS[:self.letter_id]
        return []

    def existing_article(self):
        return self.random_letter(self.used_letters)

    def new_article(self, disabled=None):
        return self.random_letter([letter for letter in self.LETTERS if letter != disabled])

    def next_letter(self):
        if self.letter_id is None:
            return

        self.letter_id += 1
        if self.letter_id >= len(self.LETTERS):
            self.letter_id = 0
