# Standard Problem Set Version 1
# Problem 8: Exclusive Elements


# U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What is the structure of the input data (e.g., list of strings, list of integers)?
# # - Should the function return a new list or modify the existing lists?



# P - Plan:
# 2. Write out in plain English what you want to do:
# - Initialize an empty list to store the exclusive elements.
# - Traverse through the first list and add elements to the new list that are not in the second list.
# - Traverse through the second list and add elements to the new list that are not in the first list.
# - Return the new list.


# 3. Translate each sub-problem into pseudocode:
# def exclusive_elemts(lst1, lst2):
#     new_lst = []
#     for elem in lst1:
#         if elem not in lst2:
#             new_lst.append(elem)
#     for elem in lst2:
#         if elem not in lst1:
#             new_lst.append(elem)
#     return new_lst

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def exclusive_elemts(lst1, lst2):
    new_lst = []
    for elem in lst1:
        if elem not in lst2:
            new_lst.append(elem)
    for elem in lst2:
        if elem not in lst1:
            new_lst.append(elem)
    return new_lst


# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# print(exclusive_elemts(lst1, lst2))

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# print(exclusive_elemts(lst1, lst2))

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["pooh", "roo", "piglet"]
# print(exclusive_elemts(lst1, lst2))



# Problem 4: Two-Pointer Two Sum

# U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Are the input lists sorted?
# - Should the function return the indices of the two numbers or the numbers themselves?

# P - Plan:
# 2. Write out in plain English what you want to do:
# - Initialize two pointers, one at the beginning and one at the end of the list.
# - While the two pointers do not cross each other:
#   - Calculate the sum of the elements at the two pointers.
#   - If the sum is equal to the target, return the indices of the two elements.
#   - If the sum is less than the target, move the left pointer to the right.
#   - If the sum is greater than the target, move the right pointer to the left.
# - If no such pair is found, return an indication that no solution exists.

# 3. Translate each sub-problem into pseudocode:
# def two_pointer_two_sum(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return (left, right)
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return None

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))
