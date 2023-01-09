##Generate an infinite fibonacci series by using Generator:
#A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The
#simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f1=fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

##Output:
0
1
1
2
:
:
:

##Approach2:
def fibonacci(n):
    a,b=0,1
    print(a)
    while (b<n):
        print(b)
        c=a+b
        a=b
        b=c
fibonacci(50)

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

##Approach3:
def fibonacci(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fibonacci(7)

##Output:
0
1
1
2
3
5
8

##Approach4: Using Recursion*********
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n=10
if n<=0:
    print('Invalid')
else:
    for i in range(n):
        print(fibonacci(i))

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
======================================================================================

#Sort A List without using A Sort Keyword:
l=[41,2,12,6,35,8,10,1,19]
n=len(l)
for i in range(n):
    print('The value of II: ',i)
    for j in range(i+1,n):
        print('The value of j: ',j)
        if l[i] > l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

##Output:
The value of II:  0
The value of j:  1
The value of j:  2
The value of j:  3
The value of j:  4
The value of j:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  1
The value of j:  2
The value of j:  3
The value of j:  4
The value of j:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  2
The value of j:  3
The value of j:  4
The value of j:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  3
The value of j:  4
The value of j:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  4
The value of j:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  5
The value of j:  6
The value of j:  7
The value of j:  8
The value of II:  6
The value of j:  7
The value of j:  8
The value of II:  7
The value of j:  8
The value of II:  8
[1, 2, 6, 8, 10, 12, 19, 35, 41]

======================================================================================

##Write a code to check whether A string is Palindrome or not:
##A word which reads the same when reversed Ex: Madam,level

##Approach1:
s='NITIN'
if s==s[::-1]:
    print('Yes, it is Palindrome')
else:
    print('No')
    
##Output:
Yes, it is Palindrome

##Approach2:
s='NITIN'
n=len(s)
x=0
for i in range(n):
    print('Value of i: ',i)
    print('Value of n: ',n)
    if s[i]!=s[n-i-1]:
        x=1
        break
if x==0:
    print('Yes, it is Palindrome')
else:
    print('No')
    
##Output:
Value of i:  0
Value of n:  5
Value of i:  1
Value of n:  5
Value of i:  2
Value of n:  5
Value of i:  3
Value of n:  5
Value of i:  4
Value of n:  5
Yes, it is Palindrome

##Approach3:
def palindrome(s):
    reverse_s=reversed(s)
    print(reverse_s)
    for i in reverse_s:
        print(i)
    temp=''.join(reversed(s))
    print(temp)
    if s==temp:
        return True
    else:
        return False
s='level'
palindrome(s)
print(palindrome(s))

##Output:
<reversed object at 0x0000019516FE7FA0>
l
e
v
e
l
level
<reversed object at 0x0000019516FE7FA0>
l
e
v
e
l
level
True


##Approach4:
def palindrome(s):
    n=len(s)
    first=0
    last=n-1
    while(first<last):
        if s[first]==s[last]:
            first+=1
            last-=1
        else:
            return False
    return True
s='level'
palindrome(s)
print(palindrome(s))

##Output:
True

======================================================================================

##To sort a dictionary / using a dictionary comprehension:

##Sorting by Key:
d1={575:'Apple',876:'Mango',132:'Grapes'}
d=sorted(d1.keys())
print(d)
d2={}
for i in d:
    d2[i]=d1[i]
print(d2)

##Using dictionary comprehension and sorting by a Value:
d1={575:'Apple',876:'Mango',132:'Grapes'}
d2={key:value for key,value in sorted(d1.items(), key=lambda x:x[1])}
print(d2)

##Output:
{132: 'Grapes', 575: 'Apple', 876: 'Mango'}
{575: 'Apple', 132: 'Grapes', 876: 'Mango'}

======================================================================================

##Find the Pair with Given Number in a list:
#Print all pairs with given sum:
l=[8,7,2,5,3,1]
n=len(l)
k=10
for i in range(n):
    for j in range(i+1,n):
        if(l[i]+l[j])==k:
            print(l[i],l[j])

##Output:
8 2
7 3

======================================================================================

##Create a fibonacci series by using a Recursion:
def rec_fib(n):
    if n <= 1:
        return n
    else:
        return (rec_fib(n-1) + rec_fib(n-2))
nterms=int(input('How many terms?: '))
if nterms<=0:
    print('Please enter a +ve integer')
else:
    for i in range(nterms):
        print(rec_fib(i))


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

======================================================================================

##String manipulation:
input = 'the sky is blue'
Required output = 'blue is sky the'

a=input.split()
print(a)
print(type(a)) ##List
b=a[::-1]
print(b)
c=' '.join(b)
print(c)

##Output:
['the', 'sky', 'is', 'blue']
<class 'list'>
['blue', 'is', 'sky', 'the']
blue is sky the

======================================================================================

##Remove Punctuation (Except Space):
input = '/*apples are & found% only @red & green'
s=''
for i in input:
    if((i>='A' and i<='Z') | (i>='a' and i<='z') | (i==' ')):
        s=s+i
print(s)

##Output:
apples are  found only red  green

======================================================================================

##Find max repeated character in a String (Time Complexity Should be lesser than 0(n2)):

s='itininiytnnhhn'
ch={}
for i in s:
 if i in ch:
    ch[i]+=1
 else:
    ch[i]=1
print(ch)
max_char=max(ch, key=ch.get)
print(max_char)

##output:
n

======================================================================================

##Find the maximum and minimum value from a list without using any predefined function:

l=[9,11,0,370,55,40,2]
mx=l[0]
mn=l[0]
for i in l:
    if i>mx:
        mx=i
    if i<mn:
        mn=i
print('Maximum: ',mx)
print('Minimum: ',mn)

##Output:
Maximum:  370
Minimum:  0

======================================================================================

##To raise an exception if element is 1 in a list:
l=[9,11,0,370,55,40,1]
sum=0
for i in l:
    if i==1:
        raise Exception('Exception: 1 is found')
    else:
        sum+=1

##Output:
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\PySpark_Programs\PySpark.py", line 5, in <module>
    raise Exception('Exception: 1 is found')
Exception: Exception: 1 is found

======================================================================================

##Difference between List, Tuple and an Array:
##List:
-Lists are mutable
-List is a container to contain different types of objects is used to iterate objects
-Syntax of List
list=['a','b','c',1,2,3]
-List iteration is slower
-List consume more memory
-Operation like insertion and deletion are better performed

##Tuple:
-Tuples are immutable
-Tuple is also similar to list but contains immutable objects
-Syntax of Tuple:
tuples=('a','b','c',1,2)
-Tuple processing is faster than list
-Tuple consume less memory
-Elements can be accessed better

##Array:
-It can only consist of value of same type
-It can directly handle arithmetic operations
-We need to import the array before work with the array
-An array are much compatible than the list
-It is more compact in memory size comparatively list
-It is suitable for sorting shorter sequence of data items
-We can print the entire list without using explicit looping

======================================================================================

##What is a lambda function, explain it with a example?
##Explain list function Append() and Extend()?*******
##How are exceptions handled in Python?
Clearly explain try, except, else and finally
try : This block will test the exceptional error to occur
except : Here you can handle the error
else : If there is no exception then this block will be executed
finally : Finally block always gets executed either exception is generated or not

try:
    #Some Code...!
except:
    #Optional Block
    #Handling of exception (If Required)
else:
    #Some code...
    #execute if no exceptional
finally:
    #Some code....(always executed)
    
======================================================================================

#What do you mean by decorator?
#How you create customised decorator?
#How you create parameterized decorator?
#How you will Add 2 Numbers using decorator?
#Explain with example
  
======================================================================================

##What do you mean by abstraction. How do you define Abstract Class or Function by using Abstraction?
##What is MRO (Method Resolution Order)?
##What do you mean by GIL (Global Interpreted Lock)?
-The Global Interpreter Lock(GIL) of Python allows only one thread to be executed at a time. It is often a hurdle, as it does not allow multi-threading in Python to save time
-The Python GIL, in simple words, is a mutex (or a Lock) that allows only one thread to hold control of the Python interpreter
-This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn't visible to developers who execute single-threaded programs, but it can be a performance bottlrneck in CPU-bound and multi-threaded code
-Since the GIL allows only one threaded to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an 'infamous' feature of Python
-Basically, GIL in Python doesn't allow multi-threading which can be considered as disadvantage

======================================================================================

##Drawbacks of not using 'WITH' statement?
##Difference between static and class method
##Difference between a list and dictionary?
##Can we use a List/Tuple as a key in dictionary?
##When should we prefer a list or a tuple real time scenario?
##Why Python is called as Dynamically typed Programming Language / What is Duck Typing (Duck Typing also known as Dynamically typed they're interchangeablly used to confuse us)?
##Why Python is called ineterpreted Language?
##What is Abstraction, how you define classes or define function using abstraction?
##What Python support-Call by reference or Call by value?
##What you know about OOPs concept?
##Is Python A Fully Object Oriented Language? >>> Nope!, find out why it is not fully oo langauge


======================================================================================

##To test whether given number is a Palindrome?

##Approach1: Generally not preferred
def palindrome(n):
    s=str(n)
    temp=s[::-1]
    if s==temp:
        return True
    else:
        return False
n=123456
print(palindrome(n))

##Approach2: Best Approach
def palindrome(n):
    temp=n
    rev_n=0
    while (temp>0):
        digit=temp%10
        print(digit)
        rev_n=rev_n*10+digit
        #rev_n=0*10+6=6
        temp=temp // 10
    if n==rev_n:
        return True
    else:
        return False
n=12345654321
print(palindrome(n))

##Output:
1
2
3
4
5
6
5
4
3
2
1
True

=================================================================

##FizzBuzz : If a number is divisible by 3 then mention 'Fizz' and number is divisible by 5 then mention 'Buzz' and if by 15 mention 'FizzBuzz' else print the number as is:

##Example1: ##Best Approach
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0: ##i%15==0
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzz(30)

##Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz

##FizzBuzz using Dictionary:
def fizzbuzz(n):
    d={3:'fizz',5:'Buzz'}
    for i in range(1,n+1):
        result=''
        for k, v in d.items():
            if i%k==0:
                result+=v
        if not result:
            result=i
        print(result)
fizzbuzz(20)

##Output
1
2
fizz
4
Buzz
fizz
7
8
fizz
Buzz
11
fizz
13
14
fizzBuzz
16
17
fizz
19
Buzz

================================================================

##Character Occurrence:
#####Least Repeating
def least_char_occurence(s):
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch) ##To print the occurrenced of all the characters
    result=min(ch,key=ch.get)
    print(result)
s='aaaaaabbbbbbbhhhhhhhssssssjjiiiiiiieeeeee'
least_char_occurence(s)

##Output:
{'a': 6, 'b': 7, 'h': 7, 's': 6, 'j': 2, 'i': 7, 'e': 6}
j

#Using counter:
from collections import Counter
s='aaaaaabbbbbbbhhhhhhhssssssjjiiiiiiieeeeee'
ch=Counter(s)
print(ch)
result_min=min(ch,key=ch.get)
result_max=max(ch,key=ch.get)
print(result_min)
print(result_max)

##Output:
Counter({'b': 7, 'h': 7, 'i': 7, 'a': 6, 's': 6, 'e': 6, 'j': 2})
j
b

#####Count of any particular element
#Using count for String, Number, List
l=[1,2,3,4,5,4,3,2,3,4,5,2,6,7]
print(l.count(4))
s='aabbccdeessddaaw'
print(s.count('a'))

##Output:
3
4

#Using for loop:
def count_char_occurence(s,ch_search):
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)
    try:
        print(ch[ch_search])
    except:
        print(0)
s='aaaaaabbbbbbbhhhhhhhssssssjjiiiiiiieeeeee'
count_char_occurence(s,'a')

##Output:

{'a': 6, 'b': 7, 'h': 7, 's': 6, 'j': 2, 'i': 7, 'e': 6}
6

#####Count of all elements
def least_char_occurence(s):
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch) ##To print the occurrenced of all the characters
s='aaaaaabbbbbbbhhhhhhhssssssjjiiiiiiieeeeee'
least_char_occurence(s)

##Output:
{'a': 6, 'b': 7, 'h': 7, 's': 6, 'j': 2, 'i': 7, 'e': 6}

================================================================

##Prime Number:
#To check if the number is a prime number or not:

##Using Flag:
def prime_number(n):
    flag=False
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=True
                break
    if flag:
       return 'No! Its not a Prime Number'
    else:
        return 'Yes! Its a Prime Number'
print(prime_number(6))

##Output:
No! Its not a Prime Number

##To optimize it and execute it in better way
def prime_number(n):
    flag=False
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i==0:
                flag=True
                break
    if flag:
       return 'No! Its not a Prime Number'
    else:
        return 'Yes! Its a Prime Number'
print(prime_number(4))

##Output:
No! Its not a Prime Number

##Using for-else: ##Best Approach
def prime_number(n):
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i==0:
                print('No! Its not a Prime Number')
                break
        else:
            print('Yes! Its not a Prime Number')
    else:
        print('No! Its not a Prime Number')
prime_number(5)

##Output:
Yes! Its not a Prime Number

##To cehck in the range:
def prime_number(start,end):
    for n in range(start,end):
        if n>1:
            for i in range(2,(n//2+1)):
                if n%i==0:
                    break
            else:
                print(n)
prime_number(20,30)

##Output:
23
29
================================================================

##Modify String Format:
#Input=I_Am_Coder
#Output=i.aM.a.cODER

#Input=This_Is_A_Good_Morning
#Output=tHIS.iS.a.gOOD.mORNING

#first_upper_letter=first_lower_letter
#remaining_lower_letter=remaining_upper_letter

##Using List
def string_format(s):
    l=[]
    temp=s.split('_')
    for i in temp:
        l.append(i[0].lower()+i[1:].upper())
    print(l)
    output='.'.join(l)
    print(output)
s='This_Is_A_Good_Morning'
string_format(s)

##Output:
['tHIS', 'iS', 'a', 'gOOD', 'mORNING']
tHIS.iS.a.gOOD.mORNING

##Without using string:
def string_format(s):
    new_s=''
    temp=s.split('_')
    for i in temp:
        new_s=new_s+i[0].lower()+i[1:].upper()+'.'
    new_s=new_s[:-1]
    print(new_s)
s='This_Is_A_Good_Morning'
string_format(s)

##Output:
tHIS.iS.a.gOOD.mORNING

=================================================================

##Second highest number in a list:
##Assuming the list will be more than 2 members:
######Using for loop:
def second_highest_number(l):
    if l[0]>l[1]:
        first=l[0]
        second=l[1]
    else:
        first=l[1]
        second=l[0]
    for i in range(2,len(l)):
        if l[i]>first:
            second=first
            first=l[i]
        elif l[i]>second:
            second=l[i]
    return second
l=[10,20,30,4,100,666]
b=[10,20,30,4,100,666,666]
print(second_highest_number(l))
print(second_highest_number(b))

##Output:
100
666 ##It's a draw back

##Let's optimize the code:
def second_highest_number(l):
    if l[0]>l[1]:
        first=l[0]
        second=l[1]
    else:
        first=l[1]
        second=l[0]
    for i in range(2,len(l)):
        if l[i]>first:
            second=first
            first=l[i]
        elif l[i]>second and first!=l[i]:
            second=l[i]
    return second
l=[10,20,30,4,100,666]
b=[10,20,30,4,100,666,666]
print(second_highest_number(l))
print(second_highest_number(b))

##Output:
100
100 ##draw back is solved


######Using reverse sort:
def second_highest_number(l):
    l.sort(reverse=True)
    print(l[1])
    l.sort()
    print(l[-2])
l=[10,20,30,4,100,22,66]
second_highest_number(l)

##Output:
66
66

##To find nth highest sal:
def second_highest_number(l,n):
    l.sort(reverse=True)
    print(l)
    print(l[n-1])
l=[10,20,30,4,100,22,66]
second_highest_number(l,5)

##Output:
[100, 66, 30, 22, 20, 10, 4]
20

Armstrong and Factorial is pending:

##Code to find the common letters between two strings

https://www.tutorialride.com/python-interview/python-interview-questions-and-answers.htm
https://www.youtube.com/watch?v=CltvwBdYaRY
https://github.com/netsetos/python_code