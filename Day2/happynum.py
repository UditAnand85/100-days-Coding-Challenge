def isHappy(n):
    seen = set()  
    
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        n = total
    
    return n == 1


print(isHappy(19))   
print(isHappy(2))    
