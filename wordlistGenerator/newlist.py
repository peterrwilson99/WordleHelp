import json
import sys
from wordfreq import word_frequency

def get_word_frequency(word):
    return word_frequency(word,'en')*100000

def create_len5_wordlist(in_path = "words.txt", out_path = "wordle-words.txt"):
    with open(in_path,'r') as readObj:
        words = readObj.read().split("\n")

    new_word_list = ""

    for word in words:
        if len(word) == 5:
            new_word_list += word + '\n'

    new_word_list = new_word_list[:-1]

    with open(out_path,'w') as writeObj:
        writeObj.write(new_word_list)
    return new_word_list.split("\n")

def create_freq_file(words, json_out_path = 'word_freq.json'):
    word_freq_dict = {}
    for word in words:
        try:
            word_freq_dict[word] = get_word_frequency(word)
        except:
            word_freq_dict[word] = 0

    with open(json_out_path, 'w', encoding='utf-8') as f:
        json.dump(word_freq_dict, f, ensure_ascii=False, indent=4)

def create_wordle_files(in_path = "words.txt", out_path = "wordle-words.txt", json_out_path = 'word_freq.json'):
    words = create_len5_wordlist(in_path, out_path)
    create_freq_file(words,json_out_path)




def main():
    if len(sys.argv) == 2:
        in_path = sys.argv[1]
        create_wordle_files(in_path = in_path)
    elif len(sys.argv) == 3:
        in_path = sys.argv[1]
        out_path = sys.argv[2]
        create_wordle_files(in_path = in_path, out_path = out_path)
    elif len(sys.argv) == 4:
        in_path = sys.argv[1]
        out_path = sys.argv[2]
        json_out_path = sys.argv[3]
        create_wordle_files(in_path = in_path, out_path = out_path, json_out_path = json_out_path)
    else:
        create_wordle_files()

if __name__ == "__main__":
        main()