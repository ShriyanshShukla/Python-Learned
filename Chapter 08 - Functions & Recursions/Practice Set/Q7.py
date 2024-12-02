def remove_split(string, word):
    new_str = string.replace(word, "")
    return new_str.split()

string = " Harry   is a    good person  "

print(remove_split(string, 'person'))