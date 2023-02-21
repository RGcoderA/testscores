# This program gets a numeric test score from the user and displays the corresponding letter grade.
# the program uses a if and else statement, as it gets the input from the users as they type there score.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = (input('Enter your test score: '))
 
# Determine the grade.
# The error which I fix are the score putting them in quotes and the number that the only error
if score >= "90":
    print('Your grade is A.')
else:
    if score >= "80":
        print('Your grade is B.')
    else:
        if score >= "70":
            print('Your grade is C.')
        else:
            if score >= "60":
                print('Your grade is D.')
            else:
                print('Your grade is F.')

