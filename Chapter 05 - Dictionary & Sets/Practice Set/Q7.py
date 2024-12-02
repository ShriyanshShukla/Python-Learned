d = {}

f1 = input("Abhishek Enter your favourite language: ")
f2 = input("Subrat Enter your favourite language: ")
f3 = input("Vishal Enter your favourite language: ")
f4 = input("Abhishek Enter your favourite language: ")

d.update({'Abhishek': f1}) 
d.update({'Subrat': f2})
d.update({'Vishal': f3})
d.update({'Abhishek': f4})

print(d) 
# As we can see the value of the same key is updated
