#Finds strongest signal parameter in 211 calls (i.e. has greatest difference in number of calls between zipcodes)
# and identifies zipcodes with greatest number of calls and least number of calls for that parameter
# coding=utf-8

import pandas as pd
# Import summary data as csv. FILL IN SOURCE ADDRESS FOR CSV FILE
summ = pd.read_csv('/Users/staceytorigoe/PycharmProjects/foodinsecurity_1/211-summary.csv', index_col=0)
# Calculate differences in parameter columns, create new dataframe of difference values.
# Index column of zipcodes should not be included in this calculation
for column in summ.iteritems():
    diffs = [summ.max()- summ.min()]
diffdf = pd.DataFrame(diffs)
# Find strongest parameter signal by finding greatest difference, print it
strongest = diffdf.idxmax(axis=1)
print("Parameter with the strongest signal difference:"), strongest
# Identify index of highest and lowest values of strongest parameter, print these
idxa = summ[strongest].idxmax(axis=0)
idxb = summ[strongest].idxmin(axis=0)
print("Zipcode containing the largest value of the parameter:"), idxa
print("Zipcode containing the smallest value of the parameter:"), idxb
