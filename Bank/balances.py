balances = {}

def depositMoney(name,amount):
    if name in balances:
        balances[name] += amount
        exists = True
    else:
        balances[name]=0
        balances[name] += amount 
        exists=False
    return exists, balances[name]

def withdrawMoney(name,amount):
    if name in balances:
        balances[name] -= amount
        exist=True
        if balances[name]<0:
            pyfraud=True
        else:
            pyfraud=False
        return exist, pyfraud, balances[name]
    else: 
        exist=False
        pyfraud=True
        bal = 0
        return exist, pyfraud, bal
    