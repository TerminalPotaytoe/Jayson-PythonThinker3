# # Define a dictionary for the points associated with each letter
# letter_points = {
#     'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
#     'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 
#     'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 
#     'Y': 4, 'Z': 10
# }

# # Function to calculate the score of a word
# def calculate_word_score(word):
#     #create score variable
#     score = 0
#     #Change word to uppercase to match with the letter in the list
#     word = word.upper()
    
#     # Loop through each letter in the word and add the letter's score into score
#     for letter in word:
#         if letter in letter_points:
#             score += letter_points[letter]
    
#     return score

# #Asks for the word 5 times
# for i in range(1, 6):
#     word = input(f"Word #{i}: ")  # Asks for Word
#     score = calculate_word_score(word)  # Calculate score for the word
#     print(f"Score #{i}: {score}")  # Print out the Score






##################################################################################################
# # 
# def merge(nomber, word):
#     print("Your password is ", end = "")
#     print(word + str(nomber))

# # merge(7, "lucky")


# my_list = [5,8,10,9,11,12,15,2]
# n = len(my_list)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
# print(my_list)

