l = [1, 123, 5, 35, 90, 77, 125]

def five(n):
    if n%5 == 0:
        return True
    return False

filtered_list = list(filter(five, l))
print(filtered_list)