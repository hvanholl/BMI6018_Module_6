#### ---------- Hannah Van Hollebeke ---- u069788484 ----- 20220108 ---------####

# --------------------------  1.a -----------------------------------------------
# Using the print() function only, get the wrong_add_function to print out where
# it is making a mistake, given the expected output for ex, "we are making an error 
# in the loop", which you would put near the loop. 
# Structure the print() statement to show what the expected output ought to be
# via f-strings: ie "The correct answer is supposed to be: 

# To get the correct output of [2,3,4], the function needs to add each element of arg1 to the corresponding element in arg2
print('2a')
def wrong_add_function(arg1,arg2):
    '''
    The function takes in two lists of integers, then it adds all of arg2 to each item of arg1.
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]    #whereas the expected correct answer is, [2,3,4]
        #Parameters --- arg1 : list of integers; arg2 : list of integers.
        #Returns --- arg1 : Elements of arg1, with each element having had the contents of arg2 added to it.
    '''
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])
        print(f'We are making an error in the loop: arg_2_sum value for outer index {arg1_index} is: {arg_2_sum}')
        print(f'The correct answer is supposed to be: {arg1[arg1_index] + arg2[arg1_index]}')   # arg1 at current index plus arg2 at arg1 current index      
        arg1[arg1_index] = arg_2_sum
        arg1_index+=1  
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_output = wrong_add_function(arg1, arg2)
print(f'Wrong_add_function output {wrong_output}')

# --------------------------------- 1.b -----------------------------------------
# Then, changing as little as possible, modify the function, using the same 
# general structure to output the correct answer. Call this new function 
# correct_add_function() 

print('2b')
def correct_add_function(arg1,arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index] # adding arg1 and arg2 at current index and assigning arg1 index to this value
        print(f'arg1 is now: {arg1} at arg1_index {arg1_index}')  # Print new value of arg1 and the current index
        print(f'arg2 is still: {arg2}')
        arg1_index += 1 
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_output = correct_add_function(arg1, arg2)
print(f'correct_add_function output is {correct_output}')


#### ---------------- 2.a ----------------------------------------------------------- ####
# Update the numeric section of the function with your changes from 1 for both 2.b and 2.c
print('No output for 2a because it is incorporated in 2b and 2c')

# 2.b
# Without modifying the string section code itself or the input directly, 
# write a try, except block that catches the issue with the input below and 
# returns an error message to the user, in case users give invalid inputs,
# (for example an input of ["5","2", 5])
# : "Your input argument [1 or 2] at element [n]
# is not of the expected type. Please change this and rerun. Name this function 
# exception_add_function()

print('2b')
def exception_add_function(arg1,arg2):      # copy and pasted the code at the bottom of assignment and updated the numeric section to give the output of 1b.

#numeric section
    try:
        sum(arg1 + arg2)    # This should raise a TypeError if the data types are mixed data types.
    except TypeError:
        # It was not clear to me what the expected type is supposed to be so I just decided to do it this way. 
        str_count = [type(arg) for arg in arg1 + arg2].count(str)   # counts the args in both arguments that are strings
        int_count = [type(arg) for arg in arg1 + arg2].count(int)   # counts the args in both arguments that are integers
        exp_type = str if str_count >= int_count else int           # define expected type as the type that is the majority to catch the odd ones out. Arbitrarily choose strings to be expected if the counts are the same.
        #print(exp_type)
        for i, val in enumerate(arg1):   # iterate through arg1 
            if type(val) != exp_type:    # If the value at the current index is not the previously defined expected type, print the following line. This will therefore print at every index this is encounted if there happened to be more than one.
                print(f'Your input argument 1 at element {i} is not of the expected type. Please change this and rerun.')
        for i, val in enumerate(arg2):   # repeat for arg2
            if type(val) != exp_type:
                print(f'Your input argument 2 at element {i} is not of the expected type. Please change this and rerun.')
    if sum([type(i)==int for i in arg1])==len(arg1) and \
        sum([type(i)==int for i in arg2])==len(arg2):
            print(f'{arg1, arg2}')
            arg1_index = 0
            while arg1_index < len(arg1):
                arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index] # adding arg1 and arg2 at current index and assigning arg1 index to this value
                arg1_index+=1 
            return arg1
#string section. Did not change.
    elif sum([type(i)==str for i in arg1])==len(arg1) and \
        sum([type(i)==str for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
            return arg1
                   
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
print(exception_add_function(arg_str_1,arg_str_2))


# 2.c
# Without modifying the string section code itself or the input directly, 
# write a try, except block that catches the issue with the input below and 
# gets it to process via the string section. IE, do not, outside the function,
# change the values of arg_str_1 or arg_str_2. Name this function 
# correction_add_function(), i.e you will not be updating the wrong_add_function,
# you will simply handle the error of wrong inputs in a seperate function, you want
# the wrong_add_function to output its current result you are only bolstering the 
# function for edge cases .

print('2c')
def wrong_add_function(arg1, arg2): # function defined is unchanged for this section except the numeric section is updated as per 2a.
#numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and \
        sum([type(i)==int for i in arg2])==len(arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index] # adding arg1 and arg2 at current index and assigning arg1 index to this value
                arg1_index+=1 
            return arg1
#string section
    elif sum([type(i)==str for i in arg1])==len(arg1) and \
        sum([type(i)==str for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
            return arg1

def correction_add_function(arg1,arg2): # define function to catch error and run call the other function within this function
    try:
        sum(arg1 + arg2)  # Raise an error if the data types are mixed.
    except TypeError:
        arg1 = [str(arg) for arg in arg1]   # convert each value to string in arg1 
        arg2 = [str(arg) for arg in arg2]   # same for arg2 
    return wrong_add_function(arg1, arg2)   # return a call to the wrong add function
    
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
print(correction_add_function(arg_str_1,arg_str_2))