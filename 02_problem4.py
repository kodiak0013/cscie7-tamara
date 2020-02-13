# Homework 02_problem4
# Exercise to declare variables, perform calculations,
# 	use if, elif, and else statements

# store number in variable called year
year = 2020

# test if number is leap year by dividing by 400 evenly
# if it is, display 'x is a leap year'
# if not, test if number is leap year by dividing by 4 evenly
# if it is, display 'x is a leap year'
# if not, display 'x is not a leap year'
if year/400 == int(year/400):
	print(year,'is a leap year')
elif year/4 == int(year/4):
	print(year,'is a leap year')
else:
	print(year,'is not a leap year')