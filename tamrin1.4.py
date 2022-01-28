
name=input('inter your first name: ')
famil=input('inter your last name: ')
scor_1=float(input('inter your scor_1: '))
scor_2=float(input('inter your scor_2: '))
scor_3=float(input('inter your scor_3: '))
avrge=(scor_1 + scor_2 + scor_3 )/3
if 20>= scor_1>=0 and 20>= scor_2>=0 and 20>= scor_3>=0:
    avrge=(scor_1 + scor_2 + scor_3 )/3
    if avrge >=  17:
        grade='aaly'
    elif 12 <= avrge <17:
        grade='mamooly'
    elif 12> avrge:
        grade='mardood'
    print(name,famil,'your avrge is:',f'{avrge:.2f}','you are:',grade)
else:
    print('error!\n score isnot between 0_20')


























