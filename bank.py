
Balance=10000

msg="""
enter 1: To Withdraw

enter 2: To credit the amount

enter 3: To view the balance amount

enter 4: To Exit """
    
def withdraw():

    A=int(input("emter the amount to withdraw:"))

    if A<=0:

        print("enter the positive number:")
        exit()

    elif Balance > A:

        print("Amount successfully withdraw")

        return Balance-A

def credit():
    
    B=int(input("emter the amount to Credit:"))

    if B<=0:

        print("enter the positive number:")

    else:
       return Balance+B

 
while True:
    print(msg)

    ch=int(input())   
    if ch==1:

       Balance= withdraw()
       print("remaining balance:",Balance)

    if ch==2:
        Balance=credit()
        print("remaining balance:",Balance)


    if ch==3:
        
        print("balance",Balance)

    if ch==4:
        print("thank you come again")
        exit()



   
