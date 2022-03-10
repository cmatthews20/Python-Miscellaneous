
overdraftCount = 0

while True:
    
    startingBalance = float(input("Please enter your starting balance: "))
    variable = str(input("Type d to deposit, w to withdraw, q to quit: "))
    transactionAmount = float(input("Please enter the transaction amount: "))
    
    if variable == "q":
        break
        
    if transactionAmount > startingBalance:
        overdraftCount += 1

    if variable == "w":
        finalBalance=startingBalance-transactionAmount
        print("Your final balance is "+str(finalBalance))

    if variable == "d":
        finalBalance=startingBalance+transactionAmount
        print("Your final balance is "+str(finalBalance))
    
    print(overdraftCount, "overdrafts so far.")