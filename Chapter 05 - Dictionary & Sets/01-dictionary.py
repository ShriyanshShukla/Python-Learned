# !!! Dictionary don't allows duplicate keys

myDict = {
    'Fast': "In a quick manner",
    'Shriyansh': "The Coder",
    'Marks': [1, 2, 5],                       # We can also add list inside a Dictionary
    'AnotherDict': {'Teacher': "Harry"}       # We can also add dictionary inside a Dictionary         
}

print(myDict['Shriyansh'])
print(myDict['Marks'])
print(myDict['AnotherDict']['Teacher'])

# Adding and Accessing items in the Dictionart
myDict['fruit'] = ["Banana"]

f = myDict['fruit']

print(myDict)
print(f)