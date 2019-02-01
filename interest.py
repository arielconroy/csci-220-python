#Ariel Robinson
#Interest.py
#Problem:
#Calculating the monthly interest charge on a credit card.
# I certify that this lab is my own work,but I
# discussed it with: Professor Stalvey

def monthlyInterestCharge ():
    print("Calculate your Credit Card's Monthly Interest Charge")
     #tells user to enter annual interest
    annualInterestRate=eval(input("Enter the annual interest rate: "))
    #tells user to enter number of days in your billing cycle
    daysInCycle=eval(input("Enter number days in the billing cycle: "))
    #tells user to enter net balance
    netBalance=eval(input("Enter the previous net balance: "))
    # tells user to enter the payment amount
    paymentAmount=eval(input("Enter the payment amount: "))
    #tells user to enter the day of payment
    dayOfPayment=eval(input("Enter the day of payment: "))

    # calculates the average daily balance
    netOverMonth=daysInCycle*netBalance
    #figures out the days before the end of the cycle 
    daysBeforeEndOfCycle=daysInCycle-dayOfPayment
    amountOverEnd=paymentAmount*dayOfPayment
    finalBalance=netOverMonth-amountOverEnd
    averageDailyBalance=finalBalance/daysInCycle
    #calculates the monthly interest charge 
    monthlyInterestRate=annualInterestRate/100/12
    monthlyInterestCharge=averageDailyBalance*monthlyInterestRate
    
    # show the monthly interest charge to the user
    print("Monthly Interest Charge is:$",round(monthlyInterestCharge,2))
