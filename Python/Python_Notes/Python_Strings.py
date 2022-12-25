Python_Strings:
==============
-In any application minimum 90% of objects are String objects.
-This is the most commonly used object type.
-##Example if yout take voter registration application, only pincode and D.O.B is int.
-The default return type for x=input() is also string even when we write 100 also, Python people have given more importance to it by default.
-Even the below ##Example of command line argument as well,
Input:
-----
py test.py 10 20

Code:
-----
import sys
argv [1]+argv[2]
10+20 ####Output is 1020 and not 30 :P

##Output:
------
1020 ##It's a string buddy

-String is any sequence of characters within single quotes or within double quotes.
-s='Rajath' or s="Rajath"
****Note: We don not have any char datatype in Python, even single character i.e. s = 'a' is also consider string which is not in other programming languages.
-Multi-line string literals we can use triple quotes 
"""Durga
    Software
    solutions"""
-'This is ' symbol' ==> Invalid
-'This is \' symbol' ==> Valid and \ is called as escape character.
-"This is ' symbol" ==> Valid
-'''This is " symbol''' ==> Valid
-'''The "Python Notes" by 'Durga' is very good''' ==> Valid
-'The \"Python Notes\" by \'Durga\' is very good' ==> Valid(but looks messy).

====================================================================
Steps to access characters of the String:
----------------------------------------

-There are multiple ways:
    -Using Index
    -Using Slice
-Python supports both positive and negative index.

##Example1:
---------
s='Durga'
#+ve Index >> Left to Right (Forward Direction)
#-ve Index >> Right to Left (Backward Direction)
            -5  -4  -3  -2  -1 >>> -ve Index
            d   u   r   g   a
            0   1   2   3   4   >>> +ve Index
s='Durga'
print(s[0])
print(s[-1])
print(s[100]) ##IndexError: string index out of range

##Output:
======
D
a

##Example2:
---------
Write a program to display characters of given string index wise (both +ve and -ve):

s=input('Enter some string: ')
i=0
for x in s:
    print('The character present at +ve index:{} and at -ve index:{}is:{}'.format(i,(i-len(s)),x))
    i+=1
    
##Output:
======
Enter some string: My name is Rajath
The character present at +ve index:0 and at -ve index:-17is:M
The character present at +ve index:1 and at -ve index:-16is:y
The character present at +ve index:2 and at -ve index:-15is: 
The character present at +ve index:3 and at -ve index:-14is:n
The character present at +ve index:4 and at -ve index:-13is:a
The character present at +ve index:5 and at -ve index:-12is:m
The character present at +ve index:6 and at -ve index:-11is:e
The character present at +ve index:7 and at -ve index:-10is: 
The character present at +ve index:8 and at -ve index:-9is:i
The character present at +ve index:9 and at -ve index:-8is:s
The character present at +ve index:10 and at -ve index:-7is: 
The character present at +ve index:11 and at -ve index:-6is:R
The character present at +ve index:12 and at -ve index:-5is:a
The character present at +ve index:13 and at -ve index:-4is:j
The character present at +ve index:14 and at -ve index:-3is:a
The character present at +ve index:15 and at -ve index:-2is:t
The character present at +ve index:16 and at -ve index:-1is:h

==========================================================================
Slice Operator:
--------------

-Syntax [begin:end]
-Above index returns substring from begin index to end-1 index
-If begin is optional, in this case default value is 0
-If end is optional, in this case default value is len(s)

##Example1:
========
s='abcdefghijk'
print(s[3:8])
print(s[2:7])
print(s[2:])
print(s[:7])
print(s[:])

##Output:
======
defgh
cdefg
cdefghijk
abcdefg
abcdefghijk

##Along with step indicator:
-Syntax >> s[begin:end:step]
-Default value for step is 1
-s[2:7] or s[2:7:1] means the same >> 2,3,4,5,6
-s[2:7:2] >> 2,4,6

##Example2:
========
s='abcdefghijk'
print(s[3:8:1])
print(s[2:7:1])
print(s[2:7:2])
print(s[2:7:3])
print(s[::1])
print(s[::3])

##Output:
defgh
cdefg
ceg
cf
abcdefghijk
adgj

*******Rules of Slice Operator:
-s[begin:end:step]
-All three begin,end and step can be either positive/negative
-If step is +ve >> We have to consider substring from left to right[Forward direction] i.e. begin to end-1
-If step is -ve >> We have to consider substring from right to left [Backward direction] i.e. begin to end+1
-Step cannot be 0, PVM will throw error*********
-If end value is 0 in the forward direction, then result is always empty
-If end value is -1 in the backward direction, then result is always empty
Default Values:
----------------
-Either forward direction / backward direction, we can take both +ve and -ve values for begin and end index.
-Forward Direction >> begin is 0 and end is len(s)
-Backward Direction >> begin is -1 and end is -(len(s)+1)

##Example3:
s='abcdefghijk'
#-11    -10     -9      -8      -7      -6      -5      -4      -3      -2      -1
#a      b       c       d       e       f       g       h       i       j       k
#0      1       2       3       4       5       6       7       8       9       10
print("The statement 1 :",s[1:6:2])
print("The statement 2 :",s[::1]) ##Forward direction
print("The statement 3 :",s[::-1]) ##Backward direction/gives reverse string*****
print("The statement 4 :",s[3:7:-1])##backward direction, begin to end+1 i.e. 3 to 8 it's empty string as it is illogical to move from 3 to 8 in backward direction
print("The statement 5 :",s[7:4:-1]) ##backward direction, 7 to 5.
print("The statement 6 :",s[0:10000:1]) ##All values, forward direction
print("The statement 7 :",s[-4:1:-1]) ##Backward direction, -4 to 2 and it's possible
print("The statement 8 :",s[-4:1:-2]) ##Backward direction, -4 to 2 and it's possible
print("The statement 9 :",s[5:0:1]) ##Forward direction, end is 0, as per rule it's illogical, empty set.
print("The statement 10 :",s[9:0:0]) ##Value Error
print("The statement 11 :",s[0:-10:-1]) ##Backward direction, 0 to -9, illogical, empty set
print("The statement 12 :",s[0:-12:-1]) ##Backward direction, 0 to -11, it's possible
print("The statement 13 :",s[0:0:1]) ##Forward direction, end is 0, as per rule it's illogical, empty set.
print("The statement 14 :",s[0:-9:-2]) ##Backward direction, 0 to -9, illogical, empty set
print("The statement 15 :",s[-5:-9:-2]) ##Backward direction, -5 to -8, it's possible
print("The statement 16 :",s[10:-1:-1]) ##Backward direction, end is -1, as per rule it's illogical, empty set.
print("The statement 17 :",s[10000:2:-1]) ##Backward direction, 10000 to 3, it's possible

##Output:
------
The statement 1 : bdf
The statement 2 : abcdefghijk
The statement 3 : kjihgfedcba
The statement 4 : 
The statement 5 : hgf
The statement 6 : abcdefghijk
The statement 7 : hgfedc
The statement 8 : hfd
The statement 9 : 
The statement 10 : ValueError: slice step cannot be zero
The statement 11 : 
The statement 12 : a
The statement 13 : 
The statement 14 : 
The statement 15 : ge
The statement 16 : 
The statement 17 : kjihgfed

===========================================================================
Mathematical operators for String:
----------------------------------
'+' >> Concatenation
'*' >> Repeatition

'Durga'+'soft' >> 'Durgasoft'
-If '+' to be applied for string, compulsory both arguments should be string.
******************-'Durga'+10 >> Will throw type error.

-'Durga'*3 >> DurgaDurgaDurga -----Valid
-3*'Durga' >> DurgaDurgaDurga -----Valid
-For '*' operator, atleast one argument should be 'int' and other string.
******************-'Durga'*3.5 >> Will throw, type Error, it's non-int datatype

Summary:
========
string+string --- Valid
string*string --- Invalid
string+int --- Invalid
string*int --- Valid

Membership Operators:
---------------------
-The in and not in operators are called as membership operators.
-'d' in 'durga' >> True
-'z' not in 'durga' >> True

##Example1:
s=input('Enter main string: ')
subs=input('Enter sub string: ')
if subs in s:
    print('Substring present in main string')
else:
    print('Substring not present in main string')
    
##Output:
Enter main string: Rajath wants to switch company
Enter sub string: company
Substring present in main string

Comparison operators:
---------------------
-The <, <=, >, >=, ==, !=
-When we try to compare two strings using '<' the ouput is calcilated based on the unicode values i.e. a=97,b=98,c=99.... and A=65,B=66,C=67...., to knoe the unique value use ord('d')

##Example1:
print('durga' < 'ravi') ##Comparison is done based on the unicode of first character, if 1st characters same, it will move to 2nd and so on...
print(ord('d'))
print('ramba'<'ramya')
print(ord('y'))

##Output:
True
100
True
121

##Example2:
s1=input('Enter First String Value: ')
s2=input('Enter Second String Value: ')
if s1==s2:
    print('Both Strings are equal')
elif s1<s2:
    print('First String is less than Second String')
else:
    print('First String is greater than Second String')
    
##Output:
Enter First String Value: Go Goa Gone
Enter Second String Value: Go Goa Gone
Both Strings are equal

##Output:
Enter First String Value: My name is Billa
Enter Second String Value: My name is Bheem
First String is greater than Second String

===============================================================================

Removing spaces from the String:
--------------------------------

##Example1:
city=input('Enter your City name: ')
if city=='Hyderabad':
    print('Hello Hyderabadi....Aadab!!!')
elif city=='Chennai':
    print('Hello Madrasi....Vanakkam!!!')
elif city=='Bangalore':
    print('Hello Kannadiga...Namaskara!!!')
else:
    print('Your entered city is invalid')

##Output:
Enter your City name: Bangalore
Hello Kannadiga...Namaskara!!!

##Output:
Enter your City name:  Bangalore 
Your entered city is invalid ##This is caused due to space before Bangalore

##Example1(Updated Code to take care unwanted spaces):
-There are three methods to remove the spaces,
    lstrip() --- #Left Strip, removes space at beginning i.e. ' 'Bangalore
    rstrip() --- #Right Strip, removes space at end i.e. Bangalore' '
    strip() --- #Both Left and Right, removes spaces at both beginning and end as well.

city=input('Enter your City name: ').strip()
if city=='Hyderabad':
    print('Hello Hyderabadi....Aadab!!!')
elif city=='Chennai':
    print('Hello Madrasi....Vanakkam!!!')
elif city=='Bangalore':
    print('Hello Kannadiga...Namaskara!!!')
else:
    print('Your entered city is invalid')
    
##Output:
Enter your City name:     Bangalore
Hello Kannadiga...Namaskara!!!

******Note: Strip() is never helpful in removing the spaces between sentence ex: 'Durga Software'

===========================================================================

String Methods: find() and rfind() to find substrings:
------------------------------------------------------
-To find the substring and it's index, we have 4 methods in total
s='ABCBA'
t='ABCDEFGHIJK'
    1. find():
    -Searches from left to right and returns index of first occurrance of substring from beginning.
    -find(substring,begin,(end-1)) We can also search for given boundary as well
    ex: 
    print(s.find('B')) >> 1
    print(s.find('X')) >> -1 ##When the substring is not available it gives an ##Output -1
    print(t.find('F',3,8)) >> 5
    print(t.find('F',3,10000)) >> 5 ##Illogical, but works :P
    print(t.find('A',3,8)) >> -1 ##When the substring is not available it gives an ##Output -1
    2. rfind():
    -Searches from right to left and returns index of first occurrance of substring from end and returns +ve indexes only.
    -rfind(substring,begin,(end-1)) We can also search for given boundary as well
    ex:
    print(s.rfind('B')) >> 3
    print(s.rfind('P')) >> -1 ##When the substring is not available it gives an ##Output -1
    print(t.rfind('E',3,8)) >> 4
    print(t.rfind('A',3,8)) >> -1 ##When the substring is not available it gives an ##Output -1
    3. index():
    -Same as find method, provides the index and only difference is, it throws value error if the given substring is not present unlike the find() which prints -1.
    ex:
    print(s.index('B')) >> 1
    print(s.index('T')) >> ValueError: substring not found
    print(t.index('F',3,8)) >> 5
    print(t.index('F',3,10000)) >> 5 ##Illogical, but works :P
    print(t.index('A',3,8)) >> ValueError: substring not found
    4. rindex():
    -Same as rfind method, provides the index and only difference is, it throws value error if the given substring is not present unlike the rfind() which prints -1.
    ex:
    print(s.rindex('B')) >> 3
    print(s.rindex('T')) >> ValueError: substring not found
    print(t.rindex('F',3,8)) >> 5
    print(t.rindex('A',3,8)) >> ValueError: substring not found
    
##Example1(Usage of index):
mail=input('Enter your mail id: ')
try:
    i=mail.index('@')
    print('Mail Id contains @ symbol, which is mandatory')
except ValueError:
    print('Mail Id does not contain @ symbol')
    
##Output:
Enter your mail id: rajath
Mail Id does not contain @ symbol

****Note: All the above four methods will always return the index of first occurance of substring, if you want to find the all the occurances in the string, then code needs to be written explicitly.

==============================================================================

Counting Substrings in the given String:
----------------------------------------
s.count(substring) >> Returns the number of occurrences of the given substring in the total string
s.count(substring,begin,end-1) >> Returns the number of occurrences of the given string from begin index to end-1 index

##Example1:
s='ABCBA'
t='ABCDEFBAABOPE'
print(s.count('B'))
print(t.count('B'))
print(t.count('b'))
print(s.count('Z'))
print(t.count('AA'))
print(t.count('B',4,100))
print(s.count('B',5,100))

##Output:
2
3
0
0
1
2
0

##Example2:
s='BBBBB'
print(s.count('B'))
print(s.count('BB'))
print(s.count('BBB'))

##Output:
5
2
1

=============================================================================

Application to print index of all occurences of the given Substring:
--------------------------------------------------------------------

#A B C A B C A B C A
#0 1 2 3 4 5 6 7 8 9

##Example1:
s='ABCABCABCA'
index_value=s.find('ABC')
print('The substring index_value: ',index_value)

##Output:
The substring index_value:  0

##Example2:
s='ABCABCABCA'
index_value=s.find('ABC')
print('The substring index_value: ',index_value)
index_value=s.find('ABC',3,10 or len(s)) ## 3 to 9 (begin to (end-1))
print('The substring index_value: ',index_value)
index_value=s.find('ABC',6,10) ## 6 to 9 (begin to (end-1))
print('The substring index_value: ',index_value)
index_value=s.find('ABC',9,10) ## 9 to 9 (begin to (end-1))
print('The substring index_value: ',index_value)

##Output:
The substring index_value:  0
The substring index_value:  3
The substring index_value:  6
The substring index_value:  -1

##Example3:
s='ABCABCABCA'
subs=input('Enter substring to search :')
index_value=s.find('ABC')
if index_value == -1:
    print('Substring not available in the string')
while index_value != -1:
    print('The {} is available at index_value : {}'.format(subs,index_value))
    ##Below is used search the remaining string values
    index_value=s.find(subs,index_value+len(subs),len(s))
    ##After finding at index value 6 it will go for 9,10 (i.e. 9 to 9), the ##Output will be -1, this will cause the while loop will stop as the condition is while != -1 Yay!!
print('The no. of occurences :',s.count(subs))

##Output:
Enter substring to search :ABC
The ABC is available at index_value : 0
The ABC is available at index_value : 3
The ABC is available at index_value : 6
The no. of occurences : 3

##Example4 (Writing our own count code):
s='ABCABCABCA'
subs=input('Enter substring to search : ')
index_value=s.find('ABC')
if index_value == -1:
    print('Substring not available in the string')
count=0
while index_value != -1:
    count+=1
    print('The {} is available at index_value : {}'.format(subs,index_value))
    ##Below is used search the remaining string values
    index_value=s.find(subs,index_value+len(subs),len(s))
    ##After finding at index value 6 it will go for 9,10 (i.e. 9 to 9), the ##Output will be -1, this will cause the while loop will stop as the condition is while != -1 Yay!!
print('The no. of occurences :',count)

##Output:
Enter substring to search :ABC
The ABC is available at index_value : 0
The ABC is available at index_value : 3
The ABC is available at index_value : 6
The no. of occurences : 3

===============================================================================

Replacing a string with another string:
---------------------------------------

Syntax > s.replace(oldString,newString)

##Example1:
s='ABABABAB'
s1=s.replace('A','B')
print(s1)

##Output:
BBBBBBBB

##Example2:
s='Durga Software Solutions'
s1=s.replace(' ','')
print(s1)
print('The no of spaces: ',s.count(' '))
##To count spaces without using replace method
print('The no of spaces: ',len(s)-len(s1))

##Output:
DurgaSoftwareSolutions
The no of spaces:  2
The no of spaces:  2

##******String objects are immutable then how we can change content by using replace() method?
Here the existing object s still remains the same, for the changes done a new object s1 is created.
Ex:
print(s) >> Learning Python Is Very Difficult
print(s1) >> Learning Python Is Very Easy

-Replace method always considers case.

##Example3:
s='Learning Python Is Very Difficult'
s1=s.replace('Difficult','Easy')
print('Case is considered :',s1)
s2=s.replace('difficult','Easy')
print('Case is ignored :',s2)

##Output:
Learning Python Is Very Easy
Learning Python Is Very Difficult

##Example4:
s='ABABABABA'
print('Before replacement :',id(s))
print(s)
s=s.replace('A','B')
print('After replacement :',id(s)) ##The id gets changed, the string is still immutable, the before replacement wala s will be killed by garbage collector, as simple as that.
print(s)

##Output:
Before replacement : 1768386510064
ABABABABA
After replacement : 1768386557424
BBBBBBBBB

======================================================================

Splitting of Strings:
---------------------

##Example1:
s='Durga Software Solutions'
l=s.split() ##****The default method for split is space
##***********The return type of split() is always list
print(type(l))
print(l)
for x in l:
    print(x)
    
##Output:
<class 'list'>
['Durga', 'Software', 'Solutions']
Durga
Software
Solutions

##Example2:
d='05-04-2019'
l=d.split('-')
print(l)
for x in l:
    print(x)
l1=d.split()
print(l1)

##Output:
['05', '04', '2019']
05
04
2019
['05-04-2019']

Joining of Strings:
-------------------
Syntax >> separator.join(l)

##Example1:
l=['Durga','Software','Solutions']
Date=['05', '04', '2019']
String1=' '.join(l)
print(type(String1))
print(String1)
String2='-'.join(l)
print(type(String2))
print(String2)
String3=''.join(l)
print(type(String3))
print(String3)
String4='-'.join(Date)
print(type(String4))
print(String4)

##Output:
<class 'str'>
Durga Software Solutions
<class 'str'>
Durga-Software-Solutions
<class 'str'>
DurgaSoftwareSolutions
<class 'str'>
05-04-2019

============================================================================

Changing case of characters of the String:
------------------------------------------
-upper() >> To convert lower to upper
-lower() >> To convert upper to lower
-swapcase() >> To convert upper to lower / lower to upper
-title() >> To convert in every word first letter to upper case
ex: Durga Software Solutions
-capitalize() >> The first letter is uppercase and remaining all words is lowercase only
ex: Durga software solutions.

##Example1:
s='Learning Python is very easy'
print('The upper case: ',s.upper())
print('The lower case: ',s.lower())
print('The swap case: ',s.swapcase())
print('The title case: ',s.title())
print('The capitalize case: ',s.capitalize())

##Output:
The upper case:  LEARNING PYTHON IS VERY EASY
The lower case:  learning python is very easy
The swap case:  lEARNING pYTHON IS VERY EASY
The title case:  Learning Python Is Very Easy
The capitalize case:  Learning python is very easy

##Example2: Write a program to check whether the given 2 strings are equal or not by ignoring case.
s1=input('Enter First String : ')
s2=input('Enter Second String : ')
if s1==s2:
    print('Both String are equal')
else:
    print('Strings are not equal')
    
##Output:
Enter First String : durga
Enter Second String : durga
Both String are equal

##Output:
Enter First String : Durga
Enter Second String : durga
Strings are not equal

##Updated Code:
s1=input('Enter First String : ')
s2=input('Enter Second String : ')
if s1.lower()==s2.lower(): ##Converting to lower case
    print('Both String are equal')
else:
    print('Strings are not equal')

###or

s1=input('Enter First String : ').lower() ##Converting to lower case at the input end itself
s2=input('Enter Second String : ').lower() ##Converting to lower case at the input end itself
if s1.lower()==s2.lower():
    print('Both String are equal')
else:
    print('Strings are not equal')

##Output:
Enter First String : DUrGa
Enter Second String : dURGA
Both String are equal

##Example3:
#Write a program to check whether provided username and password are valid or not? username is not case sensitive, but password should be case sensitive.

username=input('Enter Username: ')
password=input('Enter Password: ')
if username.lower()=='durga' and password=='anushka':
    print('Please provide login, credentials are valid')
else:
    print('Invalid credentials')
    
##Output:
Enter Username: Durga
Enter Password: anushka
Please provide login, credentials are valid

##Example4:
#Write a program to convert first and last characters as uppercase and all remaining characters should be lower case of the given string.

Str=input('Please enter a string value: ')
print(Str[0].upper()+Str[1:len(Str)-1].lower()+Str[-1].upper())

##Output:
Please enter a string value: I'm a Dood BOY
I'm a dood boY

=============================================================================

Checking starting and ending part of the String:
-----------------------------------------------
-Below two methods we can use to check whether the given string starts and ends with our requirement.
    s.startswith(substring) >> Returns True if the string starts with provided substring
    s.endswith(substring) >> Returns True if the string ends with provided substring
    
##Example1:
s='Learning Python is very easy'
print(s.startswith('Learning'))
print(s.startswith('lea'))
print(s.endswith('asy'))
print(s.endswith('asY'))

##Output:
True
False
True
False

=========================================================================

To check Type of characters present in a string:
------------------------------------------------

s.isalnum() >> [a to z, A to Z, 0 to 9]
s.isalpha() >> [a to z, A to Z]
s.islower() >> If all the alphabets symbol is lower or not
s.isupper() >> If all the alphabets symbol is upper or not
s.isdigit() >> [0 to 9]
s.istitle() >> Returns True if string is titlecase
s.isspace() >> Returns True if string contains only spaces

##Example1:
print('Durga786'.isalnum()) ##True
print('Durga786'.isalpha()) ##False
print('durga'.isalpha()) ##True
print('durga'.isdigit()) ##False
print('786786'.isdigit()) ##True
print('abc'.islower()) ##True
print('Abc'.islower()) ##False
print('abc123'.islower()) ##True
print('ABC'.isupper()) ##True
print('Durga Software Solutions'.istitle()) ##True
print('Durga software solutions'.istitle()) ##False
print(' '.isspace()) ##True

##Output:
True
False
True
False
True
True
False
True
True
True
False
True

##Example2: Write a program to check the type of character entered from the keyboard.
s=input('Enter any character : ')
if s.isalnum():
    print('It is alphanumeric character')
    if s.isalpha():
        print('It is alphabet symbol')
        if s.lower():
            print('It is lowercase symbol')
        else:
            print('It is uppercase symbol')
    else:
        print('It is digit symbol')
elif s.isspace():
    print('It is space character')
else:
    print('It is non-space special character')
    
##Output:
Enter any character : ABC
It is alphanumeric character
It is alphabet symbol
It is lowercase symbol

##Output:
Enter any character : abc432
It is alphanumeric character
It is digit symbol