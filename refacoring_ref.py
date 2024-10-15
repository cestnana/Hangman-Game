import random
import hangman_words
import hangman_art

# Initialize the game state
lives = 6
print(hangman_art.logo)

# Choose a random word from the word list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
# Uncomment this line for testing: print(f"Chosen word: {chosen_word}")

# Initialize placeholders and correct guesses tracking
display = ["_"] * word_length  # Using a list for easier updates
correct_guesses = set()

game_over = False

while not game_over:
  print(f"\n************************ {lives}/6 LIVES LEFT ************************")
  print("Word to guess: " + " ".join(display))  # Display word neatly

  guess = input("Guess a letter: ").lower()

  # Check if the letter has already been guessed
  if guess in correct_guesses or guess in display:
    print(f"You've already guessed '{guess}'. Try a different letter.")
    continue

  # Add the guess to the set of correct guesses
  correct_guesses.add(guess)

  # Check if the guess is in the chosen word
  if guess in chosen_word:
    print(f"Good guess! '{guess}' is in the word.")
    # Update the display with the correct guess
    for index, letter in enumerate(chosen_word):
      if letter == guess:
        display[index] = letter
  else:
    # Incorrect guess, reduce lives
    lives -= 1
    print(f"'{guess}' is not in the word. You lose a life.")

  # Check if the player has won or lost
  if "_" not in display:
    game_over = True
    print("**************************** YOU WIN ****************************")
  elif lives == 0:
    game_over = True
    print(f"****************** GAME OVER! The word was '{chosen_word}' ******************")

  # Display the current hangman stage
  print(hangman_art.stages[lives])