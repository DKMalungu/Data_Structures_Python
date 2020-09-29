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
|  5. |   |   |   |
|  6. |   |   |   |
|  7. |   |   |   |
|  8. |   |   |   |
|  9. |   |   |   |
|  10. |   |   |   |
|  11. |   |   |   |
|  12. |   |   |   |
|  13. |   |   |   |
|  14. |   |   |   |
| 15.  |   |   |   |
| 16.  |   |   |   |