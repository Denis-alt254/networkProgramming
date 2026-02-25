# program to return simple interest
# principle, interest, time

principle = float(input("Enter the principle: "))
interest = float(input("Enter the interest: "))
time = float(input("Enter the time in years: "))

simple_interest = principle*(interest/100)*time

print(f"Simple interest {simple_interest}%")