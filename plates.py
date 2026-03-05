def main():
    plate = input("What's your vehicle's plate?: ")
    if is_length(plate) and is_start(plate) and is_numbers_last(plate) and no_leading_zero(plate) and is_no_punctuation(plate):
        print("Valid plate")
    else:
        print("Invalid plate")

def is_length(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False

def is_start(plate):
    if plate[:2].isalpha():
        return True
    else:
        return False

def is_numbers_last(plate):
    found_number = False
    for char in plate:
        if char.isnumeric():
            found_number = True
        if char.isalpha() and found_number:
            return False
    return True

def no_leading_zero(plate):
    for char in plate:
        if char.isnumeric():
            if char == "0":
                return False
            return True
    return True

def is_no_punctuation(plate):
    for char in plate:
        if not char.isalpha() and not char.isnumeric():
            return False
    return True

if __name__ == "__main__": main()