Python Tuples:
--------------
Features of Tuples:
    -Order is preserved/applicable
    -Duplicates are allowed
    -Heterogenous objects are allowed
    -Indexing (+ve and -ve) & Slicing concept are applicable
    -Not mutable/immutable ##List is mutable
    -Using Parentesis we can represent tuple elements ##List use []
    -Here parenthesis are optional ##[] mandatory for list
    
##Example1:
t=10,'Durga',20,10
t1=(10,'Durga',20.10)
print(t)
print(t1)
print(type(t))
print(type(t1))
print(t[0])
print(t[-1])
t[2]=777 ##It will throw error, tuple is immutable
print(t)


##Output:
(10, 'Durga', 20, 10)
(10, 'Durga', 20.1)
<class 'tuple'>
<class 'tuple'>
10
10
TypeError: 'tuple' object does not support item assignment

##Example2:
t1=(10,20,30)
t2=(10,20)
t3=(10) ##Not single valued tuple, instead it's a int, please be careful
t4=(10,) ##Yay!!, so end it with a ','
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

##Output:
<class 'tuple'>
<class 'tuple'>
<class 'int'>
<class 'tuple'>

##Example3:
t1=() ##Empty tuple and it's valid
t2=(10)
t3=10
t4=(10,)
t5=(10,20,30)
t6=10,20,30
t7=(10,20,30,)
t8=10,20,30,
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(type(t5))
print(type(t6))
print(type(t7))
print(type(t8))

##Output:
<class 'tuple'>
<class 'int'>
<class 'int'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>

===========================================================================
##Creation of Tuple Object:
---------------------------
-Empty Tuple: 
    t1=()
-Single Valued Tuple: 
    t4=(10,)
    t4=10,
-Multi valued Tuple: 
    t5=(10,20,30)
    t6=10,20,30
    t7=(10,20,30,)
    t8=10,20,30,
-By using tuple function: Using this we can convert any sequence as tuple.
    t=tuple(sequence)
-With Dynamic input:
    t=eval(input('Enter tuple of values')) ##Use eval to convert to tuple, since input() by default returns string value

##Example1:
l=[10,20,30]
print(type(l))
t=tuple(l)
print(t)
print(type(t))

##Output:
<class 'list'>
(10, 20, 30)
<class 'tuple'>

##Example2:
t=tuple(range(1,11,2))
print(t)
print(type(t))

##Output:
(1, 3, 5, 7, 9)
<class 'tuple'>

##Example4:
t=tuple('Durga')
print(t)
print(type(t))

##Output:
('D', 'u', 'r', 'g', 'a')
<class 'tuple'>
<class 'tuple'>

##Example 5:
t=input('Enter Tuple of Value: ')
print(t)
print(type(t))
s=eval(t)
print(s)
print(type(s))

##Output:
Enter Tuple of Value: 10,20,30,40
10,20,30,40
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>

=============================================================================
Accessing elements of Tuple:
----------------------------
-Using Index
-Using Slice operator
    -Syntax: tuple[begin:end:step]
    -Step value can be either +ve or -ve
    -If step value is +ve then we have to consider forward direction (from left to right) from begin index to end-1 index.
    -If step value is -ve, then we have to consider backward direction (from right to left) from begin index to end+1 index
    -In  forward direction if end value is 0 then result is always empty
    -In backward direction if end value is -1 then result is always empty
    -Either forward / backward direection, we can take both +ve and -ve values for begin and end index.
        -In forward direction:
            default value for begin : 0
            default value for end : len(tuple)
        -In backward direction:
            default value for begin: -1
            default value for end: -(len(tuple)+1)

##Example1:
t=(10,20,30,40,50,60)
print(t[0])
print(t[-1])
print(t[100]) ##Index Error

##Output:
10
60
IndexError: tuple index out of range

##Example2:
t=(10,20,30,40,50,60,70,80)
print(t[2:5])
print(t[::2])

##Output:
(30, 40, 50)
(10, 30, 50, 70)

===========================================================================
Mathematical Operators for Tuple:
---------------------------------
-Concatenation operator (+) : Both object should be tuple
-Repeatation Operator (*) : One object should be tuple and other one int

##Example 1:
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
print(type(t3))
t4=t3+10 ##Error, concatenation should happen between tuple & tuple
t5=t1+[10,20] ##Error, concatenation should happen between tuple & tuple
##Output:
(10, 20, 30, 40, 50, 60)
<class 'tuple'>
TypeError: can only concatenate tuple (not "int") to tuple
TypeError: can only concatenate tuple (not "list") to tuple

##Example 2:
t1=(10,20,30)
t2= t1 * 3
print(t2)
print(type(t2))

##Output:
(10, 20, 30, 10, 20, 30, 10, 20, 30)
<class 'tuple'>

##Example 3:
t1=(10,20)
t2=(30,40)
t3=t1+t2
print(t3)
t4=t3*3
print(t4)

##Output:
(10, 20, 30, 40)
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)

===========================================================================
Equality Operators for tuple: ('==' and '!=')
-----------------------------------------
== and !=
 -No of elements must be same
 -Order of elements must be same
 -Content of elements must be same

##Example1:
t1=('Cat','Rat','Dog')
t2=('Cat','Rat','Dog')
t3=('CAT','RAT','DOG')
t4=('Rat','Dog','Cat')
print(t1==t2)
print(t1==t3)
print(t1==t4)

##Output:
True
False
False

Relational Operators: ('<','<=','>','>='):
----------------------------------

##Example2:
t1=(10,20,30)
t2=(30,15,40)
print(t1<t2)
print(t1>t2)

##Output:
True
False

##Example3:
t1=(10,20,30)
t2=(10,5,70)
print(t1<t2)
print(t1>t2)

##Output:
False
True

##Example4:
t1=(10,20,30)
t2=(10,20,30,40,50)
print(t1<t2)
print(t1>t2)

##Output:
True
False

Membership Operators: ('in' and 'not in'):
------------------------------------------
##Example5:
t=(10,20,30,40)
print(10 in t)
print(50 not in t)
print(60 in t)

##Output:
True
True
False

===========================================================================
Important methods/functions for tuple:
--------------------------------------
-len() : Returns the number elements present inside tuple
-count() : Returns no of occurrences of specified elements
-index() : Returns index of first occurrence of specified element.
##Example1:
t=(10,20,30,40)
print(len(t))
##Output:
4

##Example2:
t=(1,2,3,2,3,4,4)
print(t.count(4))
print(t.count(2))
print(t.count(1))
##Output:
2
2
1

##Example3:
t=(1,2,3,2,3,4,4)
print(t.index(2))
print(t.index(3))
print(t.count(40)) ##Error
##Output:
1
2
ValueError: tuple.index(x): x not in tuple

============================================================================
Reversing of elements of tuple:
-------------------------------
-Similar to 'list.reverse()' we can not use 'tuple.reverse()' here, since tuple is immutable.
-We can use reversed() (python inbuilt function) instead.

##Example1:
t=(10,20,30,40)
r=reversed(t)
t1=tuple(r)
print(t)
print(t1)

##Output:
(10, 20, 30, 40)
(40, 30, 20, 10)

Sorting of elements of tuple:
-----------------------------
-Similar to 'list.sort()' we can not use 'tuple.sort()' here, since tuple is immutable.
-We can use sorted() (python inbuilt function) instead.

##Example1:
t=(40, 30, 20, 10)
r=sorted(t)
t1=tuple(r)
print(t)
print(t1)

##Output:
(40, 30, 20, 10)
(10, 20, 30, 40)

##Example2:
t=(40, 50, 20, 10)
r=sorted(t,reverse=True)
t1=tuple(r)
print(t)
print(t1)

##Output:
(40, 50, 20, 10)
(50, 40, 20, 10)

======================================================================
max() and min() functions for Tuple:
------------------------------------
##Example3:
t=(40, 50, 20, 10)
print(max(t))
print(min(t))

##Output:
50
10

##*****Note: Below functions are not supported in Tuples, because below manipulate the content of tuples, but it will not allow to do it since tuple is immutable.
append()
extend()
insert()
remove()
pop()
clear()

========================================================================
##Tuple packing and unpacking:
------------------------------
##Example1:
a=10
b=20
c=30
d=40
t=a,b,c,d ##This is Tuple packing
print(t)
l=[a,b,c,d] ##This is list packing
print(l)

##Output:
(10, 20, 30, 40)
[10, 20, 30, 40]

##Example2:
t=10,20,30,40
a,b,c,d=t ##Tuple Unpacking
print(a,b,c,d)
print(type(a))

##Output:
10 20 30 40
<class 'int'>

##Example2:
t=10,20,30,40
a,b,c=t ##Tuple Unpacking error
a,b,c,d,e=t ##Tuple Unpacking error
a,*b=t ##Here *b means variable lenght arguments
print(t)
print(a)
print(type(a))
print(b)
print(type(b))

##Output:
ValueError: too many values to unpack (expected 3)
ValueError: not enough values to unpack (expected 5, got 4)
(10, 20, 30, 40)
10
<class 'int'>
[20, 30, 40]
<class 'list'>

==========================================================================
Tuple Comprehension:
--------------------
-Comprehension is not valid for tuple, though it would not throw any error during comprehension, but output data type is not tuple, instead it's a generator.

##Example:
t=(x*x for x in range(1,6))
print(type(t))
print(t)

##Output:
<class 'generator'>
<generator object <genexpr> at 0x0000022407B26260>

=======================================================================
********Differences between List and Tuple:
-----------------------------------
List:
    -List is a group of comma separated values within square brackets and square brackets are mandatory
    -List objects are mutable i.e. once we create list objects, we are allowed to change its content
    -List consumes more memory space, as the list content not fixed can increase / decrease due mutabilty
    ex: l=[1,2,3,4]
    -If content is more frequently changing like add,delete..ex: facebook/youtube comments go for list
    -Comprehension concept is applicable for list
    -Accessing list elements takes time, therefore performance is low
    -List is unhashable type, hence, we can't add/store list inside set and inside dict as keys

Tuple:
    -Tuple is a group of comma separated values within parenthesis and parenthesis are optional
    -Tuple objects are immutable i.e. once we create tuple object, we are not allowed to change it's content.
    -where as tuple consumes less memory for the same content of list, because the content is fixed due to immutablity
     ex: l=(1,2,3,4)
    -If content is constant and no add,delete is allowed..ex: cola/ticket vending machine go for tuple
    -Comprehension concept is not applicable for tuple, because if we try to apply we won't get tuple object and instead we will get a generator object
    -Tuple elements can be accessed quicker, hence performance is faster
    -Tuple is hashable, hence, we can add/store tuple inside set and inside dict as keys

##Example1:
import collections ##This is deprecated from python3.8 onwards, you might see an error while executing, just go with output given below.
l=[10,20,30]
t=(10,20,30)
print(isinstance(l,collections.Hashable))
print(isinstance(t,collections.Hashable))
print(hash(l))
print(hash(t))

##Output:
False
True
TypeError: unhashable type: 'list'
3952409569436607343

##Example2:
s={10,20}
l=[10,20,30]
t=(10,20,30)
s.add(t)
print(s)
s.add(l)

##Output:
{10, 20, (10, 20, 30)}
TypeError: unhashable type: 'list'

##Example3:
d={}
l=[10,20,30]
t=(10,20,30)
d[t]='A' ##t is tuple object as a key and value is string 'A'
print(d)
d[l]='B' ##Will throw error, list is unhashable

##Output:
{(10, 20, 30): 'A'}
TypeError: unhashable type: 'list'

Set:
    -Duplicates are not allowed and order is not preserved
    ##ex: s={10,20,30}
          s.add(5)
          print(s) ##Output {10, 20, 5, 30}
    ##As we can see, 5 is added anywhere randomly, order is not applicable
    -It stores data in the memory through hashing, i.e. each element has an hashcode, so it helps in faster retrieval/search of data.
    -Linear search / binary search algorithm.
        -Consider there are 100 students and all sat next to eavh other.
        -Linear search will work like, one by one it will search until it finds required person, if 100th student are there 100 comparison is required, time complexity for linear search is order(n)
        -Linear search is proportional to number of students.
        -Where as binary search is like it divides 100 students to 50 and checks the element is greater than middle elemnt or less than that, post that half of the 50 will be ignored, next again it will divide the remaining 50 to 25 and 25 and it goes on.
        -Therefore binary search is pretty faster and time complexity is order(log(n) to the base 2)
    -The till date the most powerful searching algorithm is the hash based algorithm, it directly goes to that hashed element and retrieves the data, it is best search ever, time complexity is order(1), i.e. just one comparison.
    -Therefore set is best option to store data, if data is something oftenly  retrieved / searched.
Dict:
    -This is also based on hashcode, but hascode used here is of keys.

###**Note: The keys present in the dict should be hashable, similarly objects present in the set should be hashable, if not we can't use or store them as a set/dict.
    
==============================================================================
##Program to take a tuple of numbers from the keyboard and print its sum and average:
t=eval(input('Enter tuple of numbers: '))
sum=0
for x in t:
    sum+=x
print('The Sum: ',sum)
print('The average: ',sum/len(t))

##Output:
Enter tuple of numbers: 10,20,30,40,50
The Sum:  150
The average:  30.0
    
##ShortCode:
t=eval(input('Enter tuple of numbers: '))
print(sum(t)) ##sum is Python function and also applicable for list and other DS as well.
print(sum(t)/len(t))

##Output:
Enter tuple of numbers: 10,20,30,40,50,60
210
35.0
