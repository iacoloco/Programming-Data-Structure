my_list = [2, 10 , 7, 1, 4]

print(sorted(my_list))

print(sorted(my_list, reverse=True))

student_grate = [('Sara', 89) , ('Rebecca', 82) , ('Mat', 91)]
print(sorted(student_grate, key=lambda x:x[1] , reverse = True))
