def priority(ch:str):
    if ch =="^":
        return 3 
    elif ch == "/" or ch == "*":
        return 2 
    elif ch == "+" or ch == "-":
        return 1 
    return 0

def infix_to_postfix(infix:str):
    stack = []
    postfix = []
    for ch in infix:
        if ch.isalnum():
            postfix.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop() # pop the '('
        else: # operator
            while stack and priority(stack[-1]) >= priority(ch):
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return "".join(postfix)


def infix_to_prefix(infix:str):
    stack = []
    prefix = []

    infix = infix[::-1] # reverse the infix expression
    infix = infix.replace("(","temp").replace(")","(").replace("temp",")") # swap '(' and ')'
    
    for ch in infix:
        if ch.isalnum():
            prefix.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                prefix.append(stack.pop())
            stack.pop() # pop the '('
        else: # operator
            while stack and priority(stack[-1]) >= priority(ch):
                prefix.append(stack.pop())
            stack.append(ch)

    while stack:
        prefix.append(stack.pop())

    return "".join(prefix)

# Example usage:
infix_expr = "(a+b)*c-d+f"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression: ", infix_expr)
print("Postfix Expression: ", postfix_expr)
print("----------------------------------------")
prefix_expr = infix_to_prefix(infix_expr)
print("Infix Expression: ", infix_expr)
print("Prefix Expression: ", prefix_expr)