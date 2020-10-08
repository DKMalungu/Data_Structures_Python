
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

### Coding Style and Documentation


