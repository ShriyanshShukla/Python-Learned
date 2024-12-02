with open('poems.txt') as f:
    poem = f.read()

if 'twinkle' in poem:
    print("Yes, This string contains the word")
else:
    print("No, This string don't contains the word")