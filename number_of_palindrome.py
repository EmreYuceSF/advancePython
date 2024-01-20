# Emre Yuce - CS231
# task1 - print out the number of palindrome words form the file
# task2 - Use comprehension method instead of functional programming   


from functools import reduce

file_path = "/users/abrick/resources/english"

available = False

try:
    with open(file_path ,"r") as file:
        words = file.readlines()
        available = True
except FileNotFoundError:
    print(f"The '{file_path.split('/')[-1]}' is not found in '{file_path[:len(file_path)-len(file_path.split('/')[-1])]}' directory")
    
if available:
    total_palindrome = len(list(filter(lambda text: text.strip()[-1::-1] == text.strip(), words))) # this works too, I believe both has same time complexity 
    print("there are", total := reduce(lambda a, b: a+1 if b.strip()[-1::-1]==b.strip() else a, words, 0), f"palindrome in the '{file_path.split('/')[-1]}' file")
    


""" OUTPUT
[eyuce@hills CS231]$ python3 number_of_palindrome.py 
there are 111 palindrome in the 'english' file
"""


