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
