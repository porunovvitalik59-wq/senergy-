import math

x = int(input(""))

count = 0
limit = int(math.isqrt(x)) 

for d in range(1, limit + 1):
    if x % d == 0:
        if d * d == x:
            count += 1          
        else:
            count += 2         

print(count)