myDict = {
    'Fast': "In a quick manner",
    'Shriyansh': "The Coder",
    'Marks': [1, 2, 5],                       
    'AnotherDict': {'Teacher': "Harry"},
     1: 2.1,           
}

print(myDict.keys())        # Print the keys of the dictionary

print(myDict.values())      # Print the values of the dictionary

print(myDict.items())       # Print the (kay,value) for all the content of the dictionary

myDict.update({'Friend': "Vishal MC"})    # Update dictionary with supplied key-value pair
print(myDict)

print(myDict.pop('Fast'))              # Removes the item

myDict2 = myDict.copy()                # Copies the dictionary

myDict2.clear()                        # Emties the dictionary

# print(myDict['Shriyansh02'])         # Error
print(myDict.get('Shriyansh02'))       # It will not throw Error even if the provided key isn't presented in
                                       # the dictionary, Instead it will return None data type