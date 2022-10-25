##The three important terms of Oops:
-Class (Model Name Sony KD-65)
-Object (Actual TV at Home)
-Reference variable (TV Remote)

1. Class is a blue-print/template/plan/model/design.
        defines data members/attributes and behaviours/methods of object.
2. Object is a physical existance of a class / an instance of a class.
3. Reference variable is used to refer an object, using this we can perform required operations on the object and we can access properties and methods of an object.
-For one class we can create multiple objects.
-For one object we can have any number of reference variables.
-Objects without any reference variable it is useless, will be cleared by Garbage Collectors.

---------------------------------------------------------------------------
##How to define a class?

##Syntax:
class classname :
    '''documentation string : contains description about class'''
    variables ##properties/attributes required for every object
    methods ##actions/behaviours
print(classname.__doc__)
help(classname)

  
##Example:
class Student:
    '''This class developed by Durga for Demo'''
    #variables
    #methods
print(Student.__doc__)
help(Studnet)

##Output:
This class developed by Durga for Demo
Help on class Student in module __main__:

class Student(builtins.object)
 |  This class developed by Durga for Demo
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 
##Within Python class, 3 types of variables are allowed:
-Instance Variables (Or Object level variables)
-Static Variables (Or class level variables)
-Local Variables (Or method level variables)

##Within Python class, 3 types of methods are allowed:
-Instance Methods
-Class Methods
-Static Methods

##Syntax of Object:
reference_variable = classname()

##How to define a class:
*****Functions defined inside class is called methods:

class Student:
    '''class developed by Durga for demo'''
    def __init__(self):     #Method     -|
        self.name = 'Durga' #Variables  -|-->>This section is called as an constructor and auto executes once object is created.
        self.rollno = 101   #Variables  -|
        self.marks = 90     #Variables  -|
    def talk(self):         #Method
        print("Hello I am: ",self.name)
        print("My roll no: ",self.rollno)
        print("My marks are: ",self.marks)
s=Student() ##Student object is created, s is reference variable, now an object with name='Durga',rollno=101,marks=90 is created(this object with name,rollno,marks is created, because whenever we create an object the special method __init__ alias constructor gets auto executed ), with reference variable we can access variables and also call  methods/properties of an object by using below print statement.
print(s) ##<__main__.Student object at 0x000002A30C060E20>
##Accessing Variables
print(s.name)  ##Durga
print(s.rollno) ##101
print(s.marks)   ##90
##Output:
Durga
101
90

##Calling Methods
s.talk()    ##No need to pass self argument, it is taken by pythong interpretor, now immediately the method talk is called and executed.
##Output:
Hello I am:  Durga
My roll no:  101
My marks are:  90

###Example 2:
class Student:
    '''class developed by Durga for demo'''
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello I am: ",self.name)
        print("My roll no: ",self.rollno)
        print("My marks are: ",self.marks)
s1=Student('Sunny',69,96)
s2=Student('Bunny',95,20)
print(s1)
s1.talk()
print(s2)
print(s2.name)
print(s2.rollno)
print(s2.marks)
s2.talk()

##Output:
<__main__.Student object at 0x0000018C30023F10>
Hello I am:  Sunny
My roll no:  69
My marks are:  96
<__main__.Student object at 0x0000018C30023EB0>
Bunny
95
20
Hello I am:  Bunny
My roll no:  95
My marks are:  20

------------------------------------------------------------------------

##Self Variable:
##What is self in "def __init__(self,anme,rollno.....)" ??
##The self is reference variable, which is always pointing to current object. Within a Python class if we want to access current object or refer a current object we need a reference variable i.e. nothing but self variable.

class Test:
    def __init__(self):
        print('Address of object pointed by self: ',id(self))
t=Test() ##An object is created, t can be used outside of the class and not within class, if we want to access current object, we need a reference variable therefore use self for it. How to know whether self is pointing to current object.
print('Address of object pointed by t: ',id(t))

##Output:
Address of object pointed by self:  2247735119728
Address of object pointed by t:  2247735119728

class Test:
    def __init__(self):  ##Constructor
        print('Constructor')
    def m1(self,x): ##Instance Method
        print('x value: ',x)
##*****The first argument for constructor and instance method is always a self, it's mandatory.....
t=Test() ##The object is created immediately and by default constructor is executed. Here we're not required to pass value/argument for the self variable , it's auto taken care by Python virtual machine. We're not responsible to pass argument to the self variable at the time of calling the instance method / constructor....
t.m1(10) ##Here we're passing value for x and not self variable.

##Output:
Constructor
x value:  10


class Student:
    '''class developed by Durga for demo'''
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello I am: ",self.name)
        print("My roll no: ",self.rollno)
        print("My marks are: ",self.marks)
s1=Student('Sunny',69,96) ###Here student object is created and immediately constructor is executed, within constructor we have self.name, it means current object name variable will be created and we're assigning value Sunny. |||ly for self.roll_no & self.marks. For which purpose we're using Self inside the constructor??, it's used to declare instance variable. 
s2=Student('Bunny',95,20)
print(s1)
s1.talk() ###One more important conclusion, we can also use self to access the instance variable :). print("Hello I am: ",self.name) we're getting the value of self.name, it's pulled from the current object created at the step of constructor.
print(s2)
print(s2.name)
print(s2.rollno)
print(s2.marks)
s2.talk()

###We use self variable for two purpose, one is to declare a instance variable and also to access the values of instance variable.

----------------------------------------------------------------------------
##Whether self is a keyword in Python?? It's not a keyword in Python, instead of self we can use delf and kelf as seen in the below example, it's not recommended though, universally accepted is self.
##Here delf and kelf both act as reference variable to current object, same as self, hence the program still executes without any issue
##The first argument is important, but not the name used, first argument used is implicit (Implicit variables are variables that you do not define. These variables are automatically provided by the framework) argument pointing to current object.
###The self variable can only be used within the class and outside of the class it's not useful. Outside of a class if we want access object we can use normal reference variables like s1, s2 etc............

class Student:
    '''class developed by Durga for demo'''
    def __init__(delf,name,rollno,marks):
        delf.name = name
        delf.rollno = rollno
        delf.marks = marks
    def talk(kelf):
        print("Hello I am: ",kelf.name)
        print("My roll no: ",kelf.rollno)
        print("My marks are: ",kelf.marks)
s1=Student('Sunny',69,96)
s2=Student('Bunny',95,20)
print(s1)
s1.talk()
print(s2)
print(s2.name)
print(s2.rollno)
print(s2.marks)
s2.talk()

##Output:
<__main__.Student object at 0x0000016ACE7E3F10>
Hello I am:  Sunny
My roll no:  69
My marks are:  96
<__main__.Student object at 0x0000016ACE7E3EB0>
Bunny
95
20
Hello I am:  Bunny
My roll no:  95
My marks are:  20

##Example2:
class Student:
    '''class developed by Durga for demo'''
    def __init__(name,rollno,marks): ###Here name becomes the implicit variable like self as it is first variable. Remaining two act as explicit variables.
        delf.name = name
        delf.rollno = rollno
        delf.marks = marks
    def talk(kelf):
        print("Hello I am: ",kelf.name)
        print("My roll no: ",kelf.rollno)
        print("My marks are: ",kelf.marks)
s1=Student('Sunny',69,96)  ###It's wrong to pass 3 arguments, as it only accepts rollno and marks and first arg is implicit.
s2=Student('Bunny',95,20)
print(s1)
s1.talk()

##Output:
Traceback (most recent call last):
  File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 11, in <module>
    s1=Student('Sunny',69,96)  ###It's wrong to pass 3 arguments, as it only accepts rollno and marks and first arg is implicit.
TypeError: Student.__init__() takes 3 positional arguments but 4 were given
###Here it says 4 because We provided 3 and one additional value was provided by Python PVM for self hence count is 4.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###Constructor: It's a special method in Python, the name of the constructor is always __init__ whatever happens hum nahi badhlenge.
#syntax:
class Test:
    def __init__(self):
        print('constructor execution...')
t1=Test()
t2=Test()
t3=Test()
##Whenever object is created constructor is executed, for every object it gets executed only once.

##Output:
constructor execution...
constructor execution...
constructor execution...

##Purpose of constructor: We know that constructor is executed at the time of object creation, then what's the purpose?, it's for declare,create and initialize the instance variables.

####Example1:
class Student:
    def __init__(self,name,rollno,marks):
        print('Creating instance variables and performing initialization....')
        self.name=name
        self.marks=marks
        self.rollno=rollno
##Let's create student object:
s1=Student('Sunny',101,90)
s2=Student('Bunny',102,95)
##The object is created, constructor is executed, s1 is the reference variable, the three arguments ('Sunny',101,90) will become arguments to (name,rollno and marks) within that self.name=name it is responsible for declaring instance variable as name (self.name=name) and it's value is assigned i.e. 'Sunny', |||ly rollno=101 and marks=90.
##Output:
Creating instance variables and performing initialization....
Creating instance variables and performing initialization....

####Example2:
class Student:
    def __init__(self,name,rollno,marks):
        print('Creating instance variables and performing initialization....')
        self.name=name
        self.marks=marks
        self.rollno=rollno
##Let's create student object:
s1=Student('Sunny',101,90)
s2=Student('Bunny',102,95)
print(s1)
print(s1.name,s1.marks,s1.rollno)
print(s2.name,s2.marks,s2.rollno)

##Output:
Creating instance variables and performing initialization....
Creating instance variables and performing initialization....
<__main__.Student object at 0x000001F4A0390F70>
Sunny 90 101
Bunny 95 102

##Note:
##For construct we can take any number of arguments, atleast one argument and that argument needs to be self.

------------------------------------------------------------------------
##Example3:
class Test:
    def m1(self):
        print('method')
s1=test() ##Creating an object
s1.m1() ##Calling the method

##Output:
method

###*****Note: The constructor is always optional inside a class, if there is no constructor then Python will internally create it's own/default constructor.

##Example4:
class Test:
    def __init__(self):
        print('Hi Constructor...')
    def m1(self):
        print('method')
t=Test() ##Here we're creating object, constructor is executed automatically.
t.__init__() ##Here we're calling constructor explicitly, hence constructor will be executed, but no new object is created. Therefore ottu 4 times constructor executed, but the object is created only once when t=Test().
t.__init__()
t.__init__()

##Output:
Hi Constructor...
Hi Constructor...
Hi Constructor...
Hi Constructor...

##Example5:
class Test:
    def __init__(self):
        print('No argument constructor....')

    def __int__(self, x):
        print('One argument constructor...')
####Upto any object is created above class is valid.
t1 = Test() ###we will get Type error missing 1 required positional argument:
t2 = Test(10)  ###This is valid and we will get 'One argument constructor...'

###****If two methods with same names, but different arguments is called as overloaded methods. This concept is not there in Python :((...........
###Out of __init__(self) and __init__(self,x) The __init__(self,x) is executed by PVM, therefore when only t1=Test() object is created, we will get Type error missing 1 required positional argument, but when t1=Test(10) it will perfectly executed.
###By default always PVM considers last or latest constructor method even though there are 100 cons
tructors with same name.

Summary:
-Constructor is a special method in python.
-The name of the constructor is always: __init__()
-We are not required to call constructor explicitly. Whenever we are creating an object, automatically constructor will be executed.
-Per object constructor will be executed only once.
-The main purpose of the constructor is to declare and initialize instance variables.
-Constructor can take atleast one argument.(atleast self).
-Within the class constructor is optional. If we are not writing constructor, then Python will provide default constructor.
-Based on our requirement we can call constructor explicitly, then it will be executed just like a normal method.
-Overloading concept is not applicable for constructors. Hence we cannot define multiple constructors within the same class. If we're trying to define multiple constructors, only last constructor will be considered.
---------------------------------------------------------------------------

##Mini application to explain OOPS:

class Movie:
    '''This class is developed by Durga for Demo'''
    def __init__(self,title,hero,heroine): ###title,hero,heroine are the Local/temporary variables to hold provided values at the time creating an object, we can also use a,b,c. The names are not important.
        self.title=title    #-----|
        self.hero=hero      #-----|---->>>self.title,hero,heroine are the Instance Variables, The self.title...are very important unlike local variables, hence called as Standard, better to match local variables same as self.title to avoid confusion.
        self.heroine=heroine#-----|
        
    def info(self):
        print('Movie name: ',self.title)
        print('Hero name: ',self.hero)
        print('Heroine name: ',self.heroine)
list_of_movies=[]
while True:
    title=input('Enter Movie Name: ')
    hero=input('Enter Hero Name: ')
    heroine=input('Enter Heroine Name: ')
    m=Movie(title,hero,heroine) ##An object is created and constructor is executed and all the self.title, hero & heroine is holding the respective inputted values.
    list_of_movies.append(m)
    print('Movie added successfully...')
    option=input('Do you want to add one more Movie[y/n]??: ')
    if option.lower()=='n':
        break
print()
print('All movies Information...')
for movie in list_of_movies: ##we can also write for 'x' in list_of_movies
    movie.info() ##We're calling the info() method defined inside the class.
    print()
    
##Output:
Enter Movie Name: Bahubali
Enter Hero Name: Prabhas
Enter Heroine Name: Eesha Rebba
Movie added successfully...
Do you want to add one more Movie[y/n]??: y
Enter Movie Name: KGF2
Enter Hero Name: Yash
Enter Heroine Name: iamHumq
Movie added successfully...
Do you want to add one more Movie[y/n]??: n

All movies Information...
Movie name:  Bahubali
Hero name:  Prabhas
Heroine name:  Eesha Rebba

Movie name:  KGF2
Hero name:  Yash
Heroine name:  iamHumq

###The details of Bahubali and KGF2 will be stored inside the heap memory, once program execution is completed Python Virtual Machine will be shut down, before shutdown of PVM, the heap memory will be cleared. Even for future reference we need data means we have to go for Files concept / databases concept.
###List, tuple, dict all are temporary storage :(.

---------------------------------------------------------------------------

###Difference between COnstructor and Method:

Method:
-We can use any name to define a method inside class ex: def talk(), m1(), info()....
-Per object, we can call the method sny number of times ex: t.m1()
-we should call method explicitly.
-We have to right business logic inside the method.

Constructor:
-We have to use __init__().
-Per object only once a constructor will be executed.
-Constructor is auto executed at the time of object creation.
-Inside constructor code is always fixed, i.e. self.name, self.rollno....We don't right any business logic, we declare and initialize instance variables inside the constructor.

##What happens if we provide method name same as class name???
It is perfectly valid, but it's not recommended...

class Test:
    def Test(self):
        print('Printing the method...')
t=Test() ##Constructor __init__ will be executed
print(t)
t.Test() ##Here we're calling the Test method.

##Output:
<__main__.Test object at 0x0000027CC2301180>
Printing the method...

------------------------------------------------------------------------------

##Basic idea about types of variables & methods within Python class:
-3 Types of variables and Methods are allowed.
##Variables:
-Instance variables 
##When value of the variable is varied from object to object, such type of variable is called instance variable ex: s1(name:Durga, rollno:101), s2(name:Ravi, rollno:102)....s3(name:Shiva,rollno:701).
##For every object a separate copy of instance variables will be created.
##Most of the times instance variables will be declared inside constructor by using self variable.
class Student:
    def __init__(self,name,rollno):
        self.name=name  ##instance variable
        self.roll_no=rollno ##instance variable
****************************
-Static variables (also known as class level variables):
##We value of the variable is not varied from object to object, such type of variable is declared at class level as static variable ex: school name.
##If the not varied variable is declared as instance variable, it's not wrong, but not recommended it will lead unecessary of wastage of memory.
class Student:
    school_name='Durgasoft' ##Static variable
##At class level only one copy will be created and that copy will be shared by every object of that class. i.e with the respective self.name and self.rollno.
##Most of the times, static variables should be declared within the class directly.
****************************
-Local variables (also known as method level variables):
##The variable declared inside a method to meet the temporary requirements of user.
class Student:
    def info(self):
        x=10    ##x is local variable
        for i in range(x):
            print(i)    ##i is local variable
*********************************************************
*********************************************************
-Instance Methods:
##Object related methods is called instance methods.
##Inside method definition if we're accessing any instance variable, then that method always talks about a particular object, because we're accessing object related instance variable, that method we have to declare as instance method.
##For instance method, first argument is always self, which is reference variable to that current object.
##*****Blind rule, for any method if the first argument is self then it is 100% a instance method.
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def getStudentInfo(self):   ##Instance Method
        print('Student Name: ',self.name) ##Here we're accessing instance variable, if we're accessing atleast one instance inside a method then it is called instance method.
        print('Student Rollno: ',self.rollno)
        
************************************************
-Class Methods:
##Inside method if we're using static variable/class variable, then that method is always talks about class related method and no where talks about particular object, such type of method we have declare as Class Method.
##How to declare as class method?? by using @classmethod (class related decorator)
##If cls is there then it is class level method.
##The first argument to the class method is always cls, which is the reference varaible to class object.
##For every class one special object will be provided by PVM to maintain class level information, which is nothing but class level object. cls is the reference variabale pointing to that object.
class Student:
    schoolname = 'Durgasoft'    ##Static variable
    @classmethod    ##Decorator compulsory
    def getSchoolInfo(cls): ##cls is a reference variable. For every class one class level object will be created by Python, this is not normal object, this is class level object to hold the class level information (schoolname='Durgasoft') for this the reference variable is cls.
        print('SchoolName: ',cls.schoolname)

##Example1:
class Test:
    @classmethod
    def m1(cls):    ##cls is reference variable poiting to class object
        print('The id of reference variable class cls: ',id(cls))  ##This print the address of class object pointed by cls
print('The id/address of Class Object created at class level: ',id(Test)) ##This is class object, id of this and id(cls) must be same.
t=Test()
t.m1() or Test.m1()

##Output:
The id of Class Object created at class level:  2601561945824
The id of reference variable class cls:  2601561945824

**********************************************
-Static Methods:
##Inside method when we're not using any instance/static variables, such type of methods are general utility method (like I'm providing some value, you give some output), these methods are declared as static methods.
##We can declare it as static method by using @staticmetod decorator
class Test:
    @staticmethod
    def getSum(a,b):
        return a+b
print('The value of sum is: ',Test.getSum(1,2))

##Output:
The value of sum is:  3

-----------------------------------------------------------------------------

##Places to declare Instance Variables:
##We can declare instance variables at three places.
-Inside constructor by using self. ##Inside class
-Inside instance method by using again self. ##Inside class
-Outside of the class, by using object reference variable.

******Inside constructor by using self. ##Inside class
class Test:
    def __init__(self):
        self.a=10 ##Instance Variable
        self.b=20 ##Instance Variable
t=Test() ##When we create an object, automatically constructor is executed, whenever the constructor is executed, instance variables are careted as part of object t where a=10,b=20. The t object contains two reference variable a & b, how to know it?
print(t.__dict__) ##Object dictionary, key & value pair

##Output:
{'a': 10, 'b': 20}

**********Inside instance method by using again self. ##Inside class
class Test:
    def m1(self):
        self.c=30 ##Instance Variable
t=Test()
print(t.__dict__)

##Output:
<Blank no data>

##The instance variables declared inside a method will be added to the object when we call that method (here it is m1).

class Test:
    def m1(self):
        self.c=30 ##Instance Variable
t=Test()
t.m1()  ##c will be added to the object
print(t.__dict__)

##Output:
{'c': 30}

***********Outside of the class, by using object reference variable
class Test:
    def __init__(self):
        self.a=10 ##Instance Variable
        self.b=20 ##Instance Variable

    def m1(self):
        self.c = 30  ##Instance Variable

t = Test() ##a,b will added to the object
t.m1()  ##c will be added to the object
t.d=40  ##Outside the class adding the instance variable to the object by using object reference variable.
print(t.__dict__)

##Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}

##Example2:
class Test:
    def __init__(self):
        self.a=10 ##Instance Variable
        self.b=20 ##Instance Variable

    def m1(self):
        self.c = 30  ##Instance Variable

t = Test() ##a,b will added to the object t1
t.m1()  ##c will be added to the object t1
t.d=40  ##Outside the class adding the instance variable t1
print(t.__dict__)
t2=Test() ##a,b will added to the object t2
print(t2.__dict__)

##Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20}

###In python number of instance variables are varied in above example from object to object. This is how Python works.
###In Java, the number of instance variables are always same for every object.

------------------------------------------------------------------------

##How to access instance variables ??
-Inside python class we can access Instance variable using self.
##Within the class, we can access instance variables by using self(of course inside constructor and insatnce method)
-Outside of the class we can access using object reference
##But outside of the class, we can access by using object reference.
class Test:
    def __init__(self):
        print('This is from Constructor...')
        self.a=10
        self.b=20
    def display(self):
        print('This is from the instance method')
        print(self.a)
        print(self.b)
t=Test() ##a,b will added to the object t1
print('Successfully object is created')
t.display() ##a,b is accessed using self
print('This is outside of the class')
print(t.a) ##a is accessed outside of class using object reference
print(t.b) ##b is accessed outside of class using object reference

##Output:
This is from Constructor...
Successfully object is created
This is from the instance method
10
20
This is outside of the class
10
20

------------------------------------------------------------------------

##How to delete instance variable?
-Within class if we want to delete it can be achieved using self:
ex: del self.variable_name and multiple deletion del self.variable_name1,self.variable_name2.....
-Outside of the class if we want to delete it can be achieved using object reference:
ex: del object_reference.variable_name
and multiple deletion del object_reference.variable_name1, object_reference.variable_name2.....
-*******Instance variables deleted for one object will not be deleted from other object because for every object separate copy of instance variables will be there.

#Example1:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    
    def m1(self):
        del self.c
t=Test()
print(t.__dict__)

##Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}

#Example2:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    
    def m1(self):
        del self.c
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)

##Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'd': 40}

#Example3:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    
    def m1(self):
        del self.c
        del self.a,self.d
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)

##Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'b': 20}

#Example4:
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.c
        del self.a, self.d
t = Test()
print('Print data after object creation: ',t.__dict__)
t.m1()
print('Print data after deletion inside class: ',t.__dict__)
t2 = Test()
print('Print data after object t2 creation: ',t2.__dict__)
del t2.b
del t2.c, t2.d
print('Print data after deletion outside class: ',t2.__dict__)

##Output:
Print data after object creation:  {'a': 10, 'b': 20, 'c': 30, 'd': 40}
Print data after deletion inside class:  {'b': 20}
Print data after object t2 creation:  {'a': 10, 'b': 20, 'c': 30, 'd': 40}
Print data after deletion outside class:  {'a': 10}

#Example5:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t1.a=888
t1.b=999
t2=Test()
print('t1: ',t1.__dict__)
print('t2: ',t2.__dict__)

##Output:
t1:  {'a': 888, 'b': 999}
t2:  {'a': 10, 'b': 20}


------------------------------------------------------------------------------

##Various places to declare the static variables:

-**********Within the class directly, but outside of any method or constructor.
class Test:
    a=10 ##Ideal way and best way to declare.
t=Test()
print(t.__dict__) ##Gives no data as output, empty dict.
print(Test.__dict__) ##The static variable is nowhere related to object, we need can't use print(t.__dict__), so we need to use print(Test.__dict__) All class members including static variable will be printed, we see other class members, because PVM will add some extra members, no need to worry about them.

##Output:
{}
{'__module__': '__main__', 'a': 10, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

-*********Inside constructor by using class name:
-*********Inside a instance method, using class name:
class Test:
    a=10
    def __init__(self):
        self.b=10 ##Instance Variable
        Test.b=20 ##Static Variable
    def m1(self):
        Test.c=30 ##static varaible
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)

##Output:
{'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x000001501B6828C0>, 'm1': <function Test.m1 at 0x000001501B682710>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
{'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x000001501B6828C0>, 'm1': <function Test.m1 at 0x000001501B682710>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20}
{'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x000001501B6828C0>, 'm1': <function Test.m1 at 0x000001501B682710>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30}

-*********Inside class method by using either cls or classname:
-*********Inside static method by using classname:
class Test:
    @classmethod
    def m2(cls):
        cls.d=40 ##Static Variable
        Test.e=50 ##Static Variable
##Inside class method we declare using either cls or class name, both are valid.
    def m3():
        Test.f=40

##Output:
{'__module__': '__main__', 'm2': <classmethod(<function Test.m2 at 0x000001C2D0B32EF0>)>, 'm3': <function Test.m3 at 0x000001C2D0B32710>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'd': 40, 'e': 50}
{'__module__': '__main__', 'm2': <classmethod(<function Test.m2 at 0x000001C2D0B32EF0>)>, 'm3': <function Test.m3 at 0x000001C2D0B32710>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'd': 40, 'e': 50, 'f': 40}

-********Outside of class by using classname:
class Test:
    print('Hey...')
Test.g=70
print(Test.__dict__)

##Output:
Hey...
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'g': 70}

----------------------------------------------------------------------------------

###How to access static variables:
-We can access static variables, either by class name or object reference (self,cls). 
************Highly recommended to use class name****************

-*********Inside Constructor: By using self or class name:
-*********Inside instance method: By using self or class name:
-*********Inside class method: By using cls or class name:
-*********Inside static method: By using class name:
-*********Outside of the class, either by object reference or class name.
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m3(cls):
        print(Test.a)
        print(cls.a)
    @staticmethod
    def m4():
        print(Test.a)
t=Test()
print('Instance Method Output')
t.m1()
print('Class Method')
Test.m3()
print('Static Method')
Test.m4()
print('Outside of the class using object reference/class name')
print(t.a)
print(Test.a)

##Output:
10
10
Instance Method Output
10
10
Class Method
10
10
Static Method
10
Outside of the class using object reference/class name
10
10

------------------------------------------------------------------------------------
##Where we can modify the value of static variable??
-We can modify the value of static variable anywhere (within the class or outside the class) by using class name.
-But inside class method, we can also use cls variable.
-We can't use neither self variable or object reference to modify the static variable.

class Test:
    a=10
    def __init__(self):
        Test.a=20 ##Modified the value
    def m1(self):
        Test.a=30
    @classmethod
    def m2(cls):
        cls.a=40
        #Test.a=50 ##Commented because end result will end up being 50 and not 40, hence tried separately, you can try it by uncommenting.
    @classmethod
    def m3(cls):
        Test.a=50
    @staticmethod
    def m4():
        Test.a=60
print('Before Modification: ',Test.a)
t=Test()
print('After Modification inside constructor: ',Test.a)
t.m1()
print('After modification inside instance method: ',Test.a)
Test.m2()
print('After modification inside class method using cls: ',Test.a)
Test.m3()
print('After modification inside class method using class name: ',Test.a)
Test.m4()
print('After modification inside static method: ',Test.a)
Test.a=70
print('After modification outside of class using class name: ',Test.a)

##Output:
Before Modification:  10
After Modification inside constructor:  20
After modification inside instance method:  30
After modification inside class method using cls:  40
After modification inside class method using class name:  50
After modification inside static method:  60
After modification outside of class using class name:  70


------------------------------------------------------------------------

###Example1:
class Test:
    a=10
    def m1(self):
        self.a=888
t=Test()
t.m1()
print(Test.a)
print(t.a)

##Output:
10
888

#Example2:
class Test:
    a=10
    def m1(self):
        Test.a=888
t=Test()
t.m1()
print(Test.a)
print(t.a)

##Output:
888
888

##Example3:
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
t1.a=888
t1.b=999
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

##Output:
t1:10,20
t2:10,20
t1:888,999
t2:10,20

#Example4:
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
Test.a=888  ##static variable a value is updated to 888
Test.b=999  ##There is no static variable b, therefore a new static variable b is created with value 999, instance variable and static variable with same is possible in Python.
print('t1:',t1.a,t1.b) ## a value is updated to 888, b is pulled from instance variable 20 and static variable 999
print('t2:',t2.a,t2.b) ## a value is updated to 888, b is pulled from instance variable 20 and static variable 999
print('Test:',Test.a,Test.b) ## a value is updated to 888, b is pulled from static variable 999

##Output:
t1: 10 20
t2: 10 20
t1: 888 20
t2: 888 20
Test: 888 999

#Example5:
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

##Output:
t1:888,999
t2:888,20

#Example6:
class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=Test()
t2=Test()
t1.m1()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

#Output:
t1:888,999
t2:10,20

#Example7:
class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=Test()
t2=Test()
t1.m1()
t2.m1()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

#Output:
t1:888,999
t2:888,999

#Example8:
class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999
t1=Test()
t2=Test()
t1.m1()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
print('Test:',Test.a,Test.b)

#Output:
t1: 888 20
t2: 888 20
Test: 888 999

-----------------------------------------------------------------------------------

##How to delete the static variables:
#Can be achieved by using class name/cls variable, nut we cannot modify/delete static variables by using object reference or self.

##Example1:
class Test:
    a=10
    @classmethod
    def m1(cls):
        del Test.a ##using class name
        #del cls.a  ##using cls variable
print(Test.__dict__)
#print("Let us call cls method and use Test.a")
#Test.m1()
print("Let us delete a outside the class")
del Test.a ##Valid
t=Test()
print(t.a) ##valid
del t.a ##Invalid, object reference cannot be used to delete/modify static variables.
print(Test.__dict__)
##Output:
{'__module__': '__main__', 'a': 10, 'm1': <classmethod(<function Test.m1 at 0x000001F43E7328C0>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
Let us call cls method and use Test.a
{'__module__': '__main__', 'm1': <classmethod(<function Test.m1 at 0x000001F43E7328C0>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

##Example2:
class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=10
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=40
        del Test.c
    @staticmethod
    def m3():
        Test.e=50
        del Test.d
print(Test.__dict__) ##This will print only 'a's value, remaining values of static variable will be printed when we call the respective methods.
t=Test() ##Object is created, 'a' is deleted and new static variable b is created.
|||ly things will go on with methods m1,m2,m3....

##Output:
{'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x00000170717228C0>, 'm1': <function Test.m1 at 0x0000017071722710>, 'm2': <classmethod(<function Test.m2 at 0x00000170717227A0>)>, 'm3': <staticmethod(<function Test.m3 at 0x0000017071B91000>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
{'__module__': '__main__', '__init__': <function Test.__init__ at 0x00000170717228C0>, 'm1': <function Test.m1 at 0x0000017071722710>, 'm2': <classmethod(<function Test.m2 at 0x00000170717227A0>)>, 'm3': <staticmethod(<function Test.m3 at 0x0000017071B91000>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20}

----------------------------------------------------------------------------

##Instance Variable vs Static Variable:

class Test:
    a=10 ##Static Variable
    def __init(self):
        self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

##Output:
t1:888,999
t2:888,20

##Instance Variable:
-These are object level variables.
-For every object, a separate copy will be created.
-By using one object ref, if we're trying to perform any changes to the instance variables, then those changes won't be reflected to the remaining objects, bec for every object a separate copy of instance variables will be there.

##Static Variable:
-These are class level variables.
-A single copy will be created at class level and shared by all objects of that class.
-If we perform any change to the static variable, then those changes will be reflected to all objects, because a single copy of static variable will be maintained at class level.

##Local Variable:
-Sometimes to meet temporary requirements of the programmer, we can declare variables inside a method directly without using self, classname or cls variable. Such type of variables are called local variables or temporary variables.
-Local variables can be used to hold temporary results.
-The local variables of a method cannot be accessed from outside of that method.
class Test:
    @staticmethod
    def average(list1):
        result=sum(list1)/len(list1) ##result is local variables.
        print('The average: ',result)
    @staticmethod
    def wish(name):
        for i in range(10):
            print('Good Evening: ',name)
            
list1=[10,20,30,40]
Test.average(list1)
Test.wish('Durga')

##Output:
The average:  25.0
Good Evening:  0 Durga
Good Evening:  1 Durga
Good Evening:  2 Durga
Good Evening:  3 Durga
Good Evening:  4 Durga
Good Evening:  5 Durga
Good Evening:  6 Durga
Good Evening:  7 Durga
Good Evening:  8 Durga
Good Evening:  9 Durga

##Local variables are local to that particular method, within that method only we can access, outside of the method we can't access.
class Test:
    def m1(self):
        a=10
        print(a)
    def m2(self):
        print(a)
t=Test()
t.m1() ##No issues
t.m2() ##Will throw error

##Output:
10
NameError: name 'a' is not defined

-------------------------------------------------------------------------------

##Mini Bank Application:
##Mini Bank Application:
class Customer:
    '''This class is developed by Durga and it describes bank operations'''
    bankname = 'DURGABANK'  ##bank name is constant for all customers, hence declare as a Static Variable.

    ##Let's create data for customer Object:
    def __init__(self, name, balance=0.0):  ##balance=0.0 is default argument, if no balance given it will 0.0
        self.name = name
        self.balance = balance

    ##Let's def instance method, because deposit needs to talk with balance which is an instance variable, if we use instance variable automatically method becomes instance method.
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("After deposit, balance: ", self.balance)

    ##Let's def instance method, because deposit needs to talk with balance which is an instance variable, if we use instance variable automatically method becomes instance method.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, can't perform this operation")
        else:
            self.balance = self.balance - amount
            print("After withdraw balance: ", self.balance)


print("Welcome to ", Customer.bankname)
name = input('Enter your name: ')
c = Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Choose your option: ')
    if option.lower() == 'd':
        amount = float(input('Enter amount to deposit: '))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw: '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for Banking')
        break
    else:
        print('Your option is invalid, Plz choose your valid option')
        
##Output:
Welcome to  DURGABANK
Enter your name: Rajath
d-Deposit
w-Withdraw
e-Exit
Choose your option: d
Enter amount to deposit: 10000
After deposit, balance:  10000.0
d-Deposit
w-Withdraw
e-Exit
Choose your option: w
Enter amount to withdraw: 4000
After withdraw balance:  6000.0
d-Deposit
w-Withdraw
e-Exit
Choose your option: w
Enter amount to withdraw: 7000
Insufficient funds, can't perform this operation
d-Deposit
w-Withdraw
e-Exit
Choose your option: r
Your option is invalid, Plz choose your valid option
d-Deposit
w-Withdraw
e-Exit
Choose your option: e
Thanks for Banking

Process finished with exit code 0

----------------------------------------------------------------------------
##Instance Methods and Demo Program:

Inside method implementation, if we are using any instance variable, then this method always talks about a particular object. Such type of methods we have to declare as instance methods.

The first argument to the instance method is always self, which is reference variable to the current object. By using this self we can access instance variable values.

def m1(self):
    pass

##Example:

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self): ##Instance Method
        print('Hi: ',self.name) ##Instance Variable
        print('your marks are: ',self.marks) ##Instance Variable
    def grade(self): ##Instance Method
        if self.marks>=60:  ##Instance Variable
            print('you got 1st Grade')
        elif self.marks>=50: ##Instance Variable
            print('you got 2nd Grade')
        elif self.marks>=35: ##Instance Variable
            print('you got 3rd Grade')
        else:
            print("You're Failed")
n=int(input('Enter No. of Students'))
for i in range(n):
    name=input('Enter Student name: ')
    marks=int(input('Enter Student marks: '))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()
    
##Output:
Enter No. of Students: 2
Enter Student name: Sunny
Enter Student marks: 56
Hi:  Sunny
your marks are:  56
you got 2nd Grade

Enter Student name: Bunny
Enter Student marks: 36
Hi:  Bunny
your marks are:  36
you got 3rd Grade


Process finished with exit code 0

-------------------------------------------------------------------------------------

##Setter and Getter Methods:
-We can set and get the values of instance variables by using setter and getter methods.
-In general IDE's are responsible to set and get values.
-Setter Method : We can use setter method to set values to instance variables. This is also known as mutator method, which keep changing.
##Syntax:
def setVariableName(self,variable):
    self.variable=variable
##Example:
def setMarks(self,marks): ##Setter method (also instance mathod)
    self.marks=marks ##Instance Variable

-Getter method : Getter Methods can be used to get values of the instance variables. This is also known as accessor methods.
##Syntax:
def getVariableName(self):
    return self.variable
##Example:
def getMarks(self):
    return self.marks

##Example:
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input('Enter No. of Students: '))
students=[]
for i in range(n):
    s=Student()
    name=input('Enter Student name: ')
    marks=int(input('Enter marks: '))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for s in students:
    print('Hello',s.getName())
    print('Your marks are: ',s.getMarks())
    print()

##Output:
Enter No. of Students: 2
Enter Student name: Sunny
Enter marks: 69
Enter Student name: Buntu
Enter marks: 59
Hello Sunny
Your marks are:  69

Hello Buntu
Your marks are:  59

----------------------------------------------------------------------------

##Class Methods Introduction and Demo Programs:
-Inside method implementation, if we are using only static variables and if we are not using any instance variable, then that method is no way related to a particular object and it is is class level method. Such type of methods we have to declare as class methods.
-We have to declare class method with @classmethod decorator.
-The first argument to the class method is always cls, which is reference variable to class object.
-For every class one special object will be created by PVM to maintain class level information, which is nothing but class level object. cls is the reference variable pointing to that object.

class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flying with {} wings'.format(name,cls.wings)) ##we can access static variables through cls or class name
Bird.fly('Parrot')
Bird.fly('Eagle')

##Output:
Parrot flying with 2 wings
Eagle flying with 2 wings

##Program to track number of objects created for a class:
class Test:
    '''For every object created I'll increment count'''
    count=0
    def __init__(self):
        Test.count=Test.count+1 ##For every object creation constructor will execute and counter will get an increment.
    @classmethod
    def getNoOfObjects(cls):
        print('The No. of objects created: ',cls.count)
Test.getNoOfObjects() ##Ideal value is 0, since no object created
t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.getNoOfObjects()

###Output:
The No. of objects created:  0
The No. of objects created:  4

-------------------------------------------------------------------------

##Difference between Instance Method vs Class Method:
##Instance Method:
-Inside method body if we are using atleast one instance variable then compulsory we should declare that method as instance method.
-Inside instance method we can access both instance and static variables.
-To declare instance method we are not required to use any decorator.
-The first argument to the instance method should be self, which is reference to current object and by using self, we can access instance variables inside method.
-We can call instance method by using only object reference.

##Class Method:
-Inside method body if we are using only static variables and if we are not using instance variables then we have to declare that method as class method.
-Inside classmethod we can access only static variables and we cannot access instance variables.
-To declare class method compulsory we should use @classmethod decorator.
-The first argument to the classmethod should be cls, which is reference variable to current class object and by using that we can access static variables.
-We can call classmethod either by using object reference or by using class name, but recommended to use classname.

-------------------------------------------------------------------------

##****************Static Methods:**************************
-Inside a method implementation, if we are not using any instance variable or static variable, such type of methods are general utility methods and these methods we have to declare as static methods.
-For static methods we won't provide self or cls at the time of declaration.
-We can declare static methods explicitly by using @staticmethod decorator
-We can access static method either by object reference or by class name. But recommended to use class name. (In general using classname directly helps in increasing the performance, object creation requires additional effort by PVM)
##Syntax:
class Test:
    @staticmethod
    def m1(): ##self/cls not applicable to static methods
        pass
Test.m1() ##We can also call by object ref, recommended is class name.

##Example:
class DurgaMath:
    @staticmethod
    def add(a,b):
        print('The Sum: ',(a+b))
    @staticmethod
    def product(a,b):
        print('The product: ',(a*b))
    @staticmethod
    def average(a,b):
        print('The Average: ',(a+b)/2)
DurgaMath.add(10,20)
DurgaMath.product(10,20)
DurgaMath.average(10,20)

##Output:
The Sum:  30
The product:  200
The Average:  15.0

-------------------------------------------------------------------------------

##Instance Method vs Class Method vs Static Method:
-If we're using any instance variables inside method body then we should go for instance method. We should call by using object reference only.
-If we're using only static variables inside method body then this method no way related to a particular object, we should declare such type of methods as classmethod. We can declare class method explicitly by using @classmethod decorator. We can call either by using object ref or by using class name (class name recommended).
-If we're not using any instance variable and any static variable inside method body, to define such type of general utility methods we should go for static methods. We can declare static methods explicitly by using @staticmethod decorator. We can call either by using object reference or by using class name.

-If we are using only instance variables > instance method
-If we are using only static variables > class method
-If we are using instance and static variables > instance method
-If we are using instance and local variables > instance method
-If we are using static variables and local variables > class method
-If we are using local variables > static method.

###When we're not using any decorators for class & static method, then how to identify which method it is???
*******For classmethod, @classmethod decorator is mandatory.
-For staticmethods,@staticmethod decorator is optional.
-Without any decorator the method can be either instance method or static method.
    -If we are calling by using object reference then it is treated as instance method.
    -If we are calling by using class name then it is treated as static method.

##Example:
class Test:
    def m1():
        print('some method')
t=Test()
t.m1() ##As we're calling using object reference, PVM machine will considered the method called as instance method, will look for self argument, if it is not there obviously it can't be a instance method and it will throw error.

##Output:
TypeError: Test.m1() takes 0 positional arguments but 1 was given

##Example1:
class Test:
    def m1(x):  ##We can pass self/delf/kelf/x etc... It's valid
        print('some method')
t=Test()
t.m1()
t.m1(10) ##Actually it expects only one value, which is already provided by PVM, therefore it throws error.

##Output:
some method
TypeError: Test.m1() takes 1 positional argument but 2 were given

##Example2:
class Test:
    def m1( ):
        print('some method')
Test.m1() ##It's static method and valid

##Output:
some method

##Example3:
class Test:
    def m1(x): ##This became instance method
        print('some method')
Test.m1()   ##We're calling as static method, throws type error.
Test.m1(10)  ##This is valid

Note: if there is no decorator, it can be either instance/static method, if we call by class name it acts as static method and if we call by object reference it acts as instance method provided we take care of argument self/x/kelf/delf

##Output:
TypeError: Test.m1() missing 1 required positional argument: 'x'
some method

------------------------------------------------------------------------------

##Accessing members of one class inside another class:
-Yes it is possible, based on our requirement we can successfully achieve it.

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number: ',self.eno)
        print('Employee Name: ',self.ename)
        print('Employee Salary: ',self.esal)
class Manager:
    def updateEmpSal(emp):
        emp.esal=emp.esal+10000
        emp.display()
##UpdateEmpSal : 
''' -May be instance/static method.
    -(emp) can be considered as self, self is current Manager(class name) object.
    -Whether esal property is there / display() method is there under class Manager? Nope!!!, hence we can say it is not instance method.
    -Therefore we can conclude it is static method'''
emp = Employee(101,'Durga',45000)
Manager.updateEmpSal(emp)

##Output:
Employee Number:  101
Employee Name:  Durga
Employee Salary:  55000

-----------------------------------------------------------------------------
##Inner Classes:******************
-The class inside another class / sometimes we can define a class inside another class, such type of class is called Inner Classes.
-When should we go for it? Let's discuss
        Without existing one type of object, if there is no chance of existing another type of object then we should go for inner classes because the Inner class object is strongly associated with outer class object.
        Ex: Consider a University running with 2 departments (CS, EEE), if the university got closed due to lack of students, then dept also won't exist, because dept can't exist as alone.
        '''without existing of one type of object(university), if there is no chance of existing another type of object (dept CS & EEE) then we should go for inner classes'''
-Advantage:
    -It improves modularity of application.
    -Improves security of the application.
    -We can go for n number of inner classes. (This is not nesting :p, this is different concept).
##Syntax:
class University:   ##Outer Class
    class Department:   ##Inner Class
        pass
    class lab
        pass
    class parking
        pass
    .
    .
    .

##Example:
class Outer:
    def __init__(self): ##Constructor
        print('Outer object creation....')
    class Inner:
        def __init__(self): ##Constructor
            print('Inner class object creation....')
        def m1(self):   ##Instance Method
            print('Inner class method')
o=Outer() ##Creating Outter class object creation
i=o.Inner() ##Creating Inner class object creation
i.m1() ##Calling the method inside inner class
##(Or)
i=Outer().Inner() ##This is also valid
i.m1()
##(Or)
Outer().Inner().m1() ##This is also valid

##Output:
Outer object creation....
Inner class object creation....
Inner class method

-------------------------------------------------------------------------------
##Nested of Inner classes and Demo Program:

##Example1:
class Outer:
    def __init__(self):
        print('Outer class object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation....')
            def m1(self):   ##Instance Method
                print('Nested Inner Class Method')
Outer().Inner().InnerInner().m1() 

##Output:
Outer class object creation
Inner class object creation
InnerInner class object creation....
Nested Inner Class Method

##Example2:
class Outer:
    def __init__(self):
        print('Outer class object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation....')
            def m1():   ##*****Static Method
                print('Nested Inner Class Method')
Outer().Inner().InnerInner.m1() ##*****No need of object reference of InnerInner class, directly we can class name, i.e. no need to use ().....

##Output:
Outer class object creation
Inner class object creation
Nested Inner Class Method

##Example3:
class Human:
    class Head:
        def talk(self):
            print('Talking....')
        class Brain:
            def think(self):
                print('Thinking...')
human=Human()
head=human.Head()
head.talk()
brain=head.Brain()
brain.think()
##(or)
Human().Head().talk()
Human().Head().Brain().think()

##Output:
Talking....
Thinking...

##Example4:
class Human:
    def __init__(self,name):
        print('Human Object Creation...')
        self.name=name
        self.head=self.Head()
    def info(self):
        print("Hello, Myself: ",self.name)
        print("I'm Full Busy with,")
        self.head.think()
        self.head.brain.talk()
    class Head:
        def __init__(self):
            print('Head Object Creation...')
            self.brain=self.Brain()
        def think(self):
            print("I'm talking.....")
        class Brain:
            def __init__(self):
                print('Brain Object Creation....')
            def talk(self):
                print("I'm talking......")
human=Human('Durga')
human.info()

##Output:
Human Object Creation...
Head Object Creation...
Brain Object Creation....
Hello, Myself:  Durga
I'm Full Busy with,
I'm talking.....
I'm talking......

##Example5:
class Person:
    def __init__(self):
        print('Person Object Creation...')
        self.dob=self.Dob()
    class Dob:
        def __init__(self):
            print('DOB Object Creation..')
P=Person()

##Output:
Person Object Creation...
DOB Object Creation..

##Enhanced Skeleton Code:
class Person:
    def __init__(self,name,dd,mm,yyyy):
        print('Person Object Creation...')
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def info(self):
        print('Name: ',self.name)
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('DOB Object Creation..')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person('Durga',24,8,1947)
p.info()

##Output:
Person Object Creation...
DOB Object Creation..
Name:  Durga
DOB=24/8/1947

----------------------------------------------------------------------------

##Nested Methods: Method inside a method....
##In Python Nested Method is allowed
-We can declare a method inside another method, such type of methods are called Nested Methods.
-Inside a metjod if any functionality repeatedly required, that functionality we can define as a separate method and we can call that method any number of times based on our requirement.
-Advantages:
    -Code Reusability
    -Modularity of the application will be improved

class Test:
    def m1(self):
        a=10
        b=20
        print('The Sum: ',a+b)
        print('The Diff: ',a-b)
        print('The Multiplication: ',a*b)
        print('The Average: ',(a+b)/2)
        
        a=100
        b=200
        print('The Sum: ',a+b)
        print('The Diff: ',a-b)
        print('The Multiplication: ',a*b)
        print('The Average: ',(a+b)/2)
        ###This is kind of repetative, instead let's call the nested method and act little smart.

class Test:
    def m1(self):
        def calc(a,b):
            print('The Sum: ',a+b)
            print('The Diff: ',a-b)
            print('The Multiplication: ',a*b)
            print('The Average: ',(a+b)/2)
            print('')
        calc(10,20)
        calc(100,200)
        calc(1000,2000)
t=Test()
t.m1()
        
##Output:
The Sum:  30
The Diff:  -10
The Multiplication:  200
The Average:  15.0

The Sum:  300
The Diff:  -100
The Multiplication:  20000
The Average:  150.0

The Sum:  3000
The Diff:  -1000
The Multiplication:  2000000
The Average:  1500.0
            
----------------------------------------------------------------------------------

##Garbage Collections and Destructors:
-In languages like C++, Programmer is responsible for both creation and destruction of objects. Usually the programmer taking very much care while creating objects, but neglecting destruction of useless objects. Because of his negligence, total memory may filled with useless objects which creates memory problems and total application will be down with these memory problems.
-But in Python, we have some assistant which is always running in the background to destroy useless objects. Because of this assistant, the chance of failing Python program with memory problems is very less. This assistant is nothing but Garbage Collector.
-Hence, the main objective of Garbage collector is to destroy useless objects.
-An object will be eligible for Garbage Collection when the object references/reference variable count is zero.

##How to enable and disable garbage collector in our program:
-By default the Garbage collector is enabled.
-To use gc module to disable/enable the GC.
-gc.isenabled() --> If GC is enabled it returns true, else false.
-gc.disable() --> To disable the GC
-gc.enable() --> To enable the GC
-The only reason when the GC will be disabled is when the,
    -Memory problems won't be raised due to good memory availability.
    -Very less objects being used in the Program.
    -Disabling also increases the performance, because it keeps running in the background.
    -Ideally not recommended to disable it.

##Example:
import gc
print('Default status of GC: ',gc.isenabled())
gc.disable()
print('Post disabling the status of GC: ',gc.isenabled())
gc.enable()
print('Post re-enabling the status of GC: ',gc.isenabled())

##Output:
Default status of GC:  True
Post disabling the status of GC:  False
Post re-enabling the status of GC:  True

-------------------------------------------------------------------------
##Role of Destructors, how it is associated with GC??
-Destructor is a special method and the name should be __del__().
-Just before destroying an object, Garbage collector always calls destructor to perform cleanup activities (Like resource deallocation activities like close db connection etc.)
-Once Destructor execution completes then GC automatically destroys that object.
-GC is meant for the destroying/killing the object, destructors performs deallocation of object from db connection etc...
-Constructor is meant for initialisation activity and not object creation.

##Example Destructor:
import time

class Test:
    def __init__(self):
        print('Object initialisation activities..')
    def __del__(self):
        print('Fulfilling last wish and performing clean up activities')
t=Test() ##Object is created
time.sleep(10)
print('End of application')

##Output:
Object initialisation activities..
End of application
Fulfilling last wish and performing clean up activities

##0r

import time

class Test:
    def __init__(self):
        print('Object initialisation activities..')
    def __del__(self):
        print('Fulfilling last wish and performing clean up activities')
t=Test() ##Object is created
t=None ##Now onwards t is not pointing to None object, no more pointing to to the Test object, GC will called destructor and post clean up activity, the GC will destroy/kill the object.
time.sleep(10)
print('End of application')

##Output:
Object initialisation activities..
Fulfilling last wish and performing clean up activities
End of application

-Once control reaches end of program, all objects which are created as the part of that program are by default eligible for GC
-If the object does not contain any ref variable then only it is eligible for GC .ie. if the ref count is zero then only object eligible for GC.


##Example2:
class Test:
    def __init__(self):
        print('Object Initialisation Activities....')
    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities...')
t1=Test()
t2=Test()
print('End of application') ##Once program reaches this point, i.e. end of application, both objects will be deleted by GC.

##No.of Object creation = no.of destryctors = no.of GCs

##Output:
Object Initialisation Activities....
Object Initialisation Activities....
End of application
Fulfilling last wish and performing cleanup activities...
Fulfilling last wish and performing cleanup activities...

##Example3:
class Test:
    def __init__(self):
        print('Object Initialisation Activities....')
    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities...')
t1=Test()
t2=Test()
t1=None ##Explicitly destroying object through GC
t2=None ##Explicitly destroying object through GC
print('End of application') ##Once program reaches this point, i.e. end of application, both objects will be deleted by GC.


##Output:
Object Initialisation Activities....
Object Initialisation Activities....
Fulfilling last wish and performing cleanup activities...
Fulfilling last wish and performing cleanup activities...
End of application

##Example4:
import time

class Test:
    def __init__(self):
        print('Constructor execution')
    def __del__(self):
        print('Destructor execution')
t1=Test() ##Object creation
t2=t1 ##For object referred t1, please give t2 reference
t3=t1 ##For object referred t1, please give t3 reference
del t1
time.sleep(5)
print('Object not destroyed after deleting t1')
del t2
time.sleep(5)
print('Object not destroyed even after deleting t2')
print('Removing last reference t3')
del t3
print('End of application')

##Output:
Constructor execution
Object not destroyed after deleting t1
Object not destroyed even after deleting t2
Removing last reference t3
Destructor execution
End of application

##Note: 
-In above program only one test object is there and 3 reference variables are there t1,t2,t3.
-If the object does not contain any ref variable then only it is eligible for GC .ie. if the ref count is zero then only object eligible for GC, therefore all the three reference variable t1,t2 and t3 needs to delinked from the test object.

##Example4:
import time
class Test:
    def __init__(self):
        print('Constructor Execution')
    def __del__(self):
        print('Destructor Execution')
l=[Test(),Test(),Test()]    ##Three objects are created, therefore three times constructor will be executed...
print('Making List object eligible for GC..')
del l ##Three Test objects will be destroyed, then how many times destructor will be called??? it's three times. If a list object is eligible for GC, then every object in that list will be destroyed by GC.
time.sleep(10)
print('End of Application')

##Output:
Constructor Execution
Constructor Execution
Constructor Execution
Making List object eligible for GC..
Destructor Execution
Destructor Execution
Destructor Execution
End of Application

##Example5:
import time
class Test:
    def __init__(self):
        print('Constructor Execution')
    def __del__(self):
        print('Destructor Execution')
l=[Test(),Test(),Test()]    ##Three objects are created, therefore three times constructor will be executed...
##del l ************************
time.sleep(10)
print('End of Application')

##Output:
Constructor Execution
Constructor Execution
Constructor Execution
End of Application
Destructor Execution
Destructor Execution
Destructor Execution

--------------------------------------------------------------------------------
***********Interview Question********************

1. What is the difference between del t1 and t1=None?

##del t1 : 
-It is used when we don't want reference variable and the object then go for it.
##t1=None : 
-It is used when we want the reference_variable and not the object.

##Example1:
class Test:
    def __init__(self):
        print('Constructor')
    def __del__(self):
        print('Destructor')
t=Test()
del t
print('End of Application')
#***********print(t) ##Throws the name error, NameError: name 't' is not defined

##Output:
Constructor
Destructor
End of Application


##Example2:
class Test:
    def __init__(self):
        print('Constructor')
    def __del__(self):
        print('Destructor')
t=Test()
t=None ##Here the reference_variable t is pointed to new object called as None, therefore the Test() will be marked as useless and available for GC.
print('End of Application')
print(t)

##Output:
Constructor
Destructor
End of Application
None

2. How to find the number of references of an object?
##This can be found out by using sys module, the sys module has getrefcount() function through this we can nail it.

#Example1:
import sys
class Test:
    pass
t1=Test()
print(sys.getrefcount(t1)) ##The count will be 2, because t1 is one variable and internally self (maintained by PVM) is also there ;) 

##Output:
2

#Example2:
import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t2
t4=t3
print(sys.getrefcount(t1)) ##Answer is 5 (t1,t2,t3,t4 & self)
del t3,t4
print(sys.getrefcount(t1)) ##Answer is 3 (t1,t2 & self)

##Output:
5
3

3. What is the difference between Constructor and Destructor??
##Constructor:
-The name of the constructor should be __init__()
-The main objective of constructor is to perform initialization activitioes of an object. Initialization means assigning the values to instance variables.
-Just after creating an object, PVM will execute constructor automatically to perform initialization activities.

##Destructor:
-The name of the destructor should be __del__().
-The main objective of destructor is to perform cleanup activities of an object. Cleanup activities means resource deallocation activities like close DB connection etc.
-Just before destroying an object, GC will execute destructor automatically to perform cleanup activities.

4. Which of following is true??
- The main purpose of constructor is to create an object - False
- The main purpose of constructor is to perform initialization of an object - True
- The main purpose of destructor is to destroy an object - False
- The main purpose of destructor is to perform cleanup activities before destroying an object - True
-Constructor is responsible to create object where as destructor is responsible to destroy object - False
-Constructor will be executed just after creating an object to perform initialization activities - True
-Destructor will be executed just before destroying object to pewrform cleanup activities - True

-------------------------------------------------------------------------------

##Using members of one class inside another class:

We can use members of one class inside another class by following two ways:
-By Has-A Relationship (Composition)
-By Is-A relationship (Inheritance)

##By Composition (HAS-A Relationship):
-By using creating an object, we can access members of one class inside another class. This approach is nothing but composition or HAS-A relationship.
-The main advantage of HAS-A relationship is Code Reusability.
##Example1:
##Best example to explain "class Car Has-A Engine reference"
class Engine:
    def useEngine(self):
        print('Engine Specific functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
    def useCar(self):
        print('Car required engine functionality')
        self.engine.useEngine()
c=Car()
c.useCar()

##Output:
Car required engine functionality
Engine Specific functionality

##Example2:
class Engine:
    def __init__(self):
        self.power='125KW'
    def useEngine(self):
        print('Engine Specific functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
        print('The power of engine is: ', self.engine.power)
    def useCar(self):
        print('Car required engine functionality')
        self.engine.useEngine()
c=Car()
c.useCar()

##Output:
Car required engine functionality
Engine Specific functionality
The power of engine is:  125KW

##Note: Here the engine class is getting reused for car class, may be for bus class in some other code. This type of code reusability is called HAS-A relationship.

----------------------------------------------------------------------------

##Example3:
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print('Car Name: {}\nModel: {}\nColor: {}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print('Employee Name: ',self.ename)
        print('Employee Number: ',self.eno)
        print('Employee Car Info: ')
        self.car.getInfo()
car=Car('Innova','2.5v','Grey Metallic')
emp=Employee('Durga',872425,car)
emp.empInfo()

##Output:
Employee Name:  Durga
Employee Number:  872425
Employee Car Info: 
Car Name: Innova
Model: 2.5v
Color: Grey Metallic

##Example4:
class SportsNews():
    def sportsInfo(self):
        print('Sports Information-1')
        print('Sports Information-2')
        print('Sports Information-3')
        print('Sports Information-4')
class MovieNews():
    def moviesInfo(self):
        print('Movies Information-1')
        print('Movies Information-2')
        print('Movies Information-3')
        print('Movies Information-4')
class PoliticsNews():
    def politicsInfo(self):
        print('Politics Information-1')
        print('Politics Information-2')
        print('Politics Information-3')
        print('Politics Information-4')
class DurgaNews():
    def __init__(self):
        self.sports=SportsNews()
        self.movie=MovieNews()
        self.politics=PoliticsNews()
durga=DurgaNews()
print("Welcome to Durga's News Channel")
print("")
print("Today's Sports News is as below: ")
durga.sports.sportsInfo()
print("")
print("Today's Movie News is as below: ")
durga.movie.moviesInfo()
print("")
print("Today's Politics News is as below: ")
durga.politics.politicsInfo()

##Output:
Welcome to Durga's News Channel

Today's Sports News is as below: 
Sports Information-1
Sports Information-2
Sports Information-3
Sports Information-4

Today's Movie News is as below: 
Movies Information-1
Movies Information-2
Movies Information-3
Movies Information-4

Today's Politics News is as below: 
Politics Information-1
Politics Information-2
Politics Information-3
Politics Information-4

#####Or
class SportsNews():
    def sportsInfo(self):
        print('Sports Information-1')
        print('Sports Information-2')
        print('Sports Information-3')
        print('Sports Information-4')
class MovieNews():
    def moviesInfo(self):
        print('Movies Information-1')
        print('Movies Information-2')
        print('Movies Information-3')
        print('Movies Information-4')
class PoliticsNews():
    def politicsInfo(self):
        print('Politics Information-1')
        print('Politics Information-2')
        print('Politics Information-3')
        print('Politics Information-4')
class DurgaNews():
    def __init__(self):
        self.sports=SportsNews()
        self.movie=MovieNews()
        self.politics=PoliticsNews()
    def getTotalNews(self):
        print("Welcome to Durga's News Channel")
        print("")
        print("Today's Sports News is as below: ")
        self.sports.sportsInfo()
        print("")
        print("Today's Movie News is as below: ")
        self.movie.moviesInfo()
        print("")
        print("Today's Politics News is as below: ")
        self.politics.politicsInfo()
durga=DurgaNews()
durga.getTotalNews()

##Output:
Welcome to Durga's News Channel

Today's Sports News is as below: 
Sports Information-1
Sports Information-2
Sports Information-3
Sports Information-4

Today's Movie News is as below: 
Movies Information-1
Movies Information-2
Movies Information-3
Movies Information-4

Today's Politics News is as below: 
Politics Information-1
Politics Information-2
Politics Information-3
Politics Information-4

##Or:
class SportsNews():
    def sportsInfo(self):
        print('Sports Information-1')
        print('Sports Information-2')
        print('Sports Information-3')
        print('Sports Information-4')
class MovieNews():
    def moviesInfo(self):
        print('Movies Information-1')
        print('Movies Information-2')
        print('Movies Information-3')
        print('Movies Information-4')
class PoliticsNews():
    def politicsInfo(self):
        print('Politics Information-1')
        print('Politics Information-2')
        print('Politics Information-3')
        print('Politics Information-4')
class DurgaNews():
    def __init__(self,sportNews,movieNews,politicsNews):
        self.sports=sportNews
        self.movie=movieNews
        self.politics=politicsNews
    def getTotalNews(self):
        print("Welcome to Durga's News Channel")
        print("")
        print("Today's Sports News is as below: ")
        self.sports.sportsInfo()
        print("")
        print("Today's Movie News is as below: ")
        self.movie.moviesInfo()
        print("")
        print("Today's Politics News is as below: ")
        self.politics.politicsInfo()
sportNews=SportsNews()
movieNews=MovieNews()
politicsNews=PoliticsNews()
durga=DurgaNews(sportNews,movieNews,politicsNews)
durga.getTotalNews()

##Output:
Welcome to Durga's News Channel

Today's Sports News is as below: 
Sports Information-1
Sports Information-2
Sports Information-3
Sports Information-4

Today's Movie News is as below: 
Movies Information-1
Movies Information-2
Movies Information-3
Movies Information-4

Today's Politics News is as below: 
Politics Information-1
Politics Information-2
Politics Information-3
Politics Information-4

---------------------------------------------------------------------------------

##By Inheritance (IS-A Relationship):
-Parent to Child Relationship.
-Parent class members are by default available to the child class and hence child class can reuse parent class functionality without rewriting. (Code Reusability). |||lr to HAS-A relationship, but not exactly same ;).
-Child class can define new members also. Hence child class can extend Parent Class functionality. (Code Extendibility).
##Ex: Amitabh fame to Abhishek and Amitab, Abhi & Aish fame to Aradhya.

##Example1:
class P:
    def m1(self):
        print('Prent Method')
class C(P): ##This is were the diff with respect to HAS-A CHild_Class(Parent_Class)
    def m2(self):
        print('Child Method')
##Note:
##-Child class has 2 methods in Total.
child=C()
child.m1()
child.m2()

##Output:
Parent Method
Child Method

##Example2:
class P:
    a=10
    def __init__(self):
        print('Parent Constructor')
        self.b=20
    def m1(self):
        print('Parent Instance Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    pass
child_class=C()
print(child_class.a)
print(child_class.b)
child_class.m1()
child_class.m2()
child_class.m3()

##Output:
Parent Constructor
10
20
Parent Instance Method
Parent Class Method
Parent static method

##Example3:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eatAndDrink(self):
        print('Eat Biryani and Drink Beer')
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        self.name=name
        self.age=age
        self.eno=eno
        self.esal=esal
    def work(self):
        print('Coding Python Programs')
    def empInfo(self):
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee No: ',self.eno)
        print('Employee Sal: ',self.esal)
e=Employee('Durga',48,872425,100000)
e.eatAndDrink()
e.work()
e.empInfo()

##Output:
Eat Biryani and Drink Beer
Coding Python Programs
Employee Name:  Durga
Employee Age:  48
Employee No:  872425
Employee Sal:  100000

##Example4: ***********Optimized code
##-We need to use Super(), if we want to call parent class members from child class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eatAndDrink(self):
        print('Eat Biryani and Drink Beer')
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name, age) ###We need to use super()
        self.eno=eno
        self.esal=esal
    def work(self):
        print('Coding Python Programs')
    def empInfo(self):
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee No: ',self.eno)
        print('Employee Sal: ',self.esal)
e=Employee('Durga',48,872425,100000)
e.eatAndDrink()
e.work()
e.empInfo()

##Output:
Eat Biryani and Drink Beer
Coding Python Programs
Employee Name:  Durga
Employee Age:  48
Employee No:  872425
Employee Sal:  100000

##Example5: Loan example with & without inheritance:
#Without:
class HomeLoan:
    300 methods
class VehicleLoan:
    300 methods
class PersonalLoan:
    300 methods
900 methods
90 hours development time

#With:
class Loan: ##Parent Class
    250 Common Methods
class HomeLoan(Loan):
    50 Specific Methods ##internally 250commonmethods+50specificmethods
class VehicleLoan(Loan):
    50 Specific Methods ##internally 250commonmethods+50specificmethods
class PersonalLoan(Loan):
    50 Specific Methods ##internally 250commonmethods+50specificmethods
400 Methods
40 hours of development time

-----------------------------------------------------------------------------
##IS-A vs HAS-A relationship:
-If we want to extend existing functionality with some more extra functionality then we should go for IS-A Relationship or Inheritance.
-If we don't want to extend and just we have to use existing functionality then we should go for HAS-A relationship or composition.

##Example5:
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getInfo(self):
        print('\tCar Name: {}\n\tModel: {}\n\tColor: {}'.format(self.name, self.model, self.color))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eatAndDrink(self):
        print('Eat Biryani and Drink Beer')
class Employee(Person):  ##Employee """IS-A""" Person.
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)  ###We need to use super()
        self.eno = eno
        self.esal = esal
        self.car = car  ##Employee """HAS-A""" Car.
    def work(self):
        print('Coding Python Programs')
    def empInfo(self):
        print('Employee Name: ', self.name)
        print('Employee Age: ', self.age)
        print('Employee No: ', self.eno)
        print('Employee Sal: ', self.esal)
        print('')
        print('Employee Car Information: ')
        self.car.getInfo() ##Employee using car functionality
car = Car('Innova', '2.5v', 'Metallic Grey')
e = Employee('Durga', 48, 872425, 100000)
e.eatAndDrink() ##Employee using Person class functionality
e.work()
e.empInfo()

##Output:
Eat Biryani and Drink Beer
Coding Python Programs
Employee Name:  Durga
Employee Age:  48
Employee No:  872425
Employee Sal:  100000

Employee Car Information: 
	Car Name: Innova
	Model: 2.5v
	Color: Metallic Grey
--------------------------------------------------------------------------------

##Composition vs Aggregation:

##Composition:
-HAS-A is also known as Composition and Aggregation as well, confused!! Let's debug it.
-UniversityObject/ContainerObject = {'CSE,ECE,EEE,IT,ME,CE'}
-Each department (CSE,IT...) can be called as DepartmentObject/ContainedObject.
-If University closes, all the department will be closed, without existing of university object, department object won't exists. In other words, without existing of container object, contained object won't exists.
##Contained Object """HAS-A""" contained object
-Therefore container object and contained objects are strongly associated. This strong association is nothing but Composition.
class University:
    def __init__(self):
        self.dept=self.Department()
    class Department:
        pass
u=University() ##This will auto create Department object as well.
d=Department()  ##***Not feasible.
##Note: Relation between inner class and Outter class object is the best example for composition

##Ouput:
Inner class, Outer class relation
NameError: name 'Department' is not defined


##Aggregation:
-Consider there are 3 professors (Contained Objects) in a department object (COntainer Object) MCA.
-In future if MCA dept is closed, the professors can work other departments or move to other CS department.
-Here contained object are not depending on container object, their exitence is not dependent on container object, they're weakly associated.
-The above concept is nothing but Aggregation.
##Department """HAS-A""" professor
class Professor:
    print('Yo yo students, welcome to engineering')
    pass
class Department:
    def __init__(self,prof):
        self.prof=prof
        print('Welcome to your respective Department')
prof=Professor()    ##Without existing department object, we've created professor.
csdept=Department(prof) ##Professor can work for CS dept
itdept=Department(prof) ##Professor can also work for IT dept as well
##Note: 
#-In above example non-existence of Department doesn't impact the existence of professor.
#-Here outer class, inner class concept don't go well.
#-In Composition objects are strongly associated where as in Aggregation objects are weakly associated.
#-In composition, container object holds directly contained objects, where as in Aggregation container object just '''holds references''' of contained objects.

##Output:
Yo yo students, welcome to engineering
Welcome to your respective Department
Welcome to your respective Department

------------------------------------------------------------------------------

##Types of inheritance:
    -Single level inheritance : ##Concept of inheriting members from one/single class to another class (Single parent and single child).
    -Multi level inheritance (aka Multiple levels of inheritance) : ##Granparent >> Parent >> Child (Concept of inheriting members of multiple classes to one/single class, with concept of one after another/step by step manner).
    -Hierarchical inheritance : ##The concept of inheriting members from one class to multiple classes which is present at same level is known as Hierarchical inheritance. (One Parent but Multiple child classes and all child classes are at same level).
    -Multiple inheritance
    -Hybrid inheritance
    -Cyclic inheritance

##Single level inheritance:
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        print('Child Method')
c=C()
c.m1()
c.m2()

##Ouput:
Parent Method
Child Method

##Multi level inheritance:
class GP:
    def m1(self):
        print('Grand Parent Method')
class P(GP):
    def m2(self):
        print('Parent Method')
class C(P):
    def m3(self):
        print('Child Method')
c=C()
c.m1()
c.m2()
c.m3()

##Output:
Grand Parent Method
Parent Method
Child Method

##Hierarchical inheritance:
class P:
    def m1(self):
        print('Parent Method')
class C1(P):
    def m2(self):
        print('Child1 Method')
class C2(P):
    def m3(self):
        print('Child2 Method')
c1=C1()
c1.m1()
c1.m2()
c1.m3() ##This will throw error
c2=C2()
c2.m1()
c2.m3()
c2.m2() ##This will throw error

##Output:
Parent Method
Child1 Method
AttributeError: 'C1' object has no attribute 'm3'. Did you mean: 'm1'?
Parent Method
Child2 Method

---------------------------------------------------------------------------

##Mutiple Inheritance:
-This is reverse of Hierarchical Inheritance.
-Hierarchical : One parent and Multiple Child classes.
-Multiple : Multiple Parents and Single Child class.
-The concept of inheriting the members from multiple classes to a single class at a time is known as multiple inheritance i.e. Multiple Parents but Single Child.
-The above concept not available in Java,CSharp,.net etc
P1Class     P2Class
m1 method   m1 method        
  \---------/
    \      /
      \   /
       Child class
       c.m1() ?? will come from P1/P2 is the question in Java & other programs, this issue is called Diamond access problem/ambiguity problem, how it is solved in Python??
-To solve above Problem in Python:
If the same method is inherited from both parent classes, then Python will always consider the order of Parent classes in the declaration of the child class.
class C(P1,P2):====>P1 method will be considered
class C(P2,P1):====>P2 method will be considered

##Example1:
class P1:
    def m1(self):
        print('Parent1 Method')
class P2:
    def m2(self):
        print('Parent2 Method')
class C(P1,P2): ##Order is important*********
    def m3(self):
        print('Child Method')
c=C()
c.m1()
c.m2()
c.m3()

##Output:
Parent1 Method
Parent2 Method
Child Method

##Example2, Solving Diamond access problem:
class P1:
    def m1(self):
        print('M1 method from Parent1 Class')
class P2:
    def m1(self):
        print('M2 method from Parent2 Class')
class C(P1,P2): ##Order is important*********
    def m2(self):
        print('Child Method')
c=C()
c.m1() ##The output comes from P1 since P1 is placed at the first place in C(P1,P2)

##Output:
M1 method from Parent1 Class


##Example3, Solving Diamond access problem:
class P1:
    def m1(self):
        print('M1 method from Parent1 Class')
class P2:
    def m1(self):
        print('M2 method from Parent2 Class')
class C(P2,P1): ##Order is important*********
    def m2(self):
        print('Child Method')
c=C()
c.m1() ##The output comes from P2 since P2 is placed at the first place in C(P2,P1)

##Output:
M2 method from Parent2 Class

----------------------------------------------------------------------------

##Hybrid & Cyclic Inheritance:

##Hybrid Inheritance:
-Hybrid means mixing/combination
-Combination of Single,Multi Level, Multiple and Hierarchical inheritances is known as Hybrid Inheritance.
##-Note: In Hybrid inheritance, metjod resolution is based on MRO algorithm.
A       B    C      ##Multiple Parents & Single Child, Nothing but Multiple Inheritance
  \     |   /
    \   |  /
      \ | /
        D       ###Single Inheritance
        |
        |
        E       ###Multi Level Inheritance
        |
        |
        F       ###Hierarchical Level Inheritance
       /\
      /  \
     /    \
    G      H
    
##Cyclic Inheritance: 
-The concept of inheriting members from one class to another class in cyclic way, is called cyclic inheritance.
-No programming language including Python doesn't provide this kind of support.
-In general this type of inheritance is not necessary in our program.
A__     ##Parent and Child are of same class
^  |
|__| 

A--->B  ##A is child of B and B is child of A
^    |
|____| 

class A(A):
    pass
##Output:
NameError: name 'A' is not defined

class A(B):
    pass
class B(A):
    pass
##Output:
NameError: name 'B' is not defined

----------------------------------------------------------------------------
##Method Resolution Order:
-Every class in Python has a parent class called as Object class, most commonly required methods for every class is inherited from Object class only.
-We can also say every Python class is a child class of Object class, Object class acts as Root to Python class hierarchy, but very rarely we use it. 

        A 
        ^
       /\
      /  \
     /    \
    B      C
    ^      ^
    \     /
     \   /
      \ /
       D  
d=D()
d.m1() ##From where this m1() will be executed? whether from B/C/A, if it is not present in B/C/A so is it from object class  ? The search is based on MRO. This can be viewed by using print(classname.mro())
-In hybrid inheritance the method resolution order is decided based on MRO algorithm.
-We can find MRO of any class by using mro() function.
print(classname.mro())

##Example1:
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):   ##****Order matters
    pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
##Output:
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

##Example2:
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(A):
    def m1(self):
        print('C class method')
class D(B,C):   ##****Order matters
    pass
    def m1(self):
        print('D class method')
d=D()
d.m1()

##Output:
D class method

##Example3:
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(A):
    def m1(self):
        print('C class method')
class D(B,C):   ##****Order matters
    pass
    '''def m1(self):
        print('D class method')'''
d=D()   ##According to MRO >>> DBCAO
d.m1()

##Output:
B class method

##Example4:
class A:
    def m1(self):
        print('A class method')
class B(A):
    pass
    '''def m1(self):
        print('B class method')'''
class C(A):
    pass
    '''def m1(self):
        print('C class method')'''
class D(B,C):   ##****Order matters
    pass
    '''def m1(self):
        print('D class method')'''
d=D()   ##According to MRO >>> DBCAO
d.m1()

##Output:
A class method

##Example5:
class A:
    pass
    '''def m1(self):
        print('A class method')'''
class B(A):
    pass
    '''def m1(self):
        print('B class method')'''
class C(A):
    pass
    '''def m1(self):
        print('C class method')'''
class D(B,C):   ##****Order matters
    pass
    '''def m1(self):
        print('D class method')'''
d=D()   ##According to MRO >>> DBCAO
d.m1()

##Output:
AttributeError: 'D' object has no attribute 'm1'

---------------------------------------------------------------------------

##Method Resolution Order (MRO) - Part2

    Object
   ^  ^   ^
  /   |    \
 /    |     \
A     B      C
^     ^      ^   
 \    /\    / \  
  \  /  \  /   \ 
   \/    \/     \
    D     E     /
    ^     ^    /
    \    /    /
     \  /    /
      \/    /
       F___/

##Example1:
class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(B,C): pass
class F(D,E,C): pass
print(A.mro()) ##A,O
print(B.mro()) ##B,O
print(C.mro()) ##C,O
print(D.mro()) ##D,A,B,O
print(E.mro()) ##E,B,C,O

##Output:
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class 'object'>]
[<class '__main__.C'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
[<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

##Example2:
class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(B,C): pass
class F(D,E,C): pass
print(F.mro())

##Output:
[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

##Example2:
class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('C class method')
class D(A,B):
    def m1(self):
        print('D class method')
class E(B,C):
    def m1(self):
        print('E class method')
class F(D,E,C):
    def m1(self):
        print('F class method')
f=F()
f.m1()

##Output:
F class method

##Example3:
class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('C class method')
class D(A,B):
    def m1(self):
        print('D class method')
class E(B,C):
    def m1(self):
        print('E class method')
class F(D,E,C):
    pass
f=F()
f.m1()

##Output:
D class method

##Example4:
class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('C class method')
class D(A,B):
    pass
class E(B,C):
    def m1(self):
        print('E class method')
class F(D,E,C):
    pass
f=F()
f.m1()

##Output:
E class method

##Example5:
class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('C class method')
class D(A,B):
    pass
class E(B,C):
    pass
class F(D,E,C):
    pass
f=F()
f.m1()

##Output:
A class method

##Example6:
class A:
    pass
class B:
    pass
class C:
    def m1(self):
        print('C class method')
class D(A,B):
    pass
class E(B,C):
    pass
class F(D,E,C):
    pass
f=F()
f.m1()

##Output:
C class method

####MRO Algorithm:
-This is also known as C3 algorithm.
-Proposed by Samuele Padroni
-Follows DLR (Depth First Left to Right) Ex: DBCA in below example
    -i.e. Child will get more priority than Parent.
    -Left Parent will get more priority than Right Parent.
        A 
        ^
       /\
      /  \
     /    \
    B      C
    ^      ^
    \     /
     \   /
      \ /
       D  
-mro(x)=x+merge(mro(p1),mro(p2),.....,parentlist)
-p1,p2...These are the immediate parent of x.
-Here we have to considered only immediate parents.
-HeadElement vs TailElement:
============================
c1,c2,c3,c4.......
c1 i.e. the first element is the Head element in the sequence of classes.
c2,c3,c4... i.e. remaining elements is considered as the Tail part in the sequence of classes.

-How does the merge works??
-Sequence of List: (ABC,BCD,DEF)
    -Take the head element from first list i.e. 'A' and next check whether it is present in the tail part of any element i.e. 'CD' and 'EF', Nope! not present.
    -If 'A' is not present in any of remaining list tail element, then please add to result and remove it from all the lists.
    -If the head present in tail part of any other list, then consider head element of the next list and continue same process.


##Example1:

    Object
   ^  ^   ^
  /   |    \
 /    |     \
A     B      C
^     ^      ^   
 \    /\    / \  
  \  /  \  /   \ 
   \/    \/     \
    D     E     /
    ^     ^    /
    \    /    /
     \  /    /
      \/    /
       F___/

A.mro()= A,O
B.mro()= B,O
C.mro()= C,O
D.mro()= D,A,B,O
E.mro()= E,B,C,O
F.mro()= x+merge(p1,p2,p3,..,parentlist)
       = F+merge(mro(D),mro(E),mro(C),DEC)
       = F+merge(DABO,EBCO,CO,DEC)
       = F+D+merge(ABO,EBCO,CO,EC)
       = F+D+A+merge(BO,EBCO,CO,EC)
       = F+D+A+E+merge(BO,BCO,CO,C)
       = F+D+A+E+B+merge(O,CO,CO,C)
       = F+D+A+E+B+C+merge(O,O,O)
       = F,D,A,E,B,C,O

class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(B,C): pass
class F(D,E,C): pass
print(F.mro())

##Output:
[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]


#Example2:

A.mro()= A,O
B.mro()= B,O
C.mro()= C,O
D.mro()= D,A,B,O
E.mro()= E,A,C,O
F.mro()= x+merge(p1,p2,p3,..,parentlist)
       = F+merge(mro(D),mro(E),DE)
       = F+merge(DABO,EACO,DE)
       = F+D+merge(ABO,EACO,E)
       = F+D+E+merge(ABO,ACO)
       = F+D+E+A+merge(BO,CO)
       = F+D+E+A+B+merge(O,CO)
       = F+D+E+A+B+C+merge(O,O)
       = F,D,E,A,B,C,O

class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(A,C): pass
class F(D,E): pass
print(F.mro())

##Output:
[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

------------------------------------------------------------------------------

##Super() function:

#Example1:
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        self.m1()
        print('Child Method')
c=C()
c.m2()

##Output:
Parent Method
Child Method

#Example2: Both Parent & Child have method name as m1():
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m1(self):
        self.m1()
        print('Child Method')
c=C()
c.m1()

##Output:
File "C:\Users\91961\PycharmProjects\pythonProject\Web\Udemy.py", line 6, in m1
    self.m1()
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

#Example3: 
-To overcome above issue of naming conflict, we can use super(), super() is a inbuilt python function used to access super class constructors, methods,variables etc explicitly inside a Child class
- We can use Super() whenever there is naming conflict/ambiguity

class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m1(self):
        super().m1()
        print('Child Method')
c=C()
c.m1()

##Output:
Parent Method
Child Method

-----------------------------------------------------------------------------

##To describe use of super():
-From child class to access the members of parent class explicitly when there is a naming conflict, then we have to use super().

##Example1:
class P:
    a=10
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent Instance Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent Static Method')
class C(P):
    def __init__(self):
        print('Child Constructor')
    def method1(self):
        print(super().a) ##also we can use self.a
        super().m1()  ##also we can use self.m1()
        super().m2()  ##also we can use self.m2()
        super().m3()  ##also we can use self.m3()
        super().__init__()  ##Naming conflict need to use super() if we want the parent constructor.
c=C()
c.method1()

##Output:
Child Constructor
10
Parent Instance Method
Parent Class Method
Parent Static Method
Parent Constructor

##Example2 (As an amateur):
class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Student(Person):
    def __init__(self,name,age,height,weight,rollno,marks):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
        print('Rollno: ',self.rollno)
        print('Marks: ',self.marks)
s=Student('Durga','48',5.7,85,872454,90)
s.display()

##Output:
Name:  Durga
Age:  48
Height:  5.7
Weight:  85
Rollno:  872454
Marks:  90

##Example2 (As a beginner):
class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Student(Person):
    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight) ##Here is the change
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
        print('Rollno: ',self.rollno)
        print('Marks: ',self.marks)
s=Student('Durga','48',5.7,85,872454,90)
s.display()

##Output:
Name:  Durga
Age:  48
Height:  5.7
Weight:  85
Rollno:  872454
Marks:  90

##Example2 (As an exp):
class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Student(Person):
    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight) ##Here is the change
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print('Rollno: ',self.rollno)
        print('Marks: ',self.marks)
s=Student('Durga','48',5.7,85,872454,90)
s.display()

##Output:
Name:  Durga
Age:  48
Height:  5.7
Weight:  85
Rollno:  872454
Marks:  90

---------------------------------------------------------------------------
##To call method of a particular super class:

class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        super().m1()
e=E()
e.m1()

##Output:
E class method

class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        super().m1()
e=E()
e.m1()

##Output:
D class method

##To access particular method:
##1st Way
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        B.m1(self) ##classname.m1(self)
e=E()
e.m1()

##Output:
B class method

##2nd Way:
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        super(C,self).m1() ##Watch out, output is not C class method..........It's little twisting ;)
e=E()
e.m1()

##Output:
B class method


class A:
    def m1(self):
        print('A class method')  ##Impratical way, not recommended
class B(A):
    def m1(self):
        super().m1()
class C(B):
    def m1(self):
        super().m1()
class D(C):
    def m1(self):
        super().m1()
class E(D):
    def m1(self):
        super().m1()
e=E()
e.m1()

##Output:
A class method

----------------------------------------------------------------------------

##super() vs Parent class instance variable:

##Example1:
class P:
    a=888 ##static varaible
    def __init__(self):
        self.b=999 ##instance variable
class C(P):
    def m1(self):
        print(self.a) ##No naming conflict
        print(self.b) ##No naming conflict
c=C()
c.m1()
##Output:
888
999      

##Example2:
class P:
    a=888 ##static varaible
    def __init__(self):
        self.b=999 ##instance variable
class C(P):
    def m1(self):
        print(super().a) ##888
        print(super().b) ##Will throw error, super() cannot be used to access the parent class instance variable, please use self.b
c=C()
c.m1()

##Output:
888
AttributeError: 'super' object has no attribute 'b'


##Example3:
class P:
    a=888 ##static varaible
    def __init__(self):
        self.b=999 ##instance variable
class C(P):
    def __init__(self):
        self.b=20 ##instance variable
    def m1(self):
        print(super().a) ##888
        print(self.b) ##Output is 20 not 999??how to access parent member?? Never possible
####**********Note: We cannot use super() to access parent class instance variables from child class. We should use self only.
c=C()
c.m1()

##Output:
888
20

-----------------------------------------------------------------------------

##Various Loop holes of Super():
-From child class constructor and instance methods, we can call parent class constructors, instance methods, class methods and static methods by using super().
-From child class, class method we cannot access parent class constructor and instance methods directly by using super(). But we can access parent class static and class methods.
    Reason: Class method no way related to Object. Without object also we can call class method. But Constructor and instance methods are always associated with object.
-From child class static method, we cannot use super() to call parent class members. But indirectly we can call parent class static and class methods.
    Reason: Static no related to object, no way related to class, instance and constructor as welllllll....

##Example1:
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent Instance Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent Static Method')
class C(P):
    def __init__(self):
        super().__init__() ##valid
        super().m1() ##valid
        super().m2() ##valid
        super().m3() ##valid
    def m1(self):
        super().__init__() ##valid
        super().m1() ##valid
        super().m2() ##valid
        super().m3() ##valid
    @classmethod
    def m2(cls):
        super().__init__() ##Error
        super().m1() ##Error
        super().m2() ##Valid
        super().m3() ##Valid
    @staticmethod
    def m3():
        super().__init__()  ##Invalid
        super().m1()  ##Invalid
        super().m2()  ##Invalid
        super().m3()  ##Invalid
c=C()
c.m1()

##Output:
Parent Constructor
Parent Instance Method
Parent Class Method
Parent Static Method
Parent Constructor
Parent Instance Method
Parent Class Method
Parent Static Method
TypeError: P.__init__() missing 1 required positional argument: 'self'
TypeError: P.m1() missing 1 required positional argument: 'self'
Parent Class Method
Parent Static Method
RuntimeError: super(): no arguments
RuntimeError: super(): no arguments
RuntimeError: super(): no arguments
RuntimeError: super(): no arguments

##We can overcome the issues of @classmrthod and @staticmethod indirectly:

##Example1:
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent Instance method')
class C(P):
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
C.m2()

##Output:
Parent Constructor
Parent Instance method

##Example2:
class P:
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent Static Method')
class C(P):
    @staticmethod
    def m2():
        super(C,C).m2()
        super(C,C).m3()
C.m2()

##Output:
Parent Class Method
Parent Static Method

-------------------------------------------------------------------------------

##Polymorphism:
Poly means Many and Morphs means Forms.
One Name but multiple forms is the concept of polumorphism.
Ex: 
1. Ourself, i.e. the behaviour of a person at home with friends, outside home with friends and in a new city.
2. The same plus '+' operator, but multiple behaviour, this is called as operator overloading.
    -Operator Overloading
    -Method Overloading
    -Constructor Overloading
    10+20 = 30
    'Durga' + 'Soft' = 'DuragSoft'
3. Let's do some method overriding,
    -Method Overriding
    -Constructor Overriding
   class P:
    def marry(self):
        print('Subbalakshmi')
   class C(P): pass
   c=C()
   c.marry()
   ##Output: Subbalakshmi
   
   class P:
    def marry(self):
        print('Subbalakshmi')
   class C(P):
    def marry(self):
        print('Katrina Kaif') ##Method Overriding
   c=C()
   c.marry()
   ##Output: Katrina Kaif
   
------------------------------------------------------------------------------
##Overloading:
-Operator overloading
-Method overloading
-Constructor overloading

##Operator Overloading:
-We can use same operator for multiple purposes, which is nothing but operator overloading.
-Pyhton supports operator overloading.
-Java won't provide support for operator overloading.

#Example1: '+' Operator
print(10+20) ##30
print('Durga'+'Soft') ##DurgaSoft

#Example2: '*' Operator
print(10*20) ##200
print('durga'*3) ##durgadurgadurga

#Example3:
class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
b2=Book(200)
print(b1+b2)

##Output: 
TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

##To overcome above type error we can use magic method __add__, whenever we try to run a '+' operator between two objects internally PVM runs the magic method __add__() available inside the class, but currently it is not defined yet, so let's use it overcome the adding of two objects.
##This is also one way of operator overloading.
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        total_pages=self.pages+other.pages
        return total_pages
b1=Book(100)
b2=Book(200)
print(type(b1))
print(type(b2))
print(b1+b2)
print(type(b1+b2))

##Output:
<class '__main__.Book'>
<class '__main__.Book'>
300
<class 'int'>

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        total_pages=self.pages+other.pages
        return total_pages
b1=Book(100)
b2=Book(200)
b3=Book(500)
print(b1+b2)
print(b2+b3)
print(b1+b3)
print(b1+b2+b3) ##Type Error, because b1+b2 will result in int and adding it to 'BOOK' type is not allowed.

##Output:
300
600
700
TypeError: unsupported operand type(s) for +: 'int' and 'Book'

-----------------------------------------------------------------------------

##List of magic methods in Python:
+ ==> __add__()
- ==> __sub__()
* ==> __mul__()
/ ==> __div__()
// ==> __floordiv__()
% ==> __mod__()
** ==> __pow__()
< ==> __lt__()
> ==> __gt__()
+= ==> __iadd__() ##Compound assignment operator
-= ==> __isub__() ##Compound assignment operator
*= ==> __imul__()
/= ==> __idiv__()
//= ==> __ifloordiv__()
**= ==> __ipow__()
%= ==> __imod__()
<= ==> __le__()
>= ==> __ge__()
== ==> __eq__()
!= ==> __ne__()

##By implementing above magic methods we can perform method overloading.

#Example1:
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student('Durga',100)
s2=Student('Ravi',200)
print(s1>s2)

##Output:
TypeError: '>' not supported between instances of 'Student' and 'Student'

#Example2:
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks > other.marks
    def __le__(self, other):
        return self.marks <= other.marks
s1=Student('Durga',100)
s2=Student('Ravi',200)
print(s1>s2)
print(s1<s2) ##To provide support lt method, internally PVM will reverse functionality to provide support, no need to explicitly implement the lt, that's cool!!
print(s1>=s2) ##Even here PVM takes care of it internally.
print(s1<=s2)

##Output:
False
True
False
True

##Example3:
class Employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
class TimeSheet:
    def __init__(self,name,workingDays):
        self.name=name
        self.workingDays=workingDays
e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary: ',e*t)

##Output:
TypeError: unsupported operand type(s) for *: 'Employee' and 'TimeSheet'

class Employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
    def __mul__(self, other):
        salary = self.salaryPerDay * other.workingDays
        return salary
class TimeSheet:
    def __init__(self,name,workingDays):
        self.name=name
        self.workingDays=workingDays
e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary: ',e*t)
print('This Month Salary: ',t*e) ##Type error, because magic method is defined in the Employee class, therefore order is important.

##Output:
This Month Salary:  12500
print('This Month Salary: ',t*e)
TypeError: unsupported operand type(s) for *: 'TimeSheet' and 'Employee'

class Employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
    def __mul__(self, other):
        salary = self.salaryPerDay * other.workingDays
        return salary
class TimeSheet:
    def __init__(self,name,workingDays):
        self.name=name
        self.workingDays=workingDays
    def __mul__(self, other):
        salary = self.workingDays * other.salaryPerDay ##swapping is required
        return salary
e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary: ',e*t)
print('This Month Salary: ',t*e)

##Output:
This Month Salary:  12500
This Month Salary:  12500

------------------------------------------------------------------------------

##Importance of __str__() method:
-Whenever we are trying to print any object reference, internally __str__() method will be called.
-The default implementation of this method returns the string in the following format: <__main__.Student object at 0x000001E89CD60F70>
-To provide meaningful string representation for our object, we have to override __str__() method in our class.


#Example:
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
s1=Student('Durga',101,95)
s2=Student('Ravi',102,98)
print(s1) ##Default string implementation reference or location will be printed
print(s2) ##Default string implementation reference or location will be printed

##Ouput:
<__main__.Student object at 0x000001E89CD60F70>
<__main__.Student object at 0x000001E89CD30E20>

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return self.name
s1=Student('Durga',101,95)
s2=Student('Ravi',102,98)
print(s1)
print(s2)

##Output:
Durga
Ravi


class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return self.rollno
s1=Student('Durga',101,95)
s2=Student('Ravi',102,98)
print(s1)
print(s2)

##Output:
TypeError: __str__ returned non-string (type int)

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return 'Name: {}, Rollno: {}, Marks: {}'.format(self.name,self.rollno,self.marks)
s1=Student('Durga',101,95)
s2=Student('Ravi',102,98)
print(s1)
print(s2)

##Output:
Name: Durga, Rollno: 101, Marks: 95
Name: Ravi, Rollno: 102, Marks: 98

----------------------------------------------------------------------------------------

##Overloading of + operator for Nesting requirements:
 
 -Let's try and understand on how to do b1+b2+b3??, it's little different from b1+b2....
 
##Example1:
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
b3=Book(500)
print(b1+b2)
print(b1+b2+b3) ##Error

##Output:
300
TypeError: unsupported operand type(s) for +: 'int' and 'Book'

##Example2:
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
b1=Book(100)
b2=Book(200)
b3=Book(500)
print(b1+b2)
print(b1+b2+b3) ##(Book(b1+b2))+b3 and will return book object and when we try to print book object, internally a str method will be called.

##Output:
<__main__.Book object at 0x0000019309502D70>
<__main__.Book object at 0x0000019309502D10>

##Example3:
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return  'Total Number of pages: {}'.format(self.pages)
b1=Book(100)
b2=Book(200)
b3=Book(500)
b4=Book(1000)
print(b1+b2)
print(b1+b2+b3) 
print(b1+b2+b3+b4)

##Output:
Total Number of pages: 300
Total Number of pages: 800
Total Number of pages: 1800

##Example4:
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        print('add method executed.......')
        return Book(self.pages+other.pages)
    def __str__(self):
        return  'Total Number of pages: {}'.format(self.pages)
    def __mul__(self,other):
        print('mul method executed.......')
        return Book(self.pages*other.pages)
b1=Book(100)
b2=Book(200)
b3=Book(500)
b4=Book(1000)
print(b1+b2)
print(b1+b2+b3) 
print(b1+b2+b3+b4)
print(b1*b2)
print(b1+b2*b3)
print(b1+b2*b3+b4)

##Output:
Total Number of pages: 300
Total Number of pages: 800
Total Number of pages: 1800
Total Number of pages: 20000
Total Number of pages: 100100
Total Number of pages: 101100
##After adding print statement for add and mul....
add method executed.......
Total Number of pages: 300
add method executed.......
add method executed.......
Total Number of pages: 800
add method executed.......
add method executed.......
add method executed.......
Total Number of pages: 1800
mul method executed.......
Total Number of pages: 20000
mul method executed.......
add method executed.......
Total Number of pages: 100100
mul method executed.......
add method executed.......
add method executed.......
Total Number of pages: 101100

-----------------------------------------------------------------------------

##Method Overloading: We say two methods are overloaded, when both methods are having same way, but different argument types.
##***************Python doesn't support method and constructor overloading concept.....
##Therefore if multiple methods of same name is defined within a class, then only the last method will be considered. Same goes with constructor.

##Example:
class Test:
    def m1(self):
       print('No-arg method')
    def m1(self,x):
       print('One-arg method')
    def m1(self,x,y):
       print('Two-arg method') ##Only last method is considered.
t=Test()
t.m1()

##Output:
TypeError: Test.m1() missing 2 required positional arguments: 'x' and 'y'
##Note: Clearly shows it only considers the last method.

##Example2:
class Test:
    def m1(self):
       print('No-arg method')
    def m1(self,x):
       print('One-arg method')
    def m1(self,x,y):
       print('Two-arg method') ##Only last method is considered.
t=Test()
t.m1(2)

##Output:
TypeError: Test.m1() missing 1 required positional argument: 'y'

##Example3:
class Test:
    def m1(self):
       print('No-arg method')
    def m1(self,x):
       print('One-arg method')
    def m1(self,x,y):
       print('Two-arg method') ##Only last method is considered.
t=Test()
t.m1(2,6)

##Output:
Two-arg method

----------------------------------------------------------------------------------

##Method Overloading:
-Two methods are said to be overloaded if both methids having same name, but different arguments types.
ex: sqrt(int), sqrt(float)
-But in Python, we cannot declare type explicitly. Based on provided value type will be considered automatically(Dynamically Typed). As type concept is not apllicable, method overloading concept is not applicable in Python.

##Example:
class Test:
    def m1(self,x):
        print('{}-argument method'.format(x.__class__.__name__)) ##Best way to find the data type
        print('{}-argument method'.format(type(x)))
t=Test()
t.m1(10)
t.m1(10.5)
t.m1('Durga')

##Output:
int-argument method
<class 'int'>-argument method
float-argument method
<class 'float'>-argument method
str-argument method
<class 'str'>-argument method

##Note: 
-Above example clearly proves that we don't need method overloading in Python, single can take care different data types since it is Dynamically typed.
-In Java it's a different case, there we need to try multiple methods for each data type, hence method overloading comes into picture.

----------------------------------------------------------------------------

##Example1: This also clearly tells, method overloading is not required.
class Test:
    def m1(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            print('Three-argument method')
        elif a is not None and b is not None:
            print('Two-argument method')
        elif a is not None:
            print('One-argument method')
        else:
            print('No-argument method')
t=Test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)
t.m1(10,20,30,40) ##Will give a type error.
t.m1(10,20,30,40,50) ##Will give a type error.

##Output:
No-argument method
One-argument method
Two-argument method
Three-argument method

##Example2: Variable length argument helps in overcoming the argument limitation.
class Test:
    def m1(self,*args):
        print('Variable length argument method')
t=Test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30,40)
t.m1(10,20,30,40,50)

##Output:
Variable length argument method
Variable length argument method
Variable length argument method
Variable length argument method
Variable length argument method

#Example3: Practical implementation of above example:
class Test:
    def sum(self,*args):
        tot=0
        for x in args:
            tot=tot+x
        print('The Sum: ',tot)
t=Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)

##Output:
The Sum:  0
The Sum:  10
The Sum:  30
The Sum:  60

-------------------------------------------------------------------------------

##Constructor overloading: Constructor overloading is also not supported in Python similar to method overloading and also similar to method overloading if there are multiple constructors with same name, then Python will consider the latest/last constructor. If really required we can achieve with
-Constructor with default arguments.
-Constructor with variable number of arguments.

#Example1:
class Test:
    def __init__(self):
        print('no-arg constructor')
    def __init__(self,x):
        print('one-arg constructor')
    def __init__(self,x,y): ##Only this will be available
        print('two-arg constructor')
t=Test() ##Error
t=Test(10) ##Error
t=Test(10,20) ##Valid

##Output:
TypeError: Test.__init__() missing 2 required positional arguments: 'x' and 'y'
TypeError: Test.__init__() missing 2 required positional arguments: 'x' and 'y'
two-arg constructor

#Example2:
class Test:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 number of arguments')
t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)
t=Test(10,20,30,40)

##Output:
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
TypeError: Test.__init__() takes from 1 to 4 positional arguments but 5 were given

#Example3:
class Test:
    def __init__(self,*args):
        print('Constructor with variable number of arguments')
t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)
t=Test(10,20,30,40)

##Output:
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments

Type of Loading          Pyhton      Java
-Operator Overloading       Yes        No
-Method Overloading         No         Yes
-Constructor Overloading    No         Yes

-----------------------------------------------------------------------------

##Method Overriding:
Whatever members present in Parent class are by default available to the child class through inheritance. Sometimes child class may not satisfy with Parent class implementation, then child class is allowed to re-define that method based on its requirement. This process is called overriding.
Overriding concept applicable for methods and constructors.

##Example1:
class Parent:
    def property(self):
        print('Land+gold+cash+power')
    def marry(self):    ##Overridden method
        print('Appalamma')
class Child(Parent):
    def marry(self):    ##Method Overriding
        print('Katrina Kaif')
c=Child()
c.property()
c.marry()

##Output:
Land+gold+cash+power
Katrina Kaif

##Example2:
class Parent:
    def property(self):
        print('Land+gold+cash+power')
    def marry(self):    ##Overridden method
        print('Appalamma')
class Child(Parent):
    def marry(self):    ##Method Overriding
        super().marry() ##To also to call parent class method
        print('Katrina Kaif')
c=Child()
c.property()
c.marry()

##Output:
Land+gold+cash+power
Appalamma
Katrina Kaif

--------------------------------------------------------------------------------

##Constructor Overriding:

##Example1:
class Parent:
    def __init__(self): ##Overriden method
        print('Parent Constructor')
class Child(Parent):
    def __init__(self): ##Overriding method
        print('Child Constructor')
c=Child()

##Output:
Child Constructor

##Example2:
class Parent:
    def __init__(self): ##Overriden method
        print('Parent Constructor')
class Child(Parent):
    def __init__(self): ##Overriding method
        super().__init__() ##To also to call parent class method
        print('Child Constructor')
c=Child()

##Output:
Parent Constructor
Child Constructor

-----------------------------------------------------------------------

Overriding Demo Program:

##Example1 (Overriding as an amateur):
class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Employee(Person):
    def __init__(self,name,age,height,weight,eno,esal):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.eno=eno
        self.esal=esal
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
        print('Eno: ',self.eno)
        print('Esal: ',self.esal)
s=Employee('Durga','48',5.7,85,872,900000)
s.display()

##Output:
Name:  Durga
Age:  48
Height:  5.7
Weight:  85
Eno:  872
Esal:  900000

##Example2 (As a pro):
class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Employee(Person):
    def __init__(self,name,age,height,weight,eno,esal):
        super().__init__(name,age,height,weight)
        self.eno=eno
        self.esal=esal
    def display(self):
        super().display()
        print('Eno: ',self.eno)
        print('Esal: ',self.esal)
s=Employee('Durga','48',5.7,85,872,900000)
s.display()

##Output:
Name:  Durga
Age:  48
Height:  5.7
Weight:  85
Eno:  872
Esal:  900000

-----------------------------------------------------------------------------

##Polymorphism Summary: Gives more flexibility / friendliness
-Overloading:
    Operator Overloading : +,*........... (same operator for multiple forms, polymorphism)
    Method & Constructor > Not feasible
-Overriding:
    Method overriding
    Constructor overriding
-A boy starts love with the word frienship, A girl ends love with the same word friendship. Word is the same, but purpose is the different. This beautiful concept of OOPs is nothing but Polymorphism.

-----------------------------------------------------------------------------

##Abstraction:
-Abstract Method
-Abstract Class
-Interface
-Abstract means, something which is not having completeness. Just outline, example an abstract page in any text book / project report etc.
-******Sometimes we don't know about implementation, still we can declare a method. Such type of methods are called abstract methods .i.e abstract method has only declaration but not implementation (.i.e empty implementation).
-In Python, we can declare abstract method by using @abstractmethod decorator.
-Abstractmethod decorator present in abc module. Hence compulsory we should import abc module. (abc : Adbstract Base Class)
-For every abstract class in Python should be child class of abc class, the ABC class is present inside ABC module.
##ex:
from abc import abstractmethod, ABC
class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheels(self):
        pass
-Child classes are responsible to provide implementation for Parent class abstract methods.
-******Sometimes implementation of class is not complete, such type of partially implemented classes are called abstract class.
Abstract class ==> Partially implemented class
-Every abstract class in Python should be child class of ABC c class, which is present in abc module.
ABC ==> Abstract Base Class.
-For abstract classes, we can't create an object.

##Example:
from abc import abstractmethod,ABC
class Vehicle(ABC): ##We can't create an object for this due to incompleteness.
    @abstractmethod
    def getNoOfWheels(self):
        pass
class Bus(Vehicle): ##This is child class and concrete one which implemented properly and we can easily create an object for this, unlike the one for Vehicle class which doesn't have complete implementation.
    def getNoOfWheels(self):
        return 6
class Auto(Vehicle):
    def getNoOfWheels(self):
        return 3
b=Bus()
print(b.getNoOfWheels())
a=Auto()
print(a.getNoOfWheels())

##Output:
6
3

#What is abstract method? The method which has only declaration but not implementation(i.e. empty implementation)
#How to declare abstract method? By using @abstractmethod decorator
#What is abstract class? Partially implemented class is nothing but abstract class.
#How to declare abstract class in Python? The class should be child class of ABC class
#Who is responsible to provide implementation for abstract methods? Child classes are responsible to provide implementation for Parent class abstract methods
#What is the advantage of declaring abstract methods in Parent Class? By declaring abstract methods in Parent class we can provide guidelines to the child classes, such that which methods compulsory  they should implment. i.e. abstract methods by default needs to be implemented by child class, they've no choice.

from abc import abstractmethod,ABC
class Vehicle(ABC): ##We can't create an object for this due to incompleteness.
    @abstractmethod
    def getNoOfWheels(self):
        pass
class Bus(Vehicle): ##type error, abstract method to be included
    pass
b=Bus()

##Output:
TypeError: Can't instantiate abstract class Bus with abstract method getNoOfWheels

---------------------------------------------------------------------------

##Important Conclusions of Abstract Method & Abstract Class.
- If a class contains at least one abstract method and if we are extending ABC class then instantiation is not possible.
"For Abstract class with abstract methods instantiation is not possible"

##Example1:
class Test: ##Not abstract, because not child class of ABC i.e. not a abstract class
    pass
t=Test() ##Instantiation is Valid

##Example2:
from abc import *
class Test(ABC): ##Test is child class of ABC i.e. it is a abstract class
    pass         ##*****Abstract class can also contain zero number of methods also
t=Test() ##Valid because, even though class is abstract but it doesn't contain any abstract method.

##Example3:
from abc import *
class Test(ABC):    ##Abstract class
    @abstractmethod
    def m1(self):   ##Abstract method
        pass
t=Test() ##TypeError : Abstract class contains atleast one abstract method for that instantiation is not possible.
TypeError: Can't instantiate abstract class Test with abstract method m1

##Example4:
from abc import *
class Test: ##Not abstract class, becaise not child class of ABC.
    @abstractmethod
    def m1(self): ##Abstract method
        pass
t=Test() ##This is valid and object creation is allowed, given the class contains abstract method, but the class is not abstract class, hence it is valid

---------------------------------------------------------------------------

##2nd Conclusion:
If we're creating child class for abstract class, then for every abstract method of parent class compulsory we should provide implmentation in the child class, otherwise child class is also abstract and we cannot create object for child class.

#Example1:
from abc import *
class Test(ABC):    ##Abstract Class
    @abstractmethod
    def m1(self): ##Abstract Method
        pass
class subTest(Test): pass ##No implementation for abstract method.
s=subTest() ##Invalid, error, TypeError: Can't instantiate abstract class subTest with abstract method m1

#Example2:
from abc import *
class Test(ABC): ##Abstract Class
    @abstractmethod
    def m1(self): ##Abstract Method
        pass
    @abstractmethod
    def m2(self): ##Abstract Method
        pass
class SubTest(Test):
    def m1(self): ##Only m1 method implementation, nothing for m2, therefore error is thrown
        print('m1 method implementation')
s=SubTest() ##Invalid, TypeError: Can't instantiate abstract class SubTest with abstract method m2
s.m1()

#Example3:
from abc import *
class Test(ABC): ##Abstract Class
    @abstractmethod
    def m1(self): ##Abstract Method
        pass
    @abstractmethod
    def m2(self): ##Abstract Method
        pass
class SubTest(Test):
    def m1(self): 
        print('m1 method implementation')
    def m2(self):
        print('m2 method implementation')
s=SubTest() ##Valid, both methods are implemented
s.m1()
s.m2()

##Output:
m1 method implementation
m2 method implementation

#Example 4
from abc import *
class Test(ABC): ##Abstract Class
    def m1(self):
        print('Non-Abstract method')
    @abstractmethod
    def m2(self): ##Abstract Method
        pass
class SubTest(Test):
    def m2(self):
        print('m2 method implementation')
s=SubTest() ##Valid, abstract method is implemented, cool!!
s.m1()
s.m2()

##Output:
Non-Abstract method
m2 method implementation

##Is a class can contain both abstract and non-abstract methods? Yes, but make sure that child class provides implementation only for abstract method of parent class or else an error will be thrown.

-------------------------------------------------------------------------------

##Interfaces in Python: An abstract class can be called as Interface if and only if the class contains only abstract method.....Officially the Interface concept is not there, indirectly we can achieve it as below......Interface simply acts as Service Requirement Specification(SRS)....


##Abstract class example:
class Test(ABC):
    def m1(self):
        print('Hi')
    @abstractmethod
    def m2(self):
        pass

##Interface
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

#Interface Demo Program:
-getStudentAttendance() #m1
-updateStudentAttendance() #m2
-getMarks() #m3
-updateMarks() #m4
-getFeeInfo() #m5
-updateFeeInfo() #m6

##The interface acts as a ***prototype/specification for any actual implementation***In below example College Automation acts as a prototype for DurgaSoftImpl 

from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
    @abstractmethod
    def m4(self):
        pass
class DurgaSoftImpl(CollegeAutomation):
    def m1(self):
        print('m1 method')
    def m2(self):
        print('m2 method')
    def m3(self):
        print('m3 method')
    def m4(self):
        print('m4 method')
d=DurgaSoftImpl()
d.m1()
d.m2()
d.m3()
d.m4()

##Example:
m1 method
m2 method
m3 method
m4 method

------------------------------------------------------------------------------

##Interface vs Abstract Class vs Concrete Class:
#Example:
Building a 100 Floor Building:
Plan ========>>>>> The initial plan/specification is Interface
||
||
Half Way Through ===>>> The Half implementation/half pending is Abstract class
||
||
Completed construction ===>>> This is concrete class

##Interface : If we don't know anything about implementation and just we have requirement specification then we should go for interface. (SRS - Service Requirement Specification)
##Abstract Class : If we are talking about implementation  but not completely then we should go for abstract class (Partially implemented class)
##Concrete Class : If we are talking about implementation completely and ready to provide service then we should go for concrete class. (Fully implementedf class)

from abc import *
class CollegeAutomation(ABC): ##Interface
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
    @abstractmethod
    def m4(self):
        pass
class DurgaSoftImpl(CollegeAutomation): ##Abstract Class, partial implementation
    def m1(self):
        print('m1 method')
    def m2(self):
        print('m2 method')
class ConcreteClass(DurgaSoftImpl): ##Concrete Class, fully completed
    def m3(self):
        print('m3 method')
    def m4(self):
        print('m4 method')
c=ConcreteClass() ##Note: We can't create object for Abstract & Interface class, we will get Type error....
c.m1()
c.m2()
c.m3()
c.m4()

##Output:
m1 method
m2 method
m3 method
m4 method

----------------------------------------------------------------------------------

##Public, Private and Protected members:

##Public:
-If a member(either method or variable) is public, then we can access that member from anywhere either within the class or from outside of the class.
-By default every member present in Python class is public, Hence we can access from anywhere either within the class or from outside of the class.

##Example:
class Test:
    def __init__(self):
        self.x=10 ##public variable
    def m1(self): ##public method
        print('Public method')
    def m2(self):
        print(self.x)
        self.m1()
t=Test()
t.m2()
print(t.x) ##We're trying to access public variable outside of the class
t.m1() ##We're trying to access public method outside of the class

##Output:
10
Public method
10
Public method

##Private:
x=10 ##Public
__x=10 ##Private
-If a member is private then we can access that member only with in the class and from outside of the class we cannot access.
-We can declare a member as private explicitly by prefixing with two underscore symbols.

class Test:
    def __init__(self):
        self.__x=10 ##private variable
    def __m1(self): ##private method
        print("private method")
    def m2(self): ##public method
        print(self.__x) ##calling private variable within class
        self.__m1() ##calling private method within class
t=Test()
t.m2()
print(t.__x) ##Trying to access private variable from outside of the class, invalid, attribute error
t.m1() ##Trying to access private method from outside of the class, invalid, attribute error

##Output:
10
private method
AttributeError: 'Test' object has no attribute '__x'
AttributeError: 'Test' object has no attribute 'm1'. Did you mean: 'm2'?

##Note:
-If a member is private then we can access that member only with in the class and from outside of the class we cannot access. But we can access indirectly as follows.
-Name Mangling will be happened for the private variables. Hence every private variable name will be changes to new name.
##__variableName===>_ClassName__VariableName
Hence we can access private variable from outside of the class as follows:
print(Objectreference._classname__variablename)
-Internally PVM changes private member e.g __x to _classname__x internally due to which we fail to access private member outside of the class, this process of changing the name is called Name Mangling.


class Test:
    def __init__(self):
        self.__x=10 ##private variable
    def __m1(self): ##private method
        print("private method")
    def m2(self): ##public method
        print(self.__x) ##calling private variable within class
        self.__m1() ##calling private method within class
t=Test()
t.m2()
print(t._Test__x) ##Accessing the private variable outside of the class.
t._Test__m1() ##Accessing the private method outside of the class.

##Note : Above indirect access is not recommended in Python, it is not a good practise. In Python public, private and protected variables are just naming convention and at language level they're not strictly implemented, but it doesn't mean we go against it ;).

##Output:
10
private method
10
private method

-------------------------------------------------------------------------------

##Protected Members: But it is just naming convention and it is not implemented in Python, may be for the future versions purpose.
x=10 ##Public Variable
__x=10 ##Private Variable
_x=10 ##Protected variable
-Protected members we can access within the class from anywhere but from outside of the class we can access only in child classes.
-We can declare members as protected explicitly by prefixing with one underscore symbol.

class Test:
    def __init__(self):
        self._x=10 ##protected variable
    def m1(self):
        print(self._x)
class SubTest(Test):
    def m2(self):
        print(self._x) ##accessing the protected member inside child class
t=SubTest()
t.m1()
t.m2()
print(t._x) ##Ideally yes, it is possible, at language level not implemented, we can still go ahead and access, just a convention.

##Output:
10
10
10

-------------------------------------------------------------------------------

##*******Data Hiding:
-Our internal data should not go out directly. i.e. outside person should not access our internal data directly.
-This OOP feature is nothing but data hiding.
-By declaring data members as private, we can implment data Hiding.
-To have a some sought of Authentication for our Data and not making it available to everyone is called as Data Hiding. 

##Example1:
class Account:
    def __init__(self,initial_balance):
        self.balance=initial_balance
a=Account(10000)
print(a.balance) ##This not correct, anyone can view my balance.

##Output:
10000

##Example2:
class Account:
    def __init__(self,initial_balance):
        self.__balance=initial_balance ##Declaring as a variable.
a=Account(10000)
print(a.__balance) ##attribute error, private variable

##Output:
AttributeError: 'Account' object has no attribute '__balance'

##Example3: To access the data authenticate way.
class Account:
    def __init__(self,initial_balance):
        self.__balance=initial_balance
    def getBalance(self):
        #validation/Authentication
        return self.__balance
a=Account(10000)
print(a.getBalance())

##Output:
10000

-----------------------------------------------------------------------------

##Abstraction:
Highlight set of services which is been offered and hide the internal implementation.
Best Example : ATM
##This is different from Data hiding, in data hiding we're hiding the data, here we're hiding the internal implementation.
#Second Example : Rest APIs / Webservices is the best example for Abstraction.
Advantage of Abstraction:
-Security
-Enhancement becomes very easy (The backend can change/implementation can be upgraded/updated, frontend remains same, no impact).
-Maintainability and Modularity (loan/customer/deposit module etc) is also easy and improved.

-Hiding internal implementation and just highlight the set of services is the concept of abstraction.
Ex:
Through Bank ATM GUI screen, Bank people are highlighting the set of services what they are offering without highlighting internal implementation. This is nothing but abstraction.
-We can implemnent abstraction through GUI screens, APIs we can implement abstraction.

-----------------------------------------------------------------------------

##Encapsulation: Process of binding/grouping/encapsulating data and corresponding behaviour (methods/actions) into a single unit is called encapsulation.
##Also we can define as hiding data behind methods is the central concept of encapsulation.
##Every Python class is an example of encapsulation.
Class Student:
    Dara : name,rollno,marks,age
    Behaviour : Read(),write(),walk(),eat()
##If any component follows data hiding and abstraction such component is called as encapsulated component.    
*****Encapsulation = Data Hiding + Abstraction

##Example:
class Account:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    def getBalance(self):
        #validation/authentication
        return self.__balance
    def deposit(self,amount):
        #validation/Authentication
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        #validation/Authentication
        self.__balance=self.__balance-amount
##In above lines we have successfully incorporated data hiding, coming to abstraction, it is like we're no way displaying backend code is not shown to end user, it is saved in server and for end user it is just a GUI, therefore abstraction is also achieved successfully.
Advantages:
-Security
-Enhancement is easy
-Maintainability/modularity is improved

Limitation:
-Performance slows down due to security and validation (because lenght of code increases).

---------------------------------------------------------------------------------

##Three Pillars of OOPs:
-Inheritance - Code reusability and extendability
-Polymorphism - Flexibility
-Encapsulation - Security