def main():
    x = float(input("What's x?: "))
    y = input("What operator do you want to use?: ").strip()
    z = float(input("What's z?: "))

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/" and z != 0:
        print(x / z)
    else:
        print("Invalid operator")

main()