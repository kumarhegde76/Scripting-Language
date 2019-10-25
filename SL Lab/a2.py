class Student:
           def __init__(self,name="kumar",age=21,marks):
		 self.name=name;
		 self.age=age;
		 self.marks =[100, 100, 100]


	   def display(self)
		print("Name is:",self.name)
		print("Age is:",self.age)
	
	   def user(self)
		self.name=input("\nEnter The name:")
		self.age=input("\nEnter The Age:")
		self.marks[0]= int(input("\nEnter Marks#1 :"))
		self.marks[1]= int(input("\nEnter Marks#2 :"))
		self.marks[2]= int(input("\nEnter Marks#3 :"))
st1=Student()



