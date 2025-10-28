n = 687 
sum = 0
for i in range(0,len(str(n))):
    sum = sum + (n % 10)
    n = n // 10
print(sum)