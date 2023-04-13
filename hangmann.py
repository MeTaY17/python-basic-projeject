import random
import time
import subprocess

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by IT SOURCECODE\n")
name = input("Enter your name: ")
print(f"Hello {name}! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count, display, word, already_guessed, length, play_game
    words_to_guess = ['Ayakkabı', 'Kültabağı', 'Buzdolabı', 'keser', 'Kazma', 'Yatak', 'Süzgeç', 'Gözlük',
                      'kanepe', 'ansiklopedi', 'Patik', 'Oklava', 'Çekyat', 'dantel', 'koltuk', 'Paspas',
                      'tepsi', 'sebzelik', 'sandık', 'perde', 'mandal']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game.lower() not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        main()
    elif play_game.lower() == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


# Initializing all the conditions required for the game:
def hangman():
    global count, display, word, already_guessed, play_game
    limit = 5
    print(f"This is the Hangman Word: {display}")
    guess = input("Enter your guess: ").strip().lower()
    if len(guess) == 0 or len(guess) >= 2 or not guess.isalpha():
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        if guess not in already_guessed:
            already_guessed.append(guess)
            for index in range(length):
                if word[index] == guess:
                    display = display[:index] + guess + display[index + 1:]
            print(display + "\n")
        else:
            print("You have already guessed that letter. Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",word)
            subprocess.call(['start', 'https://www.youtube.com/watch?v=dU5tRXRKQeY'], shell=True)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()


hangman()