Python-List:
-----------
x=10
y=10.5
z= I want both int and float inside one, we can opt for List Yay!!
To represent a group objects as a single entity, then we need to go for collection datatypes, below are the ones...
    -List
    -Tuple
    -Set
    -Dict

List:
=====
-I want to represent a group objects as a single entity provided,
    -Duplicates are allowed
    -Order of insertion is maintained/preserved
    -Heterogenous objects are allowed
    -Dynamic (based on req we can add and remove elements)
    -Index play imp role, using index we can preserve insertion order and also get to know duplicates
    -List is mutable (add,replace and remove Yay!)
    -[] representation means, it is list

##Example1:
----------
l=[]
l.append(10)
l.append('Durga')
l.append(10)
print(l)

##Output:
[10, 'Durga', 10] ###Duplicates are allowed and order preserved.

##Example2:
----------
l=[10,'Durga',10]
l[0]=77
print(l)

##Output:
---------
[77, 'Durga', 10] ##List is mutable

Creation of List Object:
------------------------
##Example3 : Empty list object
l=[]
print(type(l))

##Output:
<class 'list'>

##Example4 : If we know objects / data already then how to create list?? just elements with comma separated.
l=[10,20,30,40]

##Example5: Request end user to enter list.
l=input('Enter List : ')
print(type(l))
l1=eval(input('Enter List : '))
print(type(l1))
l2=eval(input('Enter List : '))
print(type(l2))
l3=list(input('Enter List : '))
print(type(l3))

##Output:
Enter List : 1,2,4,5
<class 'str'>
Enter List : 1,2,4,5
<class 'tuple'>
Enter List : [1,2,3,4] ##*****The way input is provided matters
<class 'list'>
Enter List : 1,2,3,4
<class 'list'>

##Example5: By using list() function can be used string to list, tuple to list etc:
l=list('durga')
print(l)
print(type(l))

##Output:
['d', 'u', 'r', 'g', 'a']
<class 'list'>

##Example6:
l=list(range(0,10,2))
print(l)
print(type(l))

##Output:
[0, 2, 4, 6, 8]
<class 'list'>

##Example7: By using split() also we can create list object, but applicable only for strings....
s='Learning Python is easy'
l=s.split()
print(l)
print(type(l))

##Output:
['Learning', 'Python', 'is', 'easy']
<class 'list'>

=============================================================================

Accessing elements of list:
---------------------------
There are two ways:
    -Index
    -By using slice operator

-4  -3  -2  -1    
10  20  30  40
0   1   2   3

##Example1: Using Index
l=[10,20,30,40]
print(l[0])
print(l[-2])
print(l[100])

##Output:
10
20
IndexError: list index out of range

##Example2: Using slice
Syntax : l[begin:end:step]
        -Begin/end index can also be +ve and -ve value
        -Step value can be a +ve/-ve value
        -If +ve Step value >> Forward direction (left to right) >> begin to end-1
        -If -ve Step value >> Backward direction(right to left) >> begin to end+1
        -In forward direction if end value is 0 then result is always empty
        -In backward direction if end value is -1 then result is always empty
        -In forward direction:
            Default value for begin is 0
            Default value for end is len(list)
        -In backward direction:
            Default value for begin is -1
            Default value for end is -(len(list)+1)
        
l=[10,20,30,40,50,60,70,80,90,100]

#-10    -9      -8      -7      -6      -5      -4      -3      -2      -1
#10     20      30      40      50      60      70      80      90      100
#0      1       2       3       4       5       6       7       8       9

print(l[2:7]) ##30,40,50,60,70
print(l[2:7:2]) ##30,50,70
print(l[4::2]) ##50,70,90
print(l[8:2:-2]) ##90,70,50
print(l[4:100]) ##50,60,70,80,90,100
print(l[4:0:2]) ##[]
print(l[::1]) ##10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(l[::-1]) ##100, 90, 80, 70, 60, 50, 40, 30, 20, 10

##Output:
[30, 40, 50, 60, 70]
[30, 50, 70]
[50, 70, 90]
[90, 70, 50]
[50, 60, 70, 80, 90, 100]
[]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

=============================================================================

Traversing elements of list:
----------------------------

##Example1:
l=[0,1,2,3,4,5,6,7,8,9,10]
i=0
##To print elements of l using while
print('While loop output')
while i < len(l):
    print(l[i])
    i+=1
##To print elements of l using for loop
print('For loop output')
for x in l:
    print(x)
##To print only even numbers
print('For loop even number output')
for x in l:
    if x%2==0:
        print(x)

##Output:
While loop output
0
1
2
3
4
5
6
7
8
9
10
For loop output
0
1
2
3
4
5
6
7
8
9
10
For loop even number output
0
2
4
6
8
10

##Example2: To print elements of list index wise:

#-6     -5      -4      -3      -2      -1
#10     20      30      40      50      60
# 0      1       2       3       4       5
##************To generate -ve index, it is nothing but
-ve index = +ve index-len(l)

##Example2:
l=[10,20,30,40,50,60]
i=0
while i<len(l):
    print('The element present at +ve index : {} and -ve index : {} is : {}'
          .format(i,(i-len(l)),l[i]))
    i+=1

##Output:
The element present at +ve index : 0 and -ve index : -6 is : 10
The element present at +ve index : 1 and -ve index : -5 is : 20
The element present at +ve index : 2 and -ve index : -4 is : 30
The element present at +ve index : 3 and -ve index : -3 is : 40
The element present at +ve index : 4 and -ve index : -2 is : 50
The element present at +ve index : 5 and -ve index : -1 is : 60

=============================================================================

Mathematical Operators for list:
-------------------------------
-Concatenation Operator(+) >> Syntax : list + list
-Repeatation Operator(*) >> Syntax : list * int

##Example1:
l1=[10,20,30]
l2=[40,50,60]
print(l1+l2)

##Output:
[10, 20, 30, 40, 50, 60]

##Example2:
l1=[10,20,30]
l2=l1+40 ##40 is int, will throw error
print(l2)
l3=l1+[40] ##converting int to list
print(l3) 
l4=l1+(40,50,60) ##Tuple not accepted
print(l4)

##Output:
TypeError: can only concatenate list (not "int") to list
[10, 20, 30, 40]
TypeError: can only concatenate list (not "tuple") to list

******Note: Compulsory both elements should be list only.

##Example3: Using repeatation operator
Syntax >> list * int
l1=[10,20]
l2=l1*2
print(l2)
l3=l1*2.0
print(l3)
l4=l1*l1
print(l4)

##Output:
[10, 20, 10, 20]
TypeError: can't multiply sequence by non-int of type 'float'
TypeError: can't multiply sequence by non-int of type 'list'

##Example4:
l1=[10,20]
l2=[30,40]
l3=l1+l2
print(type(l3))
l4=l3*3
print(type(l4))
print(l3)
print(l4+l3)
print(l4)

##Output:
<class 'list'>
<class 'list'>
[10, 20, 30, 40]
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]

==========================================================================

Equality, Relational and Membership Operators for List:
-------------------------------------------------------
Equality : == and !=
Relational : < , <= , > , >=

##Example1:
l1=['Dog','Cat','Rat']
l2=['Dog','Cat','Rat']
l3=['DOG','CAT','RAT']
l4=['Cat','Rat','Dog']
print(l1==l2)
print(l1==l3)
print(l1==l4)
print(l1!=l4)

##Output:
True
False
False
True

Rules for '==':
-Will return 'True'
    -The number of elements must be same
    -The order of elements must be same
    -The content must be same including case 

##Example2:
l1=[10,20,30,40]
l2=[50,60]
print(l1<l2) ##At first element level comparison is done 10<50 therefore it is True
print(l1<=l2) ##10<50, it's True
print(l1>l2) ##10>50, it's False
print(l1>=l2) ##10>=50, it's False

##Here the relational operators is applied for content only and not on the number of elements.
##Element to element comparison will happen
##If first elements are same, then it goes for 2nd element

##Output:
True
True
False
False

##Example3:
l1=[10,20,30]
l2=[10,20,6] ## Here element to element comparison will happen and l2 will be smaller due to 6, becuase 30>6
print(l1<l2)
print(l1<=l2)
print(l1>l2) 
print(l1>=l2)

##Output:
False
False
True
True

##Example4:
l1=[10,20,30]
l2=[10,20,30,40,50,60]
print(l1<l2)
print(l1<=l2)
print(l1>l2) 
print(l1>=l2)

##Output:
True
True
False
False

##Example5:
l1=['Ramba','Ramya'] ##Here element to element comparison will happen R & R is same, but o>a therefore l1 is smaller
l2=['Roja','Sunny']
print(l1<l2)
print(l1<=l2)
print(l1>l2)
print(l1>=l2)

##Output:
True
True
False
False

Membership Operators:
---------------------
##Example1:
l1=[10,20,30,40,50,60]
print(10 in l1)
print(100 not in l1)

##Output:
True
True

=============================================================================

##Important Methods and Functions for List: len(),count() and index():
-len() >> Returns number of elements present in the list
-count() >> Returns the number of occurrences of specified element present in the list
-index() >> Returns index of the first occurrence of the specified item

***********Note: There are two types of methods/functions, Python inbuilt function (Syntax >> function(object)) and object specific function/method (Syntax >> object.function()):

ex: 
p=[10,20,30,40]
-len(p) ##Python inbuilt and can be used on list, string etc.
-sorted(p) ##Python inbuilt
-p.append(10) ##Object specific function can only be applied on list.

##Example1:
l=[10,20,10,20,30,20,40]
print(len(l)) ##Python inbuilt
print(l.count(10))

##Output:
7
2

##Example2:
l=[1,2,1,2,3,4]
print(l.index(1))
print(l.index(2))
print(l.index(5))
##Output:
0
1
ValueError: 5 is not in list

##Example3: Please use index method after checking elements availability through membership operator 'in' as seen below:
l=[1,2,2,2,3,3]
x=int(input('Enter element to find: '))
if x in l:
    print('{} present at index: {}'.format(x,l.index(x)))
else:
    print(x,'not available in list')
    
##Output:
Enter element to find: 5
5 not available in list

======================================================================

##Important Methods and Functions for List: append() & insert():
-append() : Used to add elements at the end of the list
-insert() : To add element at specified position ##s.insert(index,element)

##Example1:
l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)

##Output:
[10, 20, 30]

##Example2: Add numbers from [1 to 100] to the list which are divisible by 10:
l=[]
for x in range(1,101):
    if x%10 == 0:
        l.append(x)
print(l)

##Output:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

##Example3:
l=[10,20,30,40]
l.insert(1,777)
print(l)

##Output:
[10, 777, 20, 30, 40]

##Example4:
l=[10,20,30,40]
l.insert(100,777) ##If specified index is greater than max index, the element will be added at the end automatically
l.insert(-100,9999) ##If specified index is smaller than min index, the element will be added at the beginning automatically
print(l)


##Output:
[9999, 10, 20, 30, 40, 777]

=======================================================================
##Important Methods and Functions for List: extend():
-extend() : To add all elements of given sequence to the list
syntax : s1.extend(s2) ##All elements present inside s2 will be added to s1

##Example1:
order1 = ['Chicken','Mutton','Fish']
order2 = ['KF','KO','RC']
order1.extend(order2)
print(order1)

##Output:
['Chicken', 'Mutton', 'Fish', 'KF', 'KO', 'RC']

##Example2:
l1=[10,20,30]
l2=[40,50]
l1.append(l2) ##Append is used to add one object at end, here the total l2 is treated as one object only.
print(l1)
print(len(l1))

##output:
[10, 20, 30, [40, 50]] ##It ends up being a nested list
4 ##Entire l2 is considered as one object only

##Example3:
l1=[10,20,30]
l2=[40,50]
l1.extend(l2)
print(l1)
print(len(l1))

##Output:
[10, 20, 30, 40, 50]
5

##Example4:
l1=[10,20,10]
l1.append('ABC')
print(l1)
print(len(l1))

##Output:
[10, 20, 10, 'ABC']
4

##Example5:
l1=[10,20,10]
l1.extend('ABC')
print(l1)
print(len(l1))

##Output:
[10, 20, 10, 'A', 'B', 'C']
6

=====================================================================
##Important Methods and Functions for List: remove():
-Syntax : s.remove() >> Used to remove specified element from the list.
-Multiple loops are available,
    -If the specified elements are present multiple times, only the first occrrence will be removed.
    -If the specified element is not available we will get value error.

##Example1:
l=[10,20,10,20,40]
l.remove(40)
print(l)
l.remove(10) ##Only first occrrence is removed
print(l)
l.remove(50)
print(l) ##Value error is thrown

##Output:
[10, 20, 10, 20]
[20, 10, 20]
ValueError: list.remove(x): x not in list

##Example2: To avoid error, use below approach
l=[1,2,3,4,5,6]
print('Before Removal: ',l)
x=int(input('Enter element to remove: '))
if x in l:
    l.remove(x)
    print('After removal: ',l)
else:
    print(x,'Not present in list')

##Output:
Before Removal:  [1, 2, 3, 4, 5, 6]
Enter element to remove: 50
50 Not present in list

##Example3: How to remove all occurrences??
l=[1,1,1,1,2,2,2,3,3]
x=int(input('Enter element to remove: '))
while True:
    if x in l:
        l.remove(x)
    else:
        break
print('After Removal: ',l)

##Output:
Enter element to remove: 2
After Removal:  [1, 1, 1, 1, 3, 3]

=========================================================================
Manipulating elements of list:
-----------------------------
-Syntax : s.pop() ##No need to pass any argument, by default it removes last element in the list and prints it.
    -Not to use pop() method on empty list, it will throw error.

##Example:
l=[10,20,30]
print('Before pop: ',l)
l.pop()
print('After pop: ',l)
l1=[]
print(l1.pop())

##Output:
Before pop:  [10, 20, 30]
After pop:  [10, 20]
IndexError: pop from empty list

##Example2:
l1=[]
if len(l1)!=0:
    print(l1.pop())
else:
    print('No elements to remove')
    
##Output:
No elements to remove

##Example3:
l=[10,20,30,40]
print(l.pop(1))
print(l)
print(l.pop(9))

##Output:
20
[10, 30, 40]
IndexError: pop index out of range

##Differences between remove() & pop() methods:
-remove()
    -l.remove() : To remove specified element
    -If the list is empty then we will get ValueError
    -The return value is None and not get ValueError (##i.e.print(remove(n)) is none)
    
-pop()
    -l.pop() : To remove & return last element
    -l.pop(index) : To remove & return element present at specified index
    -If the list is empty, then we will get IndexError
    -It returns removed element (##i.e.print(remove(n)) is value at nth place)
    

##Syntax : s.clear() ##Used to clear all elements present in the list
##Example1:
l=[10,20,30,40]
print('Before Clear: ',l)
l.clear()
print('After Clear: ',l)

##Output:
Before Clear:  [10, 20, 30, 40]
After Clear:  []

Summary:
--------
-remove() >> To remove specified element from the list
-pop() >> To remove and return last element from the list
-pop(index) >> To remove and return element present at specified index from the list
-clear() >> To remove all elements from the list
-List is dynamic and mutable:
    -To increase size/to add elements : append(),insert(),extend()
    -To decrease size/to remove elements : remove(),pop(),clear()
    
============================================================================
Ordering Elements of List : reverse() and reversed()
----------------------------------------------------
-Syntax : s.reverse() ##This is list specific function, doesn't create any new object
-Syntax : reversed(s) ##This is python function and can be applied for string, tuple, list etc and creates a new iterator object called as reversed iterator object.

##Example1:
l=[10,20,30,40]
print('Before using reverse',l)
print(type(l))
l.reverse() ##Applicable only for list
print('After using reverse',l)
print(type(l))

##Output:
Before using reverse [10, 20, 30, 40]
<class 'list'>
After using reverse [40, 30, 20, 10]
<class 'list'>

##Example2:
l=[10,20,30,40]
print('Before using reverse',l)
print(type(l))
r=reversed(l) ##Applicable for list,string,tuple etc...
print('After using reverse',l)
print(type(l))
print('Reversed iterator Object',r)
print('Reversed iterator Object',list(r))
print(type(r))

##Output:
Before using reverse [10, 20, 30, 40]
<class 'list'>
After using reverse [10, 20, 30, 40]
<class 'list'>
Reversed iterator Object <list_reverseiterator object at 0x0000024845B51570>
Reversed iterator Object [40, 30, 20, 10]
<class 'list_reverseiterator'>

##Example3:
s='Durga'
r=reversed(s)
for x in r:
    print(x,end=' ')
    
##Output:
a g r u D 

============================================================================

Ordering elements of list:
--------------------------
-Sorting elements of list:
Syntax : s.sort()
##***Note: If we want to use sort() method, all elements should be of same type / homogenous in a list, don't mix int and strings.
Default/natural sorting order:
    number >> Ascending Order
    String >> Alphabetical order

##Example1:
l=[20,5,15,0,10]
l1=['Cat','Dog','Bat','Apple']
print('Before Sorting: ',l)
print('Before Sorting: ',l1)
l.sort()
l1.sort()
print('After Sorting: ',l)
print('After Sorting: ',l1)


##Output:
Before Sorting:  [20, 5, 15, 0, 10]
Before Sorting:  ['Cat', 'Dog', 'Bat', 'Apple']
After Sorting:  [0, 5, 10, 15, 20]
After Sorting:  ['Apple', 'Bat', 'Cat', 'Dog']

##Example2: To create descending sorting order:
l=[20,5,15,0,10]
l1=['Cat','Dog','Bat','Apple']
print('Before Sorting: ',l)
print('Before Sorting: ',l1)
l.sort(reverse=True) ##Default it is false i.e. ascending
l1.sort(reverse=True) ##Default it is false i.e. ascending
print('After Sorting: ',l)
print('After Sorting: ',l1)

##Output:
Before Sorting:  [20, 5, 15, 0, 10]
Before Sorting:  ['Cat', 'Dog', 'Bat', 'Apple']
After Sorting:  [20, 15, 10, 5, 0]
After Sorting:  ['Dog', 'Cat', 'Bat', 'Apple']

##Example3: Heterogenous:
l=[20,5,15,'B','A']
print('Before Sorting: ',l)
l.sort(reverse=True)
print('After Sorting: ',l)

##Output:
TypeError: '<' not supported between instances of 'int' and 'str'

s.sort():
-List specific method
-No new list object is created, existing list object order will be changed

sorted(s):
-Python Function
-A new list object will be created

##Example 4:
l=[20,5,15,25,10]
print('Before Sorting: ',l)
l1=sorted(l)
print('After Sorting: ',l)
print('After Sorting: ',l1)

##Output:
Before Sorting:  [20, 5, 15, 25, 10]
After Sorting:  [20, 5, 15, 25, 10]
After Sorting:  [5, 10, 15, 20, 25]

===========================================================================
Aliasing and Cloning of list object:
------------------------------------
-Aliasing : 
    -The process of creating duplicate reference variable is called aliasing
    -The change made using one reference variable will automatically impact the other/aliased reference variable as well
-Cloning : 
    -To overcome the shortcomings of aliasing we go for cloning, .i.e instead of creating duplicate reference variable, let's create a complete diferent duplicate list object.

##Example1:
l1=[10,20,30,40]
l2=l1 ##Creation of duplicate reference variable
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print(l1.pop())
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print(l2.pop())
print(l1)
print(l2)
print(id(l1))
print(id(l2))

##Output:
[10, 20, 30, 40]
[10, 20, 30, 40]
2277299387008
2277299387008
40
[10, 20, 30]
[10, 20, 30]
2277299387008
2277299387008
30
[10, 20]
[10, 20]
2277299387008
2277299387008

##Example2:
l1=[10,20,30,40]
l2=l1[::] ##Cloning is done using slicing, helps in creating a complete different duplicate list object
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print(l1 is l2)
print(l1.pop()) ##Changes on l1 won't impact l2
print(l1)
print(l2)
l2.append(777)
print(l1)
print(l2)


##Output:
[10, 20, 30, 40]
[10, 20, 30, 40]
2059127421568
2059127387264
False
40
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30]
[10, 20, 30, 40, 777]

##Example3: We can use copy as well instead of slicing for cloning.
l1=[10,20,30,40]
l2=l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))

##Output:
[10, 20, 30, 40]
[10, 20, 30, 40]
2599710423680
2599710389376

===========================================================================

Nested Lists:
-------------
-List inside another list is called Nested Lists.

#10 20  [30 40]
#0  1   2
#       0   1

##Example1:
l1=[10,20,[30,40]]
print(len(l1))
print(type(l1))
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[2][0])
print(l1[2][1])

##Output:
3
<class 'list'>
10
20
[30, 40]
30
40

##Nested List as Matrix:
##Example2:
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print('Elements Row Wise: ')
for x in l:
    print(x)
print('Elements in Matrix Style: ')
for x in l: ## x Talks about each row
    for y in x: ## y talks about each element in a row
        print(y,end=' ')
    print() ##After printing all elements of a row, then with help of print() helps to print next row elements in a next line.

    
##Output:
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
Elements Row Wise: 
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
Elements in Matrix Style: 
10 20 30 
40 50 60 
70 80 90 

===========================================================================
List Comprehension:
-------------------
To create a list using easy and concise/compact code for given list/tuple or any iterable objects.

##Example1:
l=[]

##Normal Way:
for i in range(1,11):
    l.append(i)
print(l)

##Comprehension way
l=[x for x in range(1,11)]
print(l)
##***************Syntax explanation, 
##[expression for each element in sequence/range] >>> for x in range(1,11) please consider expression x i.e [x for x in range(1,11)]
##[expression for each element in sequence/range if condition]

##Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##Example2: Create a list object with 1 to 10 square values:
l=[x*x for x in range(1,11)]
print(l)

##Output:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##Example3: Print 2^x and x values for 1,2,3,4,5
l=[2**x for x in range(1,6)]
print(l)

##Output:
[2, 4, 8, 16, 32]

##Example4: Print list from 1 to 100 which are divisible by 10
l=[x for x in range(1,101) if x%10==0]
print(l)

##Output:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

##Example 5:
l1=[10,20,30,40]
l2=[30,40,50,60]
##Create a list with elements present in l1 but not in l2
l=[x for x in l1 if x not in l2]
print(l)

##Output:
[10, 20]

##Example 6: Create list with elements present in both l1 and l2:
l1=[10,20,30,40]
l2=[30,40,50,60]
l=[x for x in l1 if x in l2]
print(l)

##Output:
[30, 40]

##Example 7:
l=['Balaiah','Nag','Venki','Chiru']
##From every name in the list just consider first letter and print output
l1=[word[0] for word in l]
print(l1)

##Output:
['B', 'N', 'V', 'C']

##Example 8:
s='the quick brown fox jumps over the lazy dog'
##To split this string to multiple list of words.

words = s.split()
print(words)
l1=[[word.upper(),len(word)] for word in words]
print(l1)

##Output:
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]

##Example 8: Program to display unique vowels present in the given word:
vowels=['a','e','i','o','u']
word=input('Enter Any String: ')
result=[]
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(result)
print('The no of unique vowels is: ',len(result))

##Output:
Enter Any String: Hey what's up
['e', 'a', 'u']
The no of unique vowels is:  3

##Example 9:
vowels=['a','e','i','o','u']
word=input('Enter Any String: ')
result=[]
for ch in vowels:
    if ch in word:
        result.append(ch)
print(result)
print('The no of unique vowels is: ',len(result))

##Output:
Enter Any String: aaaaaaaaaaaaaeeeeeeeeeeeeeeeeooooooooo
['a', 'e', 'o']
The no of unique vowels is:  3

##Example 10:
vowels=['a','e','i','o','u']
word=input('Enter Any String: ')
result=[ch for ch in vowels if ch in word]
print(result)
print('The no of unique vowels is: ',len(result))

##Output:
Enter Any String: rttttfbkevdnvjlvnjfkvsjkklmjnvnbdhgfacdqwopwqd
['a', 'e', 'o']
The no of unique vowels is:  3

======================================================================
max() and min() functions for List:
------------------------------------
##Example3:
t=[40, 50, 20, 10]
print(max(t))
print(min(t))

##Output:
50
10
