# if-else statements...
age = int(input("Enter your age : "))

if age >= 18:
    print(f"As your age is {age}, you can vote!!")
else: 
    print(f"As you are below 18 years, you cannot vote!!!")

# pass : if you don't want to return anything in a condition, you can use pass...
age = int(input("Enter your age : "))
if age >= 18:
    pass
else: 
    print(f"As you are below 18 years, you cannot vote!!!")

# Ternery opetations : <condition> ? <true value> : <false value>
age = int(input("Enter your age for finall check : "))  
print(f"As your age is {age}, you can vote!!") if age >= 18 else print(f"As you are below 18 years, you cannot vote!!!")

# else-is ladder...
salary = int(input("Enter your salary : "))
if salary <= 20000:
    print ("You are underpaid !!")
elif salary >= 20000 and salary <=60000 :
    print("You are paid well !!")
else :
    print("You are rich !!")


