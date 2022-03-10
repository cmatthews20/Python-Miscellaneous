
overdraftCount = 0
startingBalance = float(input("Please enter your starting balance: "))

while True:
    
    variable = str(input("Type d to deposit, w to withdraw, q to quit: "))
    
    if variable == "q":
        break
    
    transactionAmount = float(input("Please enter the transaction amount: "))
        
    if variable == "w":
        finalBalance=startingBalance-transactionAmount
        startingBalance -= transactionAmount
        print("Your final balance is "+str(finalBalance))
        
    if variable == "d":
        finalBalance=startingBalance+transactionAmount
        startingBalance += transactionAmount
        print("Your final balance is "+str(finalBalance))
        
    if 0 > startingBalance:
        overdraftCount += 1
    
print(overdraftCount, "overdrafts.")