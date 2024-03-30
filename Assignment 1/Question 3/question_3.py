"""

1. Write a Python function named analyze_file that takes the name of a file as 
input and returns a dictionary containing the counts of characters, words, and 
lines in that file
test case:
file name : analyze
word counts = 54
character counts = 326

"""
print("Question:1 \n")
def analyze_file(input_file):
    with open (f'Assignment 1\Question 3\{input_file}.txt',"r") as f: #opening the file in read mode
        characters = f.read()  # reading the file it will make all the content of file in string
        words = characters.split() #split function will make the list of all words
        count_characters = len(characters) #counting len will give all the charcters
        count_words = len(words) #It will give the total words


    print(f"\nThe total character presents in {inp_file} are {count_characters}\n")
    print(f"The total words presents in {inp_file} are {count_words}")  


inp_file = input("Enter the name of the file: ")  # taking input the name of the file 

analyze_file(inp_file)



"""

2. Write another Python function named search_word that takes the name of a 
file and a word as input and returns the count of occurrences of that word in 
the file.

Test case:
parameter : file name , word
file name = analyze
word : hand
Expected output: 2
Actual Output :2

"""
print("\nQuestion#2\n")
def search_word(inp_file_2,word):
   
   with open (f'Assignment 1\Question 3\{inp_file_2}.txt',"r") as f: #opening the file in read mode
        file_content = f.read()
        count_of_words = file_content.count(word) #count the word which you gave input
        print(f"The total count of {word} is found to be {count_of_words}") 

inp_file_name = input("Enter file name: ")
word = input("Enter the word which you want to count: ")

search_word(inp_file_name,word)  #calling the function
