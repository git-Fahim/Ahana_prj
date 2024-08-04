# 0 1 1 2 3 5 8 13 21

Num=int(input("Enter the number of fibunacci series print:"))


if Num ==1:
    print("0")

elif Num <1:
    print("Wrong number entered:")


i=1
First_value=0
Secound_value=1
Third_value=1


while i<=Num:

   # print("fibunacci series to print ")          # 0 1 1 2 3 5 8 13
    print(First_value)
    First_value=Secound_value
    Secound_value=Third_value

    Third_value=First_value+Secound_value

    i=i+1












