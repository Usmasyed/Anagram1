first=input("Enter the first string:")
second=input("Enter the second string:")
y=''.join(sorted(first))
z=''.join(sorted(second))
lo=y.lower()
lo1=z.lower()
len1=str(len(y))
len2=str(len(z))
if len1==len2:
	if lo==lo1:
		print("Given",second,"is anagram")
else:
	print("Given",second,"is not anagram")	
