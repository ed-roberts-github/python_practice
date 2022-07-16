#!/usr/bin/env python
# coding: utf-8

# In[30]:


class Dog:
    #Class attribute
    species = "Canis familiaries"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} barks: {sound}" 
        
        

class JackRussellTerrier(Dog):
    #def speak(self, sound="Arf"):
    #    return f"{self.name} says {sound}"\
    
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.speak())
print(buddy.speak("woooooof"))


# In[21]:


class Car:
    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles."
    
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage
        
        
BlueCar = Car('blue', 20000)
RedCar = Car('red', 30000)

print(BlueCar)
print(RedCar)


# In[32]:


class GoldenRetriever(Dog):
    def speak(self, sound="bark"):
        return super().speak(sound)
    
barney = GoldenRetriever('Barney', 10)

print(barney.speak())
    

