stack = []

expression = input("Enter an expression: ")

balanced = True

for ch in expression:

    if ch == '(':
        stack.append(ch)

    elif ch == ')':
        if len(stack) == 0:
            balanced = False
            break
        else:
            stack.pop()

if len(stack) != 0:
    balanced = False

if balanced:
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")