
#giving Grades according to score

print("Enter score btw 0.0 to 1.0")
s = float(input("enter the Score "))


if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
else:
    print("BAD SCORE/ENTER CORRECT SCOPE ")
          
