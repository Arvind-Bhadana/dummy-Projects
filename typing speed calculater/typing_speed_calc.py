from re import U
from time import *
import random 

def mistaks(givn_text,user_input):
    error = 0
    for i in range(len(givn_text)):
        try:
            if givn_text[i] != user_input[i]:
                error = error+1
        except:
            error = error+1
    return error

def speed(time_s,time_e,user_input):
    delay = time_e-time_s
    delay = round(delay,2)
    type_speed = len(user_input)/delay
    return round(type_speed)
    
test =[" kept in abeyance till the central government ",
"A taking into account the present order as well as the clear stand taken by Union of India.",
"this is a sample string for typing"]

text1 = random.choice(test)
print("Typing speed test is about to start if you are ready press 'Y' else pess any key")
print()
ready = input()
ready = ready.upper()
print()

if ready == 'Y':
    print(text1)
else:
    print('Be prepaired next time')
time1 = time()
text2 = input("Enter now : ")
time2 = time()


print("Your Speed is : ",speed(time1,time2,text2),' sec./word')
print('Numbers of errors : ', mistaks(text1,text2))