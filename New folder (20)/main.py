import random

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum([d ** power for d in digits]) == num

def play_game():
    print("Welcome to the Armstrong Number Guessing Game!")
    print("Can you guess if the number is an Armstrong number?")
    print("Type 'yes' or 'no'! \n")

    for _ in range(5):  # 5 rounds
        number = random.randint(100, 999)  # 3-digit number
        print(f"Is {number} an Armstrong number?")
        answer = input("Your guess ('yes' or 'no'): ").strip().lower()

        correct = is_armstrong(number)
        if (answer == 'yes' and correct) or (answer == 'no' and not correct):
            print("Correct! \n")
        else:
            print(f"Wrong! The correct answer is {'yes' if correct else 'no'}. \n")

    print("Game over! Great job!")

play_game()