# Without Functions
marks1 = [45, 78, 86, 77]
percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/4)

# With Functions
marks2 = [33, 34, 98, 56]
percentage2 = (sum(marks2)/len(marks2))

print(percentage1, percentage2)

# Defining a Function
def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/4)
  # OR
  # return (sum(marks)/len(marks))

percentage1 = percent(marks1)
percentage2 = percent(marks2)

print(percentage1, percentage2)