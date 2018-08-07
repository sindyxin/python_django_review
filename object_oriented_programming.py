class Dog():
  #class object attribute
  #class object attributes are always the same for any instance of the class
  species = "mammal"
  def __init__(self, breed, name):  
    #self is always necessary,this methods refers to itself
    #breed is the argument and the value is passed during the instantiation or initializetion of the class itself
    self.breed = breed
    self.name = name

mydog =Dog("Labrador", "Coco")
print(type(mydog))
print(mydog.name, mydog.breed)
print(mydog.species)

class Circle():
  pi=3.14
  def __init__(self, redius=1): #redius=1 is a default value
    self.redius=redius

  def area(self):
    #must use self.redius means current redius
    #pi is objecy level attribute must use Circle.pi
    return self.redius ** 2 * Circle.pi

  def set_redius(self, new_redius):
    self.redius=new_redius
    #not all object method need to return something, some justaffect the object in place.

mycircle=Circle(3)
print(mycircle.redius)
print(mycircle.area())

mycircle.redius=10
print(mycircle.redius)
print(mycircle.area())

mycircle.set_redius(15)
print(mycircle.redius)
print(mycircle.area())

class Book():
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  #special method
  def __str__(self):
    return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
  
  def __len__(self):
    return self.pages

  def __del__(self):
    print("A book is destroyed!")
  

b = Book("Python", "Sindy", 666)
print(b)
print(len(b))
del b
print(b)  #here should show error because b instance is destroyed after del b

