import math

# Start
# Display the two options the user has to choose from i.e. 'investment' or 'bond' with their descriptions. 
# On a new line, ask the user input their decision based on the two options available.
# Convert the word that the user enters into all lowercase letters and store under a variable called 'decision'.
# If user selects 'investment':
   #Ask user to input the amount that they are depositing. Store this as a variable called 'P'.
   #Ask user to enter the interest rate as a percentage without the percentage sign. Store as a variable called 'r'.
   #Divide 'r' by 100 to find the decimal value of the percentage. 
   #Ask the user to enter the number of years that they plan on investing. Store as a variable called 't'.
   #Ask user if they want 'simple' or 'compound' interest and store this as a variable called 'interest'.
      #If 'simple', then calculate and display the amount received after the given period specified.
      #If 'compound', caluclate and display the amount received after the given period specified.
# Otherwise, if the user selects 'bond':
   #Ask the user to input the present value of the house. Store this as a variable called 'P'.
   #Ask user to enter the interest rate as a percentage without the percentage sign. Store this as a variable called 'i'.
   #Divide 'i' by 100 to find the decimal value. 
   #Divide by 12 to find the monthly interest rate and assign 'i' to take on this new value.
   #Ask user to enter the number of months they plan to take to repay the bond. Store this as a variable called 'n'.
   #Calculate and display the amount of money that the user will have to repay each month.
# If neither 'investment' or 'bond' was entered, end the programme.
# End

# Prints the two options that the user has to choose from.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Below code converts the word that the user enters all into lowercase letters so input can be recognised.
# If the user enters 'investment', then depending on whether they want to have 'simple' or 'compound' interest,
# the respective calculation will be carried out and displayed.
# However, if the user decides to enter 'bond', the bond repayment calculation will be calculated and displayed.
# If the user enters neither 'investment' or 'bond' initially, an error will be displayed and the programme will end.

decision = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if decision == "investment":

    P = float(input("Please enter the amount you are depositing: £"))
    r = float(input("Please enter the interest rate as a percentage (without the percentage sign): ")) / 100
    t = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please enter whether you would you like to have 'simple' or 'compound' interest: ")
        
    if interest == "simple":
        A = P *(1 + r*t)
        print("After {} years, you will receive £{} having chosen simple interest.".format(t, A))
     
    if interest == "compound":
        A = P * math.pow((1 + r), t)
        print("After {} years, you will receive £{} having chosen compound interest.".format(t, A))
        
elif decision == "bond":
    P = float(input("Please enter the present value of the house: £"))
    i = float(input("Please enter the interest rate (without the percentage sign): ")) / 100
    i = i / 12
    n = int(input("Please enter the number of years you plan to take to repay the bond: "))

    # The repayment calculation rounds to two decimal places.
    repayment = round((i * P)/(1 - (1 + i)**(-n)), 2)
    print("The amount that you will have to repay on the loan is £{} per month.".format(repayment))

# User will have to restart the programme and try again with the acceptable inputs.
else:
    print("This is invalid. Please try again and enter either 'investment' or 'bond' to continue.")