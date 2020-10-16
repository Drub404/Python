number_of_days = int(input("Enter number of days"))
number_of_years = int(number_of_days / 365)
number_of_weeks = int(number_of_days % 365 / 7)

remaining_number_of_days = int(number_of_days % 365 % 7)
print("Years = {0}, Weeks = {1}, Days {2}".format(number_of_years, number_of_weeks, remaining_number_of_days))
