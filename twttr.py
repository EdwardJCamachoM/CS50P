def main():
    post = input("Insert your message: ")
    print(chop(post))

def chop(post):
    result = ""
    for letter in post:
        if letter not in "AEIOUaeiou":
            result += letter
    return result

if __name__ == "__main__": main()