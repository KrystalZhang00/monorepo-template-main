# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is a concrete class. It is not defined as an abstract class, and it does not have any abstract methods (methods without implementations) that would be required for it to be considered an abstract class. 
   Concrete classes can be instantiated, and MObject does not enforce any requirements on its subclasses to implement specific methods.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The __del__ method is a special method in Python called a destructor. It is called when an object is about to be destroyed or garbage collected. it is comment out, so doesn't have any effect.
   
1. What class does Texture inherit from?
	- The Texture class inherits from the Image class. This is indicated by the line: class Texture(Image):, which means that Texture is a subclass of Image and inherits its attributes and methods.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- The Texture class inherits all the methods and attributes from the Image class. This includes the constructor __init__, the getWidth, getHeight, getPixelColorR, getPixels, and setPixelsToRandomValue methods, as well as the attributes m_width, m_height, m_colorChannels, and m_Pixels.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- The choice depends on whether Texture should be treated as a specialized image type or as an object that includes an image as part of its composition. 
    - If a Texture is fundamentally a type of Image and shares its core behavior and attributes, then an inheritance relationship makes sense.
    - If a Texture contains an Image as one of its components but is not a type of Image in the inheritance sense, then a composition relationship may be more appropriate. 
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, Python automatically creates a constructor (the __init__ method) for a class.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

Singletons in Python are not thread-safe by default. 
Thread safety must be explicitly implemented using synchronization mechanisms like locks to prevent multiple threads from creating multiple instances of a singleton. 
Python's Global Interpreter Lock (GIL) can affect the behavior of certain synchronization approaches.  
  
