



animals = [ ('a' , 'anatra') , ('b' , "bologna") , ('c' , 'cakon') ]




animals_dictionary_from_tuples = { item[0] : item[1] for item in animals}
print(animals_dictionary_from_tuples)