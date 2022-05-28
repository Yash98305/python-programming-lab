# The test has a total of N question, each question carries 3 marks for a correct answer and −1 for an incorrect answer. He attempt all the questions. X questions correct and the rest of them incorrect. pass the course he must score at least P marks.
t=int(input())
p=[]
for i in range(t):
    a,b,c=map(int, input().split(' '))
    d=a-b
    e=b*3
    if e-d>=c:
        p.append('PASS')
    else:
        p.append('Fail')
print(*p,sep='\n')
# INPUT         OUTPUT
# 3             PASS
# 5 2 3         FAIL
# 5 2 4         FAIL
# 4 0 0         