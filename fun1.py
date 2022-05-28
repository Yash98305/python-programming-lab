def sum(numbers):
    s = 0
    for x in numbers:
        s += x
    return s
a=list(map(int,input().split())) #input like 1 2 3 4 
print(sum(a))