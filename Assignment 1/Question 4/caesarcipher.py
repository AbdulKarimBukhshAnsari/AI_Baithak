"""
1. Write a Python function named encrypt_caesar to encrypt a given string 
using the Caesar cipher with a specified shift value. Provide concise 
examples and test cases to demonstrate the functionality of your 
function.


"""

#For solving this problem we use ord() function which will find the ascii value of any character 
#then this would be easy for us to to shift value

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        # Determine whether it's uppercase or lowercase
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            # Shift lowercase letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)   
    return result

# Example usage
text = "hello"
shift = 3
encrypted_text = encrypt_caesar(text, shift)
print("Encrypted text:", encrypted_text)#     for character in string:
#         character_ascii =  ord(character)


text = "World"
shift = 3
encrypted_text = encrypt_caesar(text, shift)
print("Encrypted text:", encrypted_text)#     for character in string:
#         character_ascii =  ord(character)

"""
2. Implement another Python function named find_second_min_max to 
find the second minimum and maximum elements from an integer 
array. Provide concise examples and test cases to demonstrate the 
correctness and efficiency of your function
"""

def second_min_max(nums):
    # Find the minimum and maximum values
    min_val = min(nums)
    max_val = max(nums)
    
    # Filter out the minimum and maximum values
    filtered_nums = [num for num in nums if num != min_val and num != max_val]
    
    # Find the second minimum and maximum values in the filtered list
    second_min = min(filtered_nums)
    second_max = max(filtered_nums)
    
    return second_min, second_max

# Example usage
nums = [1, 3, 5, 7, 9, 2, 4, 6, 8]
second_min, second_max = second_min_max(nums)
print("Second minimum value:", second_min)
print("Second maximum value:", second_max)



