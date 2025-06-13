# Loops
# print HELLO WORLD with number notation and EVEN/ODD lines specification for 10 times

# for => if you got sequence (collection or array type objects)
# string, list, dict, tuple, range, set
# Syntax => for interative_var in object:
# size = "1111111111"
# range() => Gives the range for the specified number
# for i in range(1, 101):
#     isEven = (i % 2 == 0)
#     evOdStr = "Odd"
#     if isEven:
#         evOdStr = "Even"
#     print(f"{i}. Hello World - {evOdStr} line")


# while => condition based
# Syntax: while condition:
# i = 1
# limit = 10
# while i <= limit:
#     isEven = (i % 2 == 0)
#     evOdStr = "Odd"
#     if isEven:
#         evOdStr = "Even"
#     print(f"{i}. Hello World - {evOdStr} line")
#     i += 1


# Sum of first 10 numbers
# sum = 0
# for i in range(1,11):
#     sum += i
# print(f"The sum of is {sum}")

# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     i += 1
# print(f"The sum is {sum}")

# else block and control statements
# sum = 0
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(f"Current number is {i}")
#     sum += i
#     # if i == 5:
#     #     break
# else:
#     print(f"The sum of is {sum}")

# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     i += 1
# else:
#     print(f"The sum is {sum}")

#Practice
# #loop
# #for loop
# for i in range(1,101):
#     if i%2==0:
#         print(f"{i} number is even")
#     else:
#         print(f"{i} number is odd")
        
# #while loop
# i=0
# while i<100:
#     if i%2==0:
#         print(f"{i} number is even")
#     else:
#         print(f"{i} number is odd")
#     i+=1
    
sum=0
for i in range(1,11):
    if i==5:
        continue
    print(f"current number{i} :")
    sum+=i
print("sum :",sum)