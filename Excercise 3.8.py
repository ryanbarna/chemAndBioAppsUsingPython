interestRate = str(input('Is the interest rate less than 8%? [y/n]'))
interestRate = interestRate.upper()
if interestRate == 'Y':
    income = input('Is the income less than $75000 [y/n]')
    income = income.upper()
    if income == 'Y':
        print('Risk of prepayment 2.6%')
    else:
        print('Risk of prepayment 6.4%')

#    print("ok")
else:
    mortgage = input('Is the mortgage less than 183000?')
    mortgage = mortgage.upper()
    if mortgage =='Y':
        print('Risk of prepayment 13.9%')
    else:
        print("Risk of prepayment 36.0%") 