from requests import get
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    value = get("https://api.coindesk.com/v1/bpi/currentprice.json")
    output = value.json()
    rate = output["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    print("RequestException")

total = float(sys.argv[1]) * rate

print(f"${total:,.4f}")
