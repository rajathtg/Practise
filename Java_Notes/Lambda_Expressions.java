Lambda Expressions:
===================
-Lambda calculus was introduced in the mathematical world in 1930s and it brought big changes
-The first programming language to use lambda expression is LISP
-Later C, C++, Objective C, C#, SCALA, RUBY, Python and finally JAVA joined the party
-Benefits of using Lambada expressions in Java:
	-To enable functional programming in JAVA
	-Write more readable, maintainable & concise code
	-To use APIs very easily & effectively
	-To enable parallel processing
	
How to write lambda expressions-Part-1:
---------------------------------------
-A nameless, modifiersless and no return type function is an anonymous function and an anonymous function is nothing but a lambda expression,

Example1:
---------
public void m1()
{
	System.out.println('Hello');
}

-Let's convert to lambda expression,
	-No need to modifier, therefore remove public
	-Return type not required, therefore remove void
	-Name of method/function not required, therefore remove m1()

() -> {System.out.println('Hello');}

Example2: To add two int values
---------
public void add(int a, int b)
{
	System.out.println(a+b);
}

(int a, int b) -> {System.out.println(a+b);}

Example3: To return the length of the string
---------
public int getLength(String s)
{
	return s.length();
}

(String s) -> {return s.length();}

*****Note: 
	-A lambda-expression can take any no. of parameters
	-If multiple parameters present then these parameters should be separated with ','
	-In the Lambda expressions body if there is only expression, then curly braces are optional
	-Based on the situation / context, compiler can guess datatypes automatically it is called as 'Type Inference', we can remove hardcoding datatypes as well
	-Similar to method body, lamdba expression body can contain any number of statements if multiple statements are there then we should enclose within curly braces
	-Even the return used in the example 3 "return s length()" is also can be guessed by compiler

Example1: () -> System.out.println('Hello');

Example2: (a, b) -> System.out.println(a+b);

Example3: s -> s.length();

=================================================================================================

Functional Interface: 















