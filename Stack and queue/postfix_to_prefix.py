def postfix_to_prefix(postfix:str):
    stack = []

    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            operator2 =stack.pop()
            operator1 =stack.pop()
            new_value = f"{ch}{operator1}{operator2}"
            stack.append(new_value)

    return stack[-1]

def prefix_to_postfix(pre:str):
    stack = []

    for ch in prefix[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            operator2 =stack.pop()
            operator1 =stack.pop()
            new_value = f"{operator2}{operator1}{ch}"
            stack.append(new_value)

    return stack[-1]

postfix = "ab-de+f*/"
prefix = postfix_to_prefix(postfix)

print("postfix string : ",postfix)
print("prefix string : ",prefix)

postfix = prefix_to_postfix(prefix)

print("prefix string : ",prefix)
print("postfix string : ",postfix)