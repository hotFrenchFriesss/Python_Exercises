# - Assignment

# Base text/string
text = "   Hello, my name is Fred Axzel Miano!   "

# 1. lower() - Converts all characters in a string to lowercase
lower_text = text.lower()

# 2. upper() - Converts all cahracters in a string to uppercase
upper_text = text.upper()

# 3. strip() - Removes all spaces the from start and end
strip_text = text.strip()

# 4. find() - Searches for the specific word position 
find_text = text.find("Axzel")

# 5. count() - Counts how many times a character appears
count_text = text.count('a')

# Prints all the variable values
print("Original string: ", text)
print("\nLowercased sentence: ", lower_text)
print("\nCapital sentence: ", upper_text)
print("\nWithout spaces: ", strip_text)
print("\nFind word: ", find_text)
print("\nNumber of \"a\": ", count_text)