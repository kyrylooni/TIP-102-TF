# Standard Problem Set Version 1
# Problem 1: Festival Lineup

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What if the lists are empty?
    # What should be done if the lengths of the artists and set_times lists are not equal?



# P - Plan
# 2. Write out in plain English what you want to do:
    # Create an empty disctionary 
    # Iterate over the length of a range of artists list:
        # Assign every artist in the list of arstist as a dictionary key
        # Assign every time in the list of times as a dictionary value 
    # return the final dictionary 

# 3. Translate each sub-problem into pseudocode:
    # def lineup(artists, set_times):
        # artists_and_times = {} 
        # for in in range(len(artists))
            # artists_and_times[arttist[i]] = times[i]
        # return final dictionary 


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def lineup(artists, set_times):
    artists_and_times = {} 

    for i in range(len(artists)):
        artists_and_times[artists[i]] = set_times[i]
    return artists_and_times


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))


#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should be done if the audiences list is empty?
# How should the function handle multiple performances with the same maximum audience size? 
# Should it sum all of them or just return the size of one performance?

# P - Plan
# 2. Write out in plain English what you want to do:
# Check if the audiences list is empty:

# If it is empty, return 0 as there are no performances.
# Create an empty dictionary to store the audience sizes and their corresponding counts.

# Iterate through the audiences list:

# For each audience size, check if it is already a key in the dictionary.
# If it is, increment the count for that audience size.
# If it is not, add it to the dictionary with a count of 1.
# Find the maximum audience size by iterating through the dictionary.

# Calculate the combined audience size for the maximum audience size:

# Multiply the maximum audience size by its count from the dictionary.
# Return the combined audience size.


# 3. Translate each sub-problem into pseudocode:
    # Check if the audiences list is empty:

    # If it is empty, return 0 as there are no performances.
    # Create an empty dictionary to store the audience sizes and their corresponding counts:

    # audience_dict = {}
    # Iterate through the audiences list:

    # For each audience in audiences:
    # If audience is already a key in audience_dict:
    # Increment the count for that audience size: audience_dict[audience] += 1
    # Else:
    # Add it to the dictionary with a count of 1: audience_dict[audience] = 1
    # Find the maximum audience size:

    # max_audience = max(audiences)
    # Calculate the combined audience size for the maximum audience size:

    # combined_audience_size = audience_dict[max_audience] * max_audience
    # Return the combined audience size:

    # return combined_audience_size

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def max_audience_performances(audiences):
    if not audiences:
        return 0 

    audience_dict = {}
    for audience in audiences:
        audience_dict[audience] = audience_dict.get(audience, 0) + 1 

    max_audience = max(audiences)
    return audience_dict[max_audience] * max_audience

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))


# Advanced Problem Set Version 1
# Problem 1: Counting Treasure

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What should be done if the treasure_map dictionary is empty?
    # How should the function handle negative values in the treasure_map dictionary? Should they be included in the total or ignored?

# P - Plan
# 2. Write out in plain English what you want to do:
    # Check if the treasure_map dictionary is empty:

    # If it is empty, return 0 as there are no treasures to count.
    # Initialize a variable to store the total treasure count:

    # total = 0
    # Iterate through the treasure_map dictionary:

    # For each location in treasure_map:
    # Add the treasure count at that location to the total.
    # Return the total treasure count:

    # return total

# 3. Translate each sub-problem into pseudocode:
    # Check if the treasure_map dictionary is empty:

    # If it is empty, return 0 as there are no treasures to count.
    # Initialize a variable to store the total treasure count:

    # total = 0
    # Iterate through the treasure_map dictionary:

    # For each location in treasure_map:
    # Add the treasure count at that location to the total: total += treasure_map[location]
    # Return the total treasure count:

# return total

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def total_treasures(treasure_map):
    total = 0
    for location in treasure_map:
        total += treasure_map[location]
    return total


treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 
