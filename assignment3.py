#QUESTION 1

a=str(input("Enter a string: "))
if a.find(" ")>0:
   c=a.split()
   for i in c:
      print(i,c.count(i))
else :
   for z in a:
      print(z,a.count(z))


#QUESTION 2

day = int(input("Input a day [1-31]: "))
month = int(input("Input a month [1-12]: "))
year = int(input("Input a year: "))

#checking if it is a leap year
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
#length of month
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyy] %d/%d/%d" % (day, month, year))



#QUESTION 3
#Creating a list of tuples having first element as number and second as square of the number

print("Type Y for yes and N for no: ")
list=[]
while (True):
    Question = input("Do you want to enter a number: ")
    if Question=="Y":
       number = int(input("Enter a number: "))
       list.append(number)
    elif Question=="N":
       break
    else:
        print("Error")

list_of_tuples = [(i,i**2)for i in list]
print(list_of_tuples)

#QUESTION 4

Grade_points=int(input("Enter your grade points: "))
if Grade_points<4:
    print("Error")
elif Grade_points==4:
    print("Your Grade is 'D' and Poor Performance")
elif Grade_points==5:
    print("Your grade is 'C' and Below Average Performance")
elif Grade_points==6:
    print("Your grade is 'C+' and Average Performance")
elif Grade_points ==7:
    print("Your grade is 'B' and Good Performance")
elif Grade_points ==8:
    print("Your grade is 'B+' and Very Good Performance")
elif Grade_points ==9:
    print("Your grade is 'A' and Excellent Performance")
elif Grade_points==10:
    print("Your grade is 'A+' and Outstanding Performance")


#QUESTION 5
a=("ABCDEFGHIJK")
count=11
while count>0:

    print(a[:count])
    count=count-1

#QUESTION 6
name = input("Enter your name: ")
SID = int(input("Enter your SID: "))
dict={SID:name}
while (True):
         Question = input("Do you want to enter your details,type Y for yes and N for no\n")
         if  Question=="Y":
             name = input("Enter your name: ")
             SID = int(input("Enter your SID: "))
             dict[SID]=name
         elif Question=="N":
             break
         else:print("error")
print(dict)
sorted_by_name={k:v for k,v in sorted(dict.items(),key=lambda v: v[1])}
print(sorted_by_name)

sorted_by_SID= {k:v for k,v in sorted(dict.items())}
print(sorted_by_SID)


#finding student's name using SID
while (True):
    Question2=input("Do you want to search for name of the student using SID;type Y for yes and N for no\n")
    if Question2 == "Y":
        find = int(input("Enter your SID/n"))
        print(dict[find])
    else:break
         

#QUESTION 7

def febonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)
number=int(input("Enter a number: "  ))
print(febonacci(number))

#QUESTION 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}


Set_A = (Set1|Set2)-(Set1&Set2)
print("a) ", Set_A)

Set_B = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("b) ", Set_B)

Set_C= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("c) ",Set_C)

Set_D = set()
for i in range(1, 11):
    if i not in Set1:
        Set_D.add(i)
print("d) ", Set_D)

Set_E = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Set_E.add(i)
print("e) ", Set_E)

