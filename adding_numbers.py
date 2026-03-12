import random

def main():
    level = select_level()
    score = 0
    for _ in range(10):
        x, y = generate_numbers(level)
        if check_answer(x, y):
            score += 1
    print(f"Your score is: {score}")

def select_level():
    while True:
        try:
            level = int(input("Select a difficulty level from 1 to 3: "))
            if level < 1 or level > 3:
                raise ValueError
            break
        except ValueError:
            pass
    return level

def generate_numbers(level):
    if level == 1:
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
    if level == 2:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)
    if level == 3:
        number1 = random.randint(100, 999)
        number2 = random.randint(100, 999)
    return number1, number2

def check_answer(x, y):
    for adds in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue
        if x + y == answer:
            return True
        else:
            print("EEE")
    print(f"{x}+{y} = {x + y}")
    return False

if __name__ == "__main__": main()

