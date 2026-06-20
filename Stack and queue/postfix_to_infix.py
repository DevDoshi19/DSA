def postfix_to_infix(postfix:str):
    stack = []

    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            operator2 =stack.pop()
            operator1 =stack.pop()
            new_value = f"({operator1}{ch}{operator2})"
            stack.append(new_value)

    return stack[-1]

def prefix_to_infix(prefix:str):
    stack = []

    for ch in prefix[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            operator1 =stack.pop()
            operator2 =stack.pop()
            new_value = f"({operator1}{ch}{operator2})"
            stack.append(new_value)

    return stack[-1]



postfix = "ab-de+f*/"
infix = postfix_to_infix(postfix)

print("postfix string : ",postfix)
print("infix string : ",infix)

prefix = "*+pq-mn"
infix = prefix_to_infix(prefix)

print("postfix string : ",prefix)
print("infix string : ",infix)