
# Chapter 2 Object Oriented Programming

## 2.1 Goals, Principles and Patterns

### 2.1.1 Object-Oriented Design Goals

Software implementations should achieve robustness, adaptability, and readability.

**Robustness**

The program should produce correct output for all the anticipated inputs in the program.
robust software is one capable of handling unexpected inputs that are not explicitly defined for its application

Example:

    A program expects integer but the user provides float number or string the program should be able to recover gracefully from this error.

**Adaptability**

Software need to be able to evolve overtime in response to changing conditions in the environment.
Therefor an important goal of good software is that it achieves adaptability and portability.
Portability is the ability of software to run with minimal changes on different hardware and operating system platforms

**Reusability**

The same code should be usable as a component of different systems in various applications.  
This will help in offsetting the cost of creating good programs.

### 2.1.2 Object-Oriented Design Principles

Principle of the object-oriented approach, which facilitate the above goals are:

1. Modularity
2. Abstraction
3. Encapsulation

**Modularity**

A software system typically consist of several different components that must interact correctly in order for the entire system to work properly.
Keeping these interactions straight requiers that these different components be well organized.
Modularity referes to an organizing principle in which different components of a software system are divided into separate functional units.

In Python we have already seen a module as a collection of closely related functions and classes that are defined together in a single file of sources code.

**Abstraction**

The notion of abstraction is to distill a complicated system down to its fundamental parts.
Applying abstarction paradigm to the design of data structure gives rise to ***abstract data types*** (ADT's).
An ADT is a matematical model of a data structure that specifies the type of data stored, the operation supported on them, and the type of parameters of the operations.
An ADT specifies what each operation does, but not how it does it.
We refer to the collective set of behaviors supported by an ADT as its ***public interface***

Python has a tradition of treating abstractions implicitly using a mechanism know as ***duck typing***.
A programmer in python assumes that an object support a set of known behaviors, with the interpreter raising a run-time error if those assumtion fails.
This is refered to as duck typing

i.e:

"when I see a bird that walk like a duck and swim like a dick and quack like a duck, I call that bird a dick" - James Whitecomb

Python supports abstact data type (ADT) using a mechanism known as an **abstract base class** (ABC).
An ABC cannot be instantiated, but it defines one or more common methods that all implementations of the abstraction must have.
An ABC is realized by one or more concrete classes that inherits from the abstract base class while providing implementations for those methods declared by the ABC.

**Encapsulation**

Different components of a software system should not reveal the internal details of their respective implementations.
The advantage of encapsulation is it allows one proggrammer without regard that other programmers will be writing code that is depended on those onternal decisions.
The only constraint on the programmer of a component is to maintain the public interface for the component as other programmers will be witing code that depends on that interface.
Encapsulation supports robustness and adaptability.

### 2.1.3 Design Patterns

**Design pattern** descibes a solution to a "typical" software design problem.
A pattern provides a general template for a solution that can be applied in many different situations.
It describes the main element of a solution in an abstracted way that can be specialized for a specifix problem at hand.
It consists of a name, which identifies the pattern; a context which descibes the scenarios for which this pattern can be applied; a template, which describes how the pattern is applied: and a result, which describes and analyzes what the pattern produces.

Design Patterns fall into two groups:

1. Patterns for solving algorithm desing problem
2. Patterns for solving software enegineering problems.

## Software Development

Traditional software development involves:
1. Design
2. Implementation
3. Testing and Debugging

### 2.2.1 Design

The design step we decide how classes will interact, what data each will store and what actions each will perform.

Rules of thumb to detemining how to design our classes:

* **Rsponsibilities:** Divide the work into different actors, each with different responsibility.
* **Independence:** Define the work for each class to be as independent from other classes as possible. Give data to the class that has jurisdiction over the actions that require acces to this data.
* **Behaviors:** Define the behaviours for each class carefullyand precisely, that the consequences of each action performed by a class will be well understood by other classes that interact with it.

### 2.2.2 Pseudo-Code

It's simply an implementation of an algorith in the form of annotations and informative text written in plan English.

Advantages of Pseudocode

* Improve the readability of any approach.
*  Acts as a bridge bettwen the program and the algorith or flowchart.
*  The main goal of a pseudo code is to explain what exactly each line of a program should do, hence making the code constractionphase easier for the programmer.

### 2.2.3 Coding Style and Documentation

**Coding Style**

The coding style implemented while reading this book is the official style guide for python code

[Official Style Guide For Python Code link](http://www.python.org/dev/peps/pep-0008/)

**Documentation**

Python provides integrated support for embedding documentation directly in source code using a mechanism know as docstring
The first statement within the body of a class or function is considered as the docstring.
Docstring is punchuated using triple quotes(""" docstring here """)

### 2.2.4 Testing and Debugging

Testing is the process of experimentally checking the correctness of a program, while debugging is the process of tracking the execution of a program and discovering the error in it.

**Testing**

The aim of testing is to aim to execut the program on a representative subset of inputs
Program often tend to fail on special cases of the input.
Such special cases need to be carefully identified and tested.

We should also consider special conditions for structures used by the program.

Top-Down testing proceeds fro the top to the bottom of the programs hierarchy.
Its typically used in conjunction with stubbing.

Stubbing - a boot -strapping technique that replaces a lower-level component with a stub, a replacement for the componenet that simulates the functionality of the original.

Example:

    if function A calls function B to get a first line of a file, when testing A we can replace B with a stub that returns a fixed string.

Bottom-up testing proceeds from lower-level components to higher- level components.

ie. A class that doesnot depend upon any other classes can be tested before another class that depends on the former.
This form of testing is usually described as **unit testing** as the functionality of a specific components is tested in isolation of the lager software project.

Python provides several forms of support for automated testing.

when functions or classes are defined in the a module, testing for that module can be emebedded in the same file

using:

    if __name__ == '__main__'

        # Perform tests
    this will ensure that the test can run withing the module but will not be run whem the module is imported. 

Better suport for automation of unit testing is provided by python's **unittest** module.
This framework allows the grouping of individual test case into lagger test suites and provides support for exacuting those suites and reporting or anamyzing the results of those test.
As software is maintained the act of regression testing is used, whereby all previous test are re-executed to ensure that changes to the software don't introduce new bugs in the reviously tested components.

**Debugging**




## 2.3 Class Definitions

A class serves as the primary means for abstraction in object-oriented programming.
A class provides a set of behaviors in the from of **member functions** (also know as **methods**) with implementations that are common to all instance of thet class.
A class also serves as a blueprint for its instance, effectively detemining the way that state information for each instance is represented in the form of attributes (also know as fields, instance variables or data members).

**The self Identifier**


**The Constructor**

**Testing the Class**

### 2.3.1 Operator Overloading and Python's Special Methods

### 2.3.2 Iterators and generator

Iterator is a bigger concept that generator.
Iterator is an object whose class has a __next__ and __iter__ methods.
Everytime you do next() call to the iterator object, you would get the next item in the sequence until the iterator object is exhausted and raise StopIteration.

However, generator is a function that returns as iterator. It looks like normal function except that is used yield instead of return

***Lazy Evaluation***

Its an evaluation strategy which delays the evaluation of an expression until its value is needed and which also avoids repeated evaluation.
Lazy evaluation can improve the efficiency of your code and save plenty of resources.

The opposite of lazy evaluation is strict evaluation. Strict Evaluation is where evaluation is done immediately when the program regardless of use.

## 2.4 Inheritance

A natural way toorganize various structural componets of a software package is in a hierarchical fashion, with similar abstract definitions grouped together in a level-by-level manner that goes from specific to more general as one traverser up the hierarchy.
The correspondence between levels if often referred to as an **"is a" relationship**
This imlementation support reuse of code, in object-oriented programming, the mechanism for a modular and hierarchical organization is a technique know as **inheritance**
This allows a new class to be defined based upon an existing class as the starting point.  
In OOP the exisiting class is typically described  as the **base class, parent class** or **supper class**, while the newly defined class is known as the **subclass** or **child class**

There are two ways in which a subclass can differentiate itself from its superclass.

1.  A subclass may **specialize** an existing behavior by providing a new implementation that **overrides** an exesting method
2.  A subclass may also **extend** it superclass by providing brand new methods

**Protected Members**

Members that are declared as protected are accessible to subclasses, but not to the general public, while member that are declared as private are not accessible to either.
Python does not support formal acces control, but names beginning with a single underscore **(-)** are conventianally akin to protected, while names beginning with a double underscore (other than specal methods) are akin to provate.