t = input("Input the  temperature you like to convert(e.g., 45F, 102C etc.) : ")
n=t[:-1]
print(n)
d= t[-1].capitalize()
if d=='C':
    print("Entered Temperature is in Celcius")
    print(f'{n}{d} = {(float(n)*1.8) + 32}F') 
    print(f'{n}{d} = {(float(n)+273.15)}K')
elif d=='F':
    print("Entered Temperature is in Farenheit")
    print(f'{n}{d} = {(float(n)-32) / 1.8}C') 
    print(f'{n}{d} = {((float(n)-32) * 5/9)+273.15}K')
elif d=='K':
    print("Entered Temperature is in Kelvin")
    print(f'{n}{d} = {(float(n)-273.15)}C')
    print(f'{n}{d} = {((float(n)-273.15) * 1.8)+32}F') 
else:
    print('You Enter wrong conversion')