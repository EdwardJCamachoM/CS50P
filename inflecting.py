import inflect

p = inflect.engine()
names_list = []

def main():
    while True:
        try:
            user_input = input("What you wanna inflect?: ")
            names_list.append(user_input)
        except EOFError:
            break
    output_list = p.join(names_list)
    print(f"Adieu, Adieu to {output_list}")

if __name__ == "__main__": main()