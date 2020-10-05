# Basic Ideas
Accessors - Methods that return information about the state of an object but don'y change that state.

Mutator / Update methods - Methods that return information about the state of an object but change it state.

immutable class - if the object of that class have fixed values ie. once declared they can subsequently change

Example - int class is immutable

The list, tuple and str classes are sequences types in python, rep a collection of values in which the order is significant.

Difference between list and tuple
List is mutable while tuple is immutable

List

* A list is a referential structure as, it technical stores a sequence of references to its elements.
* list are array-base sequence hence a list of length n and index start as zero hence the index of values in this list are 0 - n-1 inclusive.
* The constructor list produces an empty list when iterable values are provided it will provide a list of this values 
    
    Example
     
    list('Daniel') => ['D', 'a', 'n', 'i', 'e', 'l']

Tuples

* tuple provide a immutable version of a sequence 
* To express a tuple of length one as a literal a comma must be place after the element 
    Example : (2) ==> parentheses integer
              (2,) ==> iterable tuple

String (str)
* it an immutable sequence of character based upon the unicode international charcter set.
* Unicode characters can be included 
* using triple quotation marks allows newline automatically without having to insert it in multiple line string

Set and Frozenset 
* set class represents the mathematical notion of a set where a object without duplication.
* advantage of set overlist is to check if an element exist 
* set are based on hash tables

Restrictions:

    * set don't maintain values in a specif order
    * only elements of immutable type can be added inside sets
    
        Example:
            int, string, float e.t.c
    

frozenset - it an imutable form of the set type so its legal to have sets of frozenset


Dictionary (dict)
* its a mapping from a set of distinct keys to assorted values

**Important:** literals and constructors can be used to create instances of
built-in classes

Logical Operators
Supported logical operators in python are:
    
    * not - negation
    * and - conditional
    * or - coditional
    important - and and or operators do not evaluate the second operand if the results can be determined based on the value of the first operand.
    

Equality Operators
supported equality operators in python are:

    * is - same identity
    * is - not different 
    * == - equivalent 
    * != - not equivalent



Comparison Operators
comparision operators in python are:
    
    * < - less than
    * <= - less than or equal to 
    * > - greater than
    * >= - greater that or equal to
    
Bitwise Operators
Bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are 
performed on bit by bit, hence the name bitwise operators. Then the result is returned in decimal format.

    * & Bitwise AND x & y
    * | Bitwise OR x | y
    * ~ Bitwise NOT ~x
    * ^ Bitwise XOR x ^ y
    * << shift bits left, filling in with Zeros <<x
    * >> shift bit right, filling in with sign bit x<<
   
Sequence operators
The following types (str, tuple and list) support the following operator types syntaxes:
    
    * s[j] the element at postion j
    * s[start:stop] slices the indices from start (index) :All the element here: End (Index)
    * s+t this concantenats two squnces 
    * K*s reparting the s values k number of times
    * val in s checks if s contains the value k
    * val not in s check if the value is not in s
    
**Important:** Index in python start from Zero the a sequence of length n has elements from 0 to n-1. Python supports the use of negative indices they 
 denote the distance from the end of the sequence 
 
 Comparision Operation in sequences 
 All sequnce define comparison operations based on lexicographic order, performed an element by element conparison untill difference is found
 therefor 
 
    * s == t equivalent (element by element)
    * s != t not equivalent
    * s < t lexicographically less than
    * s <= t lexicographically less than or equal to
    * s > t lexicographically greater than
    * s >= t lexicographically greater than or equal to
    
Operators for Set and Dictionaries
Sets and frozensets support the following operators:
the creation of sets
s1 = {1,3,5,7,8}
s2 = {3,4,5,8,20}

    * key in s containment check
    * key not in s non-containment check
    * s1 == s2 s1 is equivalent to s2
    * s1 != s2 s1 is not equivalent to s2
    * s1 <= s2 s1 is subset of s2
    * s1 < s2 s1 is proper subset of s2
    * s1 >= s2 s1 is superset of s2
    * s1 > s2 s1 is proper superset of s2
    * s1 | s2 the union of s1 and s2
    * s1 & s2 the intersection of s1 and s2
    * s1 − s2 the set of elements in s1 but not s2
    * s1 ˆ s2 the set of elements in precisely one of s1 or s2

Operation in set are not lexicographic rather they are based on mathematical notion of a subset.

Dictionary

    * d[key] value associated with given key
    * d[key] = value set (or reset) the value associated with given key
    * del d[key] remove key and its associated value from dictionary
    * key in d containment check
    * key not in d non-containment check
    * d1 == d2 d1 is equivalent to d2
    * d1 != d2 d1 is not equivalent to d2

Compound Expressions and Operator Precedence
Python allow a chained assignment such as x = y = 0 

|   |  Type | Symbols  | Explanation  |
|---|---|---|---|
|  1. | member access  |  expr.member |   |
| 2.  |  function/method calls container subscripts/slices | expr(...), expr[...]  |   |
|  3. | exponentiation  |  ** |   |
| 4.  |  unary operators | +expr, −expr,  <sup>~</sup>expr  |   |
|  5. | multiplication, division  | *, /, //, %  |   |
|  6. | addition, subtraction  |  +, - |   |
|  7. |  bitwise shifting | <<, >>  |   |
|  8. |  bitwise-and | &  |   |
|  9. |  bitwise-xor |  ^ |   |
|  10. | bitwise-or  |  | |   |
|  11. | comparisons containment  | is, is not, ==, !=, <, <=, >, >=, in, not in  |   |
|  12. | logical-not  | not expr  |   |
|  13. | logical-and  |  and |   |
|  14. |  logical-or |   or |   |
| 15.  |  conditional | val if cond else val2  |   |
| 16.  |  assignments |  =, +=, −=, =, etc. |   |

Control Flow
Syntax in python uses block of code. The colon character is used to delimit the beginning of a block of code that acts as a body for a control structure

Conditionals 

Conditional constructs (also known as if statements) provide a way to execute a chosen block of code based on the run-time evaluation of one or more Boolean
expressions.

    if first condition:
        first body
    elif second condition:
        second body
    elif third condition:
        third body
    else:
        fourth body
        
Loops

Python offers two distinct looping constructs A while loop allows general repetition based upon the repeated testing of a Boolean condition. A for loop provides
convenient iteration of values from a defined series (such as characters of a string, elements of a list, or numbers within a given range).

While Loop

The syntax for a while loop in pythoin is as follows:

    while condition:
        body

**Important** Python doesnt have a do while loop 

For Loops 

For lopss used on any type of iterable structure such as a list, tuple, str, dic of file

    for element in iterable:
        body
        
Break and Continue Statements

Break statement is meant to terminate a while or for loop when executed within it body

continue
state causes the current iteration of a loop body to stop but with subsequent passes of the loop proceeding as expected.

Function and Methods

We use the general term function to describe a traditional, stateless function that is invoked without the context of a particular class or an instance of that class
We use the more specific term method to describe a member function that is invoked upon a specific object using an object-oriented message passing syntax
 
The first line, beginnning with the keyword def, serves as the function's signature.

    def function_name(the, number, of, parameters, and, there, name):
        The Body of the function
        return statement

Each time a function is called, Python creates a dedicated activation record that stores information relevant to the
current call. This activation record includes what is known as a namespace to manage all identifiers that have local scope within the current call.

Return Statement
A return statement is used within the body of a function to indicate that the function should immediately cease execution, and that an expressed value should 
be returned to the caller. If a return statement is executed without an explicit argument, the None value is automatically returned.

Information Passing
the identifiers used to describe the expected parameters are known as formal parameters, and the objects sent by the caller when invoking the function 
are the actual parameters. Parameter passing in Python follows the semantics of the standard assignment statement.

Files

Files are typically accessed in Python beginning with a call to a built-in function, named open, that returns a proxy for interactions with the underlying file.
    
    Example:
        variable = open('simple.txt')

The open function accepts an optional second paramter that determines the access mode

    Character Meaning
    * 'r' open for reading (default)
    * 'w' open for writing, truncating the file first
    * 'x' create a new file and open it for writing
    * 'a' open for writing, appending to the end of the file if it exists
    * 'b' binary mode
    * 't' text mode (default)
    * '+' open a disk file for updating (reading and writing)
    * 'U' universal newline mode (deprecated)

Reading from a File

The most basic command for reading via a proxy is the read method. When invoked on file proxy fp, as variable.read(k), the command returns a string 
representing the next k bytes of the file, starting at the current position. Without a parameter, the syntax variable.read( ) returns the remaining 
contents of the file in entirety

Writing to a File

When a file proxy is writable, for example, if created with access mode w or a , text can be written using methods write or writelines. For example, 
if we define fp = open( results.txt , w ), the syntax fp.write( Hello World.\n ) writes a single line to the file with the given string.

Exception Handling

Exceptions are unexpected events that occur during the execution of a program.
An exception might result from a logical error or an unanticipated situation.
In Python, exceptions (also known as errors) are objects that are raised (or thrown) by
code that encounters an unexpected circumstance. The Python interpreter can also
raise an exception should it encounter an unexpected condition, like running out of
memory. A raised error may be caught by a surrounding context that “handles” the
exception in an appropriate fashion.

|Class|Description
|-----|-----------|
|Exception|A base class for most error types
|AttributeError| Raised by syntax obj.foo, if obj has no member named foo
|EOFError|Raised if “end of file” reached for console or file input
|IOError|Raised upon failure of I/O operation (e.g., opening file)
|IndexError|Raised if index to sequence is out of bounds
|KeyError|Raised if nonexistent key requested for set or dictionary
|KeyboardInterrupt|Raised if user types ctrl-C while program is executing
|NameError|Raised if nonexistent identifier used
|StopIteration|Raised by next(iterator) if no element;
|TypeError|Raised when wrong type of parameter is sent to a function
|ValueError|Raised when parameter has invalid value
|ZeroDivisionError|Raised when any division operator used with 0 as divisor

Raising an Exception

An exception is thrown by executing the raise statement, with an appropriate instance of an exception class as an argument that designates the problem.

Syntax:

    raise ['Error_class or Type']('Message that serves has a parameter')
    
Catching an Exception

There are several philosophies regarding how to cope with possible exceptional cases when writing code.

1. The philosophy for managing exceptional cases is to "look before you leap"

The goal is to entirely avaoid the possibility of an excepton being raised through the use of a proactive conditional test.

2. The second philososphy, often embraced by python programmers is that "it is easier to ask for forgiveness than it is to get permission. by Grace Hopper

The sentiment is that we need not spend extra execution tine safeguarding against every possible exceptional case as long as there is mechanism for 
coping with a problem after it arises.

The most common way for catching error is using the try - except syntax

syntax:

    try:
        (operation)
    except [Error_class] as e:
        action when error_class is encounted 
        
 Generators
 
The most convenient technique for creating iterators in python is thought the use of generators. 
A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a yield statement is
executed to indicate each element of the series.

Additional Python Conveniences

Conditional Expressions

python supports a conditional expression syntax that can replace a simple control structure. 

The general syntax:

    expr1 if condition else expr2
    
Normal implementation

    if n >= 0:
        number = n
    else:
        number = -n
    
    result = foo(param)
    
Conditional expression implementation

    number = n if n>=0 else -n
    
Comprehension Syntax

1. List comprehension syntax

syntax:

    [expression for value in iterable if condition]
 
Normal implementation

    list_values = []

    fro x in list_values:
        if condition:
            list_values.apend

The above implementation is replicated for list, tuple, set and dictonary for comprehensive value generators

Packing and Unpacking of sequences

1. automatic packing

    When a series of comma-separated expressions are given in a large context, they will be treated as a single tuple even if no enclose parentheses are provided.
    
        data = 2, 3, 4, 5
        this will be represented as (2, 3, 4, 5) 
    
    use of packing in python is when returning multiple values from a function
        
        return a, y
        this will be represented as (a, y)

2. automatically unpacking

    allowing on to assign a series of individual identifiers to the elements of a sequence
        
        a, b, c, d = range(1, 5)

3. Simultaneous AAssignments

    The combination of automatic packing and unpacking froms a technique know as simultaneous assignment wherby we explicitly asssign a series of 
    values to a series of identifiers using as syntax:
    
        a, b, c, d = 1, 2, 3, 4
        
    in effect, the right-hand side of this assignment is automatically packed into a tiple and the automatically unpacked with its elements assigned 
    to the identifiers on the left hand side.
    
 
Scope and Namespace

With operation like x + y the name x ans y must have been previously associated with object that serve as values a NameError will be raised if no such 
definition are found. The process of determinig the value associated with an identifier is know as name resolution. 

When an identifier is assigned to a value the defination is made within a specific scope
    
    1. Top-level assignments are typically made in what is know as global scope
    2. Assignments made within the body of a function have local scope to the function call.
    
Each of the above scope in python is represented using an abstraction know as namespaces. A namespace manages all identifiers that are currently defined
in our given scope.
Python implements a namespaces with its own dictionary that maps each identifying string to its associates values.

ways of examining namespace:
    
    1. the function dir reports the namesof the identifiers in a given name spaces
        
    class Foo:
        def __init__(self, a=5, b=10):
            self.a = a
            self.b = b
        
    object = Foo()
    print(dir(object))
    
    output:
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']

    2. the function vars returns the full dictionary.
        
     class Foo:
        def __init__(self, a=5, b=10):
            self.a = a
            self.b = b
        
    object = Foo()
    print(vars(object))
    
    output:
    {'a': 5, 'b': 10}
    
Modules and the Import Statements

Python includes many values, function and classes that are organized in additional libraies known as modules that can be imported from within a program
python import statement loads definitions from a module into the current namespace. 

    example:
        from math import pi, sqrt

