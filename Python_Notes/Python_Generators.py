##Python Generators Functions:
=============================

Electrical Generator >>> Generates electricity
Python Generator >>> Generate a sequence of values
      ||
      ||
      \/
     Yield (Generator uses this special keyword to generate values)
-Generator is a special type of function, which is responsible to generate a sequence of values.
-We can write generator functions just like ordinary functions, but it uses a special keyword 'yield' to return values.
-**********Advantages of using Generators over the Traditional Collections. To hold group of vlaues we already have List, Tuple, Dict, Set etc (Traditional Collections)..... what is the need of going for Generators.

##Example(Normal Collections):
l=[x*x for x in range(10)] ##It's a list
print(l)
print(l[0])

'''What to notice?
-Here the square values of range(10) will be created as an object and stored in this list.
-Later it will be printed if prompted.
-What if we opt for range(100000000), to store these many objects heap memory is not sufficient and it will throw MemoryError 
'''
##Output:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
0

##Example Let's try using generator:
##Comprehension concept is applicable for list not for tuple
g=(x*x for x in range(10)) ##It's a tuple
##If we use a comprehension for tuple we will get generator object.
print(type(g))
while True:
    print(next(g))

##Output:
<class 'generator'>
0
1
4
9
16
25
36
49
64
81
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 5, in <module>
    print(next(g))
    
##Can we replace range(10) with range(100000000)???
-We will never get Out of memory issue in case of generators, simple reason is, generators never store any objects.
-Only when we ask next element print(next(g)), the next element is generated and provided, but in the case of the list, all the values will be created and stored at the beginning only. But, generator nothing is created in the beginning, only generated on demand.
-If we're 4 members at house, storing 100 bags of rice at the beginning only or buying/demanding 1 rice bag based on requirement is good??? same as list vs generator
-------------------------------------------------------------------------------
##Demo Program2:
===============
##Write a Generator function to generate 3 Values 'A','B','C'?
##Example1:
def mygen():
    yield 'A' ##Generate A
    yield 'B' ##Generate B
    yield 'C' ##Generate C
print('Let us print the mygen: ',mygen())
g=mygen() ##We got generator object from generator function
print('The type of g is: ',type(g))
print('Let us print g value: ',g)

##Output:
Let us print the mygen:  <generator object mygen at 0x0000023005015FC0>
The type of g is:  <class 'generator'>
Let us print g value:  <generator object mygen at 0x0000023005015FC0>

##Example2:
def mygen():
    yield 'A' ##Generate A
    yield 'B' ##Generate B
    yield 'C' ##Generate C
g=mygen() ##We got generator object from generator function
print(next(g))
print(next(g))
print(next(g))
print(next(g)) ##Will throw error, StopIteration exception, becuase there is only 3 values available.
##Let's avoid the stop iteration exception, by making changes in the code. Refer Example3

##Output:
A
B
C
StopIteration exception

##Example3:
def mygen():
    yield 'A' ##Generate A
    yield 'B' ##Generate B
    yield 'C' ##Generate C
g=mygen() ##We got generator object from generator function
for x in g:
    print(x) ##This overcame the stopiteration error

##Output:
A
B
C

##Write a generator to generate first n values.

def first_n_values_generator(n):
    i=1
    while i<=n:
        yield i ##Whenever we use yield, then it is a generator function
        i=i+1
g=first_n_values_generator(5) ##Even it supports n=1000000000 ;P, this is not supported by traditional collections i.e. list.
for x in g:
    print(x)
print(g)

##Output:
1
2
3
4
5
<generator object first_n_values_generator at 0x0000028DE1376030>

---------------------------------------------------------------------------------

##Demo Program Set-2:
##Write a generator function to generate values for countdown with provided max value:
import time
def countdown_generator(num):
    while num >= 1:
        yield num ##Whenever we use yield, then it is a generator function
        num=num-1
g=countdown_generator(5)
for x in g:
    print(x)
    time.sleep(1)
print(g)

##Output:
5
4
3
2
1
<generator object countdown_generator at 0x00000278DBB75F50>

##Write a generator function to generate Fibonacci Numbers.
-We call it a fibonacci series when the next number is sum of previous two numbers.
ex:0,1,1,2,3,5,8,13......

def fibonacci_sequence_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fibonacci_sequence_generator()
for x in g:
    print(x)

##Output:
It's crazy, please execute and try.

##Modified1:
def fibonacci_sequence_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fibonacci_sequence_generator()
for x in g:
    if x<=10:
        print(x)
    else:
        break


##Output:
0
1
1
2
3
5
8

##Modified2:
def fibonacci_sequence_generator():
    a,b=0,1
    while a<=10:
        yield a
        a,b=b,a+b
g=fibonacci_sequence_generator()
for x in g:
    print(x)


##Output:
0
1
1
2
3
5
8

##I need first 100 fibonacci numbers:
def fibonacci_sequence_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fibonacci_sequence_generator()
count=1
while count <= 10:
    print(next(g))
    count=count+1


##Output:
0
1
1
2
3
5
8
13
21
34

##Let's ask jury only, how many fibonacci numbers he needs ;P:
def fibonacci_sequence_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fibonacci_sequence_generator()
count=1
n=int(input('Enter number of fibonacci numbers you need: '))
while count <= n:
    print(next(g))
    count=count+1

##Output:
Enter number of fibonacci numbers you need: 10
0
1
1
2
3
5
8
13
21
34

------------------------------------------------------------------------------

##Performance comparison between Collections and Generators:
import random
import time
names=['Sunny','Bunny','Chinni','Vinni']
subjects=['Python','Java','DataScience']
def student_list(num):
    students=[]
    for i in range(num):
        student={'id':i,'name':random.choice(names),'subject':random.choice(subjects)}
        students.append(student)
    return students
t1=time.time()
students=student_list(10000)
t2=time.time()
print('Time required to prepare students list: ',(t2-t1))

def student_generator(num):
    for i in range(num):
        student = {'id':i,'name':random.choice(names),'subject':random.choice(subjects)}
        yield student
t1=time.time()
g=student_generator(10000)
t2=time.time()
print('Time required to prepare students generator: ',(t2-t1))

##Output:
Time required to prepare students list:  0.009972572326660156
Time required to prepare students generator:  0.0 ##Pretty Fast

---------------------------------------------------------------------------------

##Advantages and limitations of Generators:

#Advantages:
-Performance will be improved when compared with traditional collections.
-Memory utilization will be improved when compared with traditional collections.
-Best suitable if we want to handle very huge volume of data like handling data from lakhs of files, handling lakhs of record from database etc.

#Limitations:
-No Storage of data
-We cannot ask a particular element like we do in list l[0],l[1] etc. Instead in generator to access 5 element, all the elemenrts needs to be printed.

##How to convert generator object into the list based on programming requirement?
By using list() function, we can convert generator object into list:
list_obj=list(generator_obj)

def first_n_values_generator(n):
    i=1
    while i<=n:
        yield i
        i=i+1
g=first_n_values_generator(5)
for x in g:
    print('The generated value from generator function: ',x)
y=first_n_values_generator(5)
l=list(y) ##Converting generator into list
print('Generator values converted as list: ',l)

##Output:
The generated value from generator function:  1
The generated value from generator function:  2
The generated value from generator function:  3
The generated value from generator function:  4
The generated value from generator function:  5
Generator values converted as list:  [1, 2, 3, 4, 5]

##Decorator vs Generator??
#Decorator:
-If we want to extend functionality of existing function without modifying that.

#Generator:
-If we want to generate a sequence of values then we should go for generators.
-It uses a special keyword 'yield' to return values.