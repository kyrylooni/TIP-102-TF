# Advanced Problem Set Version 1
# Problem 1: Brand Filter


#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:
 
# create a filterted criterion list 
# iterate over the brands name list 
# for each brand name check whether current criterion matches an inputted criterion:
#   if it matches append the brand name to the list 
# return the final list  
#


# 3. Translate each sub-problem into pseudocode:

    # Create a filtered criterion list:

    # filtered_brands = []
    # Iterate over the brands name list:

    # For each brand in brands:
    # Check whether the current criterion matches an inputted criterion:
    # If criterion in brand["criteria"]:
    # Append the brand["name"] to filtered_brands


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def filter_sustainable_brands(brands, criterion):
    filtered_brands = [] 

    if not brands:
        return None 

    for brand in brands:
        if criterion in brand["criteria"]:
            filtered_brands.append(brand["name"])
    return filtered_brands

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]


brands_4 = []

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))
# print(filter_sustainable_brands(brands_4, "carbon-neutral"))

# Time complexity: O(N)
# Space complexity: O(N)

# Problem 2: Eco-Friendly Materials


#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:
 
# Initialize dictionary for counting materials 
# Itterate over brands:
#  Itterate over each brands' material: 
#   If brand matterial is seen first time initialize the counter of that material to 1 and add it to the dict as a key/value pair 
#       Else if the material is already known add 1 to the counter 
# return the counter dictionary  




# 3. Translate each sub-problem into pseudocode:

    # Initialize a dictionary for counting materials:

    # materials_dict = {}
    # Iterate over brands:

    # For each brand in brands:
    # Iterate over each brand's material:
    # For each material in brand["materials"]:
    # If the material is seen for the first time, initialize the counter of that material to 1 and add it to the dictionary as a key/value pair:
    # If material not in materials_dict:
    # materials_dict[material] = 1
    # Else if the material is already known, add 1 to the counter:
    # Else:
    # materials_dict[material] += 1
    # Return the counter dictionary:

    # return materials_dict


# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_material_usage(brands):
    materials_dict = {}

    for brand in brands:
        for material in brand["materials"]:
            materials_dict[material] = materials_dict.get(material, 0) + 1 
    return materials_dict



brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))



