#create a tuple
t = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(t)

#tuples are immutable, so you can not remove elements

#----------------------------------------------------------------------

#using merge of tuples with the + operator you can remove an item and it will create a new tuple
t = t[:2] + t[3:]
print(t)

#----------------------------------------------------------------------

#converting the tuple to list
l = list(t) 
#use different ways to remove an item of the list
l.remove("c") 
#converting the tuple to list
t = tuple(l)
print(t)