Python_Strings:
==============
-In any application minimum 90% of objects are String objects.
-This is the most commonly used object type.
-Example if yout take voter registration application, only pincode and D.O.B is int.
-The default return type for x=input() is also string even when we write 100 also, Python people have given more importance to it by default.
-Even the below example of command line argument as well,
Input:
-----
py test.py 10 20

Code:
-----
import sys
argv [1]+argv[2]
10+20

Output:
------
1020 ##It's a string buddy

-String is any sequence of characters within single quotes or withing double quotes.
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
-'''The "Python Notes" by 'Durga' is very goog''' ==> Valid
-'The \"Python Notes\" by \'Durga\' is very goog' ==> Valid(but looks messy).

====================================================================
Steps to access characters of the String:
----------------------------------------

-There are multiple ways:
    -Using Index
    -Using Slice
-Python supports both positive and negative index.

Example1:
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

Output:
======
D
a

Example2:
---------
Write a program to display characters of given string index wise (both +ve and -ve):

s=input('Enter some string: ')
i=0
for x in s:
    print('The character present at +ve index:{} and at -ve index:{}is:{}'.format(i,(i-len(s)),x))
    i+=1
    
Output:
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
-Aove index returns substring from begin index to end-1 index
-If begin is optional, in this case default value is 0
-If end is optional, in this case default value is len(s)

Example1:
========
s='abcdefghijk'
print(s[3:8])
print(s[2:7])
print(s[2:])
print(s[:7])
print(s[:])

Output:
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

Example2:
========
s='abcdefghijk'
print(s[3:8:1])
print(s[2:7:1])
print(s[2:7:2])
print(s[2:7:3])
print(s[::1])
print(s[::3])

Output:
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
-If step is -ve >> We have to consider substring from right to left [Backward directiob] i.e. begin to end+1
-Step cannot be 0, PVM will throw error*********
-If end value is 0 in the forward direction, then result is always empty
-If end value is -1 in the backward direction, then result is always empty
Deafault Values:
----------------
-Either forward direction / backward direction, we can take both +ve and -ve values for begin and end index.
-Forward Direction >> begin is 0 and end is len(s)
-Backward Direction >> begin is -1 and end is -(len(s)+1)

Example3:
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
print("The statement 9 :",s[5:0:1]) ##Forward direction, illogical, empty set
print("The statement 10 :",s[9:0:0]) ##Value Error
print("The statement 11 :",s[0:-10:-1]) ##Backward direction, 0 to -9, illogical, empty set
print("The statement 12 :",s[0:-12:-1]) ##Backward direction, 0 to -11, it's possible
print("The statement 13 :",s[0:0:1]) ##Forward direction, 0 to -1, illogical, empty set
print("The statement 14 :",s[0:-9:-2]) ##Backward direction, 0 to -9, illogical, empty set
print("The statement 15 :",s[-5:-9:-2]) ##Backward direction, -5 to -8, it's possible
print("The statement 16 :",s[10:-1:-1]) ##Backward direction, -5 to -8, illogical, empty set.
print("The statement 17 :",s[10000:2:-1]) ##Backward direction, 10000 to 3, it's possible

Output:
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
