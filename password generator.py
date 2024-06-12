import string
import random

s1=string.ascii_uppercase


s2=string.ascii_lowercase


s3=string.digits


s4=string.punctuation

print("                       WELCOME TO PASSWORD GENERATOR                              ")
pass_len=int(input("Enter the desired lenght of password: "))

a=print("Choose complexity of password: ")

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

n_UPPERCASE=int(input("HOW MANY UPPERCASE DO YOU WANT IN YOUR PASSWORD: "))
n_LOWERCASE=int(input("HOW MANY LOWERCASE DO YOU WANT IN YOUR PASSWORD: "))
n_DIGIT=int(input("HOW MANY DIGITS DO YOU WANT IN YOUR PASSWORD: "))
n_PUNTUATION=int(input("HOW MANY PUNCTUATIONS DO YOU WANT IN YOUR PASSWORD: "))
password=""

for i in range(1,n_UPPERCASE+1):
    char= random.choice(s1)
    password += char
    
for i in range(1,n_LOWERCASE+1):
    char= random.choice(s2)
    password += char
for i in range(1,n_DIGIT+1):
    char= random.choice(s3)
    password += char

for i in range(1,n_PUNTUATION+1):
    char= random.choice(s4)
    password += char

print(password)


print("YOUR PASSWORD IS: ")
print("".join(s[0:pass_len]))
