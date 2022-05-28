d={}
x=int(input())
for i in range(x):
    a,b=map(str,input().split())
    d[a]=int(b) # key is string and value is integer
key=input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")	
	