
name = "Geeta_123"   # String data type
a = 22 

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