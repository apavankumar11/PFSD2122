balance = 3000

def withdraw(amount):
    global balance
    balance -= amount
    return balance

def deposit(amount):
    global balance
    balance += amount
    return balance

def enquiry():
    return balance
