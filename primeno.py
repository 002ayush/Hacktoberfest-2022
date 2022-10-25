n = int(input("Enter a number:"))
k = 0
for i in range(1,n+1):
  if (n%i == 0):
    k+=1
if k==2:
  print(n,"is a primne no")
else:
  print(n,"is not a prime no")
