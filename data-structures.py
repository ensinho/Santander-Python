## here lets check some data structures in python
#  Starting with arrays!

games = ['TFT', 'Showdown', 'Pokémon Platinum']

print(games[2]) # here it prints the third element in the array, because it starts on 0
print(games[-2]) # now it will print the middle element, since it decays from the length of the array

#Append method
games.append("League of Legends") # adds a new item to the array
print("Adding a new game to games!" , games)

#Pop Method
games.pop(1) # Remove the 1 element, not the first, but the one in that position.
print("Using the pop method" , games )

'''It has a lot of methods, like insert where it can put in a specific position, remove where it removes the first occurency of an element,
pop() thar removes and return the element in a specific position. Sort that organize the list and reverse that reverses that order.'''


#Comprehension lists

numbers = [1,2,3,4,5]
squared = [x ** 2 for x in numbers if x % 2 == 0]
print(squared) # whats gonna happen?
# thats right, its gonna print thhe squared even numbers only!

newTuple = ('TFT', 'Showdown')
# a tuple its like a list, but its non mutable, it cannot be changed once its created
# and has with it some new methos, like count, index and len.


#Dictionarys - mutable and not sorted!

computer = {"user": "Enzo", "Age": 20, "SO": "Windows"}
print(computer["user"]) # it returns the value associated to the key

# update example
computer.update({"browser": 'Edge'})
print(computer) # its like an append hehe

''' It has some cool methods, 
like Key() that returns the keys of the dictionary, values(), items() for a big view, update(other_dictonary) to update based on another dict'''