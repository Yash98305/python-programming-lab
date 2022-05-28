a=input("Enter string:")
count1=0
count2=0
for i in a:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print(f"The number of digits is:{count1}")
print(f"The number of characters is:{count2}")
	