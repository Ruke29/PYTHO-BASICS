#FLOAT INTO INT, INT INTO FLOAT#
A= int(input("ENTER  NO:"))
print(A, type(A))
F = "FLOAT"
I = "INT"
SWAP= input("DO YOU WANT TO CHANGE:FLOAT/INT=")
if SWAP=="F":
    A=float(A)
    print(A, type(A))
elif SWAP=="I":
    A=int(A)
    print(A, type(A))
else:
    print("THANKS")
