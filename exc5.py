

h = float(input("enter the hours "))

rate_h = float(input("enter the rate per hour "))

if h < 40 :
    gross_pay = h * rate_h
else:
    gross_pay = (40 * rate_h ) + ((h-40)*1.5 * rate_h)
                # 40hrs + extra work 



print("Gross Pay ",gross_pay)
