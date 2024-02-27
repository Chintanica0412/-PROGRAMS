import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
ans=((b**2)-(4*a*c))
r1=(-b-math.sqrt(ans))/2*a
r2=(-b+math.sqrt(ans))/2*a
print("the result is",r1,r2)