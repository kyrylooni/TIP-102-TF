# Standard Problem Set Version 1
# Problem 1: Planning Your Daily Work Schedule

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Q: What is the goal of the problem?
    # A: The goal is to determine if there exists a pair of tasks from a given list whose combined time exactly matches a specified available time slot.
    # Q: What should the function return?
    # A: The function should return True if such a pair exists, and False otherwise.


# P - Plan
# 2. Write out in plain English what you want to do:

    # 1) Initialize an empty set called `task_set`.
    # 2) Iterate through each `time` in the `task_times` list.
    #    a) Calculate `complement` as `available_time - time`.
    #    b) If `complement` is in `task_set`, return `True`.
    #    c) Otherwise, add `time` to `task_set`.
    # 3) If no such pair is found after the loop, return `False`.
 


# 3. Translate each sub-problem into pseudocode:

    # Initialize an empty set called `task_set`:
    # task_set = set()
    # Iterate through each `time` in the `task_times` list:
    # For each time in task_times:
    # Calculate `complement` as `available_time - time`:
    # complement = available_time - time
    # If `complement` is in `task_set`, return `True`:
    # If complement in task_set:
    # return True
    # Otherwise, add `time` to `task_set`:
    # task_set.add(time)
    # If no such pair is found after the loop, return `False`:
    # return False




# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_task_pair(task_times, available_time):
    task_set = set()

    for time in task_times:
        complement = available_time - time
        if complement in task_set:
            return True
        task_set.add(time)

    return False


task_times = [30, 45, 60, 90, 120]
available_time = 105
# print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
# print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
# print(find_task_pair(task_times_3, available_time))

# Problem 2: Minimizing Workload Gaps
#U - Understand


# 1. Share 2 questions you would ask to help understand the question:
    # Q: What is the goal of the problem?
    # A: The goal is to find the smallest gap in minutes between any two consecutive work sessions.
    # Q: What are the inputs?
    # A: The input is a list of tuples, where each tuple represents a work session with 
    # a start and end time in 24-hour format (e.g., 1300 for 1:00 PM).



# P - Plan
# 2. Write out in plain English what you want to do:

    # 1) Define a helper function `convert_to_minutes(time)` to convert 24-hour time format to minutes since midnight.
    # 2) Sort the `work_sessions` list by the start time of each session.
    # 3) Initialize a variable `smallest_gap` to infinity.
    # 4) Iterate through the sorted list from the second element:
    #    a) Calculate the end time of the previous session in minutes.
    #    b) Calculate the start time of the current session in minutes.
    #    c) Compute the gap between the two.
    #    d) If this gap is smaller than `smallest_gap`, update `smallest_gap`.
    # 5) Return the `smallest_gap`.

 


# 3. Translate each sub-problem into pseudocode:

    # Define a helper function `convert_to_minutes(time)`:
    # Define convert_to_minutes(time):
    # hours = time // 100
    # minutes = time % 100
    # return hours * 60 + minutes
    # Sort the `work_sessions` list by the start time of each session:
    # work_sessions.sort()
    # Initialize a variable `smallest_gap` to infinity:
    # smallest_gap = float('inf')
    # Iterate through the sorted list from the second element:
    # For i in range(1, len(work_sessions)):
    # Calculate the end time of the previous session in minutes:
    # end_time_prev = convert_to_minutes(work_sessions[i-1][1])
    # Calculate the start time of the current session in minutes:
    # start_time_curr = convert_to_minutes(work_sessions[i][0])
    # Compute the gap between the two:
    # gap = start_time_curr - end_time_prev
    # If this gap is smaller than `smallest_gap`, update `smallest_gap`:
    # If gap < smallest_gap:
    # smallest_gap = gap
    # Return the `smallest_gap`:
    # return smallest_gap



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def convert_to_minutes(time):
    hours = time // 100
    minutes = time % 100
    return hours * 60 + minutes

def find_smallest_gap(work_sessions):
    # Sort the work sessions based on start times
    work_sessions.sort()

    smallest_gap = float('inf')

    for i in range(1, len(work_sessions)):
        # Calculate the end time of the previous session and the start time of the current session
        end_time_prev = convert_to_minutes(work_sessions[i-1][1])
        start_time_curr = convert_to_minutes(work_sessions[i][0])

        # Calculate the gap between the end of the previous session and the start of the current session
        gap = start_time_curr - end_time_prev

        # Update the smallest gap found
        if gap < smallest_gap:
            smallest_gap = gap

    return smallest_gap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
# print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
# print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
# print(find_smallest_gap(work_sessions_3))