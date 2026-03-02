
# DICTIONARY DEFINITION
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# MAIN FUNC DEFINITION - PRINTS WELCOME MESSAGES
def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    # MAKES A COPY OF WORDS DICTIONARY TO USE IT LATER AS AN OUTPUT
    original_words = WORDS.copy()
    
    # WHILE THE LENGTH OF WORDS DICTIONARY IS MORE THAN 0
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word! ")
        # IF INPUT == "GRAPHIC" THE GAMES END, THE LOOP ENDS WHEN THE DICTIONARY LENGTH HITS 0
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        # IF WORDS.pop MAKES THE LENGTH OF WORDS GOES TO 0 THEN THE LOOP ENDS, AS THE DICTIONARY LENGTH HITS 0
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points")
    # TO BE PRINTED AFTER THE LOOP ENDS
    print("That's the game!")
    # SELECT AND PRINTS THE VALUES OF THE DICTIONARY'S COPY AS ITS COUNT WENT TO 0
    for keys, values in original_words.items():
        print(f"{keys} was worth {values} points.") 

main()