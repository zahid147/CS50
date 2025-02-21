import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    match = re.search(r"^\d+\.\d+\.\d+\.\d+$", ip)

    if match:
        list = ip.split(".")
        for i in range(4):
            if not 0 <= int(list[i]) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
