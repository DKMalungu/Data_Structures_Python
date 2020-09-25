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