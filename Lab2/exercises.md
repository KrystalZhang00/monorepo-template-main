# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? 
  - A good example would be a function called 'pop' which only removes one element.
  - A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.


Yes, the names of functions should ideally correlate to what they do, and they should act as good "verbs" that describe the action the code is performing.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)


Dictionaries and lists are two different data structures in programming, each with its own characteristics and use cases.
the main differences between dictionaries and lists lie in their underlying data structures, the way they store and retrieve data, and their use cases:

-Lists are ordered collections that store elements in a contiguous block of memory, and you access elements by index.
-Dictionaries are key-value pairs, where data is stored in a hash table, and you access values by their associated keys. Dictionaries can be ordered or unordered depending on the programming language.


3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?


Yes, a list allows for random access.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?


Pros:
Flexibility: Generic data structures can handle any data type, providing code flexibility and reducing redundancy.
Code Reusability: They promote code reusability across projects by avoiding the need for specialized data structures.
Reduced Redundancy: Using one data structure for multiple types reduces code duplication.
Simplicity: Consistent use simplifies code and enhances readability.
Support for Custom Types: Generic structures can work with custom data types, facilitating complex applications.
Cons:
Performance Overhead: They may be less efficient due to dynamic typing, leading to slower execution.
Type Safety: Generic structures may lack strong type safety, potentially causing runtime errors.
Complexity: Handling multiple types can make code more complex.
Lack of Optimization: Specialized structures can outperform generic ones.
Debugging Challenges: Debugging can be more challenging, as type issues may only surface at runtime.





## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).


It is well named. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?


No, it appears that the library generally follows the practice of avoiding functions with a large number of arguments.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  


**kwargs in Python is a way to accept a variable number of keyword arguments in a function or method, collecting them into a dictionary.
Advantages:
Flexibility: Makes methods versatile.
Extensibility: Allows adding new arguments without breaking existing code.
Default Values: Supports default values.
Disadvantages:
Readability: May reduce code readability.cha
Error Handling: Handling unexpected arguments can be complex.
Lack of Type Checking: Doesn't enforce type checks.
Documentation Needed: Requires clear documentation for proper usage.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?



setting arguments to None or other predetermined values in Python methods is a common practice to provide flexibility, 
usability, and safety when using those methods. It allows users to easily customize the behavior when necessary 
while providing reasonable defaults for common scenarios.
