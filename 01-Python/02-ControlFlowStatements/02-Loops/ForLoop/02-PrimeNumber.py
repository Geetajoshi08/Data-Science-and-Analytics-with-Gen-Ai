# prime numbers...
num = int(input("Enter first number : "))

if num <=1:
       print("Number is not prime")
else:
     for i in range(2,num):
        if num % i == 0 :
              print("Not a prime !!")
              break
     else:
        print("Is prime!!")
