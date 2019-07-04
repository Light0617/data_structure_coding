# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    opening_brackets_stack = []
    failed_position = -1
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            bracket = Bracket(next, i + 1)
            opening_brackets_stack.append(bracket)

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack or not opening_brackets_stack[-1].Match(next):
                failed_position = i + 1
                break
            opening_brackets_stack.pop()
    if len(opening_brackets_stack) == 0 and failed_position == -1:
        print('Success')
    elif failed_position != -1:
        print(failed_position)
    else:
        print(opening_brackets_stack[-1].position)

    # Printing answer, write your code here
