def main():
    print(gauge(get_fraction()))

def get_fraction():
        while True:
            try:
                tank_fraction = input("Enter the fraction of fuel your tank has: ")
                x, y = tank_fraction.split("/")
                return convert(int(x), int(y))
            except ValueError:
                pass
            except ZeroDivisionError:
                pass

def convert(x, y):
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__": main()