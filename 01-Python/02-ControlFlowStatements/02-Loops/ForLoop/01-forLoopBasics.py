# for loop in python...
# user input...
n = int(input("Tell the number for table : "))
for i in range(n,(n*10)+1,n) :
    print(i)

# loop in string...
s = "How are you !"
for i in s:
    print(i)

# 2nd way to apply loop in string...
s = "Hello I am Geeta !"
for i in range(0,len(s),1):
    print(s[i])

# print user input n times...
s = input("Enter any word : ")
a = int(input("Enter the amount you want the word to be displayed : "))
for i in range(a):
    print(s) 

# Sum of user given digits...
b = (input("Enter any number : "))
sum = 0
for i in range(len(b)):
    sum = sum + int(b[i])
print("Sum is : ",sum)

# Sum of odd and even numbers in a range
num = int(input("Enter your range : "))

even_sum = 0
odd_sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of even numbers is : {even_sum}")
print(f"The sum of odd numbers is : {odd_sum}")

