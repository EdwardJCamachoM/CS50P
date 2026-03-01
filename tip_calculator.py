def main():
    bill = get_bill()
    tip = calculate_tip(bill)
    total = bill + tip
    print(f"Tip amount: ${tip:.2f}")
    print(f"Total: ${total:.2f}")

def get_bill():
    bill = float(input("Bill amount: "))
    return bill

def calculate_tip(bill):
    tip = int(input("Tip percentage (10, 15, 20): "))
    tip = bill * (tip / 100)
    return tip

if __name__ == "__main__":
    main()