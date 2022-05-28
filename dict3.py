d={}
x=int(input())
for i in range(x):
    a,b=map(str,input().split())
    d[a]=int(b) #key is string and value is integer
print("Initial dictionary")
print(d)
key=input("Enter the key to delete: ")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)