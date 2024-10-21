#CHECK DIGITS#
NUM = int(input("ENTER DIGIT:"))
if NUM>=0 and NUM<=10:
    print("ITS A SINGLE DIGIT")
elif NUM>=10 and NUM<=100:
    print("ITS A DOUBLE DIGIT")
elif NUM>=100 and NUM<=1000:
    print("ITS A TRIPLE DIGIT")
else:
    print("ITS A INVALID NUMBER")