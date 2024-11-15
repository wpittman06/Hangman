import random

words = ["biscotti", "shortbread", "thin mints", "snickerdoodle", "chocolate chip", "white chocolate macadamian"]

# Randomly choose a word from the list
chosenWord = random.choice(words)
displayWord = ['_' for _ in chosenWord] # creates a list of underscores
attempts = 10 # number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in displayWord:
    #Taking empty string concatenating it with displayWord to show chars in word
    print("\n" + ''.join(displayWord)) 
    guess = input("Guess a letter: ").lower()
    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            if letter == guess:
                displayWord[index] = guess #reveals letter
    else:
        print("That letter isn't in the word")
        attempts -= 1

#Game conclusion
if '_' not in displayWord:
        print("You guessed the word!")
        print(' '.join(displayWord))
        print("You won!!!!")
else:
     print("You ran out of attempts. The word was: " + chosenWord)
     print("You lost!!!")

# Would like to add a restart button to start the game at conclusion
# Would like to add an end game button to stop the game at conclusion
# Would like to add a guess the word functionality if you think you know the answer