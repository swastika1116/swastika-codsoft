import string
import random

s1=string.ascii_uppercase
 

s2=string.ascii_lowercase


s3=string.digits


s4=string.punctuation

print("                       WELCOME TO PASSWORD GENERATOR                              ")
pass_len=int(input("Enter the desired lenght of password: "))

print('''
1=strong password
2=average password
3=weak password''')

a=int(input("Choose complexity of password: "))


s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
    
random.shuffle(s)

password=""

if a==1:
    print(password)
    
    
    for i in range(pass_len):  
        password += random.choice(s1+s2+s3+s4)

if a==2:
    print(password)

    for i in range(pass_len):
        password += random.choice(s1+s3)

    
if a==3:
    print(password)

    for i in range(pass_len):
        password += random.choice(s1)
        
print(password)
