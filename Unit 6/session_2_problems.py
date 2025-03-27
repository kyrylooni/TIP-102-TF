# Standard Problem Set Version 1
# Problem 3: Prioritizing Suspects


#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:

    # Check if the suspect ratings list is empty:

    # If the list is empty, return None because there are no suspects to prioritize.
    # Create two separate linked lists:

    # One for suspects with ratings greater than the threshold.
    # Another for suspects with ratings less than or equal to the threshold.
    # Traverse the suspect ratings linked list:

    # For each suspect:
    # If their rating is greater than the threshold, add them to the "greater" list.
    # If their rating is less than or equal to the threshold, add them to the "less or equal" list.
    # Combine the two lists:

    # Link the end of the "greater" list to the start of the "less or equal" list.
    # Ensure the last node of the combined list points to None:

    # This ensures the linked list is properly terminated.
    # Return the head of the combined list:

    # If the "greater" list is not empty, return its head.
    # Otherwise, return the head of the "less or equal" list.

  

# 3. Translate each sub-problem into pseudocode:

    # Check if the suspect ratings list is empty:

    # If suspect_ratings is None, return None.
    # Create two separate linked lists:

    # Initialize a dummy node for the "greater" list: greater_head = Node(0).
    # Initialize a dummy node for the "less or equal" list: less_or_equal_head = Node(0).
    # Initialize pointers for both lists:

    # greater = greater_head.
    # less_or_equal = less_or_equal_head.
    # Traverse the suspect ratings linked list:

    # Set current = suspect_ratings.
    # While current exists:
    # If current.value > threshold:
    # Add the node to the "greater" list: greater.next = current.
    # Move the greater pointer forward: greater = greater.next.
    # Else:
    # Add the node to the "less or equal" list: less_or_equal.next = current.
    # Move the less_or_equal pointer forward: less_or_equal = less_or_equal.next.
    # Move to the next node: current = current.next.
    # Combine the two lists:

    # Link the end of the "greater" list to the start of the "less or equal" list: greater.next = less_or_equal_head.next.
    # Ensure the last node of the combined list points to None:

    # less_or_equal.next = None.
    # Return the head of the combined list:

    # If greater_head.next exists, return greater_head.next.
    # Otherwise, return less_or_equal_head.next.




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


# Function to partition the linked list
def partition(suspect_ratings, threshold):
    if not suspect_ratings:
        return None
    
    greater_head = Node(0)  
    less_or_equal_head = Node(0)  
    
    greater = greater_head
    less_or_equal = less_or_equal_head
    
    current = suspect_ratings
    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            less_or_equal.next = current
            less_or_equal = less_or_equal.next
        current = current.next
    

    greater.next = less_or_equal_head.next
    less_or_equal.next = None  
    

    if greater_head.next:
        return greater_head.next
    else:
        return less_or_equal_head.next
    
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

# print_linked_list(partition(suspect_ratings, 3))


# Time Complexity: O(N) because each node is visited exactly once.
# Space Complexity: O(1) because the algorithm uses a constant amount of extra space for pointers.

# Problem 4: Puzzling it Out

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:

    # Should the function handle cases where one or both timelines are empty? If so, what should it return in such cases?
    # Are the timelines guaranteed to be sorted, or should the function handle unsorted timelines as well?


# P - Plan
# 2. Write out in plain English what you want to do:

    #  Check if either of the timelines is empty:

    # If one of the timelines is empty, return the other timeline as the merged result.
    # Initialize a temporary head node:

    # This will serve as the starting point for the merged timeline.
    # Use two pointers to traverse both timelines:

    # One pointer (p1) for the known_timeline.
    # Another pointer (p2) for the witness_timeline.
    # Compare the values of the nodes pointed to by p1 and p2:

    # If the value of p1 is less than or equal to the value of p2:
    # Add the node from p1 to the merged timeline.
    # Move the p1 pointer to the next node.
    # Otherwise:
    # Add the node from p2 to the merged timeline.
    # Move the p2 pointer to the next node.
    # Attach any remaining nodes:

    # If one of the timelines still has nodes left after the traversal, attach the remaining nodes to the merged timeline.
    # Return the merged timeline:

    # Return the merged timeline starting from the node after the temporary head.

  

# 3. Translate each sub-problem into pseudocode:
    
    # Check if either of the timelines is empty:

    # If known_timeline is None, return witness_timeline.
    # If witness_timeline is None, return known_timeline.
    # Initialize a temporary head node:

    # Create a dummy node: temp_head = Node(0).
    # Set a pointer current to temp_head.
    # Use two pointers to traverse both timelines:

    # Set p1 to known_timeline.
    # Set p2 to witness_timeline.
    # Compare the values of the nodes pointed to by p1 and p2:

    # While both p1 and p2 exist:
    # If p1.value <= p2.value:
    # Add the node from p1 to the merged timeline: current.next = p1.
    # Move the p1 pointer to the next node: p1 = p1.next.
    # Else:
    # Add the node from p2 to the merged timeline: current.next = p2.
    # Move the p2 pointer to the next node: p2 = p2.next.
    # Move the current pointer to the next node: current = current.next.
    # Attach any remaining nodes:

    # If p1 still has nodes, attach them to the merged timeline: current.next = p1.
    # If p2 still has nodes, attach them to the merged timeline: current.next = p2.
    # Return the merged timeline:

    # Return the merged timeline starting from the node after the temporary head: return temp_head.next`



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


def merge_timelines(known_timeline, witness_timeline):
    temp_head = Node(0)  
    current = temp_head
    

    p1 = known_timeline
    p2 = witness_timeline
    
    while p1 and p2:
        if p1.value <= p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
 
    if p1:
        current.next = p1
    else:
        current.next = p2
    
    return temp_head.next


known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))