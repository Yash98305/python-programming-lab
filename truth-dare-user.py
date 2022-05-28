import random as r
c=int(input('How many players you are :\n'))
p=[]
for i in range(c):
    name=input('Enter Player Name : ')
    p.append(name)
print()
while 1:
    b=r.sample(p,k=2)
    for i in range(2):
        if i == 1:
            print(f'Selected Person For Truth/Dare Question :\n{b[i]}\n')
        else:
            print(f'Person Who Give Truth/Dare :\n{b[i]}')
    en=(input())
    print("Thanks You",p[0],'and',p[1],'For Playing Truth/Dare Game .....')
    print("Have A Nice Day !!!\n")
    after=int(input("Enter '1' for replay and '0' for exit :\n"))
    if after==1:
        continue
    else:
        break
print("Thanks You Guys For Playing Truth/Dare Game")
print("Have A Nice Day !!!")



