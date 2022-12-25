# Constants for the number of categories
CATEGORY_1 = 0
CATEGORY_2 = 1
CATEGORY_3 = 2

# Constants for the number of new members per category
CATEGORY_1_LOWER_BOUND = 0
CATEGORY_1_UPPER_BOUND = 5
CATEGORY_2_LOWER_BOUND = 6
CATEGORY_2_UPPER_BOUND = 10
CATEGORY_3_LOWER_BOUND = 11
CATEGORY_3_UPPER_BOUND = 15

# Array to store the names and number of new enrollees
trainers = []

# Prompt the user to enter the number of trainers
num_trainers = int(input("Enter the number of trainers: "))

# Loop through the number of trainers and get their names and number of new enrollees
for i in range(num_trainers):
    name = input("Enter the name of trainer {}: ".format(i+1))
    enrollees = int(input("Enter the number of new enrollees for trainer {}: ".format(i+1)))

    # Add the name and enrollees to the trainers array
    trainers.append((name, enrollees))

# Initialize the counters for each category
num_category_1 = 0
num_category_2 = 0
num_category_3 = 0

# Loop through the trainers and count how many are in each category
for trainer in trainers:
    name, enrollees = trainer
    if enrollees >= CATEGORY_1_LOWER_BOUND and enrollees <= CATEGORY_1_UPPER_BOUND:
        num_category_1 += 1
    elif enrollees >= CATEGORY_2_LOWER_BOUND and enrollees <= CATEGORY_2_UPPER_BOUND:
        num_category_2 += 1
    elif enrollees >= CATEGORY_3_LOWER_BOUND and enrollees <= CATEGORY_3_UPPER_BOUND:
        num_category_3 += 1

# Display the results
print("Number of trainers in category 1 (0-5 new members): {}".format(num_category_1))
print("Number of trainers in category 2 (6-10 new members): {}".format(num_category_2))
print("Number of trainers in category 3 (11-15 new members): {}".format(num_category_3))
