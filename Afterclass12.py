
# Shopping List Manager using File Handling

# Step 1: Create a shopping list and write it to a file
file = open("shopping_list.txt", "w")

file.write("Milk\n")
file.write("Bread\n")
file.write("Eggs\n")
file.write("Rice\n")

file.close()

print("Shopping list created successfully!")

# Step 2: Read and display the complete file
file = open("shopping_list.txt", "r")

print("\nOriginal Shopping List:")
content = file.read()
print(content)

file.close()

# Step 3: Append new items to the file
file = open("shopping_list.txt", "a")

file.write("Apples\n")
file.write("Sugar\n")

file.close()

print("New items added successfully!")

# Step 4: Read the updated file line by line
file = open("shopping_list.txt", "r")

print("\nUpdated Shopping List:")

for line in file:
    print(line.strip())

file.close()
