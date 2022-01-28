
height=float(input('pleaz inter your height(c.m): '))
weight=float(input('pleaz inter yor weight(k.g): '))
height=height/100          #ghad bayad bar hasb metr bashe#
result=weight/(height**2)
if result < 18.5:
    bmi='under weight'
elif 18.5 <= result < 24.9:
    bmi='normal'
elif 24.9 <= result < 29.9:
    bmi='over weight'
elif 29.9 <= result < 34.9:
    bmi= 'obese'
elif 34.9 <= result:
    bmi='extremly obese'
print('yor BMI is:',bmi)


























