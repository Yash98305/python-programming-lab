a=input("Enter string:")
l=[]
l=a.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))