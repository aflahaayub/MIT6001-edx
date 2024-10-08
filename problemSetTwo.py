def calculateBalance(balance, annualInterestRate = 0.02, monthlyPaymentRate = 0.18):
    """
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

    For each month, calculate statements on the monthly payment and remaining balance. 
    At the end of 12 months, print out the remaining balance. 
    Be sure to print out no more than two decimal digits of accuracy - so print 
    
    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
    """
    month = 1
    remainingBalance = 0

    return 0