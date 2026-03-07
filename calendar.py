months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        try:
            user_input = input("Enter a date: ")
            user_input = user_input.title()
            if "/" in user_input:
                dates = user_input.split("/")
                month = int(dates[0])
                days = int(dates[1])
                year = int(dates[2])
            else:
                dates = user_input.replace(",", "").split(" ")
                month = int(months.get(dates[0]))
                days = int(dates[1])
                year = int(dates[2])
            if month > 12 or days > 31:
                raise ValueError
            print(f"{year}-{month:02d}-{days:02d}")
        except ValueError:
            pass

if __name__ == "__main__": main()