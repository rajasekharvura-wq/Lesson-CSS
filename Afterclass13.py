# Open the notes file
file = open("notes_txt", "r")

# Read the first 10 characters
preview = file.read(10)
print(preview)

# Go back to the beginning
file.seek(0)

# Read all lines
lines = file.readlines()

# Close the file
file.close()

# Create a new organized file
new_file = open("Afterclass13.py", "w")

# Check each line
for line in lines:

    # Keep IMPORTANT and TODO lines
    if line.startswith("IMPORTANT:") or line.startswith("TODO:"):
        new_file.write(line)

# Close the new file
new_file.close()

print("Notes organized successfully!")