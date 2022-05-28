def ispalindrom(x):
    return x[::]==x[::-1]
a=input('Enter number or word : ')
print('is palindrom') if ispalindrom(a)==1 else print('is not palindrom') 