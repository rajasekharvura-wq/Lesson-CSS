# ---- FILE HANDLING - My Bucket List ------------------------------
# Topics: open() | file modes r/w/a | read() | readlines() | write() | close()


# -- Part 1: Write your bucket list to a file -------------------------
# 'w' mode creates the file if it does not exist.
# If the file already exists, 'w' wipes the old content and starts fresh.
file = open("bucket-list.txt", "w")
file.write("1. Visit the Eiffel Tower\n")
file.write("2. Learn to play the guitar\n")
file.write("3. Code my own game\n")
file.close()  # Always close the file when done writing
print("Bucket list saved to bucket-list.txt")


# -- Part 2: Read your bucket list from the file -----------------------
# 'r' mode opens the file for reading.
file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()



# --- Part 3: Count the items ---------------------------
# readlines() returns a list - one item per line.
# len() counts the number of lines (items) in the file.
file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items in your bucket list.")
file.close()


# --- Part 4: Add more items - append mode ---------------------
# 'a' mode opens the file and moves to the END.
# write() now adds new content AFTER the existing content - nothing is deleted.
file = open("bucket-list.txt", "a")
file.write("4. Travel to Japan\n")
file.write("5. Run a 5k\n")
file.close()
print("\n2 more items added!")


# --- Part 5: Read the updated file -----------------------
# Open in 'r' mode again to confirm the new items are saved.
file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()