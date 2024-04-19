#problem 1:
#Create a Python Class called Basicclass that just contains a static variable called theVariable. Assign theVariable a value of 1.

class BasicClass:
    theVariable = 1

#Problem 2:
#given the following ExampleClass class, create an instance of the class and reference each of its attributes using the dot operator.

class Exampleclass:
    age = 24
    name = 'John Doe'
    location = 'Toronto, Ontario'

# solution goes here:

example_instance = Exampleclass
print(example_instance.age)
print(example_instance.name)
print(example_instance.location)

#Create a Python class called BirthdayBoy that takes in two variable:
   #A string called name
   #An integer called age
#Do not forget your init function!

#Within BirthdayBoy, create a method called birdthday that increase the value of age by 1.
#Once this class has been created, create a instance of the class then call the birthday method on that class to increase its age.
#Check that the age has been appropiately increased by the birthday method by referencing it using the dot operator (for example, instance.age)

class BirthdayBoy:

    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1



me = BirthdayBoy("Nick" , 24)

#print(me.name)
#print(me.age)

me.birthday()
print(me.age)

