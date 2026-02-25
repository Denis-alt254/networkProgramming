# program to compute if amount is greater tha 5000 give you discount of 10%
# if 1000-4999 discount of 5%
# less than 1000 no discount

amount = int(input("Enter the amount: "))

if amount >= 5000:
    result = (amount*0.9)
    print("Discount is 10%")
elif amount >= 1000:
    result = (amount*0.95)
    print("Discount is 5%")
else:
    result = (amount*1)
    print("NO discount")

print(f"Result = {result}")