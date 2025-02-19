# # Template Questions

# 1. Share 2 questions you would ask to help understand the question:
#   
  
# 2. Write out in plain English what you want to do: 
#   

# 3. Translate each sub-problem into pseudocode:
#   

# 4. Translate each sub-problem into pseudocode:
#   

# 5. Translate the pseudocode into Python and share your final answer:


# Standard Problem Set Version 1
# Problem 5: Total Honey

# U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What is the structure of the input data?
# - Should the function return the total amount of honey or print it?

# P - Plan
# 2. Write out in plain English what you want to do:
# - Initialize a variable to keep track of the total honey.
# - Traverse through the list of jars.
# - For each jar, add the amount of honey to the total.
# - Return the total amount of honey.

# 3. Translate each sub-problem into pseudocode:
# def total_honey(jars):
#     total = 0
#     for jar in jars:
#         total += jar
#     return total

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def total_honey(jars):
    total = 0
    for jar in jars:
        total += jar
    return total

# Example usage:
jars = [2, 3, 5, 1, 4]
print(total_honey(jars))  # Output: 15

# Advanced Problem Set Version 1
# Problem 1: Hunny Hunt

# U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What is the structure of the input data (e.g., list, string, integer)?
    # What should be the output of the function (e.g., a specific data type, printed result, returned value)?

# P - Plan
# 2. Write out in plain English what you want to do:
    # Traverse the range of list 
    # if the value of a current element of the list is the same as a target
        # return index 
    # otherwise return -1 
# 3. Translate each sub-problem into pseudocode:

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# def linear_search(lst, target):
# for elem in range(lst):
    # if the lst[curr_idx] == target:
        # return idx
    # return -1 

def linear_search(lst, target):
	for i in range(len(lst)):
		if (lst[i] == target):
			return i 
	return -1 


items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))




# Advanced Problem Set Version 2
# Problem 1: Words Containing Character

# U - Understand
# 1. Share 2 questions you would ask to help understand the question:

# Should the program capure only uppercase or lower case character of the same letter, or both?
# What should be the output of the function (e.g., a specific data type, printed result, returned value)?


# P - Plan
# 2. Write out in plain English what you want to do:

    # create a new list for idecies 
    # Traverse through the list of words. 
    # If the character is a part of the word return the index of the word in the list 
    # append the value of new indicies and return a list 

# 3. Translate each sub-problem into pseudocode:
    # def words_with_char(words, x):
        #idx_lst = [] 
        # for w in wds:
            # if char in w:
                # idx_lst.append(wds[w])
            # return idx_lst

                

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def words_with_char(words, x):
	idx_lst = []
	i = 0 
	for word in words:
		if x in word:
			idx_lst.append(i)
		i += 1 
	return idx_lst


# words = ["batman", "superman"]
# x = "a"
# print(words_with_char(words, x))


# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# print(words_with_char(words, x))

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# print(words_with_char(words, x))





