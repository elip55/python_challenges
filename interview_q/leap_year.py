
# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5
# The year is a leap year (it has 366 days)
# The year is not a leap year (it has 365 days)


# Basic input to check for leap year
year = int(input("Input the year."))

# Calculations and output 
if year % 4 != 0: 
    print(f"{year} is not a leap year.")
elif year != 100: 
    print(f"{year} is a leap year.")
elif year != 400: 
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year.")