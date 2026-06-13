# Number Sign Check...
num = int(input())
if num > 0 :
    print("Positive")
elif num == 0 :
    print ("Zero")
else : 
    print("Negative")


# Check for 'a' in string...
a = input()
if 'a' in a :
    print("a found")
else :
    print("a not found")


# Print the middle character of the string...
word = input()
middle = len(word)//2
if len(word)%2 != 0:
    print(word[middle])
else :
    print(word[middle-1])


# print thee 3rd character of the string...
word = input()

if len(word) >= 3:
    print(word[2])
else:
    print("Not enough characters")
