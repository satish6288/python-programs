input_string = "prrogrammmt"
#words= input_string.split()
char = {}
for word in input_string:
    if word in char:
        char[word]+=1
    else:
        char[word]=1
duplicates = {word: count for word, count in char.items() if count > 1}
print(duplicates)
# Example usage
