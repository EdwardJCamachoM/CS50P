# Ask user for their name
name = input("What's your name? ")

# Remove white spaces from str and Capitalize user's name
name = name.strip().title()

# Split user's name into first name and last name

first, last = name.split()

# Say hello to user
print("hello,", last)
print(f"hello, {first}")