from random import choice

with open("wordle-words.txt",'r') as readObj:
        words = readObj.read().split("\n")

class WordleHelper:
    def __init__(self):
        self.possible_words = words
        self.num_options = len(words)

    def remove_letter(self,char, print_change = True):
        new_word_list = []
        for word in self.possible_words:
            if char.lower() not in word.lower():
                new_word_list.append(word)
        self.modify_possible_words(new_word_list, print_change)

    def remove_letters(self, chars = []):
        if isinstance(chars,str):
            new_chars = []
            for index in range(len(chars)):
                new_chars.append(chars[index])
            
            new_chars = list(dict.fromkeys(new_chars))
            chars = new_chars

        for char in chars:
            self.remove_letter(char, print_change = False)
        print(self.num_options, "words possible")

    def letter_exists_index(self, char, index):
        new_word_list = []
        for word in self.possible_words:
            if char.lower() == word[index].lower():
                new_word_list.append(word)
        self.modify_possible_words(new_word_list)
    
    def letter_exists_but_not_at_index(self, char, index):
        new_word_list = []
        for word in self.possible_words:
            if char.lower() in word.lower() and char.lower() not in word[index].lower():
                new_word_list.append(word)
        self.modify_possible_words(new_word_list)
    
    def letter_exists(self,char, print_change = True):
        new_word_list = []
        for word in self.possible_words:
            if char in word:
                new_word_list.append(word)
        self.modify_possible_words(new_word_list, print_change)
    
    def letters_exist(self,chars=[]):
        for char in chars:
            self.letter_exists(char,print_change = False)
        print(self.num_options, "words possible")
    
    def modify_possible_words(self, new_word_list, print_change = True):
        self.possible_words = new_word_list
        self.num_options = len(new_word_list)
        if print_change:
            print(self.num_options, "words possible")

    def give_guess_word(self):
        print("Good Guess: ",choice(self.possible_words))

    def print_words(self):
        for word in self.possible_words:
            print(word)


def workspace():
    wordleGame = WordleHelper()
    

if __name__ == "__main__":
    workspace()