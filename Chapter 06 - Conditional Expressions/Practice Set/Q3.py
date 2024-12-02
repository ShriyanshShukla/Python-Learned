spam = False
spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click on this"

text = input("Write an Email: ")

if spam1 in text:
    spam = True
elif spam2 in text:
    spam = True
elif spam3 in text:
    spam = True
elif spam4 in text:
    spam = True

if spam:
    print("This text is spam")
else:
    print("This text is not spam")