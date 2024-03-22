# created a function that find the second smallest Item in the List

my_list = [5, 8 ,3 ,2,6, 7]

def searchSecondItem(listy):
    if len(listy) < 1:
       return print("no item in the list")
    if len(listy) > 2:
       
       listySorted = sorted(listy)

       return  print(listySorted[1])
    

searchSecondItem(my_list)