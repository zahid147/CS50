import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matchs = re.match(r"(\d\d?(?::\d\d)?)\s(AM|PM)\sto\s(\d\d?(?::\d\d)?)\s(AM|PM)", s)
    if matchs:
#check
#        return f"{matchs.group(1)} {matchs.group(2)} {matchs.group(3)} {matchs.group(4)}"
        if ":" in matchs.group(1):
            sh, sm = matchs.group(1).split(":")
            sh, sm = int(sh), int(sm)
        else:
            sh, sm = int(matchs.group(1)), 0

        if ":" in matchs.group(3):
            eh, em = matchs.group(3).split(":")
            eh, em = int(eh), int(em)
        else:
            eh, em = int(matchs.group(3)), 0

        if sm > 59 or em > 59:
            raise ValueError

        if matchs.group(2) == "PM":
            if not sh == 12:
                sh += 12
        elif sh == 12 and matchs.group(2) == "AM":
            sh = 0
        elif matchs.group(4) == "PM":
            if not eh == 12:
                eh += 12
        elif matchs.group(3) == "12" and matchs.group(4) == "AM":
            eh = 0
        return f"{sh:02d}:{sm:02d} to {eh:02d}:{em:02d}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
