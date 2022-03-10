
def setStartingBalance():
    startBal=float(input("Input starting balance: "))
    return startBal

def depositAmount(amount, balance):
    revisedBalance=balance+amount
    if amount>=0:
        return revisedBalance
    else:
        return balance

def withdrawAmount(amount, balance):
    revisedBalance=balance-amount
    if amount<0:
        return balance, False
    elif balance>=amount:
        return revisedBalance, False
    else:
        return revisedBalance, True
    