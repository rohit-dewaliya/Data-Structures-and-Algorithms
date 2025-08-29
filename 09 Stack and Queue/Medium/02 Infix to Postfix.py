def remove_spaces(s):
    sanitized = ""
    for char in s:
        if char != ' ':
            sanitized += char

    return sanitized

def tokenize(expr):
    tokens = []
    num = ""
    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(num)
                num = ""
            if ch.strip():
                tokens.append(ch)
    if num:
        tokens.append(num)
    return tokens

def infix_postfix(s):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    tokens = tokenize(s)

    for char in tokens:
        if char.lstrip('-').isdigit():
            print(char)
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
                postfix.append(stack.pop())
    return postfix

def fix_unary_operators(expr):
    tokens = tokenize(expr)
    fixed = []
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == '-' and (i == 0 or tokens[i - 1] in "(+-*/^"):
            if i + 1 < len(tokens) and tokens[i + 1].lstrip('-').isdigit():
                fixed.append("-" + tokens[i + 1])
                i += 2
                continue
            elif i + 1 < len(tokens) and tokens[i + 1] == "(":
                fixed.append("0")
                fixed.append("-")
                i += 1
                continue

        fixed.append(token)
        i += 1

    return fixed

def calculator(num_1, num_2, operator):
    result = 0
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    elif operator == '/':
        result = num_1 / num_2
    elif operator == '^':
        result = num_1 ** num_2
    return result

def calculate(s):
    stack = []

    tokens = fix_unary_operators(s)
    postfix = infix_postfix(tokens)

    for char in postfix:
        if char.lstrip('-').isdigit():
            stack.append(int(char))
        else:
            num_2 = stack.pop()
            num_1 = stack.pop()

            result = calculator(num_1, num_2, char)
            stack.append(result)
        print(stack, char)
    return int(stack.pop())

s = "- (3 + (4 + 5))"
result = calculate(s)
print("Result: ", result)