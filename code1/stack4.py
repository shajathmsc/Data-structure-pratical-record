stack = []

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1

    if operator == '*' or operator == '/':
        return 2

    if operator == '^':
        return 3

    return 0


expression = input("Enter infix expression: ")

postfix = ""

for ch in expression:

    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()

        stack.pop()

    else:
        while (stack and stack[-1] != '(' and
               precedence(stack[-1]) >= precedence(ch)):
            postfix += stack.pop()

        stack.append(ch)


while stack:
    postfix += stack.pop()

print("Infix Expression  :", expression)
print("Postfix Expression:", postfix)
