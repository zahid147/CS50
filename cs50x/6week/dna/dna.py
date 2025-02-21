import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        sys.exit("Proper usage: python dna.py /database/file /sequence/file")

    if "databases" not in sys.argv[1] or "sequences" not in sys.argv[2]:
        sys.exit("Proper usage: python dna.py /database/file /sequence/file")

    # TODO: Read database file into a variable
    data = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    sub = list(data[0].keys())[1:]

    result = {}
    for subsequence in sub:
        result[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for person in data:
        match = 0
        for subsequence in sub:
            if int(person[subsequence]) == result[subsequence]:
                match += 1

            if match == len(sub):
                print(person["name"])
                return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
