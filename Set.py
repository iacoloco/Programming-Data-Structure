#Created a set

primary_colors = set(["red" , "yellow"])

#to add a value we can use add. function

primary_colors.add("blue")

#we can write a set with {} eather

numbers_a = {10 ,20, 30, 40,}
numbers_b = {30, 40, 50, 60}
print("number a list: ", numbers_a)
print("number b list: ", numbers_b)
# and combine them
union_set = numbers_a.union(numbers_b)

print(".union : ",union_set)

#Intersection. function : allow to see wich element are in 2 set

intersection = numbers_a.intersection(numbers_b)

print("intersection function: ", intersection)

#Subtract the elements in 2 set

    #Subtract the elements in from b to   =   WIll return the Items Unique to A

a_menus_b = numbers_a.difference(numbers_b) 
print("a - b : ", a_menus_b)

    #Subtract the elements in from a to b = WIll return the Items Unique to A
b_menus_a = numbers_b.difference(numbers_a)
print("b - a: ", b_menus_a) 

#symetric difference function (symmetric_difference) "will return all Item NOT SHARE IN 2 Sets"

symetric_numbers = numbers_a.symmetric_difference(numbers_b)
print("symmetric_difference: ", symetric_numbers)


# FROZENSET : allow to make a immutable SET, (we can't add item)

frozen_primary_colors = frozenset(["red, 'yellow", "blue"])

# This function CAN NOT BE DONE!!!! :    frozen_primary_colors.add("orange")



#
def find_number(numero, listy):
    for number in listy:
        if number == numero:
            return True
    return False  # Return False after the loop if number is not found

def finf_number(numero,listy):

    for number in listy:
        if number == numero:
           print("True")
        else:
            print("false")

print(find_number(100,numbers_a))