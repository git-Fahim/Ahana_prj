Name=input("enter the string:")




print(Name)

b=(Name[::-1])

if Name == b:
    print(b,"==",Name," is palindrome")

else:
    print(b,"!=",Name," is not palindrome")
