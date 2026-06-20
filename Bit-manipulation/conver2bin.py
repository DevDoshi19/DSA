def convert2binary(n)->str:
    binary = ""
    
    while n > 0:
        if n % 2 == 0 :
            binary += "0"
        else:
            binary +="1"
            
        n = n // 2
        
    return binary[::-1]

def convert2decimal(s)->int :
    number = 0
    power = 0
    index = len(s) - 1

    while index >= 0 :
        number = (int(s[index]) * (2**power)) + number
        power += 1
        index -= 1

    return number
        
    
print(convert2binary(9))
print(convert2decimal("1001"))
print(convert2binary(13))
print(convert2decimal("1101"))