def createAccnt(initial_acnt):
    print("\nCreating account")
    name = input("\nEnter name : ")
    dob = input("enter dob : ")
    phone = input("phone : ")
    address = input("address : ")
    acnt = initial_acnt + 1
    initial_acnt = acnt
    cust = bank(name,dob,phone,address,acnt)
    print("\naccount created with details : ")
    print("name : ",name)
    print("account number : ",acnt)
    print("dob : ",dob)
    print("phone : ",phone)
    accntnumber.append(acnt)
    accounts.append(cust)
    return cust,initial_acnt

def details():
    print("\nRetrieving Details\n")
    phone = input("enter the phone number : ")
    for i in accounts :
        if(i.phone == phone):
            print("\nDetails are")
            print("name : ",i.name)
            print("account : ",i.acnt)
            print("dob : ",i.dob)
            print("phone : ",i.phone)
            print("address : ",i.add)

def withdraw():
    print("\nWithdrawing Amount\n")
    number = int(input("Enter the acnt number : "))
    amt = 0
    for i in accounts :
        if(i.acnt == number):
            amount = int(input("enter amount to be withdrawn : "))
            amt = amount
            if(amount > i.balance):
                print("insufficient balance")
            else:
                print("amount withdrawn")
                i.balance = i.balance - amount
                print("Remaining balance : ",i.balance)
        else:
            print("user not found")
    trans = "Amount "+ str(amt) +" withdrawl from " + str(number)
    transactions.append(trans)

def deposit():
    print("\nDepositing Amount\n")
    number = int(input("enter the acnt number : "))
    amt = 0
    for i in accounts :
        if(i.acnt == number):
            amount = int(input("enter amount to be deposited : "))
            amt = amount
            i.balance = i.balance + amount
            print("Remaining balance : ",i.balance)
    trans = "Amount "+ str(amt) +" deposited into " + str(number)
    transactions.append(trans)

def transfer():
    print("\nTransfering Amount\n")
    number1 = int(input("enter your acnt number : "))
    number2 = int(input("enter receivers acnt number : "))
    amount = int(input("enter amount you wanted to send : "))
    for i in accounts:
        if(i.acnt == number1):
            bal1 = i.balance
            if(bal1 < amount):
                print("cannot transfer amount due to low balance : ",bal1)
                break
            else:
                i.balance = bal1 - amount
                bal1 = i.balance
                
        if(i.acnt == number2):
            bal2 = i.balance
            i.balance = bal2 + amount
            bal2 = i.balance
    print("amount transferred successfully")
    print("balance : ")
    print( f'{number1} : {bal1}')
    print(f'{number2} : {bal2}')
    trans = str(number1) + " transferred RS" + str(amount) + "to account" + str(number2)
    transactions.append(trans)

def print_trans():
    print("Printing transactions : \n")
    for i in transactions:
        print(i)

def Exiting():
    print("Exiting")
    return False
    

            
class bank:
    def __init__(self,name,dob,phone,address,acnt):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.add = address
        self.balance = 0
        self.acnt = acnt

    



if __name__ == "__main__":

    
    accntnumber = []
    initial_acnt = 1069700
    accounts = []
    transactions = []
    yes = True
    while(yes):
        
        print("---------------------------------")
        print("1 : create account")
        print("2 : view details by number")
        print("3 : withdraw")
        print("4 : deposit")
        print("5 : fund transfer")
        print("6 : print transaction")
        print("7 : exit")
        op = int(input("\nenter option : "))

        match op:
            case 1 : _,initial_acnt = createAccnt(initial_acnt)
            case 2 : details()
            case 3 : withdraw()
            case 4 : deposit()
            case 5 : transfer()
            case 6 : print_trans()
            case 7 : yes = Exiting()
            

        

    
        
        
