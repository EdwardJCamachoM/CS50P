fruits = {
"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50, "Kiwi": 90,
"Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100, "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80
}

def main():
    user_input = input("What fruit are you curious about?: ")
    if user_input.title() in fruits:
        print("Item: ", user_input.title())
        print("Calories: ", fruits.get(user_input.title()))
    else:
        print("Invalid Fruit - Choose one of the following list:")
        for fruit in fruits:
            print(fruit)

if __name__ == "__main__": main()
