//All Java files needs to have .java as extension
//After writing the code, compile it, it will turn into a byte code and finally JVM understands it
//Execution will start from a file which we specify and it needs to have main method which is an entire method signature
//Example of a main method is public static void main (string a[])
//when we run below program, we will get an error class is missing, so add claa as well
//Everything in Java is an object

class Hello
{
    public static void main(String a[])
    {
        int x = 6; //Java is strongly typed
        //y = 7; //This won't work like Python :(
        System.out.println("Hello World");
    }
}

//javac <file name>.java (This is for compiling .i.e it generates class file)
//java <class name> (****don't mention .class, Here actual execution happens)
//Once we compile above piece of code, it generates .class file
//.class file is byte code, which human doesn't understand
//Whenever we run something like an advanced code, we also need additional libraries
//Java Runtime Environment = JVM + Libraries
//As developer we generally install JDK, JDK = JRE = JVM + Libraries
//After developing on acer I want to run on Vivi's machine, he only needs JRE & JRE not JDK
//That's why Java is called as WORA : Write Once Run Anywhere
//Java is a Strongly Typed Language, that is we need to specify variable type, we can't blindly specify variables

class Num{
    public static void main(String a[]){
        int num1 = 1;
        int num2 = 3;
        System.out.println(num1 + num2);
        byte x = 127;
        System.out.println(x);
        double y = 2.3;
        float z = 2.4f;
        System.out.println(z);
        char c = 'k';
        boolean b = true;
        System.out.println(c);
        System.out.println(b);
        int bin = 0b101; //Output is 5
        int hex = 0x7E; //Output is 125
        int num_zero = 10_00_00_000; //Output is 100000000 and it's New feature in Java helps in identifying num_zeroes for programmer
        System.out.println(bin);
        System.out.println(hex);
        System.out.println(num_zero);
        char t = 'a';
        t++; //Output seems to be surprising, it gives as b
        System.out.println(t);
    }
}

//In Java we have two types of Data Types, Primitive and "We shall get to know as we proceed"
//Primitive can be divided in 4 types
    //Integer : byte, short, int, long
    //Float : double, float
    //Character : String
    //Boolean : true, false (Note : 0,1 doesn't work)
//int : 4 bytes
//Long : 8 bytes
//Short : 2 bytes
//byte : 1 byte : ranges between -128 to 127
//So until 127 we can use byte as datatype, helps in saving more memory
//char : 2 bytes
//Java by default supports UNICODE and not ASCII
//UNICODE : 2 bytes .i.e 16 bits

Type Casting / Conversion:
==========================

class CC{
    public static void main(String a[]){
        byte b = 127;
        int c = b; //This will work and called as implicit conversion
        System.out.println(c);
        byte t = 118;
        int s = 176;
        t = (byte) s; //This called as Type Casting aka Explicit Conversion, provided int value is in the range of -128 to 127, if it is greater than the range, it will take modulus value of it .i.e int value % 256 (256 is sum of byte range -128 to 127)
        System.out.println(t);
        float f = 5.6f;
        int k = (int)f; //Post casting we would lose the decimal values
        System.out.println(k);
        //Let's check out Type Promotion, see below example,
        byte m = 10;
        byte n = 30;
        int result = m * n; //Since output of multiplying two byte values is greater than 127 we're promoting or storing as int
        System.out.println(result);
    }
}

Assignment Operatrors:
======================
class CC{
    public static void main (String a[]){
        int num1 = 7;
        int num2 = 8;
        //num1 += 8; This also works
        //num1++; This is increment by 1 and also called post increment
        //++num1; This is also increment and also called pre increment
        /*Based on usage both pre & post are different when we assign to a variable
         * int result = num++; This fetch the value and then increment, o/p is 7 only
         * int result = ++num; This will increment and then fetch the value
         */
        int result = num1 + num2;
        System.out.println(result);
        int sub1 = 7;
        int sub2 = 8;
        //sub1 -= 8; This also works
        //sub1--; This is decrement by 1
        int result2 = sub1 - sub2;
        System.out.println(result2);
        int div1 = 7;
        int div2 = 8;
        int result3 = div1 / div2;
        //div1 /= 8; This also works
        System.out.println(result3);
        int mod1 = 7;
        int mod2 = 8;
        int result4 = mod1 % mod2;
        //mod1 %= 8; This also works
        System.out.println("The modulus output: ");
        System.out.println(result4);

    }
}

Relational Operators:
=====================
class CC{
    public static void main (String a[]){
        //Relational Operators
        /* < is the less than
         * > is the greater than
         * <= is the less than and equal too
         * >= is the greater than and equal too
         * == is the equal value check
         * != is the not equal to check
         * For comparison, the output is general a boolean
         */
        int x = 6;
        int y = 5;
        boolean result = x < y;
        System.out.println(result); //It's false
        int z = 6;
        int b = 6;
        boolean result1 = z <= b;
        System.out.println(result1); //It's true

    }
}

Logical Operators:
==================
class CC{
    public static void main (String args[]){
        //Logical Operators
        /*
         * & is the AND operator
         * || is the OR operator
         * ! is the NOT operator
         */
        int x = 7;
        int y = 5;
        int a = 5;
        int b = 9;
        boolean result = x>y || a<b ; //Also called as Short Circuit output, because it Or operator x>y is True it won't check whether a < b since if one value is True output is true, that's saves time
        System.out.println(result);
		System.out.println(!result); //Gives the negated output
    }
}

Conditional Statements1:
========================
class CC{
    public static void main (String args[]){
        //Conditional Statements
        int x = 20;
        if(x>10 && x<=20)
            System.out.println("Hello");
        else
            System.out.println("Bye");
    }
}

Conditional Statements2:
========================
class CC{
    public static void main (String args[]){
        //Conditional Statements
        int x = 20;
        if(x>10 && x<=20){ //If there are more than one line, then curly braces become mandatory
            System.out.println("Hello");
            System.out.println("Thank You");
        }
        else
            System.out.println("Bye");
    }
}

Conditional Statements3:
========================
class CC{
    public static void main (String args[]){
        //Conditional Statements
        int x = 20;
        int y = 40;
        int z = 50;
        if(x>y && x>z){
            System.out.println(x);
            System.out.println("Thank You");
        }
        else if (y>x && y>z){
            System.out.println(y);
            System.out.println("Bye");
        }
        else
            System.out.println(z);
    }
}

Ternary Operator: Shortcut for if else
=================
class CC{
    public static void main (String args[]){
        //Old School
        int x = 5;
        if(x%2==0)
            System.out.println("The input number is even");
        else
            System.out.println("The input number is odd");
        //Short Cut using a Ternary Operator:
        int result = 0;
        int n = 5;
        result = n%2==0 ? 10 : 20;
        System.out.println(result);

    
    }
}

Switch Statements:
==================
class CC{
    public static void main (String args[]){
        //Switch Statements
        int n = 3;
        switch(n){
            case 1:
                System.out.println("Monday");
                break; //Break is important or else once case 1 is matched it also executes remaining cases as well
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            default:
                System.out.println("Enter a valid number");
        }
    }
}

Looping in Java: In general For loop is used the most, while loop in case of reading files, connecting with DB for reading data etc and do while is the least used
================
While Loop:
-----------
class CC{
    public static void main(String args[]){
        int i = 1;
        while(true){ //This goes on forever
            System.out.println("Hi"+i);
            i++;
        }
    }
}

class CC{
    public static void main(String args[]){
        int i = 1;
        while(i<=7){ //This prints Hi 7 times
            System.out.println("Hi"+i);
            int j = 1;
            while(j<=3){
                System.out.println("Hello"+j);
                j++;
            }
            i++;
        }
        System.out.println("Bye"+i); //i value is 8, because while condition failed when i value was 8
    }
}

do-while Loop:
--------------
class CC{
    public static void main(String args[]){
    //do while : When we want to get an output atleast once even when condition is false or not in favour, it's good to opt for do while
    int i = 5;
    do{
        System.out.println("Hi" + i);
        i++;
    }while(i<=4);
    }
}

For Loop:
---------
class CC{
    public static void main(String args[]){
    //For Loop:
        for(int i=1;i<=4;i++){ //We can pass multiple arguments within this, better and concise way of writing code
            System.out.println("Hi"+i);
        }
    }
}

class CC{
    public static void main(String args[]){
    //For Loop:
        for(int i=1;i<=5;i++){
            System.out.println("Day"+i);
                for(int j=1;j<=9;j++)
                {
                    System.out.println("    "+(j+8)+"-"+(j+9));
                }
        }
    }
}