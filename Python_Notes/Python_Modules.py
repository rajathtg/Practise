#Modules: Group of functions/variables/classes saved in a file is called modules.
##By default every .py file is a module as simple as that
##The most required functions,variables and class frequently used can be imported from modules.py file.

###Simple example of Module durgamath.py:
x = 'Durga'
y = 'Hyderabad'
def difference(a,b):
    print('The difference:',a-b)
def add(a,b):
    print('The Sum: ',a+b)
def product(a,b):
    print('The product: ',a*b)
class Test:
    pass
    
##Example syntax to access the module:
import modulename ##Then all the module available for usage
modulename.variablename  ##To use a module
modulename,functionname()  ##To call a function

##My requirement is to write a test.py and pull in the above modules.
import durgamath ####All the available modules inside the durgamath is available for usage
print(durgamath.x) ###Durga
print(durgamath.y) ###Hyderabad
durgamath.add(10,20)
durgamath.difference(10,20)
durgamath.product(10,20)

##Output:
Durga
Hyderabad
The Sum:  30
The difference: -10
The product:  200

#*****Note: The durgamath.py file should be saved at the project level and not at any folder level of the given project.
##Advantages:
#Code Reusability
#Length of the code is reduced and readability is increased
#Maintability of the application will be improved, because any changes is required, it will be done at only one place i.e durgamath.py file only.
#We can maintain different modules like database,logging,credebtials related etc...
#Internal performance is improved, how? the durgamath.py module is used by test.py file for the first time then inside __pycache__ a durgamath.pyc (machine level compiled code/translated)file is created and next time when a testfile.py imports it, internally it will be pointed to durgmath.pyc, similarly in future the module is required by 1000 new .py files all will be pointed to .pyc only

-----------------------------------------------------------------------
###Module aliasing

import durgamath as m
print(m.x)
m.add(10,20)##Helps in reducing the length of the code
durgamath.product(10,20) ##Will throw Name error, post defining alias name, original name is not allowed

##Output:
Durga
The Sum:  30

####I want to access x, y and add function directly:
#from durgamath import x,y ##To use only specific ones
from durgamath import * ##To use all the variables/functoins/class
print(x)
add(10,20)

##Output:
Durga
The Sum:  30

-----------------------------------------------------------------------
###Member Aliasing

#Let's add member aliasing to make better readability:
from durgamath import add as a,product as p
a(10,20)
p(10,20)

##Output:
The Sum:  30
The product:  200

#***Note: As usual original name is not allowed to use
-----------------------------------------------------------------------
###Various possible import statements:
1. import module1 ##To import a module
2. import module1,module2,module3...  ##To import multiple modules
3. import module1 as m1
4. import module1 as m1, module2 as m2, module3 as m3....
5. from module1 import member1
6. from module1 import member1,member2,member3...
7. from module1 import *
8. from module1 import member1 as mb1,member2 as mb2...

----------------------------------------------------------------------
##Module Naming COnflicts: If two modules has variables/modules/class of same name it will create a conflict, how python manages it and how can we resolve it by following certain rules.

##module1.py
def add(a,b):
    print("module1 add function: ",a+b)

##module2.py  
def add(a,b):
    print("module2 add function: ",a+b)
    
##Example1:
from module1 import *
from module2 import *
add (10,20)

##Output:
module2 add function: 30

##Example1:
from module2 import *
from module1 import *
add (10,20)

##Output:
module1 add function: 30

*****Note: Here the most recent module will be considered, this is similar to below code
x = 10
x = 20
x = 30
print(x) ###Output : 30

###How to make both modules available?
import module1
import module2
module1.add(10,20)
module2.add(10,20)

##Output:
module1 add function: 30
module2 add function: 30

###More simpler way:
from module1 import add as a1
from module2 import add as a2
a1(1,20)
a2(10,20)

##Output:
module1 add function: 30
module2 add function: 30

-----------------------------------------------------------------------
##Reloading a module:
##Consider the below example, we're trying to load same module multiple times, but ideally inside the Python Virtual Machine, module will be loaded only one time, i.e. for the first time when it is called.
##Advantage of above scenario is, performance improvement.
##Disadvantage is, if the module is updated, the updated module won't reflect when same module called again and again :(

import module1
import module1
import module1
.
.
.
. 

##Example:

#module1.py
def add(a,b):
    print('Sum of value',a+b)

#testfile.py
import module1
module1.add(10,20)

##Output:
Sum of value 30

##Updated Example

#testfile.py
import module1
import time
module1.add(10,20)
print("Entering the sleeping mode")
time.sleep(40)
print("Just now woke now")
module1.difference(10,20)

##While it is sleeping, the module1 is updated as below:
def add(a,b):
    print('Sum of value: ',a+b)
def difference(a,b):
    print('Difference of value: ',a-b)

##Output:
Entering the sleeping mode
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\practise\testfile.py", line 7, in <module>
    module1.difference(10,20)
AttributeError: module 'module1' has no attribute 'difference'
Just now woke now

#****Note: To overcome above provlem use reload function

#testfile.py
from imp import reload
import module1
import time
module1.add(10,20)
module1.difference(10,20)
print("Entering the sleeping mode")
time.sleep(40)
print("Just now woke now, trying to use module again")
reload(module1)
module1.difference(10,20)

##Module1 updated meanwhile testfile is sleeping:
def add(a,b):
    print('Sum of value',a+b)
def difference(a,b):
    print('Difference of value: ',a-b)
def pro(a,b):
    print('Pro of value: ',a*b)

##Output:
DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
  from imp import reload
Sum of value 30
Difference of value:  -10
Entering the sleeping mode
Just now woke now, trying to use module again
Pro of value:  200

-------------------------------------------------------------------------

##********Finding members of module by using dir() function:

1. dir() ---> To list out all members of current modules
2. dir(modulename) ---> To list out all members of specified module

##testfile.py:
x=888
y=999
def add(a,b):
    print(a+b)
print(dir())

##Output:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'x', 'y']
##In the above output apart from add,x,y other members are added by Python interpreter.

##To print all members present in math module:
import math
print(dir(math))

##Output:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

##*****Note: Explain Difference between dir() and help() functions?
dir(math) --> Just list out all members of the diven module, as seen above.
help(math) --> Will provide the documentation related to that module, as seen below.
##Output:
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        .
        .
        .
        .
        .
        .
        .
        .

-----------------------------------------------------------------------
##Extra members added by python interpreter for every module:
#The extra member added by Python interpreter can also be used by Developer for carrying out the execution based on requirement.

__doc__ ---> To hold docstring
__file__ ---> To hold file name
__name__ ---> Most valuable, will look into this next********
__loader__ ---> Which loader is responsible to load this module
__package__ ---> This module is related to which package, Group of functions is module, group of modules is package.

###Example1:
'''This module provides demo explanation about built in members'''
print("The docstring used is: ",__doc__)

##Output:
The docstring used is:  This module provides demo explanation about built in members

##Example2:
import os
print("The filename used is: ",__file__)
print("The File Absolute Path: ",os.path.abspath(__file__))
print("The Directory Name: ",os.path.dirname(os.path.abspath(__file__)))

##Output:
The filename used is:  C:\Users\91961\PycharmProjects\pythonProject\practise\testfile.py
The File Absolute Path:  C:\Users\91961\PycharmProjects\pythonProject\practise\testfile.py
The Directory Name:  C:\Users\91961\PycharmProjects\pythonProject\practise

##****Note: The absolute paths are used mainly in the Django
-----------------------------------------------------------------------
##Special Variable: __name__

##When the module1.py is directly executed from command line (py module1.py) or through IDE, then it is called direct method. If it is direct execution then the value what we get is __main__

##When the module1.py is imported in the test.py and through that if it is executed then considered as indirect way. In the indirect execution name of the module/.py file name i.e module1.

#module1.py:
print(__name__)

##Output:
__main__

#test.py:
import module1
print('The previous line is the name of the module')

##Output:
module1 ###This is what is to be noted
The previous line is the name of the module


##Example2:

#module1.py:
if __name__ == '__main__':
    print("The program is executed directly")
else:
    print("The program is executed indirectly")
##Output:
The program is executed directly

#test.py:
import module1
print('The previous line is the name of the module')
##Output:
The program is executed indirectly
The previous line is the name of the module

--------------------------------------------------------------------------
##Use of __name__

#module1.py:
def f1():
    print('f1 execution....')
def f2():
    print('f2 execution....')
def f3():
    print('f3 execution....')
f1()
f2()
f3()

#Output:
f1 execution....
f2 execution....
f3 execution....

#testfile.py:
import module1
module1.f1()

#Output:
f1 execution....
f2 execution....
f3 execution....
f1 execution....

###It's a big flaw :(, I wanted only f1

##Solution:
def f1():
    print('f1 execution....')
def f2():
    print('f2 execution....')
def f3():
    print('f3 execution....')
if __name__=='__main__': ##To enter into if only if it is direct execution
    f1()
    f2()
    f3()

#Output:
f1 execution....
f2 execution....
f3 execution....


#testfile.py:
import module1
module1.f1()

##Output:
f1 execution....

-----------------------------------------------------------------------
##Working with Math Module:

##testfile

from math import *
print(factorial(4))
print(sqrt(4))
print(fabs(-10.6))
print(fabs(10.6))
print(ceil(10.5))
print(floor(10.5))

##Output:
24
2.0
10.6
10.6
11
10

##Read radius from input and print area of circle:
from math import *
r = int(input('Enter radius: '))
area=pi * r**2 ##Also we can write pi * r *r or pi * pow (r,2)

import math
def find_area(r):
        return math.pi*math.pow(r,2)

##Output:
Enter radius: 3
28.274333882308138

##More Example:
You are creating a function that manipulates a number. The function has the following requirements:
A float value passed to the function. The function must take absolute value of the float. Any decimal points after the integer must be removed. which two math functions should be used?
##Answer:
math.fabs(x)
math.floor(x)

#testfile.py:
from math import *
print(floor(fabs(-12.893)))

#Output:
12

You are writing an application that uses the sqrt function. The program must reference the function using the name sq.
Which of the following import statement required to use?
##Answer:
from math import sqrt as sq

##testfile.py:
from math import sqrt as sq
print(sq(4))

##Output:
2.0

##Consider the below code:
import math
l = [str(round(math.pi)) for i in range (1,6)] ##For loop will be executed 5 times from 1 to 5, therefore rounded pi value 3 will be printed 5 times
print(l)

##Output:
['3', '3', '3', '3', '3']

------------------------------------------------------------------------------

##Working with random module:
#To generate random int numbers/objects for OTP/Authentication etc...
random()
uniform()
randint()
randrange()
choice()

#random() : Meant for generating a random float number between 0 and 1 (not inclusive) i.e. 0<x<1 and not 0<=x<=1.
#Note: It doesn't take any arguments.

##Example
from random import *
print(random())
#Output:
0.876750280504664

##To generate 10 such numbers:
from random import *
for i in range(10):
    print(random())
#Output:
0.15198231644489246
0.2985185098566403
0.3243670618662917
0.03926121483093359
0.2229102547587659
0.1526752565608308
0.6705563791452009
0.48686242504765176
0.13682149497998675
0.9661843084310691

#Uniform() : This needs an argument uniform(begin,end). A random float number between begin and end a random float number will be generated and not inclusive.

#Example:
from random import *
print(uniform(0,5))
#Output:
1.8664321417417984

#Example:
from random import *
for i in range(10):
    print(uniform(0,5))
#Output:
2.201962883960151
2.929144887294306
1.8820723354155406
2.3073124749683633
1.532323499786995
1.346120562220789
4.635511184373151
4.872736901966529
2.2843799363172224
3.5070323104959833

-------------------------------------------------------------------------

#randint() : Meant for generating random int value and compulsory we need to give begin and end and both are inclusive.

##Example:
from random import *
print(randint(1,10))
##Output:
10

##Example:
from random import *
for i in range(1,10):
    print(randint(1,10))
##Output:
2
7
1
7
8
4
1
2
10

##*********randrange(): We need to provide begin, end and step value. 
#The output will be from begin to end-1 with the given step value.
#The begin is optional, the default value is 0
#Step is optional, the default value is 1
#end is must.

from random import *
print(randrange(5)) ##It will generate value either 0,1,2,3,4
print(randrange(1,11)) ##It will generate value from 1 to 10
##Output:
3
9

from random import *
for in range(10):
    print(randrange(1,11,2)) ##It will generate only odd numbers
##Output:
3
9
9
3
5
9
9
5
5
7

-------------------------------------------------------------------------

##choice(): To generate a random object from list, tuple, string etc. 
#Syntax > choice(sequence)
##Note: The sequence needs to be indexable, because internally Python performs index.

##Example:
from random import *
fruits=['Apple','Banana','Orange','Mango']  ##List
for i in range(5):
    print(choice(fruits))

##Output:
Apple
Orange
Apple
Mango
Apple

##Example:
from random import *
fruits=('Apple','Banana','Orange','Mango') ##Tuple
for i in range(5):
    print(choice(fruits))
    
##Output:
Banana
Orange
Banana
Banana
Orange

##Example:
from random import *
fruits={'Apple','Banana','Orange','Mango'} ##Set
for i in range(5):
    print(choice(fruits))
##Output:
TypeError: 'set' object is not subscriptable

##Example:
from random import *
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ' ##String
for i in range(5):
    print(choice(alphabets))
    
##Ouput:
Q
I
B
W
R

--------------------------------------------------------------------------

##Write a Program to generate 6-digit random number, which can be used as OTP?

##Example:
from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
##Output:
9 5 4 3 7

##Example:
from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='') ##sep='',This will avoid the space between numbers

##Output:
36101

##Example
from random import *
for i in range(6):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='') ##sep='',This will avoid the space between numbers
##Output:
73376
27851
43450
14742
99113
61865

##Example:
from random import *
otp=''
for i in range(6):
    otp=otp+str(randint(0,9)) ##str is used for +, both argument should be str for concatenation.
print(otp)

##Output:
043588

Example:
This won't work:
randint(000000,999999) ##It always takes from 0
randint(100000,999999) ##It is not correct

-------------------------------------------------------------------------

##Write a Program to generate a random password of 6 length whgere 1,3,5 characters are alphabet symbols and 2,4,6 charactera are digits?

##Example:
from random import *
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ##We can use smaller case if required
digits = '0123456789'
print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')

##Output:
F9D2E3

##Example:
from random import *
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
for i in range(10):
    print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')
    
##Output:
Q3K6c2
w1Q9B6
Q0O1f1
b4o4E1
I2M0A8
l4O3f8
a0a4t3
b2O7R1
n2P0c9
h5F1E0

##Example:
from random import *
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
for i in range(10):
    print(choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),sep='')
    
##Output:
F9563f
ScreTF
JOPcfd
9t88fr
h6fNLi
SzdNB6
AFOEf1
v0X1vp
JtfjoB
TxAfJK

-------------------------------------------------------------------------

##Write a program to generate Fake Employee Data for Database Testing:
#Employee Name : Should contain 3 to 10 char, 1st char in uppercase and remaining char in lower case
#Employee Number : Should start with "e-" followed by 4 digits. ex: e-1234
#Employee Salary : Should be float value from 10000 to 50000
#Employee City : Should be from [Hyd,Chn,BLR,Pune,Del,Mum ]
#Employee Mobile Number : Should be 10 digit, where 1st number shoul be 6 to 9 and no restriction on remaining digits. eg: 9848098480
#Designation : [SE,SSE,TL,PL,PM]

##Example:
from random import *
alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']
designations = ['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']

def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2,9)
    for i in range(n):
        name = name+choice(alphabets)
    return name
print(get_fake_name())

def get_fake_num():
    eno = 'e-'
    for i in range(4):
        eno = eno+choice(digits)
    return eno
print(get_fake_num())

def get_fake_sal():
    esal = round(uniform(10000,50000),2)
    return esal
print(get_fake_sal())

def get_fake_city():
    city = choice(cities)
    return city
print(get_fake_city())

def get_fake_mbno():
    mbno = choice('6789') ##To select the number amongst these 4 digits only, kind of hard coded
    for i in range(9):
        mbno=mbno+choice(digits)
    return mbno
print(get_fake_mbno())

def get_fake_designation():
    designation = choice(designations)
    return designation
print(get_fake_designation())

##Output:
Hnjrfibwoq
e-9959
24878.54
Chennai
6030196890
Project Lead

##Example2:
from random import *
alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']
designations = ['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']

def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2,9)
    for i in range(n):
        name = name+choice(alphabets)
    return name
#print(get_fake_name())

def get_fake_num():
    eno = 'e-'
    for i in range(4):
        eno = eno+choice(digits)
    return eno
#print(get_fake_num())

def get_fake_sal():
    esal = round(uniform(10000,50000),2)
    return esal
print(get_fake_sal())

def get_fake_city():
    city = choice(cities)
    return city
#print(get_fake_city())

def get_fake_mbno():
    mbno = choice('6789') ##To select the number amongst these 4 digits only, kind of hard coded
    for i in range(9):
        mbno=mbno+choice(digits)
    return mbno
#print(get_fake_mbno())

def get_fake_designation():
    designation = choice(designations)
    return designation
#print(get_fake_designation())

def generate_fake_data():
    print('Employee Name: ',get_fake_name())
    print('Employee Number: ',get_fake_num())
    print('Employee Salary: ',get_fake_sal())
    print('Employee City: ',get_fake_city())
    print('Employee Mobile#: ',get_fake_mbno())
    print('Employee Designation: ',get_fake_designation())
    return

for i in range(10):
    generate_fake_data()
    print() ##To print blank line
    
##Output:
Employee Name:  Ossfgsmmgo
Employee Number:  e-0698
Employee Salary:  21737.91
Employee City:  Delhi
Employee Mobile#:  7949870104
Employee Designation:  Project Lead

Employee Name:  Oyrssqrh
Employee Number:  e-9976
Employee Salary:  46940.56
Employee City:  Pune
Employee Mobile#:  8269181529
Employee Designation:  Project Manager

Employee Name:  Fzowrgxaq
Employee Number:  e-1637
Employee Salary:  41216.35
Employee City:  Mumbai
Employee Mobile#:  8924131495
Employee Designation:  Software Engineer

Employee Name:  Xvr
Employee Number:  e-7421
Employee Salary:  38246.23
Employee City:  Delhi
Employee Mobile#:  8729738413
Employee Designation:  Team Lead

Employee Name:  Yzfvxe
Employee Number:  e-3991
Employee Salary:  18375.9
Employee City:  Mumbai
Employee Mobile#:  7143497978
Employee Designation:  Project Lead

Employee Name:  Qijdze
Employee Number:  e-7424
Employee Salary:  16468.34
Employee City:  Chennai
Employee Mobile#:  9060878198
Employee Designation:  Software Engineer

Employee Name:  Nqcj
Employee Number:  e-8928
Employee Salary:  10729.54
Employee City:  Bangalore
Employee Mobile#:  7122227779
Employee Designation:  Senior Software Engineer

Employee Name:  Opxvusgn
Employee Number:  e-2140
Employee Salary:  22548.97
Employee City:  Bangalore
Employee Mobile#:  8985432314
Employee Designation:  Team Lead

Employee Name:  Lpmm
Employee Number:  e-4233
Employee Salary:  45554.06
Employee City:  Mumbai
Employee Mobile#:  6298194298
Employee Designation:  Software Engineer

Employee Name:  Usew
Employee Number:  e-0359
Employee Salary:  38296.86
Employee City:  Chennai
Employee Mobile#:  8767300625
Employee Designation:  Project Lead
