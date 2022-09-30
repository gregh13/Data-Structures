# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            char = Bracket(next, i)
            opening_brackets_stack.append(char)

        if next in ")]}":
            top = opening_brackets_stack.pop()
            if top == "[" and next != "]" or top == "(" and next != ")" or top == "{" and next != "}":
                return False
    return bool(opening_brackets_stack)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
