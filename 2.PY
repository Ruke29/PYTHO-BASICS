#SWAP NUMBERS#
A= int(input("ENTER 1ST NO:"))
B= int(input("ENTER 2ND NO:"))
print("BEFORE SWAP:", A,B)
SWAP= input("DO YOU WANT TO SWAP:Y/N=")
if SWAP=="Y":
    A,B=B,A
    print("AFTER SWAPPING:",A,B)
elif SWAP=="N":
    print("og values:", A,B)
else:
    print("THANKS")
