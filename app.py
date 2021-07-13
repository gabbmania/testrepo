sentence = "This is a common interview question. So you have to answer it correctly or else you will fail!"

char_dict = {}
for char in sentence:
    if char in char_dict:
        char_dict[char] += 1
    elif char not in char_dict:
        char_dict[char] = 0

sorted_char_dict = sorted(char_dict.items(), key=lambda value: value[1], reverse=True)
print(sorted_char_dict)
print(f"The most frequent character in the 'sentence' variable aside from 'space' is '{sorted_char_dict[1][0]}'.")
