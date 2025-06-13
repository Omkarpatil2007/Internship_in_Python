
# Tuple
# Data Structure
# Multilpe values in a single variable
# Similar to array (dynamic array) => supports multiple datatype value assignment

# Denoted by ()
# numbers = (10,20,30,40,50,60)
# print(numbers)
# print(type(numbers))

# emp = ("John", 32, "Software Developer", True)
# print(emp)

# Ordered => They maintain the order of elements
# Immutable => Items cannot be changed after creation
# Duplication

# Access an item from tuple
# #           0           1           2       3           4
# brands = ("Apple", "Microsoft", "Google", "Amazon", "Oracle")
# #           -5          -4          -3          -2      -1
# print(brands[2])
# print(brands[-3])

# # Slicing => accesing a portion of tuple
# print(brands[1:4])
# print(brands[:3])
# print(brands[2:])

# Add a new item to tuple
#           0           1           2       3           4
# brands = ("Apple", "Microsoft", "Google", "Amazon", "Oracle")
#           -5          -4          -3          -2      -1

# Concatinating tuple with tuple
# brands += ("Meta",)
# print(brands)

# Changing existing elements in tuple
# brands[2] = "Alphabet"
# print(brands)

# Iterate over a tuple
# numbers = (1,2,3,4,5,6,7,8,9,10)
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)

# Tuple to List
# numbers = (1,2,3,4,5,6,7,8,9,10)
# print(numbers)
# numbers = list(numbers)
# print(numbers)
# numbers.append(1000)
# print(numbers)
# numbers = tuple(numbers)
# print(numbers)


# Dictionary
# Collection of items or elements
# key: value pair (mapping type)
# {}

# emp = ("John", 32, "Software Developer", True)
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# print(emp)

# Accessing a value from dictionary
# Does not supports indexing
# Values are accessed with the help of keys
# print(emp["position"])

# # Add new data to a dictionary
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# emp["salary"] = 3.5
# print(emp)
# # Update an existing value in dictionary
# emp["salary"] = 4.9
# print(emp)

# # Remove an element
# del emp['salary']
# print(emp)


# Methods
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# values()
# print("------------ Values ------------")
# print(emp.values())
# for v in emp.values():
#     print(v)

# # keys()
# print("------------ Keys ------------")
# print(emp.keys())
# for k in emp.keys():
#     print(k)

# items()
# print("------------ Items ------------")
# print(emp.items())
# for i in emp.items():
#     print(f"The '{i[0]}' key has the value of '{i[1]}'")
# for k,v in emp.items():
#     print(f"The '{k}' key has the value of '{v}'")

# update()
# emp.update({'salary': 3.5})
# print(emp)
# emp.update({'salary': 6.9})
# print(emp)

# PREPARE A DATA OF EMPLOYEE => ID, NAME AND EMAIL BY USER INPUTS AND DISPLAY THEM
# List of dictionaries

# # Ask the number of employees
# employees = []
# size = int(input("Enter number of employees: "))

# for i in range(1, size + 1):
#     print(f"========== Employee {i} details ==========")
#     eid = input("Enter employee id: ")
#     name = input("Enter employee name: ")
#     email = input("Enter employee email: ")
#     employees.append({
#         'id' : eid,
#         'name' : name.title(),
#         'email' : email.lower(),
#     })

# for emp in employees:
#     # Each "emp" is a dictionary
#     for key, value in emp.items():
#         print(f"{key.title()}: {value}")
#     print("---------------------------")


# Enter subject: English
# Enter marks for English: 39
# ....

# English => 39 => FAILED


#Practice
# #tuple
# numbers=(1,2,3,4,5,6)
# print(numbers)
# print(type(numbers))

# #acess tuple
# tup=("omkar","shubz","soham","rohit","vedant")
# print(tup[2])
# print(tup[2:-1])

# #concat tuple
# tup +=("atish",)
# print(tup)

# #sum of tuple
# tup=(12,13,24,35,56,65)
# sum=0
# for i in tup:
#     sum += i
# print("sum of tuple is:", sum)

# #tuple convert into list and change element 
# tup1=(13,23,45,66,54,65)
# print(tup1)
# list1=list(tup1)
# print(list1)
# list1.append(113)
# print(list1)
# tup2=tuple(list1)
# print(tup2)

#Dictionary
dict1={"id":12,
       "name":"omkar",
       "mo.no":1234
       }
print(dict1)

#acess value using key
print(dict1["id"])

dict1["email"]="omkar@123"
print(dict1)

#update dictionary
dict1["id"]=13
print(dict1)

#remove an element
del dict1["email"]
print(dict1)

#method
print("-----------------keys--------------------")
print(dict1.keys())
for k in dict1.keys():
    print(k)

print("----------------values------------------")
print(dict1.values())
for j in dict1.values():
    print(j)

print("--------------------items-------------------")
dict2={"id":12,
       "name":"omkar",
       "mo.no":1234
       }
print(dict2.items())
for k,v in dict2.items():
    print(k,v)
    
# #update
# dict1.update({"id":14})
# print(dict1)

# employess=[]
# size=int(input("enter number of employees :"))

# for i in range(1,size+1):
#     print(f"---------employees{i}details-----------")
#     eid=input("enter the id:")
#     name=input("enter the name :")
#     email=input("enter the email :")
#     employess.append({"id":eid,
#                       "e_name":name,
#                       "email":email
#                     })
    
# for emp in employess:
#     for key,value in emp.items():
#         print(f"{key.title()}:{value}")
      
# marks={}
# size=int(input("how many subject:"))
# for i in range(0,size):
#     print("-------------Student{i}Details-------------")
#     a=input("enter the subject :")
#     b=int(input("enter the sub marks :"))
#     if b<0 and b>100:
#         print("invalid marks")
#         exit()
#     marks.update({a:b})
#     print(marks)
    
# fails=0
# for j in marks.values():
#     if j<40:
#         fails+1
    
# if fails>0:
#     print("ATKT")
# if fails>=2: 
#     print("Failed")
# else:
#     sum=sum(marks.values()) 
#     print("total marks :",sum) 
    
#     per=sum/size
#     print("percentage :",per)
    
#     if per >= 75:
#         print("Grade A")
#     elif per >=60 and per < 75:
#         print("Grade B")
#     elif per >=40 and per < 60:
#         print("Grade C")
#     else:
#         print("failed..!")   


