# Advanced Problem Set Version 1
# Problem 1: Villager Class

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:

    # What are the required arguments for the constructor?
    # What properties does the class Villager have?


# P - Plan
# 2. Write out in plain English what you want to do:

    # 1) Define the class `Villager`.
    # 2) Define the `__init__()` constructor with parameters `name`, `species`, and `catchphrase`.
    # 3) Initialize the `name` property with the `name` parameter.
    # 4) Initialize the `species` property with the `species` parameter.
    # 5) Initialize the `catchphrase` property with the `catchphrase` parameter.
    # 6) Initialize the `furniture` property as an empty list.

# 3. Translate each sub-problem into pseudocode:



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    
        # Problem 2: Add Furniture
        # I - Implement
        # 4. Translate the pseudocode into Python and share your final answer:
    
    def add_item(self, item_name):
        self.furniture.append(item_name)




apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)


# Problem 2: Add Furniture
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:

# P - Plan
# 2. Write out in plain English what you want to do:

    # Define add_item function as a part of the Villager class 
    # Append each furniture item in the furniture list 


# 3. Translate each sub-problem into pseudocode:
    # Define add_item function as a part of the Villager class:

    # def add_item(self, item_name):
    # Append each furniture item to the furniture list:

    # self.furniture.append(item_name)


alice = Villager("Alice", "Koala", "guvnor")
# # print(alice.furniture)

alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
# # print(alice.furniture)



# Problem 3: Group by Personality


#U - Understand
# 1. Share 2 questions you would ask to help understand the question:



# P - Plan
# 2. Write out in plain English what you want to do:
    # Create an empty list for the peronality name 
    # Itterate over the each villager in list of townies 
    # if the curent villager personality is the same as personality type:
        # add villager's name in the personality list 
    # return updated list 

# 3. Translate each sub-problem into pseudocode:

    # Create an empty list for the personality names:

    # personality_lst = []
    # Iterate over each villager in the list of townies:

    # For each villager in townies:
    # If the current villager's personality is the same as the personality type:
    # If villager.personality == personality_type:
    # Add the villager's name to the personality list:
    # personality_lst.append(villager.name)
    # Return the updated list:

    # return personality_lst

    # Problem 3: Group by Personality
    # I - Implement
    # 4. Translate the pseudocode into Python and share your final answer:

def of_personality_type(townies, personality_type):
    personality_lst = []
    
    for villager in townies:
        if villager.personality == personality_type:
            personality_lst.append(villager.name)
    
    return personality_lst
        
  

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))


