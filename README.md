# Exploratory Data Analysis on Loan Data from Prosper

## Aim
This project aims to understand the factors that affect loan outcome status. Valid loan status include Current, Completed, Defaulted, Charged off, and Past due 

## Dataset

[The dataset](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv) contains `113,937` loans with `81` variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. See this data [dictionary](https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/edit#gid=0) to understand the dataset's variables.

## Summary of Findings

- On bivariate exploration, I found out that completed loans have very much lower `Interest rate` less than 20%, while the other categories with interest rate more than 20%

- Similar to the first finding, completed loans also showed very low DebtToIncomeRatio while the other categories were much higher

- Owning a home tells a little of of someone's financial status/monthly income. My analysis revealed that loanees who recieved more than 15k/month were mostly home owners

- Monthly Income has an effect on DebtToIncomeRatio: a higher monthly income will definitely reduce the DTI ratio than a lower one

- What I discovered was that, loanees who completed thier loans recieved more monthly income, borrowed lesser amount, and consequently had lesser DTI ratio. This made it easy for them to complete there loan debts. On the other hand, Incomplete loans (Defaulted, Chargedoff, Past due) was as a result of either low monthly income,  high monthly payment, which consequently resulted to a very high Debt-to-income ratio


## Motivation
This project is part of the requirement for a successfull completion of the `Alx-Udacity Data Analytics nanodegree program`


## Technologies/libraries
- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
