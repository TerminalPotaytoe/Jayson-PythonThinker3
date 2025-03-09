# Define a dictionary for the points associated with each letter
letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 
    'Y': 4, 'Z': 10
}

# Function to calculate the score of a word
def calculate_word_score(word):
    # Initialize the score to 0
    score = 0
    # Convert the word to uppercase to match the dictionary keys
    word = word.upper()
    
    # Loop through each letter in the word and add its corresponding score to the total
    for letter in word:
        if letter in letter_points:
            score += letter_points[letter]
    
    return score

# Ask for 5 words
for i in range(1, 6):
    word = input(f"Word #{i}: ")  # Input word
    score = calculate_word_score(word)  # Calculate score for the word
    print(f"Score #{i}: {score}")  # Output the score
