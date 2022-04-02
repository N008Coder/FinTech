# FinTech
Challenge 1 to analyze different aspects of a couple loans and whether or not it's worth it to buy a loan, based on Present Value using a given discount rate
We start with some basic statistical analysis, including an N-count, total value of the loans, and an average value of the loan.
Then, given these parameters: Cost of loan, Future Value, Remaining months of payment, repayment interval, and a discount rate, we can:
    Provide a recommendation on whether or not to buy the loan using an If statement, a comparison, and the Present Value calculation
We then use a For loop to filter through the available loans and if the loan has a price less than or equal to $500, then we'll add it to an inexpensive_loans list.
Lastly, we use the Pathlib and CSV modules to save the results of the Python script as a CSV file with a header that we set. The contents of the file will include our header as well as the rows of data that fit our inexpensive_loans criteria
