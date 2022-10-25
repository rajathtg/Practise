##Functions in Python: Group of repeatatedily required statements is called functions and use of functions is code reusability.

a = 20
b = 10
print("The Sum:", a+b)
print("The Diff:", a-b)
print("The Product:", a*b)
a = 200
b = 10
print("The Sum:", a+b)
print("The Diff:", a-b)
print("The Product:", a*b)
##Output:
The Sum: 30
The Diff: 10
The Product: 200
The Sum: 210
The Diff: 190
The Product: 2000

###Above code is repeatative hence use below:

def calculate(a,b):
    print("The Sum:", a+b)
    print("The Diff:", a-b)
    print("The Product:", a*b)
calculate(20,10)
calculate(200,10)
##Output:
The Sum: 30
The Diff: 10
The Product: 200
The Sum: 210
The Diff: 190
The Product: 2000

"""Types of functions in Python:
There are two functions
    -Built in functions or predefined functions : These are Python provided functions i.e. id(), type(), print(), eval(), input().....
    -User defined functions / customized functions : These are written by the user to meet requirements ex : calculate in previous example.
Syntax:
    def function_name(parameters):
    '''doc string'''
    body
    return value
In above syntax we're using two keywords
    -def (mandatory)
    -return (optional)
"""

##To call a simple function (we can call it n number of times):
def wish():
    print("Hello friends good evening")
wish()
wish()
wish()
##Output:
Hello friends good evening
Hello friends good evening
Hello friends good evening

##Write a function to take name of the student as input and print wish message by name?
def student(name):
    print("Hello friends good evening from:",name)
    print("Hey Wassup",name,"Good Morning")
student("Durga")
##Output:
Hello friends good evening from: Durga
Hey Wassup Durga Good Morning

##Write a function to take a number as input and print its squaree value??
def squareit(numerical):
    print("The square of the number is :",numerical * numerical)
    sq = numerical * numerical
    print("The square of {} is : {}".format(numerical,sq))
squareit(4)
##Output:
The square of the number is : 16
The square of 4 is : 16

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##Return Statement : A function can return some value based on the business logic.

##Write a function to accept 2 numbers as input and return sum?
def num(numerical1, numerical2):
    sum_value = numerical1 + numerical2
    #return sum_value
print("The sum value is :",num(3, 7))

##Output: Will not throw any error, ideally there should be print statement inside function (like last example) or output needs to be returned only then can be captured in later stages or else it will be none or blank like below.
'''If there is no return statement mentioned explicity then the default return statement or value is none'''
The sum value is : None

def f1():
    print("Hello")
x = f1()
print("The Return Value :",x)

##Output: Because function execution "Hello" is printed, since nothing is returned, the return value of x is None (default return value)
Hello
The Return Value : None


def num(numerical1, numerical2):
    sum_value = numerical1 + numerical2
    return sum_value
print("The sum value is :",num(3, 7))
result = num(10,20)
print("The sum value is :",result)

##Output:
The sum value is : 10
The sum value is : 30

##Write a function to find factorial of given positive one int value?
def factorial(num):
    result = 1
    while num >=1:
        result = result * num
        num = num-1
    return result
print("The value is :",factorial(4))

##Output:
The value is : 24

##Write a function to find factorial for a range of positive int value?
def factorial(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result

for i in range(1, 6):
    print("The factorial of", i, "is :", factorial(i))
    
##Output:
The factorial of 1 is : 1
The factorial of 2 is : 2
The factorial of 3 is : 6
The factorial of 4 is : 24
The factorial of 5 is : 120

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##To return multiple values from a function:

'''In C,Java a method/function can return only one value, but a Python can return multiple values from a function'''

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub
x,y = sum_sub(20,10)
print("The sum :",x)
print("The sub :",y)

##Output:
The sum : 30
The sub : 10

"""Note: In Python a group of comma separated values is called as tuple
ex: return sum,sub (***The brackets are optional), hence internally it is always considered as tuple which is a single value getting returned that contains multiple values"""

def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div
x,y,z,a = calc(20,10)
t = calc(20,10)
print(type(t))
print(t)
print("The sum :",x)
print("The sub :",y)
print("The mul :",x)
print("The div :",y)
print(type(x))
print("The list of values are :")
for i in t:
    print(i)

##Output:
<class 'tuple'>
(30, 10, 200, 2.0)
The sum : 30
The sub : 10
The mul : 30
The div : 10
<class 'int'>
The list of values are :
30
10
200
2.0

##Types of arguments in Python:

def f(a,b):
    print(a+b)
f(10,20)
'''a,b are called as formal parameters and 10,20 are called actual arguments, but ppl interchangeably use the names.
Types of arguments in Python:
-Positional arguments
-Keyword arguments
-Default arguments
-Variable length arguments
'''

##Positional arguments: The order of arguments is imp, a=100 & b=200 in below ex, as simple as seen. Even the number of arguments is also imp, if calculate(100) will throw error.
def calculate(a,b):
    print("The Sum:", a+b)
calculate(100,200)
calculate(100)

##Output:
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 4, in <module>
    calculate(100)
TypeError: calculate() missing 1 required positional argument: 'b'
The Sum: 300

##Keyword arguments: Here the order is not important, but the number of arguments is imp, if calculate(100) will throw error. This is widely used due to flexibility for programmer. We can use both positional & keyword arguments in the programming simultaneously, note that we first need to mention positional argument first and then keyword argument, even the order comes into picture as seen below invalids.
def calculate(a,b):
    print("The Sum:", a+b)
calculate(a=100,b=200)
calculate(b=200,a=300)
calculate(100,b=200) #Valid
#calculate(200,a=300) #Invalid - TypeError: calculate() got multiple values for argument 'a'
#calculate(b=200,300) ##Invalid - SyntaxError: positional argument follows keyword argument


##Output:
The Sum: 300
The Sum: 500
The Sum: 300

##Default arguments:
def wish(name):
    print("Good Morning",name)
#wish() ##Invalid - TypeError: wish() missing 1 required positional argument: 'name'
wish("Durga")

##Output:
Good Morning Durga

'''To overcome above error, we can hardcode parameter value'''
def wish(name = 'Guest'):
    print("Good Morning",name)
wish()
wish("Durga")

##Output:
Good Morning Guest
Good Morning Durga

##Acceptable function definitions:
def wish(name,msg): #Valid
    pass
def wish(name = 'Guest',msg = 'Good Morning'):  #Valid
    pass
def wish(name,msg='Good Morning'):  #Valid
    pass
def wish(name = 'Guest',msg): ##Invalid - SyntaxError: non-default argument follows default argument
    pass

##Variable length argument (also called var arg): We can call the function by passing any number arguments like 0,100,10000,even null... this type argument is called variable length argument.
def f(*n):
    print("Variable length argument function value is :",*n)
f()
f(10)
f(0,10,1000)

##Output:
Variable length argument function value is :
Variable length argument function value is : 10
Variable length argument function value is : 0 10 1000

'''Internally even here n becomes a tuple
f() - Tuple with no value
f(10) - Tuyple with 1 value
f(0,10,1000) - Tuple with 3 values
'''

def f(*n):
    print(type(n))
    print("Variable length argument function value is :",*n)
f()
f(10)
f(0,10,1000)

##Output:
<class 'tuple'>
Variable length argument function value is :
<class 'tuple'>
Variable length argument function value is : 10
<class 'tuple'>
Variable length argument function value is : 0 10 1000

Best example for var-args:
def f(*n):
    total = 0
    for x in n:
        total = total + x
    print("The sum is :",total)
f()
f(30)
for x in range(1,6):
    print("The sum value is :",f(x))
    
##Output:
The sum is : 0
The sum is : 30
The sum is : 1
The sum value is : None
The sum is : 2
The sum value is : None
The sum is : 3
The sum value is : None
The sum is : 4
The sum value is : None
The sum is : 5
The sum value is : None

def f(*n):
    print(n)
f(10,20) #Will lead to creation of tuples
y = f((10,20,30),(40,50,60)) ##Will lead to creation Tuple of tuples, similarly tuple of list/dict is passed, then tuple of list/disct is created.
print(type(f(10,20)))
print(type(y))

##Output:
(10, 20)
((10, 20, 30), (40, 50, 60))
(10, 20)
<class 'NoneType'>
<class 'NoneType'>

++++++++++++++++++

##Combination of normal arguments & variable length arguments:
def f(x,*y):
    print(x)
    print(y)
    for n in y:
        print(n)
f(10)
f(10,20,30,40,50)
f() #Invalid - TypeError: f() missing 1 required positional argument: 'x'

##Output:
10
()
10
(20, 30, 40, 50)
20
30
40
50

'''This function is also valid, pinch, we need to specify the normal argument'''
def f(*x,y):
    print(x)
    print(y)
f(10,20,30,y=40)
f(10,20,30,40) ##Invalid - TypeError: f() missing 1 required keyword-only argument: 'y'

##Output:
(10, 20, 30)
40

##******Below function definition is not possible i.e. more than one variable length can't be defined
def f(*x,*y): ##Invalid - SyntaxError: invalid syntax
    print(x)
    print(y)
f(10,20,30,40)

++++++++++++++++++++++++++++++++++++++++++++++

###*******Explain differences between *args and **kwargs??
#Whatever we tried above are the *args
##Below is the explanation for **kwargs, here dictionary is created unlike the tuples in *args:
##This is called as variable length key-word arguments
def f(**kwargs):
    print(kwargs)
f()
f(name = 'Durga')
f(name = 'Durga', rollno = 101)
f(a=10,b=20,c=30,d=40)
f(10) ##Invalid - TypeError: f() takes 0 positional arguments but 1 was given
f('Durga') ##Invalid - TypeError: f() takes 0 positional arguments but 1 was given

##Output:
{}
{'name': 'Durga'}
{'name': 'Durga', 'rollno': 101}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}

###Using both *args & **kwargs:
def f(*args,**kwargs):
    print(args)
    print(kwargs)
f()
f(10,20,a=30,b=40)
f(a=30,b=40,10,20) ##Invalid - SyntaxError: positional argument follows keyword argument

##Output:
()
{}
(10, 20)
{'a': 30, 'b': 40}

def f(**kwargs,*args): ##Invalid - SyntaxError: invalid syntax
    pass

##Valid conclusion:
def f(*y,x=10):
    print(x)
    print(y)
f(10,20,30,x=10)

def f(x,y,z=4,a=8):
    print(x,y,z,a)
f(1,2)
f(1,2,z=10)
f(1,2,a=100)
f(1,2,z=80,a=100)
f(1,2,a=80,z=100)
f(a=80,y=100,x=34) #Interesting
f(1,2,5,6)
f() #Invalid - TypeError: f() missing 2 required positional arguments: 'x' and 'y'
f(1,2,y=7) #Invalid - TypeError: f() got multiple values for argument 'y'
f(1,2,z=7,k=9) #Invalid - TypeError: f() got an unexpected keyword argument 'k'
f(1,2,5,6,7) #Invalid - TypeError: f() takes from 2 to 4 positional arguments but 5 were given
f(z=190,3,4) #Invalid - SyntaxError: positional argument follows keyword argument

##Output:
1 2 4 8
1 2 10 8
1 2 4 100
1 2 80 100
1 2 100 80
34 100 4 80
1 2 5 6

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##In functional programming we have two types of variables:
#Local variable : The variables declared inside function
#Global variable : The variables declared outside function

a=10 ##Global variable
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()

##Output:
10
10

def f1():
    a=10 ##Local variable
    print(a)
def f2():
    print(a) ##Invalid - NameError: name 'a' is not defined
f1()
f2() 

'''In Python global & local variable can have same name'''
a=10 ##Global variable
def f1():
    a=100 ##Local variable
    print(a)
def f2():
    print(a)
f1()
f2()

##Output:
100 ##Interesting
10

a=10 ##Global variable
def f1():
    global a #This bring the global variable available to the function for req modification
    a=100 ##Changing value of global variable 
    print(a)
def f2():
    print(a)
f1()
f2()

##Output:
100
100

'''To make local variable inside the function as global and below'''
def f1():
    #global a = 10 ##Invalid - SyntaxError: invalid syntax
    global a ##Make it global and declare it separately
    a=100
    print(a)
def f2():
    print(a)
f1()
f2()

##Output:
100
100

a=10
def f1():
    print(a)
    global a #Invalid - SyntaxError: name 'a' is used prior to global declaration
    a=100
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    print(a) #Invalid - UnboundLocalError: local variable 'a' referenced before assignment
    a=100
    print(a)
def f2():
    print(a)
f1()
f2()

'''To get global variable inside the function by overriding the local variable, use below way'''
a = 888
def f1():
    a = 999
    print(a) #a=999
    print(globals()) #{'__name__': '__main__','a':888....etc} In the form of dict it prints all the available global values
f1()

##Output:
999
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000023944D502E0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\91961\\PycharmProjects\\pythonProject\\Web\\Udemy.py', '__cached__': None, 'a': 888, 'f1': <function f1 at 0x0000023944C73E20>}

'''To get specifically required value'''
a = 888
def f1():
    a = 999
    print(a) #a=999
    print(globals().get('a'))
    print(globals()['a'])
f1()

##Output:
999
888
888

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Recursive functions: The function that calls itself is called recursive function, helps in solving the complex problems very easily, when used the length of code will be reduced.

'''Theoretical Concept:
3! = 3 * 2!
   = 3 * 2 * 1!
   = 3 * 2 * 1 * 0!
   = 3 * 2 * 1 * 1
   = 6
n! = n * (n-1)!
'''

def factorial(n):
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1) #Here the factorial function internally calls factorial function, this is recursion
    return  result
print("factorial of 4 is :",factorial(4))
for i in range(0,11):
    print("factorial of {} is : {}".format(i,factorial(i)))

##Output:
factorial of 4 is : 24
factorial of 0 is : 1
factorial of 1 is : 1
factorial of 2 is : 2
factorial of 3 is : 6
factorial of 4 is : 24
factorial of 5 is : 120
factorial of 6 is : 720
factorial of 7 is : 5040
factorial of 8 is : 40320
factorial of 9 is : 362880
factorial of 10 is : 3628800

###Internal tracing for recursive function:

def factorial(n):
    print("Execution of factorial function for n :",n)
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)
    print("Returning factorial({}) is : {}".format(n,result))
    return  result
print(factorial(3))

##Output: 
Execution of factorial function for n : 3
Execution of factorial function for n : 2
Execution of factorial function for n : 1
Execution of factorial function for n : 0
Returning factorial(0) is : 1
Returning factorial(1) is : 1
Returning factorial(2) is : 2
Returning factorial(3) is : 6
6

###Max to what depth the recursion function will be executed:
count = 0
def factorial(n):
    global count
    count = count + 1
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)
    return  result
print(factorial(997))
print("The number of times factorial function is executed :",count)

##Output:
403597244616453902342926527652907402110903352461393891430307973735196631901068423726375883385358710213700663198466197719394411318126551961682447808198924968051643330792790545975658652366984953410102994729193397927862707860663312211428139657339199210288839829245965893084586772188847949801354437616450752245066665598898009417557796737695167521343249479413631414534202184726421479392615730781173164526393982880263279118925406206180689438683308644696334133955184235540077242451165903811018277198321800315958279899941381566151490917379981054549852483223292752438981198080270888254399197574536460570473430371595872403169486757166154294941258045311241382930836862005052391967478429035362983199050663230586866257612402804942403442331663944341683350732204123565349869446216232111598995678724462182568501131746383857706790400107507266739002631612931124112227909672935742104968533278074796000335855930432060517447195226436187301231195091058916141500005034486568847599649004940677693185232218378659444854645703908824934015144550035704605317977378620311855095356769488892217130200011250491151641531090120083765159221969755314437880209281708574493693840125338722070514029362985801732618715060934298236579096167095859504053310608725711198457200226544350445941157734863407428532431126485686678788466148681975019174010453297639004006819520704463840773528691224455265229985489764356909675383800245969276679872407757924211918488179598530382266647547907226165479802976547896939656888813256826539067915695278878516257396920983511389029563101112325372395464739783143361362879872578550147571168136083391354242735142803988735616917749898060073075542403509536490539404444972668319521415425667918323473675966566332390993259591959049424070380861864682206986463729281557338747466546627859206287571996491606797979064142819469589200812679026561288124087136359830959867034513441434850212864818601504529520195828528045600869420646442863720485414968365312690523835026508545772659712105161137693595262919371358840019473383802028344531181679417716563013501242477291139042422814166369601152223293596957527530934652046662174154235850073391729650007182794396630407081318880947107940245036774649857429379220776637356890211596540009349092255988047909417594778375705723841918167663026277009033939654785671715045122185315730249393616044737902170116980736000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
The number of times factorial function is executed : 998

##Note: max is factorial(997) and for factorial(998) we get below error:
RecursionError: maximum recursion depth exceeded in comparison

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##The function without any name or nameless functions is called Anonymous function or Lambda functions:
##This the function used for Instant usage, hence it generally doesn't need name, ex(conductor name we don't care while travelling in bus, only usage of him is for getting the ticket, that's it).
##Concise code and readability will increase.
##Lambda function is used for one time use or instant use.

##This is normal function, because this has a name.
def squareit(n):
    return n*n

##This is nameless function, lambda function:
s = lambda n : n*n ##lambda input.arguments : expression
print(s(4))

##Output:
16

s = lambda a,b : a+b
print(s(10,20))

##Output:
30

##Lambda function to find biggest of given numbers:
##Two input values:
bigger = lambda a,b : a if a > b else b
print(bigger(10,20))
print(bigger(-10,-20))

##Output:
20
-10

##Three input values:
bigger = lambda a,b,c : a if a > b and a > c else b if b > c else c
print(bigger(10,2,3))

##Output:
10

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##We require to pass function as argument to another function, below are the function which can accept another function as argument and it can be achieved using lambda:
#filter(function,sequence) : If input has 10 elements, then output will have <=10.
#map(function,sequence) : If input has 10 elements, then output will also have 10 elements.
#reduce(function,sequence) : If input has 10 elements, then output will have only 1 element. Reduce needs to be imported from functools.

##Without filter function:
l = [1,2,3,4,5,6,7,8,9,10]
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1 = []
for n in l:
    if isEven(n) == True:
        l1.append(n)
print(l1)
print(type(l1))

##Output:
[2, 4, 6, 8, 10]
<class 'list'>

##With filter function:
l = [1,2,3,4,5,6,7,8,9,10]
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1 = filter(isEven,l)
print(l1)
print(type(l1))
l2 = list(filter(isEven,l))
print(l2)
print(type(l2))

##Output:
<filter object at 0x000001DDBDA61570>
<class 'filter'>
[2, 4, 6, 8, 10]
<class 'list'>

##Lambda & Filter together:
l = [1,2,3,4,5,6,7,8,9,10]
l1 = lambda n : n%2 ==0
l2 = list(filter(l1,l))
print(l2)
print(type(l2))

##Output:
[2, 4, 6, 8, 10]
<class 'list'>

##Example 2, filter function():
p=[0,1,2,3,4,5,6,7,8,9,10]
even_no = list(filter(lambda n:n%2==0,p))
print("List of even_nos are: ",even_no)
odd_no = list(filter(lambda n:n%2!=0,p))
print("List of odd_nos are: ",odd_no)

##Output:
List of even_nos are:  [0, 2, 4, 6, 8, 10]
List of odd_nos are:  [1, 3, 5, 7, 9]
List of numbers divisible by 3 and odd are: [3, 9]

##Example 3, filter function():
heroines = ['Katrina', 'Kareena', 'SunnyLeone', 'Piggy']
startswithK = list(filter(lambda n:n[0]=='K', heroines))
print("Heroines name starting with 'K' are: ",startswithK)
lengthby5 = list(filter(lambda n:len(n)%5 == 0, heroines))
print("Heroines divisible by 5 are: ",lengthby5)
odd = list(filter(lambda name:len(name)%2!=0,heroines))
print("Heroines name with odd length are: ",odd )

##Output:
Heroines name starting with 'K' are:  ['Katrina', 'Kareena']
Heroines divisible by 5 are:  ['SunnyLeone', 'Piggy']
Heroines name with odd length are:  ['Katrina', 'Kareena', 'Piggy']

-----------------------------------------------------------------------------------
##Map() : For every elements in the list/sequence apply new function and generate new value.

l = [1,2,3,4,5]
def squareIt(n):
    return n*n
l1 = list(map(squareIt,l))
print("Square result of each element is: ",l1)

squareIt_lambda=list(map(lambda n:n*n,l))
print("Square result of each element is: ",squareIt_lambda)

##Output:
Square result of each element is:  [1, 4, 9, 16, 25]

##Let's try it on multiple sequences:
##Syntax : map(lambda x,y:x*y,take x value from list1,y value from list2)
##Syntax : map(lambda x,y:x*y,l1,l2)
l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=list(map(lambda x,y:x*y,l1,l2))
print("The mul value of two lists is: ",l3)

##Output:
The mul value of two lists is:  [5, 20, 45, 80, 125]

****Note: In the above list if one of them have lesser or more elements compare to other, then the extra elements will be ignored.

l1=[1,2,3,4,5,6,7,8]
l2=[5,10,15,20,25,30]
l3=list(map(lambda x,y:x*y,l1,l2))
print("The value of the mul is: ",l3)

##Output:
The value of the mul is:  [5, 20, 45, 80, 125, 180]

##Multiple lists is also possible:
l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=[5,4,3,2,1]
l4=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print("The mul value of two lists is: ",l4)

##Output:
The mul value of two lists is:  [11, 16, 21, 26, 31]

-------------------------------------------------------------------------
##Reduce() function: Reduce () function reduces sequence of elemts into a single element by applying the specified function.
from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
result1=reduce(lambda x,y:x*y,l)
print("The output value is: ",result)
print("The output value is: ",result1)

##Output:
The output value is:  150
The output value is:  12000000

##Find the Sum of first 100 Numbers by using reduce() function?
from functools import reduce
l=range(1,101)
result=reduce(lambda x,y:x+y,l)
print("The value of sum of first 100 numbers is: ",result)

##Output:
The value of sum of first 100 numbers is:  5050

Logic:
n*(n+1)/2 = 100*(100+1)/2 = 5050

