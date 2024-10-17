import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print(number_to_guess)

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break


if __name__ == "__main__":
    number_guessing_game()
