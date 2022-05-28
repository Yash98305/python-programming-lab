d={}
x=int(input())
for i in range(x):
    a,b=map(str,input().split())
    d[a]=int(b) #key is string and value is integer
print(d)