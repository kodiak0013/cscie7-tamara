# Homework 03_problem1

# store number in variables called a and b and set their values to 1 and 3 respectively
a = 1
b = 3

# if a equals the whole integer of, b divided by 2, then set b variable equal to value of a
if a == b // 2:
    b = a

# if b equals the remainder of, a multiplied by 2 plus 1 all divided by 2 then set a variable a
#   equal to 2 times value of b
if b == (2 * a + 1) % 2:
    a = 2 * b

# set a variable equal to value of a plus value of b
a = a + b

# set b variable equal to remainder of value of a divided by 3
b = a % 3
