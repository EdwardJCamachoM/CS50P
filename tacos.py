menu = {
"Burritos": 4.25,
"Bowl": 7.50,
"Nachos": 11.20,
"Quesadilla": 8.50,
"Super Burrito": 5.25,
"Super Bowl": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}


def main():
    bill= 0
    while True:
        try:
            user_input = input("Que vas a comer?: ")
            if user_input.title() in menu:
                bill += menu[user_input.title()]
                print(f"${bill:.2f}")
        except EOFError:
            print(f"\n${bill:.2f}") 
        except KeyboardInterrupt:
            break
if __name__ == "__main__": main()