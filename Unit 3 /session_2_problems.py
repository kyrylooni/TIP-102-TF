# Import the deque module
from collections import deque 

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Should the queue follow a max-priority structure (where higher priority values indicate higher precedence),
    #  or is a lower numerical value considered a higher priority?

    # If two requests have the same priority, should they be processed in 
    # the order they arrived (FIFO order within the same priority level)?

# P - Plan
# 2. Write out in plain English what you want to do:

	# 1. Store the performance requests in a queue  that higher-priority requests are processed first.
	# 2. Sort the requests by priority in descending order to ensure that performances with higher priority values come first.
	# 3. If two requests have the same priority, maintain their original order of arrival (FIFO order within the same priority level).
	# 4. Extract the performance names from the sorted requests and return them in the correct order.
	# 5. Return the final list of performances in order of processing.

# 3. Translate each sub-problem into pseudocode:

    # FUNCTION process_performance_requests(requests):
    #     SORT requests BY priority IN DESCENDING ORDER, MAINTAIN original order for ties
    #     performance_order = []
    #     FOR each (priority, name) IN requests:
    #         APPEND name TO performance_order
    #     RETURN performance_order


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def process_performance_requests(requests):

    queue = deque(sorted(requests, reverse=True))
    
    performance_results = []
    while queue:
        priority, performance = queue.popleft()
        performance_results.append(performance)
    

    return performance_results


# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))



# Problem 3: Collecting Points at Festival Booths
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Should the points be collected in the order they appear in the list (LIFO stack behavior), 
    # or should they simply be summed up?

    # Are there any conditions where points are removed from the stack, or is it just a summation process?

# P - Plan
# 2. Write out in plain English what you want to do:

	# 1. Initialize an empty stack to store collected points.
	# 2. Iterate through the list of booth points and push each point onto the stack.
	# 3. Sum up all the points in the stack to get the total points collected.
	# 4. Return the total points as the final result.

# 3. Translate each sub-problem into pseudocode:

# FUNCTION collect_festival_points(points):
#     CREATE empty stack
    
#     FOR each point IN points:
#         PUSH point TO stack
    
#     total_points = SUM of all values IN stack
    
#     RETURN total_points


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def collect_festival_points(points):
    stack = []
    total_points = 0 

    for point in points:
        stack.append(point)

        total_points += stack.pop()
    return total_points

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 
