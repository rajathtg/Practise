Set Datastructures:
-------------------
Group of unique objects as single entity where order is not important.
-*****Duplicates are not allowed
-*****Order is not applicable/insertion order is not preserved(because elements added to memory based on hash code, therefore we don't know in which order elements are added)
-Indexing and slicing concepts are not applicable (since no order is maintained, therefore no question of indexing/slicing)
-Objects are represented within curly braces via comma separated values
-Fyi...
    List >> []
    Tuple >> ()
    Set >> {}
    Dict >> {}
-Heterogenous objects are allowed
-It's mutable
-Mathematical operations such as union,intersection,difference can be applied

##Example1:
s={} ##*****By default empty curly braces means dict and not set, Python people gave more importance to dict because, dict is more commonly used compared to set
print(type(s))

##Output:
<class 'dict'>

##Example2:
s=set()
print(type(s))

##Output:
<class 'set'>

##Example3:
s=set()
print(type(s))
s.add(10)
s.add('Z')
s.add('A')
s.add(20)
s.add(10) ##This is not added, because duplicates are not allowed
print(s)
print(s[0]) ##TypeError: 'set' object does not support indexing
print(s[1:3]) ##TypeError: 'set' object is not subcriptable

##Output:
<class 'set'>
{'A', 10, 'Z', 20} ##Insertion Order not preserved

##Output:
<class 'set'>
{'Z', 10, 20, 'A'} ##Insertion Order not preserved

Difference between List & Set:
------------------------------
##List:
-Duplicates are allowed
-Insertion order is preserved
-Representation is through square brackets []
-Indexing and slicing concepts are applicable

##Set:
-Duplicates are not allowed
-Insertion oreder is not preserved
-Representation is through curly brackets {}
-Indexing and slicing concepts are not applicable

==============================================================================

##Creation of Set Object:
-------------------------

##Example1: To create empty Set
s={} ##This is for dict
s=s() ##This is the correct way *********

##Example2: If we already have data, then we can create it like below:
s={10,20,30,40}

##Example3: By using set function:
-Set function is used to convert the given collection/iterable objects such as list, string, range() then we can use set function.

l=[10,20,30,40,10] ##List object
s=set(l)
print(s)

##Output:
{40, 10, 20, 30}

s=set(range(0,101,10)) ##Range object
print(s)

##Output:
{0, 100, 70, 40, 10, 80, 50, 20, 90, 60, 30}

s=set('apple') ##String object
print(s)

##Output:
{'a', 'e', 'l', 'p'}

##Example4: To create through dynamic input
s=eval(input('Enter set of value: '))
print(s)

##Output:
Enter set of value: {1,'M','M',9,88,77}
{1, 'M', 88, 9, 77}

=============================================================================
##Mathematical, Equality, Relational and Membership Operators for Set:

##Example1: '+' and '*' not applicable for set
s1={10,20,30}
s2={30,40,50}
s3=s1+s2
s3=s1*3

##Output:
TypeError: unsupported operand type(s) for +: 'set' and 'set'
TypeError: unsupported operand type(s) for *: 'set' and 'int'

##Example2: '==' & '!=' operator, this is applicable
-Result will be called true, if both contains same number elements and same element and order is not important
s1={10,20,30}
s2={30,10,20}
print(s1==s2)
s1={10,20,30}
s2={30,10}
print(s1==s2)
print(s1!=s2)

##Output:
True
False
True

##Example3: Relational operators for set is applicable, but not meaningfully implemented, no need to worry about this.
s1={10,20,30}
s2={10,20,5,6,7}
print(s1<s2)
print(s1<=s2)
print(s1>s2)
print(s1>=s2)

##Output:
False
False
False
False

##Example4: Membership operators, perfectly applicable ('in' & 'not in')
s={10,20,30,40}
print(10 in s)
print(50 in s)
print(50 not in s)

##Output:
True
False
True

=============================================================================
##Important functions and methods for set:

-len() >> Returns number of elements present in set
-add() >> To add individual elements to set we use add() it is set specific method, in list we use append(), the reason behind not using append() for set is, in general append() is used to append an element at the end of the list always, but in set element can be added at any point, therefore add() is used over append().
-update() >> To add multiple items to the set, we can pass any number of arguments, but every argument passed should be iterable object (like list,string,range etc).

##Example1:
s={10,20,30,40}
print(len(s))

##Output:
4

##Example2:
s={10,20,30,40}
s.add(50)
print(s)

##Output:
{40, 10, 50, 20, 30}

##Example3:
s={10,20}
l=[30,40]
s.update(l)
print(s)
s.update(range(1,6),'Durga')
print(s)

##Output:
{40, 10, 20, 30}
{'a', 1, 2, 3, 4, 5, 'D', 40, 10, 'g', 20, 'u', 30, 'r'}

Difference between add and update:
----------------------------------
-add():
    -We can use add() method to add individual item to the set.
    -add() method can take only one argument
    
-update():
    -We can use update() method to add multiple items to the set
    -This can take any number of arguments, but all arguments should be iterable objects
    
##Example4: Which of the following are valid?
s=set()
s.add(10)
print(s)
s.add(10,20,30) ##Error, only 1 argument allowed
print(s)
s.update(10) ##Error, int value not allowed, not iterable
print(s)
s.update(range(1,10,2),range(0,10,2))
print(s)

##Output:
{10}
TypeError: set.add() takes exactly one argument (3 given)
TypeError: 'int' object is not iterable
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

============================================================================
##Methods to remove elements from set:
-remove() >> Syntax : s.remove(x) ##if x is not available then we will get key error
-discard() >> Syntax : s.discard(x) ##if x is not available then it will not throw any error, just discard and move on
-pop() >> Syntax : s.pop() ##to remove any one random elemnt, no control on what will be removed and returns remaining elements
-clear() >> Syntax : s.clear() ##to remove all elements from set

##Example1:
s={10,20,30,40}
s.remove(30)
print(s)
s.remove(50) ##Key error
print(s)

##Output:
{40, 10, 20}
KeyError: 50

##Example2:
s={10,20,30,40}
s.discard(30)
print(s)
s.discard(50) ##No Error is thrown
print(s)

##Output:
{40, 10, 20}
{40, 10, 20}

##Example3:
s={10,20,30,40}
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop()) ##Error, because set is empty
print(s)

##Output:
40
{10, 20, 30}
10
{20, 30}
20
{30}
30
set()
KeyError: 'pop from an empty set'

##Example4:
s={10,20,30,40}
print(s)
s.clear()
print(s)

##Output:
{40, 10, 20, 30}
set()

==============================================================================
##Set specific methods for mathematical operations:

-union() >> To combine elements from two set and return all elements present inside s1 and s2 (sorry boss, duplicates are not allowed)
-intersection >> To combine and return common elements between s1 and s2
-difference() >> To remove elements present in s1 but not in s2
-symmetric_difference() >> It's double of difference() i.e. To remove elements present in s1 but not in s2 and also to remove elements present in s2 but not in s1

##Example1:
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.union(s2) ##s3 = s1|s2 also works the same way
print(s3)

##Output:
{40, 10, 50, 20, 60, 30}

##Example2:
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.intersection(s2) ##s3=s1&s2 also works the same way
print(s3)

##Output:
{40, 30}

##Example3:
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.difference(s2) ##s3=s1-s2 also works the same way
s4=s2.difference(s1) ##s4=s2-s1 also works the same way
print(s3)
print(s4)

##Output:
{10, 20}
{50, 60}

##Example4:
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.symmetric_difference(s2) ##s3=s1^s2 also works the same way
print(s3)

##Output:
{10, 50, 20, 60}

===========================================================================
##Aliasing, Cloning and Comprehension of Set:
---------------------------------------------
-Aliasing : 
    -The process of creating duplicate reference variable is called aliasing
    -But disadvantage is, if changes done to s1 will impact s2.
Cloning:
    -The process of creating a separate new object similar to existing object, were the changes done to s1 won't impact s2 is called cloning

##Example1:
s1={10,20,30}
s2=s1 ##Aliasing
s2.add(50)
print(s1)
print(s2)

##Output:
{10, 20, 50, 30}
{10, 20, 50, 30}


##Example2:
s1={10,20,30}
s2=s1.copy() ##Cloning
s2.add(50)
print(s1)
print(s2)

##Output:
{10, 20, 30}
{10, 20, 50, 30}

Set Comprehension:
------------------
-For set comprehension concept is applicable.

##Example1:
s={x*x for x in range(1,6)}
print(s)
print(type(s))

##Output:
{1, 4, 9, 16, 25}
<class 'set'>

##Example2:
s={2**x for x in range(1,6)}
print(s)
print(type(s))

##Output:
{32, 2, 4, 8, 16}
<class 'set'>

============================================================================
##Practise program for Set:
---------------------------
##Write a program to eliminate duplicates present in the List?

##Approach1: By using set
l=[10,10,20,30,10,20,30]
s=set(l) ##Duplicates are removed
print(s)
l1=list(s) ##Converting back to list
print(l1)

##Output:
{10, 20, 30}
[10, 20, 30]

##Approach2: Without using set
l=[10,10,20,30,10,20,30]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

##Output:
[10, 20, 30]

##Write a program to print different vowels present in the given word?

##Approach1:
word = input('Enter any word to search for vowels: ').lower()
s=set(word)
print(s)
v={'a','e','i','o','u'}
result=s&v ##intersection method
print(result)
print(sorted(result)) ##Result is sorted, but datatype list

##Output:
Enter any word to search for vowels: mAngo pple pine Under
{' ', 'u', 'o', 'p', 'i', 'n', 'a', 'l', 'e', 'r', 'm', 'd', 'g'}
{'u', 'i', 'a', 'e', 'o'}
['a', 'e', 'i', 'o', 'u']
{'u', 'o', 'e'}