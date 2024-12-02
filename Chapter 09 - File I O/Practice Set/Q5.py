bad_words = ['Gadha', 'Pagal', 'Brainless']

with open('donkey.txt') as f:
    a = f.read()

for word in bad_words:
    if word in a:
        a = a.replace(word, '######')

with open('donkey.txt', 'w') as f:
    f.write(a)

# s = '''Donkey donkey What do you do?
# Carry loads for all of you,
# Donkey what do you eat?
# Oh! Grass and leaves and carrots so sweet,
# Donkey donkey I love you,
# Oh! Thank you boy, I love you too.'''
# l = s.split()

# print(l)
# for word in l:
#     if word.upper() == 'DONKEY':
#         a = l.index(word)
#         l.remove(word)
#         l.insert(a, '######')
# print(l)