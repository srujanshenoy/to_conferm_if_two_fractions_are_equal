print("N1/D1 =? N2/D2")
X = float(input("N1: "))
Y = float(input("D1: "))

while Y == 0:
    print("oops! Denominator can not be 0!)
    Y = float(input("D1: "))

Z = float(input("N2: "))
W = float(input("D2: "))

while W == 0:
    print("oops! Denominator can not be 0!")
    W = float(input("D2: "))

P1 = X*W
P2 = Y*Z
if P1 == P2:
    print("the fractions are equal.")
else:
    print("the fractiions are not equal.")
