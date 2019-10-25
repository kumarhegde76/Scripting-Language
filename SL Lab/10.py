a ={}
while(True):
	print("Enter reg no,-1 to exit")
	m = int(input())
	if m==-1:
		break
	else:
	     print("Enter name")
	     n = input()
	     a[m] = n
for k,v in a.items():
	if k%2==0:
		print(v)
