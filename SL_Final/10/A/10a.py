from functools import reduce
lst=list(map(int,input("Enter 6 Numbers\n").split()))
lst1=[x*3 for x in lst]
sum=reduce(lambda x,y:x+y,lst)
print(sum)
sum=reduce(lambda x,y:x+y,lst1)
print(sum)


