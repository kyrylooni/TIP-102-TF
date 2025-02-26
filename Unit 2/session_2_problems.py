# Standard Problem Set Version 2
# Problem 1: Most Endangered Species

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:

    # What should be done if the species_list is empty?
    # How should the function handle cases where multiple species have the same minimum population? 
    # Should it return the first one it encounters or all of them?


# P - Plan
# 2. Write out in plain English what you want to do:
    # Check if the species_list is empty:

    # If it is empty, return None or an appropriate message indicating that there are no species to evaluate.
    # Initialize a variable to store the most endangered species:

    # Set it to the first species in the list.
    # Iterate through the species_list starting from the second species:

    # For each species, compare its population with the population of the current most endangered species.
    # If the current species has a smaller population, update the most endangered species to the current species.
    # Return the name of the most endangered species:

    # Return the name of the species with the smallest population.

# 3. Translate each sub-problem into pseudocode:
    # Check if the species_list is empty:

    # If it is empty, return None or an appropriate message indicating that there are no species to evaluate.
    # Initialize a variable to store the most endangered species:

    # most_endangered_species = species_list[0]
    # Iterate through the species_list starting from the second species:

    # For each species in species_list[1:]:
    # If species["population"] is less than most_endangered_species["population"]:
    # Update most_endangered_species to the current species
    # Return the name of the most endangered species:

    # return most_endangered_species["name"]

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def most_endangered(species_list):
    most_endangered_species = species_list[0]
    
    for species in species_list[1:]:
        if species["population"] < most_endangered_species["population"]:
            most_endangered_species = species
    return most_endangered_species["name"]


# Problem 2: Identifying Endangered Species
#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:

    

# 3. Translate each sub-problem into pseudocode:
    

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What should be done if the observed_species list is empty?
    # How should the function handle cases where a species appears multiple times in the observed_species list? 
    # Should it count each occurrence or only unique species?


# P - Plan
# 2. Write out in plain English what you want to do:
    # Check if the observed_species list is empty:

    # If it is empty, return 0 as there are no species to count.
    # Convert the endangered_species list to a set:

    # This will allow for faster lookup times when checking if a species is endangered.
    # Initialize a variable to store the count of endangered species:

    # count = 0
    # Iterate through the observed_species list:

    # For each species in observed_species:
    # If the species is in the endangered_set, increment the count.
    # Return the count of endangered species:

    # return count
    

# 3. Translate each sub-problem into pseudocode:
    # Check if the observed_species list is empty:

    # If it is empty, return 0 as there are no species to count.
    # Convert the endangered_species list to a set:

    # endangered_set = set(endangered_species)
    # Initialize a variable to store the count of endangered species:

    # count = 0
    # Iterate through the observed_species list:

    # For each species in observed_species:
    # If the species is in the endangered_set, increment the count: count += 1
    # Return the count of endangered species:

    # return count
    

# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    

    count = 0
    for species in observed_species:
        if species in endangered_set:
            count += 1
            
    return count