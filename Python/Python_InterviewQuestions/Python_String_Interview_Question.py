##Write a program to reverse total content in the given string?
#Using Slice Operator
#Using reverse() operator
#By manipulating character by character

##Example1: Using Slice Operator
s='durga'
print(s[::-1])

#Output:
agrud

##Example2: Using reversed() function
s='durga'
print(reversed(s))
r=reversed(s)
for ch in r:
    print(ch)
##Let's print all characters in single line
output=''.join(r)
print(output)

##Output:
<reversed object at 0x0000019C3AF224A0>
a
g
r
u
d
agrud

##Example3: Using while loop
s=input("Provide your string: ")
output = ''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1 ##i-=1 also works
print(output)

##Output:
Provide your string: Durga
agruD

===================================================================================

##Write a program to reverse order of words in a string?
Input : Learning Python is ver easy
Output : easy very is Python Learning

##Example1:
s=input("Provide your string: ") ##Learning Python is very easy
##Let's split string into list of tokens
l=s.split() ##By default split will consider space for splitting
print(l)
l1=l[::-1]
print(l1)
l2=' '.join(l1)
print(l2)

##Output:
Provide your string: Learning Python is very easy
['Learning', 'Python', 'is', 'very', 'easy']
['easy', 'very', 'is', 'Python', 'Learning']
easy very is Python Learning

===================================================================================

##Write a program to reverse internal content of each word?
Input : Learning Python is ver easy
Output : gninraeL nohtyP si yrev ysae

##Example1:
s=input("Provide your string: ") ##Learning Python is very easy
##Let's split string into list of tokens
l=s.split() ##By default split will consider space for splitting
print(l)
l1=[]
l2=[] ##Creating empty list
for x in l:
    l1.append(x) ##Gives output same as s
    l2.append(x[::-1]) ##Here actual reversal happens
print(l1)
print(l2)
output=' '.join(l2)
print(output)

##Output:
Provide your string: Learning Python is very easy
['Learning', 'Python', 'is', 'very', 'easy']
['gninraeL', 'nohtyP', 'si', 'yrev', 'ysae']
gninraeL nohtyP si yrev ysae

===================================================================================

##Write a program to reverse internal content of every second word present in the given string?
Input : one two three four five six
Output : one owt three ruof five xis

##Example1:
s=input("Provide your string: ") ##one two three four five six
l=s.split()
print(l)
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i]) ##l[i] means just append the word without any changes
    else:
        l1.append(l[i][::-1]) ##l[i][::-1] means append the word with reversal
    i+=1
print(l1)
output=' '.join(l1)
print(output)

##Output:
Provide your string: one two three four five six
['one', 'two', 'three', 'four', 'five', 'six']
['one', 'owt', 'three', 'ruof', 'five', 'xis']
one owt three ruof five xis

===================================================================================

##Write a program to print words present at even & odd index separately for given string?
Input : one two three four five six
Output1 : one three five
Output2 : two four six

##Example1:
s = input("Provide your string: ")
l=s.split()
print(l)
i=0
odd_str=[]
even_str=[]
while i<len(l):
    if i%2==0:
        even_str.append(l[i])
    else:
        odd_str.append(l[i])
    i+=1
print(odd_str)
print(even_str)

##Output:
Provide your string: one two three four five six
['one', 'two', 'three', 'four', 'five', 'six']
['two', 'four', 'six']
['one', 'three', 'five']

===================================================================================

##Write a program to print each letter present at even & odd index separately for given string?
s = input("Provide your string: ") ##DurgaSoft
i=0
print("Characters present at even index")
while i<len(s):
    print(s[i])
    i=i+2
i=1
print("Characters present at odd index")
while i<len(s):
    print(s[i])
    i=i+2
###Let's go with the slice operator to make life easier
print("Characters present at even index :",s[::2])
print("Characters present at odd index :",s[1::2])

##Output:
Provide your string: DurgaSoft
Characters present at even index
D
r
a
o
t
Characters present at odd index
u
g
S
f
Characters present at even index : Draot
Characters present at odd index : ugSf

===================================================================================

##Write a program to merge characters of 2 strings into a single string by taking characters alternatively?

input: s1='RAVI' s2='TEJA'
Output: RTAEJIA

##If strings are having same lenght:
s1='RAVI'
s2='TEJA'
output=''
i,j=0,0
while i<len(s1) or i<len(s2): ##Even if we use 'and' also gives same output
    output=output+s1[i]+s2[j]
    i+=1
    j+=1
print(output)

##Output:
RTAEVJIA

##If strings are not having same lenght:
s1='RAVIKIRAN'
s2='TEJA'
output=''
i,j=0,0
output=''
while i<len(s1) or i<len(s2):
    if i<len(s1):   ##This help in preventing index error
        output=output+s1[i]
        i=i+1
    if j<len(s2):   ##This help in preventing index error
        output=output+s2[j]
        j=j+1
print(output)       

##Output:
RTAEVJIAKIRAN

===================================================================================

##Write a program to Sort characters of the string, first alphabet symbols followed by digits:
input : B4A1D3
output: ABD134

##Example1:
s='B4A1D3'
a=sorted(s) ##It always sorts numbers first and later alphabets and default output is list
b=str(a)
print(a)
print(b)
print(type(a))
print(type(b))

##Output:
['1', '3', '4', 'A', 'B', 'D']
['1', '3', '4', 'A', 'B', 'D']
<class 'list'>
<class 'str'>

##Example2:
s='B4A1D3'
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
print(alphabets)
print(digits)
print(sorted(alphabets)+sorted(digits))
output=''.join(sorted(alphabets)+sorted(digits))
print(output)

##Output:
['B', 'A', 'D']
['4', '1', '3']
['A', 'B', 'D', '1', '3', '4']
ABD134

##Example3:
s='B4A1D3'
alphabets=''
digits=''
for ch in s:
    if ch.isalpha():
        alphabets+=ch
    else:
        digits+=ch
output=''
for ch in sorted(alphabets):
    output=output+ch
for ch in sorted(digits):
    output=output+ch
print(output)

##Output:
ABD134

===================================================================================

##Write a program for the requirement, input a4b3c2 and expected output aaaabbbcc:
s='a4b3c2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        print(x)
    else:
        d=int(ch)
        print(d)
        output=output+x*d
        print(output)
print(output)

##Output:
a
4
aaaa
b
3
aaaabbb
c
2
aaaabbbcc
aaaabbbcc

==================================================================================

##Write a program for the following requirement
input : a3z2b4a3z2b4
output: aaaaaabbbbbbbbzzzz
s='a3z2b4a3z2b4'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        print(x)
    else:
        d=int(ch)
        print(d)
        output=output+x*d
        print(output)
print(output)
print(sorted(output)) ##This gives output in the form of list
a=''.join(sorted(output))
print(a)

##Output:
a
3
aaa
z
2
aaazz
b
4
aaazzbbbb
a
3
aaazzbbbbaaa
z
2
aaazzbbbbaaazz
b
4
aaazzbbbbaaazzbbbb
aaazzbbbbaaazzbbbb
['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'z', 'z', 'z', 'z']
aaaaaabbbbbbbbzzzz

==================================================================================

##Write a program for the following requirement
input : aaaaaabbbbbbbbzzzz
output: 7a8b4z

##Example1:
s='aaaaaabbbbbbbbzzzz'
output=''
previous=s[0] ##This will consider 0th index character i.e. a
c=1
i=1
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    i=i+1
print(output)

##Output:
6a8b

******Note: We're unable to consider the last character, therefore we need to add last character z:

##Example1: Updated Version
s='aaaaaabbbbbbbbzzzz'
output=''
previous=s[0] 
c=1
i=1
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1: ##This will print or consider z as it is a last character
        output=output+str(c)+previous
    i=i+1
print(output)

##Output:
6a8b4z

==================================================================================

##Write a program for the requirement, input a4k3b2 and expected output aeknbd:
input : a4k3b2
output : aeknbd ##a+(4th character after a i.e. e)+k+(3rd character after k .i.e n)+so on.....
##To find the unicode of any character, use ord('a') >> 97
##To find the character of any unicode, use chr(98) >> basestring

s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        output=output+newc
print(output)

##Output:
aeknbd

==================================================================================

##Write a program to remove duplicate characters from the given input string:

 ##Approach1:
s='AAAAAAABBBBBBBSSSSSSSSS'
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

##Output:
ABS

##Approach2:
z='AAAAAAABBBBBBBXXXXXX'
l=[]
for ch in z:
    if ch not in l:
        l.append(ch)
output=''.join(l)
print(output)

##Output:
ABX

##Approach3
s='DDDDEEEEEEEFFFFF'
s1=set(s) ##No guarnatee of order as it is a Set
print(output) 
output=''.join(s1)

##Output:
EDF

==================================================================================

##Find no of occurrences of each character present in given string with count()

##Approach1:
z='AAAAAAABBBBBBBXXXXXX'
l=[]
for ch in z:
    if ch not in l:
        l.append(ch) ##We've appended all the unique characters
for ch in sorted(l):
    print('{} occurs {} times'.format(ch,z.count(ch)))
    
##Output:
A occurs 7 times
B occurs 7 times
X occurs 6 times

##Approach2:
##Approach3
s='DDDDEEEEEEEFFFFF'
s1=set(s) ##No guarnatee of order as it is a Set
for ch in sorted(s1):
    print('{} occurs {} times'.format(ch,s.count(ch)))
    
##Output:
D occurs 4 times
E occurs 7 times
F occurs 5 times

==================================================================================

##Find no of occurrences of each character present in given string without using count()

##This can be achieved by using a dict data type:
d={} ##Empty dictionary
d[k]=v ##Syntax for adding key-value pair to dictionary
d={}
d['A']=100
d['B']=200
print(d) ##{'A':100,'B':200}
d['A']=300
print(d) ##{'A':300,'B':200}
##Duplicate values are allowed, but not duplicate keys
d.get('A') #300
d.get('Z') #None
d.get(k,defaultvalue) ##If value is there then it will print or else it will print the default value passed to it
d.get('A',0) #300
d.get('Z',0) #0

##Example1:
d={}
d['A']=1
d['B']=2
d['A']=d.get('A',0)+1 ##****************
print(d) ##{'A':2,'B':2}

##Example2:
d={'A':100,'Z':200,'C':300}
for k,v in d.items():
    print(k,v)
    
##Output:
A 100
Z 200
C 300

##Example2:
d={'A':100,'Z':200,'C':300}
for k,v in sorted(d.items()):
    print(k,v)
    
##Output:
A 100
C 300
Z 200

##To find occurrences of each character without using count:
s='DDDCCAACCCCCZZZZDDDBBB'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1 ##***********
print(d)
for ch in sorted(d.items()):
    print(ch)
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))
    
##Output:
{'D': 6, 'C': 7, 'A': 2, 'Z': 4, 'B': 3}
('A', 2)
('B', 3)
('C', 7)
('D', 6)
('Z', 4)
A occurs 2 times
B occurs 3 times
C occurs 7 times
D occurs 6 times
Z occurs 4 times

==================================================================================

##Write the program for the following requirement:
input : ABAABBCA
output : 4A3B1C

##Example1:
s='ABAABBCA'
output=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output=output+str(v)+k
print(output)

##Output:
4A3B1C

==================================================================================

##Write the program for the following requirement:
input : ABAABBCA
output : A4B3C1

##Example1:
s='ABAABBCA'
output=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output=output+k+str(v)
print(output)

##Output:
A4B3C1

==================================================================================

##Program to find the number of occurrences of each vowel present in given string:

##Example1:
s=input('Provide your string: ')
v={'a','e','i','o','u','A','E','I','O','U'} ##Square brackets can also be used
d={}
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))

##Output:
Provide your string: missiSSippIAAEUUUUUOOOO
A occurs 2 times
E occurs 1 times
I occurs 1 times
O occurs 4 times
U occurs 5 times
i occurs 3 times

==================================================================================

##Program to check whether the given two strings are anagrams or not?
 
##Two strings are said to be anagrams if both are having same content irrespective of characters position:
##Ex: lazy and zaly

s1=input("Enter first string: ")
s2=input("Enter second string: ")
if(sorted(s1)==sorted(s2)):
   print("The strings are anagrams")
else:
   print("The strings aren't anagrams")

##Output:
Enter first string: lazy
Enter second string: zaly
The strings are anagrams

Enter first string: LazY
Enter second string: lAzY
The strings aren't anagrams

Enter first string: hindu
Enter second string: god
The strings aren't anagrams

==================================================================================

##Write a program to check whether the given string is palindrome or not?

##A string is said to be palindrome if original string and its reversed string are equal:
##Ex: level, madam

s=input("Enter Some Palindrome String: ")
if s==s[::-1]:
    print('The given string is a Palindrome')
else:
    print('The given string is not a palindrome')

##Output:
Enter Some Palindrome String: Rajath
The given string is not a palindrome

Enter Some Palindrome String: madam
The given string is a Palindrome

==================================================================================

##To generate words from given input strings by taking characters alternatively

##Approach1: Throws error, only works when all strings have same length

s1='abcdefg'
s2='xyz'
s3='12345'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    output=s1[i]+s2[j]+s3[k]
    print(output)
    i=i+1
    j=j+1
    k=k+1

##Output:
ax1
by2
cz3
IndexError: string index out of range

##Approach2:
s1='abcdefg'
s2='xyz'
s3='12345'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    output=''
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
    if k<len(s3):
        output=output+s3[k]
        k=k+1
    print(output)

##Output:
ax1
by2
cz3
d4
e5
f
g