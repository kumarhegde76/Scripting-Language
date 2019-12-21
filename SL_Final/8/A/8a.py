dict ={'xe':'xenon','cr':'crepton','re':'redon'}

elesym=input("Enter The Symbol to add :\n")
elename=input("Enter Name of the Element to add :\n")
if elesym in dict:
	print("You have entered same value")


elif elesym not in dict:
	dict[elesym]=elename
print(dict)
print("Number of Element in the list is :",len(dict))


x=input("Enter Symbol to search :")
if x in dict:
	print("Element Found and value is :",dict[x])
else:
	print("Element Not Found")
