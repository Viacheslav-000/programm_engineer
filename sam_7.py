with open('sam_7_5.txt', 'r') as file:
    text = file.read()

sen = text.split()

max_word = max(sen, key=len)
print(max_word, len(max_word), sep='\n')