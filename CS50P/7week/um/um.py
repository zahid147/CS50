import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    match = re.findall(r"\b(u|U)(m|M)(\b)[^A-Za-z]?", s)
    return len(match)


if __name__ == "__main__":
    main()
