import re
email_condition = "^[a-z] + [\._]? + [a-z 0-9] + [@]/w + [.]/w {2,3}$"
user_input = input ("enter the email : ")

if re.search(email_condition,user_input):
    print('Right email')
else:
    print("wrong email")