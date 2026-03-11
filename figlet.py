import sys
import random
import pyfiglet

def main():
    slant = input("Write a text to figlet: ")
    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        slant = pyfiglet.figlet_format(slant, font=sys.argv[2])
        print(slant)
    elif len(sys.argv) == 1:
        slant = pyfiglet.figlet_format(slant, font=random.choice(pyfiglet.FigletFont.getFonts()))
        print(slant)
    else:
        sys.exit()

if __name__ == "__main__": main()