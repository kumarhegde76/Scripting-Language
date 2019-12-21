class Student:
	name=''
	age=''
	lst=[]
	mylst=[]

	def __init__(self,name,age,lst):
		self.name=name
		self.age=age
		self.lst=lst
	def Display(self):
		print(self.name,'',self.age,'',self.lst)
	def accept(self):
		myname=input("Enter Name\n")
		myage=input("Enter Age\n")
		mymarks=list(map(str,input().split()))
		p=Student(myname,myage,mymarks)
		p.Display()
obj=Student('a','12',[12,15,16])
obj.Display()
obj.accept()

