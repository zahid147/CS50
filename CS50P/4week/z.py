from json import dumps
from requests import get

value = get("https://api.coindesk.com/v1/bpi/currentprice.json")
output = value.json()
value = dumps(value.json(), indent=" ")

print(output["bpi"]["USD"]["rate_float"])

#print(value)