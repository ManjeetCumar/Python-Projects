''' conditions for a valid email
    a-z alphabets lower case, first case only alpha
    0-9 digits
    . _ only once
    @ only once
    . after @ shd be on 2nd or 3rd position onward
'''
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"

user_email = input('Enter Your Email :')

if re.search(email_condition, user_email):
    print("Right Email ")
else:
    print("Wrong Email")