#Ques1

def Tower_of_Hanoi(n,source,destination,auxiliary):
    if n==1:
        print("Move disc 1 from source",source,"to destination",destination)
        return
    Tower_of_Hanoi(n-1,source,auxiliary,destination)
    print("Move disk",n,"from source",source,"to destination",destination )
    Tower_of_Hanoi(n - 1, auxiliary, destination, source)
n=3
Tower_of_Hanoi(n,"A","C","B")


#Ques2
from math import factorial

# Using Iteration
n = int(input("Enter number of rows: "))
for i in range(n):
    print(end=(n-i)*" ")
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

#Using recursion

def pascaltriangle(num):
    if num == 1:
        return [[1]]
    else:
        result = pascaltriangle(num-1)
        current_row = [1]
        previous_row = result[-1]
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")
    for j in i:
        print(j, end =" ")
    print()


#Ques3
a=int(input("Type an integer: "))
b=int(input("Type another integer: "))
remainder=a%b
quotient=a/b
print("a) The remainder function is callable: ",callable(quotient))
print("The quotient function is callable: ",callable(remainder))
if quotient==0:
    print("b) Quotient is zero")
else:
    print("b) Quotient is non-zero")
if remainder==0:
    print("Remainder is zero")
else:
    print("Remainder is non-zero")
list=[]
list.append(int(remainder+4))
list.append(int(remainder+5))
list.append(int(remainder+6))
list.append(int(quotient+4))
list.append(int(quotient+5))
list.append(int(quotient+6))
list1=[(i)for i in list if i>4]
print("c) list of numbers greater than 4: ",list1)
set=set(list1)
print("d) set is:",set)
frozen_set=frozenset(set)
print("e) Immutable set: ",frozen_set)
c=max(set)
print("f)",c)
print("  hash value: ",int(hash(c)))


#Ques4
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def __del__(self):
        print("Object destroyed")
s=Student("Geetanshu Garg",21103045)
print("The name of the student is %s and his/her roll number is %d" % (s.name,s.roll_number))
del s


#Ques5
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def record(self):
        print("Name is",self.name,"and salary is",self.salary)

e1=Employee("Mehak","40,000")
e2=Employee("Ashok","50,000")
e3=Employee("Viren","60,000")
e1.record()
e2.record()
e3.record()
e1.salary="70,000"
print("\nSalary of Mehak updated")
e1.record()
del e3
print("Record of Viren deleted")




#Ques6

a=str(input("George enter a word: "))
list1=[i for i in a]
sorted_list1=sorted(list1)
print("List1: ",list1)
b=str(input("Barbie enter a word using letters in List1: "))
list2=[j for j in b]
sorted_list2=sorted(list2)

if sorted_list1 != sorted_list2:
    print("The Words Aren't Matching, Friendship Is Fake!")
else:
    print("Type Y for Yes and N for No")
    Question = input("Is the word meaningful: ")
    if Question=="Y":
        print("Friendship is True")
    elif Question =='N':
        print("Meaningless Word , Friendship Is Fake!")
    else:print("Error")