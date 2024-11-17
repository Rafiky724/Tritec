def longer_valid_parentheses(s):
    stack = []  
    count = 0  

    for char in s:
        if char == "(":  
            stack.append("(")  
        elif char == ")":  
            if stack:  
                stack.pop()  
                count += 1  

    return count  