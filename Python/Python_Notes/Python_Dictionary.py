Dictionary Datastructures:
--------------------------

-The list, tuple and Set, all three was meant for individual objects
-If we want to represent group objects as key-value pairs then we need to opt for dictionary
rollno-name
mobilenumber-address
ipaddress-domain_name
-Syntax >> {k1:v1,k2:v2,k3:v3}

##Example1:
d={100:'Durga',200:'Ravi'}
print(d)
print(type(d))

##Output:
{100: 'Durga', 200: 'Ravi'}
<class 'dict'>

##When to opt for dictionaries:
    -When we want represent group of key-value pairs
    -Duplicate keys are not allowed, but values can be duplicated
    -Insertion order is not preserved, because data is stored based on hash code of the keys
    -Indexing and Slicing are not allowed
    -Heterogenous objects are allowed for both keys and values
    -It's mutable
    -Dynamic in nature, as per req we can increase/decrease the objects

##Example2:
d={100:'Durga',200:'Ravi','A':400,'Sunny':69,100:'Shiva',45:'Ravi'} ##Duplicate keys will be removed, but duplicate values are retained
print(d)
print(type(d))

##Output:
{100: 'Shiva', 200: 'Ravi', 'A': 400, 'Sunny': 69, 45: 'Ravi'}
<class 'dict'>

=======================================================================
##Creation of Dict Objects:

##Example1: Empty Dict
d={}
d1=dict()
print(d)
print(type(d))
print(d1)
print(type(d1))

##Output:
{}
<class 'dict'>
{}
<class 'dict'>

##Example2: If we know data already:
d={100:'Durga',200:'Ravi'}
print(d)
print(type(d))

##Output:
{100: 'Durga', 200: 'Ravi'}
<class 'dict'>

##Example3: Using dict() function
l=[(100,'A'),(200,'B'),(300,'C'),(100,'S')] ##It's a list of tuples
print(l)
d=dict(l)
print(d)
print(type(d))

##Output:
[(100, 'A'), (200, 'B'), (300, 'C'), (100, 'S')]
{100: 'S', 200: 'B', 300: 'C'}
<class 'dict'>

##*****Note:
        -We can try using tuple of tuples
        -Set of tuples
        -Lists of lists
        -Tuple of lists
        -Set of lists is not supported, because set is hashable and lists inside it is not hashable, hence won't work

##Example4:
l=((100,'A'),(200,'B'),(300,'C'),(100,'S')) ##It's a tuple of tuples
print(l)
d=dict(l)
print(d)
print(type(d))

##Output:
((100, 'A'), (200, 'B'), (300, 'C'), (100, 'S'))
{100: 'S', 200: 'B', 300: 'C'}
<class 'dict'>

##Example5:
l={(100,'A'),(200,'B'),(300,'C'),(100,'S')} ##It's a set of tuples
print(l)
d=dict(l)
print(d)
print(type(d))

##Output:
{(100, 'A'), (100, 'S'), (300, 'C'), (200, 'B')}
{100: 'S', 300: 'C', 200: 'B'}
<class 'dict'>

##Example6:
l={[100,'A'],[200,'B'],[300,'C'],[100,'S']} ##It's a set of lists, it will throw error
print(l)
d=dict(l)
print(d)
print(type(d))

##Output:
TypeError: unhashable type: 'list'

##Example7:
l={(100,'A',90),(200,'B','C'),(300,'C'),(100,'S')} ##It's a set of tuples, it will throw error
print(l)
d=dict(l)
print(d)
print(type(d))

##Output:
ValueError: dictionary update sequence element #2 has length 3; 2 is required

##Example8: By using Dynamic input:
d=eval(input('Enter Dictionary: ')) ##Eval is used to convert to dictionary, because by default input's return datatype is string
print(d)
print(type(d))

##Output:
Enter Dictionary: {100: 'Shiva', 200: 'Ravi', 'A': 400, 'Sunny': 69, 45: 'Ravi'}
{100: 'Shiva', 200: 'Ravi', 'A': 400, 'Sunny': 69, 45: 'Ravi'}
<class 'dict'>

============================================================================
##How to access data from the Dictionary:
Syntax >> d[key]=value

##Example1: To access data through a key
d={100: 'Shiva', 200: 'Ravi', 'A': 400, 'Sunny': 69}
print(d[100])
print(d['Sunny'])
print(d[300]) ##Will throw error

##Output:
Shiva
69
KeyError: 300

##Example2: We can avoid key error using membership operator
d={100: 'Shiva', 200: 'Ravi', 420: 400, 96: 69}
key=int(input('Enter key to find value: ')) ##Key can't always be int type, just for our example we have opted for int type
if key in d:
    print('The corresponding value: ',d[key])
else:
    print('Specified key is not available')


##Output:
Enter key to find value: 500
Specified key is not available
Enter key to find value: 96
The corresponding value:  69

How to add/update data in dictionary:
-------------------------------------

##Example1:
d={100: 'Shiva', 200: 'Ravi'}
d[300]='Shiva' ##Adding new key & value
print(d)
d[100]='Sunny' ##Updating existing key & value, since duplicates are not allowed, existing value is updated
print(d)

##Output:
{100: 'Shiva', 200: 'Ravi', 300: 'Shiva'}
{100: 'Sunny', 200: 'Ravi', 300: 'Shiva'}

How to delete data in dictionary:
---------------------------------
Syntax >> del d[key]
    -If the key is available, it will be deleted
    -If the key is not available, it will throw error

##Example1:
d={100: 'Shiva', 200: 'Ravi', 300: 'Shiva'}
del d[100] ##Deleting existing key
print(d)
del d[200],d[300] ##Deleting multiple keys
print(d)
del d[500] ##Error, trying to delete non-existance key
print(d)

##Output:
{200: 'Ravi', 300: 'Shiva'}
{}
KeyError: 500

=======================================================================

##Write a program to enter name and marks into dictionary and display information on the screen?

n=int(input('Number of Students: '))
d={}
for i in range(n):
    name=input('Enter name of the Student: ')
    marks=int(input('Enter marks of the Student: '))
    d[name]=marks ##Creating dictionary
print(d)
print(type(d))
##To display data in the form tabular
print('*'*20)
print('Name','\t\t','Marks') ##\t\t will provide two tabs
print('*'*20)
for name in d:
    print(name,'\t\t',d[name])

##Output:
Number of Students: 3
Enter name of the Student: Siva
Enter marks of the Student: 67
Enter name of the Student: Ravi
Enter marks of the Student: 68
Enter name of the Student: Sunny
Enter marks of the Student: 69
{'Siva': 67, 'Ravi': 68, 'Sunny': 69}
<class 'dict'>
********************
Name 		 Marks
********************
Siva 		 67
Ravi 		 68
Sunny 		 69

=================================================================================
##Mathematical, Equality, Relational and Membership Operators for Dict:

-The '+' is not applicable for dictionary
-The '*' is not applicable for dictionary
-The '==' is applicable, will true if number of keys and values are same and same keys and values are matched, order is not important
-The '>','<','>=' and '<=' are not applicable to dictionary
-The 'in' and 'not in' is applicable only for keys(sensible) and not applicable for values

##Example1:
d1={'Siva': 67, 'Ravi': 68}
d2={300:'C',400:'D'}
d3=d1+d2 ##Type error
d4=d1*3 ##Dupliocates not allowed, type error
print(d1==d2)
d3={'Ravi': 68,'Siva': 67}
print(d1==d3)
print(d1>d3) ##Error, not supported


##Output:
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
False
True
TypeError: '>' not supported between instances of 'dict' and 'dict'

##Example2:
d1={100:'A',200:'B'}
print(100 in d1)
print(300 in d1)
print('A' in d1) ##It never checks for value

##Output:
True
False
False

=============================================================================

##Important functions/methods for Dict:
---------------------------------------

-len(dict) : It returns number of items present in dict, item means key-value pairs
-dict.get(key) : We won't get key error, instead gives none
-dict.get(key,default_value) : If specified key is not available return default value instead of none
-dict1.update(dict2) : All key value pairs present in dict2 to be added/updated to dict1, duplicates are not allowed, if key is duplicated, then the duplicate key value pair of dict2 is considered instead of dict1(sensible)

##Example1:
d1={100:'A',200:'B'}
print(len(d1))

##Output:
2

##Example2:
d={100:'A',200:'B',300:'C'}
print(d.get(100))
print(d.get(600)) ##Will return None
print(d.get(600,'Guest'))
print(d.get(300,'Guest')) ##Will return default value

##Output:
A
None
Guest
C

##Example3:
dict1={100:'A',200:'B'}
dict2={400:'D',300:'C',200:'E'}
dict1.update(dict2)
print(dict1) ##Duplicates not allowed but latest value for 200 i.e. 'E' is added

##Output:
{100: 'A', 200: 'E', 400: 'D', 300: 'C'}

================================================================================
##Important Methods and Functions for Dict:Keys(),Values() and Items():

##Example1:
d={400:'D',300:'C',200:'E'}
k=d.keys()
print(k)
print(type(k))
##To view keys in separate line:
for key in k:
    print(key)
print(type(key))

##Output:
dict_keys([400, 300, 200])
<class 'dict_keys'>
400
300
200
<class 'int'>


##Example2:
d={400:'D',300:'C',200:'E'}
v=d.values()
print(v)
print(type(v))
##To view values in separate line:
for value in v:
    print(value)
print(type(value))

##Output:
dict_values(['D', 'C', 'E'])
<class 'dict_values'>
D
C
E
<class 'str'>

##Example3:
d={400:'D',300:'C',200:'E',100:'A'}
i=d.items()
print(i)
print(type(i))
for items in i:
    print(items)
print(type(items))

##Output:
dict_items([(400, 'D'), (300, 'C'), (200, 'E'), (100, 'A')]) ##This is a list of items
<class 'dict_items'>
(400, 'D')
(300, 'C')
(200, 'E')
(100, 'A')
<class 'tuple'>

##Example4:
d={400:'D',300:'C',200:'E',100:'A'}
i=d.items()
print(i)
print(type(i))
for items in i:
    print(items)
print(type(items))
##Most common approach to retrieve data from dictionary as seen below
##To fetch key,value in every items:
for k,v in i:
    print(k,'....',v)
print(type(k))
print(type(v))

##Output:
dict_items([(400, 'D'), (300, 'C'), (200, 'E'), (100, 'A')])
<class 'dict_items'>
(400, 'D')
(300, 'C')
(200, 'E')
(100, 'A')
<class 'tuple'>
400 .... D
300 .... C
200 .... E
100 .... A
<class 'int'>
<class 'str'>

==========================================================================

##Write a program to get value from the dictionary for the given key?
##Write a program to get key from the dictionary for the given value?

##Program1:
d={400:'D',300:'C',200:'E',100:'A'}
##Based on key finding value:
key=int(input('Enter key to get value: '))
if key in d:
    print('The corresponding value: ',d.get(key))
else:
    print('The specified key is not available')
    
##Output:
Enter key to get value: 100
The corresponding value:  A

##Program2: Finding key based on value:
d={400:'D',300:'C',200:'E',100:'A',101:'A'}
##Based on key finding value:
value=input('Enter value to find key: ')
available=False
for k,v in d.items():
    if v==value:
        print('The corresponding key: ',k)
        available=True
if available==False:
    print('The specified value not found in dict')
    
##Output:
Enter value to find key: D
The corresponding key:  400

Enter value to find key: A
The corresponding key:  100
The corresponding key:  101

=========================================================================
##Important Methods and Functions for Dict:pop(),popitem() and clear():

dict.pop(key):
    -Removes item associated with specified key and returns the corresponding value
    -We will get KeyError if specified key is not available

dict.pop(key,value):
    -Removes item associated with specified key and returns the corresponding value
    -We will not get KeyError if specified key is not available, instead it will return the provided value
dict.popitem():
    -An arbitary key,value pair will be removed, not sure which one and returns that item
    -If the dict is empty then we will get KeyError
dict.clear():
    -Removes all items(key-value pairs) from the dictionary and dictionary becomes empty
   
##Example1:
d={400:'D',300:'C',200:'E',100:'A',101:'A'}
print(d.pop(300))
print(d)
print(d.pop(500))

##Output:
C
{400: 'D', 200: 'E', 100: 'A', 101: 'A'}
KeyError

##Example2:
d={400:'D',300:'C',200:'E',100:'A',101:'A'}
print(d.pop(300,'Guest'))
print(d)
print(d.pop(500,'Guest'))

##Output:
C
{400: 'D', 200: 'E', 100: 'A', 101: 'A'}
Guest

##Example3:
d={400:'D',300:'C',200:'E',100:'A',101:'A'}
print(d.popitem())
print(d)

##Output:
(101, 'A')
{400: 'D', 300: 'C', 200: 'E', 100: 'A'}

##Example4:
d={400:'D',300:'C',200:'E'}
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d)
print(d.popitem())##Will throw error

##Output:
(200, 'E')
(300, 'C')
(400, 'D')
{}
KeyError: 'popitem(): dictionary is empty'

##Example5:
d={400:'D',300:'C',200:'E'}
d.clear()
print(d)

##Output:
{}