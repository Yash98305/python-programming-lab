keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:") #key is letter/string
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    keys.append(element)
print("For values:") #value is integer
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print(f"The dictionary is:\n{d}")