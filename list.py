#Linear Search
my_list = [2, 5, 0, 8 ,10, 7]

def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False
item = 7
print(search(item,my_list))
print(my_list.index(item))