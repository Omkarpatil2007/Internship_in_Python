# List
# Data Structure
# Multilpe values in a single variable
# Similar to array (dynamic array) => supports multiple datatype value assignment

# Denoted by []
# numbers = [10,20,30,40,50,60]
# print(numbers)
# print(type(numbers))

# emp = ["John", 32, "Software Developer", True]
# print(emp)

# Ordered => They maintain the order of elements
# Mutable => Items can be changed after creation
# Duplication

# Access an item from list
#           0           1           2       3           4
# brands = ["Apple", "Microsoft", "Google", "Amazon", "Oracle"]
#           -5          -4          -3          -2      -1
# print(brands[2])
# print(brands[-3])

# Slicing => accesing a portion of list
# print(brands[1:4])
# print(brands[:3])
# print(brands[2:])


# Add a new item to list
#           0           1           2       3           4
# brands = ["Apple", "Microsoft", "Google", "Amazon", "Oracle"]
#           -5          -4          -3          -2      -1

# Concatinating list with list
# brands += ["Meta"]
# print(brands)

# Use the append() to add new element to the list
# brands.append("Meta")
# print(brands)


# Add element to a specific index
# use insert() method
# brands.insert(8, "Meta")
# print(brands)


# Changing existing elements in list
# brands[2] = "Alphabet"
# print(brands)


# Remove an element from the list
#           0           1           2       3           4
# brands = ["Apple", "Microsoft", "Google", "Amazon", "Oracle"]
#           -5          -4          -3          -2      -1

# del keyword
# del brands[1]

# Using remove() method
# rmItem = "Googlee"
# if rmItem in brands:
#     brands.remove(rmItem)
# else:
#     print(f"No item with value '{rmItem}'")
# print(brands)


# Length of a list
# listCount = len(brands)
# print(listCount)


# Iterate over a list
# numbers = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)


# Empty list
# numbers = []
# for i in range(5):
#     num = input("Enter number: ")
#     if (num.isnumeric()):
#         numbers.append(int(num))

# sum = 0
# if len(numbers) > 0:
#     for n in numbers:
#         sum += n
#     print(sum)


# Methods
langs = ["Java", "Python", "C#", "PHP", "C#"]

# pop()
# removedLang = langs.pop(2)
# print(f"The lang removed is {removedLang}")
# print(langs)

# index()
# print(langs.index("C#"))

# count()
# print(langs.count("C#"))

# reverse()
# langs.reverse()
# print(langs)


# # sort()
# langs.sort()
# print(langs)

# langs.sort(reverse=True)
# print(langs)

#Practice
# #task
# marks=[]
# n=int(input("how many subject :"))
# for i in range(n):
#     mark=int(input(f"enter the sub{i+1} :"))
#     if mark<0 or mark>100:
#         print("invalid marks")
#         exit()
#     marks.append(mark)

# fails=0
# for m in marks:
#     if m<40:
#         fails+1

# if fails>2:
#     print("failed")
# if fails>0:
#     print("ATKT") 
# else:
#     sum=sum(marks)
#     print("total  sum :",sum)
   
#     per=sum/n
#     print("percentage :",per)   
    
#     if per >= 75:
#         print("Grade A")
#     if per >=60 and per < 75:
#         print("Grade B")
#     if per >=40 and per < 60:
#         print("Grade C")
#     else:
#         print("failed..!")  
              
              
#List
# num=[1,2,3,4,5,76,9]
# print(num)

#acess an item for list
# name=["omkar","vedant","shubz","rohit","soham"]
# print(name[2])

#slicing 
# name=["omkar","vedant","shubz","rohit","soham"]
# print(name[2:4])

#concat
# name=["omkar","vedant","shubz","rohit","soham"]
# name+=["virat"]
# print(name)

#replce element in list
# name=["omkar","vedant","shubz","rohit","soham"]
# name[3]="om"
# print(name)

#del statement
# del name[2]
# print(name)

#iterate over a list and sum
# num=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in num:
#     sum+=i
#     print(i)
# print(sum)
    
#using romove method
# name=["omkar","vedant","shubz","rohit","soham"]
# a="omkar"
# if a in name:
#     name.remove(a)
# else:
#     print(f"no item with value{name}")
# print(name)

# num=[]
# for i in range(5):
#     a=input("Enter the number:")
#     if(a.isnumeric()):
#         num.append(int (a))

# sum=0
# if len(num)>0:
#     for n in num:
#         sum+=n
#     print(sum)         
            
#methods
langs=["c++","python","java","PHP","C#"]

print(langs.pop(2))

print(langs.index("python"))

print(langs.count("python"))