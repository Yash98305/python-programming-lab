# t=2,9,4,4,5,1,5
# for i in (t):
#     if t.count(i)>1:
#         print(i)
a=tuple(map(int,input().split()))
print(a)
ls=[]
for i in (a):
    if a.count(i)>1 and i not in ls:
        print(i)
        ls.append(i)