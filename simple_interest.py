# program to return simple interest
# principle, interest, time

# principle = float(input("Enter the principle: "))
# interest = float(input("Enter the interest: "))
# time = float(input("Enter the time in years: "))

# simple_interest = principle*(interest/100)*time

# print(f"Simple interest {simple_interest}")

def simple_interest(principle, rate, time):
   print(f"Simple Interest = {principle*rate/100*time:.2f}")
    
simple_interest(1000, 12, 2)


# def SI(P,R,T):
#     return P*R/100*T
# a=SI(600,5,3)
# print (a)
