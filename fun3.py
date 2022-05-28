def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
a=int(input('Enter a no.: '))         
print('No. is Prime') if prime(a)==1 else print('No. is not Prime')	