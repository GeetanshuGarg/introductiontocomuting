#Ques1
string="Python is a case sensitive language"
print(len(string))
print(string[::-1])
new_string=string[10:]
print(new_string)
edited_string="object oriented"
print(new_string.replace("case sensitive language","object oriented"))
print(string.index("a"))
print(string.replace(" ",""))


#Ques2
Name=input("Enter your name: ")
SID=input("Enter your SID: ")
department_name=input("Enter department name: ")
CGPA=input("Enter your CGPA: ")
print("Hey,%s Here!"%Name)
print("My SID is %s"%SID)
print("I am from %s department"%department_name,"and my CGPA is %s"%CGPA)



#Ques3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)




#Ques4
a=input("Enter first number: ")
b=input("Enter second number: ")
c=input("Enter third number: ")
if(a>=b) and (a>=c):
    largest=a
elif(b>=a) and (b>=c):
    largest=b
else:
    largest=c
    print("Three the largest number: ",largest)




#Ques5
a=str(input(("Type the string: ")))
b="Yes"
c="No"
if(a.find("name")>0):
    observation=b
else:
    observation=c
print(observation)




#Ques6
a=int(input("Enter length of first side: "))
b=int(input("Enter length of second side: "))
c=int(input("Enter length of third side: "))
d="No"
e="Yes"
if (a+b>c and a+c>b and b+c>a) :
    observation=e
else:
    observation=d
print(observation)
