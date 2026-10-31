principle_amount_in_rupees=float(input("Enter principle amount in rupees: "))
Rate_of_interest_in_percent=float(input("Enter rate of amount in percent: "))
time_in_year=float(input("Enter time in year: "))
simple_interest_in_rupees=(principle_amount_in_rupees*Rate_of_interest_in_percent*time_in_year)/100
print(f"simple interest is {simple_interest_in_rupees} rupees")