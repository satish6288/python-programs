request = [
    "a1 b1 c1",
    "x y",
    "",
    "z",
    "p",
    "q r",
    "a2 b2",
    "c2",
    "######",
    "a3",
    "b3 c3",
    "a4 b4 c4"
]

def process_requests(request_list):
    keys = ['repo', 'package', 'version']
    res = []

    # Temporary variable to hold partial entries
    temp_parts = []

    for entry in request_list:
        if not entry or entry == "######":
            continue
        parts = entry.split()
        temp_parts.extend(parts)

        # If we have enough parts to form a complete dictionary
        while len(temp_parts) >= 3:
            sub_dict = {keys[i]: temp_parts[i] for i in range(3)}
            res.append(sub_dict)
            temp_parts = temp_parts[3:]  # Remove processed parts

    return res

response = process_requests(request)
print(response)