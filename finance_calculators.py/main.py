# A program that allow user to access: Investment calculator and Home loan calculator
import math
#  Requesting user to make input selection
print("Investment - to calculate the amount of interests you will earn on your investment")  # Will display explanation
print("Bond - to calculate the amount you will pay om a home loan\n")  # Will display explanation
option = input("choose between 'investment' or 'bond'\n")

financial_calculator = option.casefold()  # case fold() will lowercase any input selection


if financial_calculator == 'investment':
    deposit = input("Enter the amount you want to Deposit:\n")
    interest_rate = input("Enter the interest rate without % :\n")
    number_years = input("Enter the number of years you are planning to invest for:\n")
    p = float(deposit)
    r = float(interest_rate)
    t = float(number_years)
    interest_type = str(input("Choose whether you want 'simple' or 'compound' interest:\n"))  # Interest types
    interest = interest_type.casefold()

    if interest == 'simple':
        A = p * (1 + r / 100 * t)  # \100 to convert r to a decimal
        print(f"Your total will be R{A}: \n")
    elif interest == 'compound':
        A = p * math.pow((1 + r / 100), t)
        print(f"Your total will be R{A}: \n")

elif financial_calculator == 'bond':
    present_value = input("Enter the present value of the house:\n")
    interest_rate = input("Enter the interest rate without % :\n")
    number_of_months = input("Enter the number of months you planning to take to repay the bond:\n")
    p = float(present_value)
    i = float(interest_rate)
    n = float(number_of_months)
    monthly_repayment = float(p*i/100/12)/(1 - (1+i/100/12)**(-n)) 
    print(f"you will pay R{monthly_repayment} per month for {n} months \n")
    print(f"Total Monthly repayment:R{monthly_repayment} ")

else:
    print("Please enter a valid selection:")
