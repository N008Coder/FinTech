# coding: utf-8
# below, we import the modules with the functions that we'll use to create a file path and write to a csv file

import csv
from pathlib import Path

#doc-String (similar to comment, but can go many lines and shows up in different places)
"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
loan_count=len(loan_costs)
# Used the f-string to print out the total number of loans in the loan_costs list
print(f"Total number of loans = {loan_count}")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# This time, stored the message as a variable and used a "," to concatenate the message with less lines of code
message = "The total cost of all the loans ="
loan_sum=sum(loan_costs)
print(message,loan_sum)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
avg_loan = loan_sum / loan_count
#print(f"The average loan value is {avg_loan}")
#print("The average loan value is " + str(avg_loan))
message = "The average loan value is"
print(message, avg_loan)
# Use the shortest when it makes sense to. Above, I've replaced the contents of the message variable with what I now want it to display
# Displaying different ways to print the message above. 

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
months = loan.get("remaining_months")
print(f"There are {months} months left for the loan")
# Above, we search the dictionary's Key:Value pairs by searching up the Key and returning the Value
# In the print statement above, I decided to use F-string rather than inserting variables with "," because it would require 3
# variables to be inserted and therefore be less readable
# This extracting of the Values from within the dictionary will make it possible to run calculations using these Values as inputs

fv = loan.get("future_value")
message = "The FV ="
print(message, fv)
# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount = .2
pres_v = fv / (1 + discount/12)**months
message = "PV ="
print(message, pres_v)

# Above is the calculation that takes in a given discount rate, Future Value, and Months left on the loan and outputs a Present Value (current worth)
# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if pres_v > loan["loan_price"]:
    print("It's worth paying at least the cost of the loan to pick this one up.")
else:
    print("This loan is too expensive, we'll be better off passing on this one.")

# This conditional statement compares the "true worth" of the loan that we calculated to the acutal cost and provides a recommendation based on that comparison
# In this case I did not replace the contents of the "message" variable since it doesn't make the code shorter or more readable

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def pv(future_value,remaining_months,annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12)**remaining_months
    return present_value
disc = .2
present_value = pv(new_loan["future_value"],new_loan["remaining_months"],disc)

# Above, we define a function to calculate the Present Value by simply calling the function, and passing the correct arguments to the parameters


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
message = "The present value of the loan is:"
print(message,present_value)
# Extra note on the above syntax, a comma between variables will automatically provide a space, regardless of if there's a space after the comma within the print function

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"]<=500:
        inexpensive_loans.append(loan)

# The For loop above looks at the loan price of each line within the list and if it passes the criteria of having a price <= 500,
# then it will add that dictionary to the newly created list inexpensive_loans. This is a way of filtering through a list


# @TODO: Print the `inexpensive_loans` list
message = "Here's the data on all the cheap loans:"
print(message, inexpensive_loans)        


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
output_path = Path("inexpensive_loans.csv")


with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())


# Above, we call upon the imported modules to create the set-up and then run the set-up to save the filtered list of dictionaries (inexpensive_loans)
# and save that list into a CSV file by separating out each value in the dictionary as a comma-delineated value and showing the Keys as a header in the 1st row