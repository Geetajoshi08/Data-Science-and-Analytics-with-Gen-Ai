# This a single line comment
"""And this is a 
   multi line 
   comment!! """

# Variables...
a = 22            # int data type
b = 56.98         # float data type
c = 23j          # complex data type

name = "Geeta_123"   # String data type
answer = True        # boolean data type

#type checker...
print(type(a))
print(type(b))
print(type(c))
print(type(name))
print(type(answer))

# type conversion...
a = str(a)
b = int(b)

print("\nThe converted data types are : ")
print(type(a))
print(type(b))

# String indexing...
print("\n"+name[7], name[3])

# Formatted string...
# normal printing is like : print("my name is ", name, " and age is ", a), but formatted string can be writen as :
print(f"\nMy name is {name} and age is {a}")

# String slicing...
print("\n"+name[0:9:1])       # This is the default slicing where whole string gets printed!! 
print(name[0:9:2])

# Reversing string using string slicing...
print("\n"+name[::-1])

# Taking Input...
ques = input("\nHow was the output : good or okayokay ?? ")
print(f"The anwer was {ques}") 


