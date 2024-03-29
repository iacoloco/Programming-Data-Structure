# CHALLENGE :
# CREATE A PROGRAM THAT DETERMINES WHETER A PIECE OF TEXT HAS UNIQUE CHARACTERS.

#Hit : Remember that a Set has always unique characters, it can not contain sames values.

#Try this to Undestand
#string_set = set("Hello")
#print(string_set)

def find_if_Text_has_unique_Character(text):
    convertion_to_set = set(text)
    if len(convertion_to_set) == len(text):
       return True
    else:
        return False
    

#test: "Hello World"
print(find_if_Text_has_unique_Character("hello world"))
#test: "sample"
print(find_if_Text_has_unique_Character("sample"))

#Implementation of the funtion:

def find_if_Text_has_unique_CharacterV2(text):
    convertion_to_set = set(text)
    return len(convertion_to_set) == len(text)

#test implementation:

print('test v2 word- hello world: ' ,find_if_Text_has_unique_CharacterV2("hello world"))
print("test v2 word-sample: ",find_if_Text_has_unique_CharacterV2("sample"))

