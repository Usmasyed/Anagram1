def factorial(a):
	if a==1:
		return a
	else:
		return a*factorial(a-1)
x=int(input("Enter your number:--"))
z=factorial(x)
print("factorial of",x,"is",z)
