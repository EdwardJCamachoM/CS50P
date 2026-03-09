import random

cards = ["jack", "queen", "king", "ace"]

def main():
    random.seed(1)
    print(random.choices(cards, k=2))



main()