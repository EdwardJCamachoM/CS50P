
def main():
    print("Change owed: ", machine())

def machine():
    amount_due = 50
    while amount_due > 0:
        print("Amount due: ", amount_due)
        amount_paid = int(input("Insert coin: "))
        if amount_paid == 25 or amount_paid == 10 or amount_paid ==5:
            amount_due -= amount_paid
    return -amount_due

if __name__ == "__main__": main()