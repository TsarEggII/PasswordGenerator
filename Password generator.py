import random

print(Welcome:=input("Welcome to the password generator, press any button and then enter to continue!"))
print(Name:=input("What is your name? It can be real or fake."))
print(Country:=input("Where are you from? It can be real or fake."))

def NameScramb(n):
    pt1=0
    ran1=0
    for i in range(len(str(n))):
        ran1=random.randint(1,1000)
        pt1+=ran1
    return pt1

def CountryScramb(c):
    pt2=0
    ran2=0
    for i in range(len(str(c))):
        ran2=random.randint(1,1000)
        pt2+=ran2
    return pt2

Password=str(NameScramb(Name)) + str(CountryScramb(Name))

print(Password)