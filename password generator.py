import string
import random

s1=string.ascii_uppercase


s2=string.ascii_lowercase


s3=string.digits


s4=string.punctuation

print("                       WELCOME TO PASSWORD GENERATOR                              ")
pass_len=int(input("Enter the desired lenght of password: "))

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))


random.shuffle(s)



print("YOUR PASSWORD IS: ")
print("".join(s[0:pass_len]))
