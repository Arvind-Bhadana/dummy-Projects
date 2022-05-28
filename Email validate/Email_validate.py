email = input("enter the email address : ")
k,j,d=0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3] =='.') ^ (email[-4]=='.'):
                for i in email:
                    if i== i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d=1


                if k==1 or j==1 or d==1:
                    print('invlaid emial plese check and try again ')
                    print("Hint : Only these charactor are allow '.','_','@'")
                    
            else:
                print('invlaid email ')
                print("Hint : Use '.in' or '.com' only at the end of email address") 
        else:
            print('invlaid email ')
            print("Hint: you should include '@' in then mail address only one time")

    else:
        print('invalid email ')
        print('Hint: First letter must be alphbate')
else:
    print("invalied email")
    print('Hint: email must contain more then 6 charrectors')