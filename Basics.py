#Author:-SWAPNIL PATEL
#Date:-1/10/2020
#Topic:-Basic Python
#-----------------------------Variables in python----------------------------------#
#varaibles= Containers to store data/datatypes
#Datatypes=int,str,float,bool,chr,etc...,
print("~Variables tutorial starts from here:")
print("1) This are the examples of vraiables datatypes:-")
a="Swapnil" #String
b=32        #integer
c=34.5      #float
print("→",type(a))  #type() is used to findout type of datatypes used in the variables.
print("→",type(b))
print("→",type(c))

print(''' ''')
#-----------------------------STRINGS AND SLICING-----------------------------------#
print("~STRINGS AND SLICING tutorial starts from here:")
a="Swapnil is a good boy"
print("1) The length of the stinrg can be found by using len() function:-")
v=len(a)                                #length of the variable a 
print("→",v)
print("2) Slicing example for strings:-")
print("→",a[0:21:2])                        #Slicing [Starting index:Ending index:Jump index]
print(''' ''')
#----------------------------Booleans in python-------------------------------------#
#it has 2 output i.e TRUE OR FALSE
print("~Booleans tutorial starts here:")
print("1) Example output for Bool Function")
print("→",10<9) #o/p will be FALSE
print("→",10>9) #o/p will be TRUE

#another way is by bool() function
print("→",bool("Swapnil"))
print("→",bool(23568))
print("→",bool())
print(''' ''')
#--------------------------operators in python--------------------------------------#
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

#-------------------------Lists in python--------------------------------------------#
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort() 	Sorts the list
print("~Lists tutorial starts here:")
print("1) Basic List:-")
list=["Apple","Banana","cherry"]
print("→",list)
#Slicing can also be done in list
print("2) Using len() function to find the length of the list:-")
print("→",len(list)) # length of list is 3
print("3) SLicing can also be used in List same as we do in strings:-")
print("→",list[0:2]) #0:-is starting index,2:-is ending index.
print("→",list[-3:-1]) # Negative indexing means starting from the end of the list.

list[2]="Swapnil"
print("→",list) #Here,Cherry is updated by Swapnil. 
list2=[1,2,3,4]
list3=[5,6,7,8]


list4= list +list2+ list3 #Adding 2 or more lists.
print("→",list4)

list.append("Swap") # Methods cannot be used directly in print() function,But on the other hand Function can be used directly in the print() function
print("→",list)

list.extend(list2)
print("→",list)
print(''' ''')
#--------------------------Tuples in python------------------------------------------#
#Every Methods and functions are not applicable to tuples,because it is unchangable
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
print("~Tuples tutorial starts here:")
tuple=("Apple","Banana","Cherry")
print(tuple)
print(len(tuple)) #len() function
print(tuple[0:2]) #slicing can also be done on tuples too... 
print(''' ''')
#--------------------------Sets in python------------------------------------------#
# Method	            Description
# add()	                Adds an element to the set
# clear()	            Removes all the elements from the set
# copy()	            Returns a copy of the set
# difference()	        Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()         	Remove the specified item
# intersection()	    Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	        Returns whether two sets have a intersection or not
# issubset()	        Returns whether another set contains this set or not
# issuperset()      	Returns whether this set contains another set or not
# pop()	                Removes an element from the set
# remove()	            Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	            Return a set containing the union of sets
# update()	            Update the set with the union of this set and others

#Slicing cannot be doen on sets
print("Sets tutorial starts here:")
set={"Apple","Banana","Cherry"}
print(set)
print(len(set)) #len() function
print(''' ''')
#--------------------------Dictionaries in python------------------------------------------#
# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary
print("~Dictionaries tutorial starts here:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
x = thisdict.get("year")
print(x)

#Change Values
#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red" #Here "color" is your key & "red" is your value
print(thisdict)

#Nested Dictionaries
#A dictionary can also contain many dictionaries, this is called nested dictionaries.


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(''' ''')
#--------------------------Conditional Statements in python------------------------------------------#

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
print("~Conditional Statements tutorial starts here:")
#Basic if syntax
a = 33
b = 200
if b > a:
  print("b is greater than a") #Here in Conditional Statements while using print() function tab space in compulsory,orelse it will be considered as an error

# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

#basic if & elif Syntax
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#SHORT HAND OR ONE LINER SYNTAX
# FOR IF STATEMENT
a = 33
b = 200
if a>b: print("a is grater than b")  

#FOR IF ELSE STATEMENT
a = 33
b = 200
print("S") if a>b else print("P") #HERE,in if else one liner we use print() fun. first and than the condition

#also can have multiple if else statement in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#logical operators in conditional statement
#AND & OR
#1)AND Operator
a=200
b=33
c=500
if a>b and a<c:
  print("Both conditons are true")
else:
  print("Conditions are false")

#2)OR Operator
a=1
b=2
c=3
if a<b or a>c:
  print("Conditions are true")
else:
  print("conditions are false")

# #The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

print(''' ''')

# Python Loops
# Python has two primitive loop commands:

# while loops
# # for loops
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

