from cs50 import get_string


def main():

    # taking input
    text = get_string("Text: ")

    # using function
    grade = readability(text)

    # print result
    if (grade >= 16):
        print("Grade 16+")
    elif (grade < 1):
        print("Before Grade 1")
    else:
        print("Grade", grade)


def readability(text):

    letter, word, sentence = 0, 1, 0

    for i in range(0, len(text)):
        if (text[i].isalpha()):
            letter += 1
        elif (text[i].isspace()):
            word += 1
        elif (text[i] == '.' or text[i] == '?' or text[i] == '!'):
            sentence += 1

    L, S = (letter / word * 100), (sentence / word * 100)
    index = (0.0588 * L - 0.296 * S - 15.8)

    return round(index)


if __name__ == "__main__":
    main()