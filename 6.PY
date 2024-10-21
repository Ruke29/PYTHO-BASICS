#AREA CALCULATOR#
print("CHOOSE AREA 1= CIRCLE")
print("CHOOSE AREA 2= SQUARE")
print("CHOOSE AREA 3= TRIANGLE")
c= int(input("ENTER AREA :"))
if c==1:
    R= int(input("ENTER RADIUS:"))
    AREA=3.14*R*R
    print("AREA OF CIRCLE IS:",AREA)
if c==3:
    L= int(input("ENTER L:"))
    B= int(input("ENTER B:"))
    H= int(input("ENTER H:"))
    AREA = 0.5*L*B*H
    print("AREA OF CIRCLE IS:",AREA)
if c==2:
    S=int(input("ENTER SIDE:"))
    AREA= S*S
    print("AREA OF SQUARE IS:",AREA)
else:
    print("THANKS")

