def find_combination_indices(s, target):
    # Use a dictionary to store the complement values and their indices
    complements = {}
    for i, num in enumerate(s):
        complement = target - num
        if complement in complements:
            # Return the indices of the numbers that add up to the target
            return [complements[complement],s[i]]
        complements[num] = i
    return "No combination found"

s = [2, 7, 14, 15]
target = 9
result = find_combination_indices(s, target)
print(result)


