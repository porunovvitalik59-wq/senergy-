n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

reversed_numbers = numbers[::-1]
print(*reversed_numbers)
