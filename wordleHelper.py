from random import choice
import json

with open("wordle-words.txt",'r') as readObj:
    words = readObj.read().split("\n")
with open("word_freq.json") as readObj:
    word_freq = json.load(readObj)

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
    
    def letter_exists_but_not_at_indexs(self, char, indexs):
        for index in indexs:
            self.letter_exists_but_not_at_index(char, index, False)
        print(self.num_options, "words possible")
        
    def letter_exists_but_not_at_index(self, char, index, print_change = True):
        new_word_list = []
        for word in self.possible_words:
            if char.lower() in word.lower() and char.lower() not in word[index].lower():
                new_word_list.append(word)
        self.modify_possible_words(new_word_list, print_change)
    
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
        self.possible_words.sort(key=get_word_freq, reverse=True)
        print("Good Guess: ",self.possible_words[0])

    def give_top_5_guess_words(self):
        self.possible_words.sort(key=get_word_freq, reverse=True)
        print("Good Guess: ",self.possible_words[0:5])

    def print_words(self):
        for word in self.possible_words:
            print(word)

def get_word_freq(word):
    return word_freq[word]

def workspace():
    wordleGame = WordleHelper()
    wordleGame.remove_letters("udiwm")
    wordleGame.letter_exists_but_not_at_index("a",0)
    wordleGame.letter_exists_but_not_at_index("a",4)
    wordleGame.letter_exists_but_not_at_index("o",4)
    wordleGame.letter_exists_but_not_at_index("o",1)
    wordleGame.letter_exists_but_not_at_index("n",4)
    wordleGame.give_top_5_guess_words()
    

if __name__ == "__main__":
    workspace()