# Homework 05_problem1
# Exercise to use module function to count number of X within
# 	sequence

# Import module called mymodule.py
import mymodule
import os

# store string in variable called filename and set equal to 'ecoli.fasta'
filename = 'ecoli.fasta'

# check if file exists
if not os.path.exists(filename) :
    print('Error:',filename,"doesn't exist")
else:

    # split filename into segments delimited by '.'
    # store string in variable called name and extension set equal to first part
    #   of split and second part respectively
    name, extension = filename.split('.')

    # store dictionary in variable called my_dict
    my_dict = dict()

    # check if uppercase of extension variable equals 'FASTA'
    #   if it does not, display error message
    #   if it does, continue code
    if not extension.upper() == 'FASTA':
        print('Error: file extension is not .fasta')
    else:

        # store file object in variable called fin
        fin = open(filename,'r')

        # store read contents of fin variable in variable called content
        content = fin.read()

        # store list in variable called my_list and populate elements with 'A','C','G','T'
        my_list = ('A','C','G','T')

        # Loop through each index in list my_list
        #   store index of list in variable called my_letter
        #   store content variable in variable called my_content
        #   call function called count_letter from mymodule module
        for i in range (0,len(my_list)):
            my_letter = my_list[i]
            my_content = content
            mymodule.count_letter(my_letter, my_content) #call function

        # Close file
        fin.close()