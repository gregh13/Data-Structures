# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        print("----------")
        print(opening_brackets_stack)
        print(next)
        if next in "([{":
            char = Bracket(next, i+1)
            opening_brackets_stack.append(char)

        if next in ")]}":
            top = opening_brackets_stack.pop()
            print(top)
            if (top.char == "[" and next != "]") or (top.char == "(" and next != ")") or (top.char == "{" and next != "}"):
                unmatched_bracket = Bracket(next, i+1)
                return True, unmatched_bracket
        print(opening_brackets_stack)
    if opening_brackets_stack:
        open_bracket = opening_brackets_stack[-1]
        return True, open_bracket

    return False, None


def main():
    text = input()
    mismatch, bracket = find_mismatch(text)
    if mismatch:
        print(bracket.position)
    else:
        print("Success")


if __name__ == "__main__":
    main()
