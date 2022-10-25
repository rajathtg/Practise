####**********Decorator Functions:
-In Python everything is Object, yes, even the class, function is also an object.
-Even FUnction is also internally considered as an object only.
-For the existing function, we can give another name, which is nothing but function aliasing.
-If we delete one name, still we can access that function by using alias name.
-Declaring one function inside another function is called nested function. 

#Example:
def f1():
    print('Hello')
print(f1)
print(id(f1))

##Output:
<function f1 at 0x0000023D18993E20> ##This says it's a function type object located at address 0x0000023D18993E20
2461428956704

##Function Aliasing: For existing function if we're giving another name, it is called function aliasing.
def wish(name):
    print('Good Morning: ',name)
greeting=wish ##Aliasing ##Now both wish and greeting is pointing to same object. Both wish and greeting are reference variables.
print(id(wish))
print(id(greeting))
wish('Durga')
greeting('Durga')
del wish ##We're deleting wish
greeting('Sunny') ##Still we can use other name, i.e. greeting to still continue with the program.

##Output:
1543905623584
1543905623584
Good Morning:  Durga
Good Morning:  Durga
Good Morning:  Sunny

##Nested function:
def outer():
    print('Outer function execution started')
    def inner():
        print('Inner function execution')
    print('Outer function execution completed')
outer()
inner() ##NameError: name 'inner' is not defined. Did you mean: 'iter'? - The inner() function is local to outer() and we can't call it outside.

##Ouput:
Outer function execution started
Outer function execution completed

def outer():
    print('Outer function execution started')
    def inner():
        print('Inner function execution')
    inner() ##Calling inner function and we can call inner function any number of times
    inner()
    inner()
    print('Outer function execution completed')
outer()

##Output:
Outer function execution started
Inner function execution
Inner function execution
Inner function execution
Outer function execution completed

--------------------------------------------------------------------------------

##Function as return value and argument to another function:

##Example1:
def outer():
    def inner():
        print('inner function execution')
    return inner
f1=outer() ##This is a outer() function call and this will return inner function object, to save inner returned object we are using f1 variable, this f1 variable will acts as reference variable pointing to the same objectnpointed by inner and also as aliasing for inner.
f1() ##Here the outer() function returns inner() function

##Output:
inner function execution

##Example2:
def outer():
    def inner():
        print('inner function execution')
    return inner()
##return inner : Here it returns inner function object
##return inner() : Here the inner method call will be executed, that inner method call will return something, that returned value will be returned again.
##If we want a function to return another function then usage of () needs to be prohibited, it is not function call.
outer()

##Output:
inner function execution

##Example3:
def outer():
    def inner():
        print('inner function execution')
    return inner
outer ##No ouput
outer() ##No ouput
f1=outer ##No ouput
f1() ##No ouput
f1=outer()
f1() ##inner function execution

##*******Diff between f1=outer and f1=outer() 
-Outer without () is called just a outer object, if we use outer(), then it is outer function call.
-f1=outer is called function aliasing.
-f1=outer() here outer() will return inner function object for that object f1 will act as a reference variable.

##Example3: Passing one function as an argument to other
def f1(func):
    func()
def f2():
    print('f2 function')
f1(f2) ##Here we're calling f1 by passing f2 as an argument, then f2 will become func. Therefore, whenever we're calling func() internally which function will be executed? it's f2

##Output:
f2 function

##Example4:
filter(function,list)
map(function,list)
reduce(function,list)
##In the above example filter,map and reduce all three are functions and to which we're passing one more function.

----------------------------------------------------------------------------------

##Decorator:
-Basically it is also a function, acts as a beauty parlour which takes in one function, decorate it and provide an output.
-Syntax:
def decorator_function(input_function):
    def output_function():
        Add extra power
    return output_function
    
-Decorator is a function which can take a function as argument and extend its functionality and returns modified function with extended functionality.
-The main objective of decorator functions is we can extend the functionality of existing function without modifying that function.

##Example1:
def display():
    print('Showing a person as it is') ##Then marriage is cancelled.
display()

##Output:
Showing a person as it is

##Example2:
def decor(func):
    def inner():
        print('Send the person to Beauty Parlour')
        print('Showing a person with full of decoration')
    return inner
##The decorator is defined and ready
##Let's associate the decorator with our display function
@decor
def display():
    print('Showing a person as it is')
display()
##By default whenever we call a function, Pyhton will check is there any decorator configured for the given function.
##If there is any decorator then PVM will not execute display(), instead it will look for the decorator, the return function of the decorator needs to be executed.
##@decor ===> display() ===> decor(display()) ====> return inner ===> print('Send the person to Beauty Parlour') and print ('Showing a person with full of decoration')
##Without decor output will be same as example1.
##**************The number of arguments for display() and inner() should match or else it will not work.

##Output:
Send the person to Beauty Parlour
Showing a person with full of decoration

##Example3:
def decor(func):
    def inner():
        print('Send the person to Beauty Parlour')
        print('Showing a person with full of decoration')
    return inner
##We don't have a decor
def display():
    print('Showing a person as it is')
display()

##Output:
Showing a person as it is

-----------------------------------------------------------------------------

##Demo program2:
===============

##Example1:
def add(a,b):
    print(a+b)
add(10,20)

##Output:
30

##Example2 : With Decorator
def decor_for_add(func):
    def inner(a,b): ##Need to have same set of arguments as of add()
        print('#'*30)
        print('The Sum: ',end='') #End is used make sure the value is not printed in next line, to check what it is, try removing it and executing.
        func(a,b) ##This prints data from print(a+b) of below add function.
        print('#'*30)
        #print('The Sum: ',a+b) ##Use this and avoid confusion of using end='' and func(a,b) ;)
    return inner
@decor_for_add
def add(a,b):
    print(a+b)
add(10,20)
'''
Execution Steps:
-Once add(10,20) is called, PVM will check any decorator is defined for it or not.
-If decorator is present, PVM will execute it, by passing add as input to decor_for_add, i.e. decor_for_add(add)
-Since decorator decor_for_add(add) returns inner, therefore it will call inner function.
-Then the inner(10,20) will be executed.
-'#' will be printed 30 times and so on
'''

##Output:
##############################
The Sum:  30
##############################

-----------------------------------------------------------------------------

##Example3:
def decor(func):
    def inner(name): ##No. of argument should be same
        if name=='Sunny':
            print('#'*50)
            print("Hello Sunny, you're very important for us")
            print('Very very Good Morning')
            print('#'*50)
        else:
            func(name)
    return inner
@decor ##If decorator is not required, then we can remove @decor
def wish(name):
    print('Good Morning: ', name)
wish('Durga')
wish('Sunny')

##Output:
Good Morning:  Durga
##################################################
Hello Sunny, you're very important for us
Very very Good Morning
##################################################

##Example4:
def decor(func):
    def inner(name):
        names=['CM','PM','Minister']
        if name in names:
            print('#'*50)
            print("Hello {}, you're very important for us".format(name))
            print('Very very Good Morning')
            print('#'*50)
        else:
            func(name)
    return inner
@decor
def wish(name):
    print('Good Morning: ', name)
wish('CM')
wish('PM')
wish('Sunny')

##Output:
##################################################
Hello CM, you're very important for us
Very very Good Morning
##################################################
##################################################
Hello PM, you're very important for us
Very very Good Morning
##################################################
Good Morning:  Sunny

##Example5:
def division(a,b):
    print(a/b)
division(10,2)
division(10,0)

##Output:
5.0
ZeroDivisionError: division by zero

##Example6:
def smart_division(func):
    def inner(a,b):
        if b==0:
            print('Hello Stupid, How we can divide with 0')
        else:
            func(a,b)
    return inner
@smart_division
def division(a,b):
    print(a/b)
division(10,2)
division(10,0)

##Output:
5.0
Hello Stupid, How we can divide with 0

##Summary:
-Decorator function should be defined first and the we can use:
-While defining decorator, the number of arguments must be matched.

--------------------------------------------------------------------------------

##To call same function with and without Decorator:

def decor(func):
    def inner(name): ##No. of argument should be same
        if name=='Sunny':
            print('#'*50)
            print("Hello Sunny, you're very important for us")
            print('Very very Good Morning')
            print('#'*50)
        else:
            func(name)
    return inner

def wish(name):
    print('Good Morning: ', name)
decorated_wish=decor(wish) ##Cool!!
wish('Durga')
wish('Sunny')
decorated_wish('Durga')
decorated_wish('Sunny')

##Output:
Good Morning:  Durga
Good Morning:  Sunny
Good Morning:  Durga
##################################################
Hello Sunny, you're very important for us
Very very Good Morning
##################################################

--------------------------------------------------------------------------------

##Decorator Chaining: Multiple decorators can be configured for one function.
##We can define multiple decorators for the same function and all these decorators will form decorator chaining.

def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        func()
    return inner1
@decor1
def f():
    print('Original function')
f()

##Output:
Decorator1 Execution
Original function

def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        func()
    return inner2
@decor2
def f():
    print('Original function')
f()

##Output:
Decorator2 Execution
Original function

##Let's merge both:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        func()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        func()
    return inner2
@decor2
@decor1
def f():
    print('Original function')
f()

##*****f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output)

##Output:
Decorator2 Execution
Decorator1 Execution
Original function

##Let's advance a little:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        ##func()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        ##func()
    return inner2
@decor2
@decor1
def f():
    print('Original function')
f()

##*****f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output)

##Output:
Decorator2 Execution

##Let's advance a little  by changing decor order:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        ##func()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        ##func()
    return inner2
@decor1
@decor2
def f():
    print('Original function')
f()

##*****f() >>> decor2 >>> inner2(decor2 output) >>> decor1 >>> inner1 (decor1 output)

##Output:
Decorator1 Execution

----------------------------------------------------------------------------------

##Example1:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        ##func()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        func()  ##*****calls input function of inner2 i.e. it calls inner1
    return inner2
@decor2
@decor1
def f():
    print('Original function')
f()

##*****f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> func() (inner2 calls it's input function i.e. inner) >>> inner1

##Output:
Decorator2 Execution
Decorator1 Execution

##Example2:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        func() ##*******calls input function of inner1 i.e. f()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        func()  ##*****calls input function of inner2 i.e. it calls inner1
    return inner2
@decor2
@decor1
def f():
    print('Original function')
f()

##*****f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> func() (inner2 calls it's input function i.e. inner) >>> inner1 >>>  func() (inner1 calls it's input function i.e. f())

##Output:
Decorator2 Execution
Decorator1 Execution
Original function

##Example3:
def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        ##func()
    return inner1
def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        f()  ##*****calls actual input function i.e. f()
    return inner2
@decor2
@decor1
def f():
    print('Original function')
f()

##*****f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> f() >>> decor1 >>> inner1 (decor1 output) >>> decor2 >>> inner2 (decor2 output) >>> ...................

##Output:
Decorator2 Execution
Decorator2 Execution
Decorator2 Execution
Decorator2 Execution
Decorator2 Execution
:
:
:
:
RecursionError: maximum recursion depth exceeded while calling a Python object

--------------------------------------------------------------------------------------

##Final Demoprogram on Decorator Chaining:
-----------------------------------------

##Example1:
def decor1(func):
    def inner1():
        x=func() ##****num() will be called and consider return value i.e. 20
        return x * x
    return inner1
@decor1
def num():
    return 20
print(num())

##num() >>> decor1 >>> inner1() >>> num() >>> 20 * 20

##Output:
400

##Example2:
def decor1(func):
    def inner1():
        x=func() ##****num() will be called and consider return value i.e. 20
        return x * x
    return inner1
def decor2(func):
    def inner2():
        x=func() ##****num() will be called and consider return value i.e. 20
        return x * 100
    return inner2
@decor2
def num():
    return 20
print(num())

##num() >>> decor2 >>> inner2() >>> num() >>> 20 * 100

##Output:
2000

##Example3:
def decor1(func):
    def inner1():
        x=func() ##****num() will be called and consider return value i.e. 20
        return x * x
    return inner1
def decor2(func):
    def inner2():
        x=func() ##****inner1 is the input and it's returned value i.e. 400 will be called
        return x * 100
    return inner2
@decor2
@decor1
def num():
    return 20
print(num())

##num() >>> decor1 >>> inner1() >>> num() returned value >>> 20 * 20 >>> decor2 >>> inner2() >>> inner1() returned value >>> 400 * 100

##Output:
40000

##Example4:
def decor1(func):
    def inner1():
        x=func() ##****inner2 is the input and it's returned value i.e. 2000 will be called
        return x * x
    return inner1
def decor2(func):
    def inner2():
        x=func() ##****num() will be called and consider return value i.e. 20
        return x * 100
    return inner2
@decor1
@decor2
def num():
    return 20
print(num())

##num() >>> decor2 >>> inner2() >>> num() returned value >>> 20 * 100 >>> decor1 >>> inner1() >>> inner2() returned value >>> 2000 * 2000

##Output:
4000000