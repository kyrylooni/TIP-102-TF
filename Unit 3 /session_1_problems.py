# Standard Problem Set Version 1
# Problem 1: Post Format Validator

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should be done if the input string is empty or contains no parentheses?
# How should the function handle cases where there are unmatched opening or closing parentheses? Should it return False immediately or continue checking the rest of the string?


# P - Plan
# 2. Write out in plain English what you want to do:
    # Initialize a stack to keep track of the opening tags as you encounter them.
    # Iterate through the posts
        # If it's an opening tag, push it onto the stack
        # If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag
            # If yes, pop the opening tag from the stack (we've found its match!)
            # If no, the tags are not properly nested and we should return False
    # After processing all characters, if the stack is empty, all tags were properly nested and we should return True. If the stack is not empty, some opening tags were not closed, so return False

# 3. Translate each sub-problem into pseudocode:
    # Initialize a stack to keep track of the opening tags as you encounter them:

    # stack = []
    # Define a dictionary to map closing tags to their corresponding opening tags:

    # [matching_tags = {')': '(', ']': 'matching_tags = {')': '(', ']': '[', '}': '{'}
    # Iterate through the posts:

    # For each char in post:
    # If it's an opening tag, push it onto the stack:
    # if char in '([{':
    # stack.append(char)
    # If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag:
    # elif char in ')]}':
    # if not stack or stack.pop() != matching_tags[char]:
    # return False
    # After processing all characters, if the stack is empty, all tags were properly nested and we should return True. If the stack is not empty, some opening tags were not closed, so return False:

    # return len(stack) == 0


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_valid_post_format(post):
  stack = []
  matching_tags = {')': '(', ']': '[', '}': '{'}

  for char in post:
    if char in '([{':
      stack.append(char)
    elif char in ')]}':
      if not stack or stack.pop() != matching_tags[char]:
        return False

  return len(stack) == 0
        
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))




# Problem 2: Reverse User Comments Queue
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:



# P - Plan
# 2. Write out in plain English what you want to do:
    # 1. Initialize an empty stack to temporarily store the comments.
    # 2. Iterate through each comment in the input list:
        #    1. Push each comment onto the stack.
    # 3. Initialize an empty list to hold the reversed comments.
        # 4. Pop elements from the stack one by one, appending each to the reversed comments list.
    # 5. Once the stack is empty, return the reversed comments list.



# 3. Translate each sub-problem into pseudocode:
    # Initialize an empty stack to temporarily store the comments:

    # stack = []
    # Iterate through each comment in the input list:

    # For each comment in comments:
    # Push each comment onto the stack:
    # stack.append(comment)
    # Initialize an empty list to hold the reversed comments:

    # reversed_comments_lst = []
    # Pop elements from the stack one by one, appending each to the reversed comments list:

    # While stack is not empty:
    # reversed_comments_lst.append(stack.pop())
    # Once the stack is empty, return the reversed comments list:

    # return reversed_comments_lst



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_comments_queue(comments):
    stack = []
    reversed_comments_lst = []

    for c in comments:
      stack.append(c)

    while stack:
      reversed_comments_lst.append(stack.pop())
    
    return reversed_comments_lst

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

    
    




# Problem 3: Check Symmetry in Post Titles
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:

    # What should be done if the input title is empty or contains no alphanumeric characters?
    # How should the function handle cases where the title contains mixed case letters? Should it consider 'A' and 'a' as matching characters?


# P - Plan
# 2. Write out in plain English what you want to do:

    # 1. Initialize two pointers, `left` at the start of the title and `right` at the end.
    # 2. While `left` is less than `right`:
    #    1. Move `left` pointer to the right if the current character is not alphanumeric.
    #    2. Move `right` pointer to the left if the current character is not alphanumeric.
    #    3. Compare the characters at `left` and `right` (convert both to lowercase):
    #       1. If they don't match, return `False`.
    #       2. If they do match, move both pointers towards the center.
    # 3. If all characters match, return `True`.


# 3. Translate each sub-problem into pseudocode:

    # Initialize two pointers, left at the start of the title and right at the end:

    # left = 0
    # right = len(title) - 1
    # While left is less than right:

    # Move left pointer to the right if the current character is not alphanumeric:
    # while left < right and not title[left].isalnum():
    # left += 1
    # Move right pointer to the left if the current character is not alphanumeric:
    # while left < right and not title[right].isalnum():
    # right -= 1
    # Compare the characters at left and right (convert both to lowercase):
    # if title[left].lower() != title[right].lower():
    # return False
    # If they match, move both pointers towards the center:
    # left += 1
    # right -= 1
    # If all characters match, return True:

    # return True



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_symmetrical_title(title):
    left_p = 0
    right_p = len(title) - 1

    while left_p < right_p:
        while left_p < right_p and not title[left_p].isalnum():
            left_p += 1
    
        while left_p < right_p and not title[right_p].isalnum():
            right_p -= 1 
    
        if title[left_p].lower() != title[right_p].lower():
            return False
        left_p =+ 1 
        right_p =+ 1 
    
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 






# I - Implement
# 4. Translate the pseudocode into Python and share your final answer: