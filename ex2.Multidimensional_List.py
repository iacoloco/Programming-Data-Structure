#Multimensinal List

seating_chart =[ 
                [ "SArah" , "Claire" , "Ben" , "Taylor", "Eva"],#i=0
                ["Frankie", "George", "Linsey", "Izzy", "Jack"] ,#i=1
                ["Katherine", "Lauren", "Mary" , "Nathan", "Olie"],#i=2
                ["Chad", "April", "Mat", "Thomas", "Penny"]#i=3
]             

#print Where seet each student

for name, arrays in enumerate(seating_chart):
    print("The value of outer for loop", arrays)
    for element, student_name in enumerate(arrays):
       
        print(f" nested loop ,{student_name} , is in row {element+1}, seat {element+1}")

