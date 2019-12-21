#Create list with inputs from user
n = int(input("Enter number of elements : ")) 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("List is - ", a) 


#Determine maximum elements in the list
print("Maximum Element in a List is")
print (max(a)) 


#Determine minimum elements in the list
print("Minimum Element in a List is")
print (min(a)) 

#Insert new element into the list
x=int(input("Enter a value to insert :"))
a.append(x)
print("Element Inserted -", a)

#Delete an element from the list
print("Deleting value")
a.remove(x)
print("Element Deleted -",a)

#check value present in a list
n = int(input("Enter The value to check :"))

if (n in a): 
	print ("Element Exists") 
else:
	print("Element Not in a List")
