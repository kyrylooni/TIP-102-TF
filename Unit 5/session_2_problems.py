# Standard Problem Set Version 1
# Problem 2: Linked Up

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What is a linked list?
    # How do we create a linked list?


# P - Plan
# 2. Write out in plain English what you want to do:
    # Link the nodes by referencing each node's value starting with the head node 
    # print it by callimng print_linked
  

# 3. Translate each sub-problem into pseudocode:

    # Link the nodes by referencing each node's value starting with the head node:

    # Create the nodes with their values:
    # kk_slider = Node("K.K. Slider")
    # harriet = Node("Harriet")
    # saharah = Node("Saharah")
    # isabelle = Node("Isabelle")
    # Link the nodes together:
    # kk_slider.next = harriet
    # harriet.next = saharah
    # saharah.next = isabelle
    # Print the linked list by calling print_linked_list:

    # print_linked_list(kk_slider)



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider = Node(kk_slider.value, Node(harriet.value, Node(saharah.value, Node(isabelle.value))))
# print_linked_list(kk_slider)


# Problem 3: Daily Tasks
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   What happens if the task list is empty?
#     If the task list is empty, the new task will be the only node in the list.


# P - Plan
# 2. Write out in plain English what you want to do:
    # initialize the start node to be the task node 
    # assign next node to be the head node 
    # return the start node (which is the task node in this case)
  

# 3. Translate each sub-problem into pseudocode:

    # Initialize the start node to be the task node:

    # start_node = Node(task)
    # Assign the next node to be the head node:

    # start_node.next = head
    # Return the start node (which is the task node in this case):

    # return start_node



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def add_first(head, task):
    start_node = Node(task) 
    start_node.next = head
    return start_node

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))



# Problem 4: Halve List
# 1. Share 2 questions you would ask to help understand the question:
    # 1) Start at the head of the linked list.
    # 2) While the current node is not None, do the following:
    #     a) Divide the value of the current node by two.
    #     b) Move to the next node in the list.
    # 3) Return the head of the modified linked list.


# P - Plan
# 2. Write out in plain English what you want to do:
    # initialize current pointer to be head 
    # while current pointer exists
        # take each node's value and divide by 2 
        # move the pointer to the next node 
    # return the head 

  

# 3. Translate each sub-problem into pseudocode:
    # Initialize current pointer to be head:

    # current = head
    # While current pointer exists:

    # while current:
    # Take each node's value and divide by 2:
    # current.value = current.value / 2
    # Move the pointer to the next node:
    # current = current.next
    # Return the head:

    # return head




# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def halve_list(head):
    current = head
    while current:
        current.value = current.value / 2 
        current = current.next 
    return head



node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))