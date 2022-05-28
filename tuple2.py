#create a tuple
t = tuple(map(int,input().split())) #2, 4, 5, 6, 2, 3, 4, 4, 7
print(t)
a=int(input('Enter a no. for checking there appearance : '))
#return the number of times it appears in the tuple.
count = t.count(a)
print(count)