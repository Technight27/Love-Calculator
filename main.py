
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
m=name1+name2
n=m.lower()

a=n.count("t")
b=n.count("r")
c=n.count("u")
d=n.count("e")
e=a+b+c+d
f=n.count("l")
g=n.count("o")
h=n.count("v")
i=n.count("e")
j=f+g+h+i
z=str(e)+str(j)
k=int(z)
if k<10 or k>90:
  print(f"Your score is {k}, you go together like coke and mentos.")
elif k>40 and k<50:
  print(f"Your score is {k}, you are alright together.")
else:
  print(f"Your score is {k}.")




