#Functions: A group of statements which are repeatedly required, can be used inside functions and can be called whenever required, i.e code reusability.
#Modules: Group of functions/variables/classes saved in a file is called modules.
##By default every .py file is a module as simple as that
##The most required functions,variables and class frequently used can be imported from modules.py file.

###Simple example of functions:
def calc(a,b):
    print('The sum: ',a+b)
    print('The difference: ',a-b)
    print('The product: ',a*b)
calc(10,20)
calc(100,200)

###Simple example of Module:
developer = 'Durga'
location = 'Hyderabad'
def difference(a,b):
    print('The difference:',a-b)
def add(a,b):
    print('The Sum: ',a+b)
def product(a,b):
    print('The product: ',a*b)
class Test:
    pass
    
*****Note: The above variable/function/class will be saved to module1.py
Now let's use it in a code:

from module1 import * ##The module is imported
print(developer)
print(location)
add(10,20)
difference(10,20)
product(10,20)

##Output:
Durga
Hyderabad
The Sum:  30
The difference: -10
The product:  200

-------------------------------------------------------------------------

##Python Packages: A group of related items is called package
#Group of statements is called functions, group of functions is called module and group of module is called package and package also can contain multiple sub packages.
-A collection of related modules into a single unit is nothing but package.
-Package is an encapsulation mechanism to group related modules into a single unit.
-Package is simply folder or directory
-Package contains a group of related modules and sub packages also.
##If we want to consider any folder as python package, it should contain compulsarily one file i.e. __init__.py, even though there are no modules.
##From Python 3.3 onwards the file __init__.py is not mandatory for Python Package, it's optional.

##Advantages of Package:
-Naming conflicts
    ex: loan.homeloan.account
        loan.vehicleloan.account
-Unique Identification
-Modularity will be increased
-Readability of application is improved
-Maintainability is improved and easily we can update changes

--------------------------------------------------------------------------
##Steps to create a package and access the modules in it.

#Plan
D:\  
    test.py  ##This is our code
    pack1  ##Name of the package
        __init__.py ##Not mandatory since 3.3 and it's empty
        module1.py  ##Module created by us and saved in same location as of __init__.py
            f1
            
##module1.py:
def f1():
    print("This is from f1 functio present in module1 module of pack1 package")
    
##test.py: To learn how to import pack1 and access the function inside module1 under pack1
import pack1.module1
pack1.module1.f1()

#Output:
This is from f1 functio present in module1 module of pack1 package.

#Alternative way and recommended way test.py:
from pack1.module1 import f1
f1()

#Output:
This is from f1 functio present in module1 module of pack1 package.

###***Note: From python3.3 onwards __init__.py is not mandatory, hence we can still go ahead and delete it.

###Let's work with the subpackages:

D:\durgaclasses>
    test.py
    com ##Package
        __init__.py ##Not mandatory since 3.3 and it's empty
        module1.py  ##Module name
            f1() ##function inside
        durgasoft   ##SubPackage
            __init__.py ##Not mandatory since 3.3 and it's empty
            module2.py
                f2()
                
##test.py : How to access f1() and f2()???

##Module1.py
def f1():
    print("This is from f1 of module1 present in com package")
    
##Module2.py
def f2():
    print("This is from f2 of module2 present in com.durgasoft package")
   
#Alternative way and recommended way test.py:
from com.module1 import f1
from com.durgasoft.module2 import f2
f1()
f2()

##Output:
This is from f1 of module1 present in com package
This is from f2 of module2 present in com.durgasoft package



--------------------------------------------------------------------------
##Importance of __init__.py file:
#While using a package if we want to perform any activity automatically then we have to define that activity inside this __init__.py file, like open DB connection, mainly the __init__.py is meant for initialisation activity and code inside __init__ will be auto executed.

D:\durgaclasses>
    test.py
    com ##Package
        __init__.py ##Not mandatory since 3.3 and it's empty
        module1.py  ##Module name
            f1() ##function inside

##Module1.py
def f1():
    print("This is from f1 of module1 present in com package")

#Alternative way and recommended way test.py:
from com.module1 import f1
f1()

##Output:
This is from f1 of module1 present in com package

##In the above example the f1() function executed directly since inside __init__.py is empty there was no initialization.

##Example2:

##Module1.py
def f1():
    print("This is from f1 of module1 present in com package")

#Alternative way and recommended way test.py:
from com.module1 import f1
f1()

##*****__init__.py:
print("I'm from __init__ file and I get executed automatically")

##Output:
I'm from __init__ file and I get executed automatically
This is from f1 of module1 present in com package

---------------------------------------------------------------------------

###Relationships between Function, Module, Package and Library:
Repeated statements req > Functions > Module > Package > Library

Library
    Pack1       Pack2       Pack3............Packn
    Module1,2..n
    f1,2,3.....n

#Functions contains a group of repeatedly required lines of code.
#Module contains a group of repeatedly required functions(of course variables and classes also).
#Package contains a group of related modules (of course sub packges also)
#Library contains a group of related packages. 

------------------------------------------------------------------------

##Need of installing Python Packages ?
D:\durgaclasses>
    test.py
    com ##Package
        __init__.py ##Not mandatory since 3.3 and it's empty
        module1.py  ##Module name
            f1() ##function inside

##Module1.py
def f1():
    print("This is from f1 of module1 present in com package")

#Alternative way and recommended way test.py:
from com.module1 import f1
f1()

##Output:
This is from f1 of module1 present in com package

In the above all examples the test.py and package were available in the same directory/folder/location, hence it was printing results.
Once we move the py file out of directory and execute it, it throws module not available error, to overcome this error we need to install the package on our system so it can be accessed from anywhere in our system, then how to do it???
Stay tuned!!!

----------------------------------------------------------------------------
##How to install a Python Package:
##We need to use setup script called as setup.py, and call stup() function and the function is available in setuptools module.

##setup.py
from setuptools import setup
setup( name='patterns',
       version='0.1'
       packages=['patterns'] ##if there are multiple packages, include them by comma separated.
)

##setup.py Recommended way:
from setuptools import setup,find_package
setup( name='patterns',
       version='0.1'
       packages=find_packages() ##This will find and install all the available packages in the given location.
)

The setup.py file should be placed in the same location where the patterns folder is available.

D:\durgaclasses>
    setup.py
    patterns ##Package
        __init__.py ##Not mandatory since 3.3 and it's empty
        module1.py  ##Module name
            f1() ##function inside

#Post placing just run below command, that's it package will be anywhere we want, pip install will call setup.py file and setup.py is responsible to install the required package:
pip install .
pip uninstall patterns ##This will uninstall pattern package.