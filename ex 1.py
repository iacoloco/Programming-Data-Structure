#Problem statement: compute the average number of pets each student
#has in a given class.

student_pet_count_list = [0, 1, 5, 3, 7]
num_student = len(student_pet_count_list)
print("the student are", num_student)
#student 1 bough 2 pets
student_pet_count_list[0] = student_pet_count_list[0] + 2
print("student 1 bough:" ,student_pet_count_list[0]) 

#add a student at the end(append) with 10 pets
student_pet_count_list.append(10)  
print(student_pet_count_list)
#sum the number of pets
sum=0
for individual_pet_count in student_pet_count_list:
     sum = sum + individual_pet_count

print("The numbers of pets are:", sum)
#average 
average= sum / num_student
print("the average of pets per student is:", average)