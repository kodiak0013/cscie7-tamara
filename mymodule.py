# Homework 05_problem1_module
# Exercise to write module with function to count number of X within
# 	sequence

# store dictionary in variable called my_dict
my_dict = dict()

# function to count letter in variable called consonant, within sequence
#   in variable called content
def count_letter(consonant, content):
    # Loop through each letter in content variable
    for letter in content:
        # test if letter already exists in dictionary
        # if it does not, set value of letter key equal to 1
        # if it does, set value of letter key equal to value of itself plus 1
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] = my_dict[letter] + 1
    # display letter and its count
    print(consonant, my_dict[consonant])
    # clear dictionary of keys
    my_dict.clear()


