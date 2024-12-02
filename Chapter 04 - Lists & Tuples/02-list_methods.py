list = [1, 8, 7, 2, 21, 15]

list_sorted = list.sort()    
print(list_sorted)

# sort() function doesn't return anything so we can't assgin it to different variabel it will sort the main list variable
print(list)

l = [2, 5, 9, 7, 10, 6]

l.sort()           # Sorts the list

l.reverse()        # Reverses the list

l.append(1)        # Adds the element at the end of the list(1)
l.append(0)        #                                        (0)

l.insert(1, 544)   # Inserts the element at the provided index

l.pop(2)           # It will remove the element from the provided index(9)

l.remove(544)      # Removes the given element from the list(544)

print(l)