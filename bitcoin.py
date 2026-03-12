import requests
import sys

r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = r.json()
price = data["bitcoin"]["usd"]

def main():
        try:
            user_input = float(input("How many bitcoins?: "))
            bitcoin = float(user_input) * price
        except ValueError:
            sys.exit()
        print(f"${bitcoin:,.2f}")

if __name__ == "__main__": main()