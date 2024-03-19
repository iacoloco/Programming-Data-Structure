#Multimensinal List

seating_chart =[ 
                [ "SArah" , "Claire" , "Ben" , "Taylor", "Eva"],#i=0
                ["Frankie", "George", "Linsey", "Izzy", "Jack"] ,#i=1
                ["Katherine", "Lauren", "Mary" , "Nathan", "Olie"],#i=2
                ["Chad", "April", "Mat", "Thomas", "Penny"]#i=3
]             

#print Where seet each student

for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} , is in raw {i+1}, seat {j+1}")


