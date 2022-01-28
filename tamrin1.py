
import math
a=float(input('pleaz inter first number: '))
op=input('choose a charakter: ')
b=float(input('pleaz inter second number: '))
if op== '+':
    result= a+b
if op== '*' :
    result= a*b
if op== '-' :
    reult= a-b
if op=='/' and b!=0:
    result=a/b
if op== '/' and b==0:
   result='b namotabar' 
if op=='factorial':
    result=math.factorial(a), math.factorial(b)
if op=='radical':
    result=a**(1/b)
if op=='sin':
    result=math.sin(math.radians(a)), math.sin(math.radians(a))
if op=='cos':
    result=math.cos(math.radians(a)), math.cos(math.radians(b))
if op=='tan':
    result=math.tan(math.radians(a)), math.tan(math.radians(b))
if op=='cot':
    result=math.cos(math.radians(a)) / math.sin(math.radians(a)), math.cos(math.radians(b)) / math.sin(math.radians(a)) 
    
print(result)    

