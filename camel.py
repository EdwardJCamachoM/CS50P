def main():
    name = input("Enter the camelCase text to convert: ")
    print(convert(name))

def convert(name):
    result = ""
    for letter in name:
        if letter.isupper():
            result += ("_" + letter.lower())
        else:
            result += (letter)
    return result

if __name__ == "__main__": main()