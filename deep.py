def main():
    user_value = input("What's the answer to the Great Question of Life, the Universe and Everything?: ")
    
    if user_value in ["42", "forty-two", "forty two"]:
        print("yes")
    else:
        print("no")

main()