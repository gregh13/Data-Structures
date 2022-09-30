# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    # Checks if brackets match, returns boolean value
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    # Initialize stack
    opening_brackets_stack = []

    # Loop through text with the character and index
    for i, next in enumerate(text):

        # Check if open bracket
        if next in "([{":
            # Format char and add to stack
            char = Bracket(next, i+1)
            opening_brackets_stack.append(char)

        # Check if closed bracket
        if next in ")]}":

            # Check if there are any open brackets
            if not opening_brackets_stack:
                return True, Bracket(next, i+1)

            # Grab most recent open bracket
            top = opening_brackets_stack.pop()

            # Check if most recent open bracket matches this closing bracket
            if not are_matching(top.char, next):

                # Format char and return
                unmatched_bracket = Bracket(next, i+1)
                return True, unmatched_bracket

    # Check if any unclosed open brackets remain
    if opening_brackets_stack:
        open_bracket = opening_brackets_stack[-1]
        return True, open_bracket

    # Everything matches
    return False, None


def main():
    text = input()
    mismatch, bracket = find_mismatch(text)

    # Per the assignment specifications, print the position of the most recent error otherwise print Success
    if mismatch:
        print(bracket.position)
    else:
        print("Success")


if __name__ == "__main__":
    main()
