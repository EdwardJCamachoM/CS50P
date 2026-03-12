import random

def main():
    while True:
        try:
            level = int(input("Enter the limit number to guess: "))
            if level < 1:
                raise ValueError
            break
        except ValueError:
            print(f"Enter a valid number")

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input(f"Enter a number from 1 to {level}: "))
            if guess < 1 or guess > level:
                raise ValueError
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print(f"Enter a valid number from 1 to {level}")

if __name__ == "__main__": main()