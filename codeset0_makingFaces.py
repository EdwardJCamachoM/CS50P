def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji

def main():
    message = input("Input: ")
    message = convert(message)
    print(message)

main()