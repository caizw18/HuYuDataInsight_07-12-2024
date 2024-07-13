def twoSum(nums, target):
    # Create a dictionary to store the value and its index
    num_map = {}

    # Iterate over the list
    for index, num in enumerate(nums):
        # Calculate the difference needed to reach the target
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_map:
            # If found, return the indices of the current number and the complement
            return [num_map[complement], index]

        # Store the number and its index in the dictionary
        num_map[num] = index

    # Return an empty list if no solution is found (this shouldn't happen as per the problem description)
    return []


# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))