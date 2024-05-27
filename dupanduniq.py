def find_duplicate_chars(geeksforgeeks):
    # Create empty sets to store unique and duplicate characters
    #unique_chars ={}
    duplicate_chars = {}
 
    # Iterate through each character in the string
    for char in geeksforgeeks:
        # If the character is already in unique_chars, it is a duplicate
        if char in duplicate_chars:
            duplicate_chars[char]+=1
        # Otherwise, add it to unique_chars
        else:
            duplicate_chars[char]+=1
    duplicate_chars = {char:count for char,count in duplicate_chars.items if count > 1}
    return duplicates
 
# Example usage:
print(find_duplicate_chars("geeksforgeeks")) # Output: ['e', 'g', 'k', 's']


