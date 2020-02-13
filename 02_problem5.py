# Homework 02_problem5
# Exercise to declare variables, capture UDF, perform calculations,
# 	use if, elif, and else statements

# prompt user to enter number, read in number, store in variable
# 	called my_answer
my_answer = input('Please enter a number: ')

#
# test user entry is valid entry
#

# test if user entry is positive integer
# if not, display 'x is not a valid year'
# if it is, test if number is 0 or negative
# if it does, display 'x is not a valid year'
if not my_answer.isdigit():
	print(my_answer,'is not a valid year')
elif int(my_answer) < 1:
	print(my_answer,'is not a valid year')
else:

	# store integer in variable called my_year
	my_year = int(my_answer)

	# test if number is leap year by dividing by 400 evenly
	# if it is, display 'x is a leap year'
	# if not, test if number is leap year by dividing by 4 evenly
	# if it is, display 'x is a leap year'
	# if not, display 'x is not a leap year'
	if my_year/400 == int(my_year/400):
		print(my_year,'is a leap year')
	elif my_year/4 == int(my_year/4):
		print(my_year,'is a leap year')
	else:
		print(my_year,'is not a leap year')