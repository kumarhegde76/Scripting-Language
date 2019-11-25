class Person:
	def __init__(self,name,age):
	 self.name=name;
	 self.age=age;
p1=Person("Suppandi",21)

print("\n Name of a Person #1 is",p1.name)
print("\n Age of the Person #1 is",p1.age)


print("\n *** Printing after deleting Age attribute for p1 ***")
del p1.age


print("\n Name of a Person #1 is",p1.name)
#print("\n Age of the Person #1 is",p1.age) #This line will give an error
#Error is AttributeError 
print("\n *** printing After deleting p1 ***")
del p1

print("\n Name of a Person #1 is",p1.name) #This line will give an error
#Error is NameError: name 'p1' is not defined
