def celsToKel(cel):
	return cel + 273
def celsToFarh(cel):
	far = 32 + (1.8 * cel)
	return far
print("Welcome to tempeature convertor\n\n")
while(True):
	print("Enter anything for conversion and type 'no' to exit")
	x = input()
	if(x=="no"):
		break
	else:
		print("1:Celsius to Kelvin \n2:Celsius to Farheneit")
		choice = int(input())
		cel = int(input("Enter temperature in celsius :"))
		if(choice==1):
			print("Celsius to Kelvin: ",celsToKel(cel))
		elif(choice==2):
			print("\ncelsius to farheneit: ",celsToFarh(cel))	
		else:
			print("\n\nInvalid Choice please Try Again\n")
