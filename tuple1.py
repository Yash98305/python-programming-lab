#create a tuple
t = (4, 6, 2, 8, 3, 1) 
print(t)

#tuples are immutable, so you can not add new elements

# --------------------------------------------------------------------------

#using merge of tuples with the + operator you can add an element and it will create a new tuple
t = t + (9,)
print(t)

# --------------------------------------------------------------------------

#adding items in a specific index
t = t[:5] + (15, 20, 25) + t[:5]
print(t)

# --------------------------------------------------------------------------

#converting the tuple to list
listx = list(t)

# --------------------------------------------------------------------------

#use different ways to add items in list
listx.append(30)
t = tuple(listx)
print(t)