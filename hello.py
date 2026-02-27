### This function captures the user's name

def main(to):
    name = input("What's your name? ")
    hello(name)

### This function prints the value captured by the function name "main"

def hello(to="world"):
    print("hello,", to)

main()