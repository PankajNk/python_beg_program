


h =input("enter the hours ")

try :
    float(h)>=0
except:
    print("Please ,enter numeric input")
    print("\n")
    h =input("enter the hours ")

rate_h = input("enter the rate per hour ")

try :
          float (rate_h)>=0
except :
          print("Error")
          print("\n")
          rate_h =input("enter the rate per hour ")


rate_h= float(rate_h)
h= float(h)
if h < 40 :
    gross_pay = h * rate_h
else:
    gross_pay = (40 * rate_h ) + ((h-40)*1.5 * rate_h)
                # 40hrs + extra work 



print("Gross Pay ",gross_pay)
