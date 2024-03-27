#Find the second smallest number in an array


my_list = [2, 10 , 7, 1, 4]

#print(sorted(my_list))
# the big Notation in this function is n log n because use sorted function
def find_the_second_smallest(lst):
    if list == []:
        return print("list empty")
    elif len(lst) > 1 :
        sorted_list = sorted(lst)
        return print("the second smallest is: " , sorted_list[1] )

#find_the_second_smallest(my_list)

# A better solotution with O(n) will be:

def Find_Second_v2(lst):
    if len(lst) < 2:
        return None
    smalles = float('inf')
    secondSmallest = float('inf')
    for num in lst:
        if num < smalles:
            secondSmallest = smalles
            smalles = num
            
        elif num < secondSmallest:
            secondSmallest = num
    return secondSmallest

print(Find_Second_v2(my_list))




 
