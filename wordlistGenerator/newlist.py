with open("new_list.txt",'r') as readObj:
    words = readObj.read().split("\n")

new_word_list = ""

for word in words:
    if len(word) == 5:
        new_word_list += word + '\n'

new_word_list = new_word_list[:-1]

with open("new-5-list.txt",'w') as writeObj:
    writeObj.write(new_word_list)