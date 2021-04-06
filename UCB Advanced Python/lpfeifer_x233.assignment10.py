#Lauren Pfeifer X442.3 Assignment 10


#QUESTION 1
''' Write a simple Rectangle class. It should do the following: Accepts length and width as parameters when 
creating a new instance Has a perimeter method that returns the perimeter of the rectangle Has an area method 
that returns the area of the rectangle Don't worry about coordinates or negative values, etc.'''

class Rectangle:
    def __init__(self, width=1, height=1): 
        self.length = 1
        self.width = 1
    
    def rectangle_area(self):
        return self.length*self.width
    
    def perimeter(self):
        return self.length*2 + self.width*2
    
newRectangle = Rectangle(1, 1)
print(newRectangle.rectangle_area())
print(newRectangle.perimeter())
        


#QUESTION 2
'''Python provides several modules to allow you to easily extend some of the basic objects in the language. 
Among these modules are UserDict, UserList, and UserString. (Refer to the chart in Topic 10.3 to see what the 
methods you need to override look like. Also, since UserDict and UserList are part of the collection module, 
you can import them using from collections import UserDict and from collections import UserList.)
Using the UserList module, create a class called Ulist, and override the add, append, and extend methods so 
that duplicate values will not be added to the list by any of these operations.'''

from collections import UserList

class UList(UserList): #why the use of "." instead of ","
    def __init__(self): #why don't we have type -> (self, type)
        UserList.__init__(self)
        self.data = data #not sure why the have the "self" part of the "self.data" here. It's a variable, okay...
        return super().__init__()
    
    def add(self, newvalue):
        for item in newvalue: #new value is the object, but not clear where it came from or why its used
            if item in self.data:
                print("%r already exists, will not add." % item)
            else:
                self.data += [item]
                return super().add(newvalue)
        
    def append(self, newvalue):
        for newvalue in self.data: #Why is new value used here? Confused bc in the add block it's got another use
            if item in self.data:
                print("%r already exists, will not add." % newvalue)
            else:
                return super().append(newvalue)
    
    def extend(self, newvalue = []):  #still unclear why we have newvalue here and it's equal to an empty list
        for item in newvalue:
            if item in self.data:
                print("%r already exists, will not add." % item)
            else:
                return super().extend(newvalue)
        return self.data
    
mylist = Ulist([3,4,5])
print(mylist)