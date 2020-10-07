
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

