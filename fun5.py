def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
a=int(input())
print(f'{a} is a perfect number') if perfect_number(a)==1 else print(f'{a} is not a perfect number')