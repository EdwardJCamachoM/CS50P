def main():
    print(gauge(get_fraction()))

def get_fraction():
        while True:
            try:
                tank_fraction = input("Enter the fraction of fuel your tank has: ")
                x, y = tank_fraction.split("/")
                tank_percentage = round((int(x)/int(y)) * 100)
                if int(x) > int(y):
                    raise ValueError
                return tank_percentage
            except ValueError:
                pass
            except ZeroDivisionError:
                pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__": main()