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
d={400:'D',300:'C',200:'E'}cdcd
d.clear()
print(d)

##Output:
{}

===========================================================================

Important functions/methods for dict : setdefault() and copy()
--------------------------------------------------------------

Syntax >> setdefault(k,v):
    -If the specified key is already available then simply returns associated value without any replacement
    -If the specified key is not already available then new key-value pair will be added

##Example1:
d={100:'A',200:'B'}
print(d.setdefault(300,'Durga'))
print(d)
print(d.setdefault(100,'Durga')) ##It returns A not Durga since key 100 is already there and has value 'A'
print(d)

##Output:
Durga
{100: 'A', 200: 'B', 300: 'Durga'}
A
{100: 'A', 200: 'B', 300: 'Durga'}

Aliasing and Cloning:
--------------------

##Example2: Aliasing concept
dict1={100:'A',200:'B'}
dict2=dict1
dict2[300]='C'
print(dict1) ##Changes made to dict2, affects dict1 as well
print(dict2)

##Output:
{100: 'A', 200: 'B', 300: 'C'}
{100: 'A', 200: 'B', 300: 'C'}

##Example3: Creating a copy()
dict1={100:'A',200:'B'}
dict2=dict1.copy()
dict2[300]='C'
print(dict1) ##Changes made to dict2, doesn't affect dict1
print(dict2)

##Output:
{100: 'A', 200: 'B'}
{100: 'A', 200: 'B', 300: 'C'}

==============================================================================

##Write a program to take dictionary from the keyboard and print sum of values??

d=eval(input('Enter Dictionary: '))
sum=0
for item in d.items():
    sum=sum+item[1] ##It creates tuples and we're extracting second index which is a value
print('The sum of values: ',sum)

##Output:
Enter Dictionary: {'A':500,'B':350}
The sum of values:  850

##Using the inbuilt sum function:
d=eval(input('Enter Dictionary: '))
print('The sum of values: ',sum(d.values()))

##Output:
Enter Dictionary: {'A':69,'B':350}
The sum of values:  419

=================================================================================

##Write a program to find number of occurrences of each letter present in the given string?

##Program skeleton structure:
input = 'AAABBC'
##Here A has occurred 3 times, B has occurred 2 times and C only once.
output = {'A':3,'B':2,'C':1}

##Actual Program:
word=input('Enter any string: ')
d={}
for char in word:
    d[char]=d.get(char,0)+1
 """   Here d[A] = d.get(A,0)+1
              =0+1
         d={'A':1}
         d[A] = d.get(A,0)+1
              =1+1
         d={'A':2}
         :
         :
         :"""
    
print(d)
for k,v in d.items():
    print(k,'Occurs',v,'times')

##Output:
Enter any string: BBBCCCDDAAA
{'B': 3, 'C': 3, 'D': 2, 'A': 3}
B Occurs 3 times
C Occurs 3 times
D Occurs 2 times
A Occurs 3 times

========================================================================

##Write a program to find number of occurrences of each vowel present in the given string:

word=input('Enter any string: ').lower()
vowels={'a','e','i','o','u'}
d={}
for char in word:
    if char in vowels:
        d[char]=d.get(char,0)+1
    else:
        print(char,'Is not a Vowel')
print(d)
for k,v in d.items():
    print(k,'Is a vowel and it occurred',v,'times')
##If sorting is required we can use below two lines:
#for k,v in sorted(d.items()):
#    print(k,'Is a vowel and it occurred',v,'times')

##Ouput:
Enter any string: VVVAAAIIIooooPPlluuuuuuuUU
v Is not a Vowel
v Is not a Vowel
v Is not a Vowel
p Is not a Vowel
p Is not a Vowel
l Is not a Vowel
l Is not a Vowel
{'a': 3, 'i': 3, 'o': 4, 'u': 9}
a Is a vowel and it occurred 3 times
i Is a vowel and it occurred 3 times
o Is a vowel and it occurred 4 times
u Is a vowel and it occurred 9 times

=============================================================================

##Write a program to accept student name and marks from the keyboard and create a dictionary. Also display student marks by taking student name as input?

##Example1:
n = int(input('Enter no of Students: '))
d = {}
for i in range(n):
    name=input('Enter Student Name: ')
    marks=int(input('Enter Student Marks: '))
    d[name]=marks
print('Student data insertion completed...')
print('*'*30)
print('NAME','\t\t','MARKS') ##\t\t is used to provide tab space
print('*'*30)
for k,v in d.items():
    print(k,'\t\t',v)
    
##Output:
Enter no of Students: 2
Enter Student Name: Sunny
Enter Student Marks: 69
Enter Student Name: Mia
Enter Student Marks: 96
Student data insertion completed...
******************************
NAME 		 MARKS
******************************
Sunny 		 69
Mia 		 96

##Example2: To implenent the search operation
n = int(input('Enter no of Students: '))
d = {}
for i in range(n):
    name=input('Enter Student Name: ')
    marks=int(input('Enter Student Marks: '))
    d[name]=marks
print('Student data insertion completed...')
print('*'*30)
print('NAME','\t\t','MARKS')
print('*'*30)
for k,v in d.items():
    print(k,'\t\t',v)
print('Search Operation Started...')
while True:
    name=input('Enter Student Name to get marks: ')
    marks=d.get(name,-1) ##if -1 is not mentioned, it will print none
    if marks==-1:
        print('Student not found')
    else:
        print('Marks of',name,'are',marks)
    option=input('Do you want to find another Student marks(yes/no): ').upper()
    if option=='NO':
        break
print('Thanks for using our application')

##Output:
Enter no of Students: 2
Enter Student Name: Shiva
Enter Student Marks: 100
Enter Student Name: Mani
Enter Student Marks: 200
Student data insertion completed..
******************************
NAME 		 MARKS
******************************
Shiva 		 100
Mani 		 200
Search Operation Started...
Enter Student Name to get marks: Mani
Marks of Mani are 200
Do you want to find another Student marks(yes/no): yEs
Enter Student Name to get marks: Shiva
Marks of Shiva are 100
Do you want to find another Student marks(yes/no): Y
Enter Student Name to get marks: Nino
Student not found
Do you want to find another Student marks(yes/no): y'
Enter Student Name to get marks: Heman'
Student not found
Do you want to find another Student marks(yes/no): N
Enter Student Name to get marks: Ji
Student not found
Do you want to find another Student marks(yes/no): nO
Thanks for using our application

========================================================================

Dict Comprehension:
-------------------
Syntax:
d={x:x*x for x in range(1,6)}
##In x:x*x >>> x=key & x*x=value

##Example1:
d={x:x*x for x in range(1,6)}
print(d)

##Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

##Example2:
d={x:2**x for x in range(1,6)}
print(d)

##Output:
{1: 2, 2: 4, 3: 8, 4: 16, 5: 32}

=============================================================================

##Merging of Collections:
-------------------------

##List Merging:
l1=[10,20]
l2=[30,40]
l3=l1+l2
print(l3)
##Alternative way to merge
l4=[*l1,*l2] ##*l1 means, all values of l1 and *l2 means, all values of l2
print(l4)

##Output:
[10, 20, 30, 40]
[10, 20, 30, 40]


##Tuple Merging:
t1=(10,20)
t2=(30,40)
t3=t1+t2
print(t3)
t4=(*t1,*t2)
print(t4)

##Output:
(10, 20, 30, 40)
(10, 20, 30, 40)


##Set Merging:
s1={10,20}
s2={30,20}
s3=s1+s2 ##TypeError
print(s3)
s4={*s1,*s2}
print(s4) ##Duplicates will be removed and order will not be maintained

##Output:
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{10, 20, 30}

##Dict Merging:
dict1={100:'A',200:'B'}
dict2={300:'C',400:'D'}
d1=dict1+dict2 ##TypeError
print(d1)
d2={**dict1,**dict2}
print(d2)

##Output:
{100: 'A', 200: 'B', 300: 'C', 400: 'D'}

##Dict Merging: Conclusion2
dict1={100:'A',200:'B'}
dict2={100:'C',400:'D'}
d2={**dict1,**dict2} ##Values of dict1 are replaced with dict2, if we give {**dict2,**dict1} then whatever in dict2 is replaced with dict1
print(d2)

##Output:
{100: 'C', 200: 'B', 400: 'D'}

=================================================================================

##Nested Collections:
---------------------
-Collections inside a collection is called Nested Collections.
-In Django and Rest API, the Nested collection is widely used.

##Example:
l1=[(10,20,30),(40,50,60)]
print(l1[0][1]) ##20
print(l1[1][2]) ##60

##Output:
20
60

##Example2:
d={'Cars':('Innova','Honda','Maruthi'),
   'Mobiles':('Samsung','Iphone','Nokia')
   } ##It's a dictionary of Tuples
##To display second car
print(d['Cars'][1]) ##We can also try d.get(key)
print(d.get('Cars')[2])
##To display Mobile names
print(d['Mobiles'][1]) ##We can also try d.get(key)
print(d.get('Mobiles')[2])
##To display all mobiles:
print(d.get('Mobiles'))
##To display in each row
for x in d['Mobiles']:
    print(x)
    
##Output:
Honda
Maruthi
Iphone
Nokia
('Samsung', 'Iphone', 'Nokia')
Samsung
Iphone
Nokia

====================================================================================
##Implementation of Supermarket by using Dict:

##Example1:
Supermarket = {
                    'store1':
                            {
                                'name' : 'Durga General Store',
                                'items': [
                                    {'name':'soap','quantity':20},
                                    {'name':'brush','quantity':30},
                                    {'name':'pen','quantity':40}
                                ] ##List
                            }, ##Dict
                    'store2':
                            {
                                'name':'Sunny Book Store',
                                'items':[
                                    {'name':'python','quantity':100},
                                    {'name':'django','quantity':200},
                                    {'name':'java','quantity':300}
                                ] ##List
                            } ##Dict
} ##Dict
print(Supermarket)
##To print name of Stores:
print('Name of the Store1:')
print(Supermarket['store1']['name'])
print(Supermarket.get('store1')['name'])
##To print names of all items present in store1:
print('To print names of all items present in store1:')
print(Supermarket['store1']['items'])
for d in Supermarket['store1']['items']:
    print(d['name'])
##To print quantity of django:
print('To print quantity of django')
print(Supermarket['store2']['items'][1]['quantity'])
for d in Supermarket['store2']['items']:
    if d['name']=='django':
        print(d['quantity'])
        
##Output:
{'store1': {'name': 'Durga General Store', 'items': [{'name': 'soap', 'quantity': 20}, {'name': 'brush', 'quantity': 30}, {'name': 'pen', 'quantity': 40}]}, 'store2': {'name': 'Sunny Book Store', 'items': [{'name': 'python', 'quantity': 100}, {'name': 'django', 'quantity': 200}, {'name': 'java', 'quantity': 300}]}}
Name of the Store1:
Durga General Store
Durga General Store
To print names of all items present in store1:
[{'name': 'soap', 'quantity': 20}, {'name': 'brush', 'quantity': 30}, {'name': 'pen', 'quantity': 40}]
soap
brush
pen
To print quantity of django
200
200

======================================================================================

##List inside Set and Dictionary:

-Set, Dict and Tuple are hashable
-Where as List is unhashable, hence we can't add list to set and also list to dict as keys
-******But in dict we can use list for values

##Example1:
set={(10,20,30)}
print(set)
set={[1,2,3]}
print(set) ##TypeError

##Output:
{(10, 20, 30)}
TypeError: unhashable type: 'list'

##Example2:
dict={(1,2):'One'}
print(dict)
dict={[1,2]:'One'}
print(dict)
dict={(2,3):['Goa','Gone']} ##We can use list for values in dict
print(dict)

##Output:
{(1, 2): 'One'}
TypeError: unhashable type: 'list'
{(2, 3): ['Goa', 'Gone']}

