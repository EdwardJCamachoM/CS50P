def main():
    groceries = groceries_list()
    for item in groceries:
        print(item)

def groceries_list():
    groceries = []
    while True:
        try:
            user_input = input("Enter an item: ")
            groceries.append(user_input.upper())
        except EOFError:
            break
        except KeyboardInterrupt:
            break
    groceries.sort()
    return groceries

if __name__ == "__main__": main()