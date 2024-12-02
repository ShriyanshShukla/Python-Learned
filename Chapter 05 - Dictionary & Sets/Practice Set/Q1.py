myDict = {
    'Pankha': "Fan",
    'Dabba': "Box",
    'Vastu': "Item"
}

print("Options are:", myDict.keys())
a = input("Enter the hindi word: ")

print("The meaning of your word is:", myDict.get(a))