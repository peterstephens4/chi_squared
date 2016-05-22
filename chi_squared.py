#  Peter Stephens
#  5/21/2016

#  Performs the Chi-squared test on Lending Club Data and prints the result

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections
import subprocess

#  Clean the directory of old png files
p = subprocess.Popen("rm -rf *.png",  shell=True)

#  Read in Lending Club Data form git hub repository
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#  Clean Data:  Remove null value rows
loansData.dropna(inplace=True)

#  Get counts of observations for each number of credit lines
frequency = collections.Counter(loansData['Open.CREDIT.Lines'])
unique_open_credit_lines =  len(frequency)

credit_lines = list(frequency.values())
most_freq_num_open_credit_line = max(credit_lines)

#  Plot the frequency information for credit lines opened
plt.figure()
plt.bar(frequency.keys(), frequency.values(), width=1)
plt.savefig("Bar_Plot_Open_Credit_Lines.png") 

#  Perform the Chi-squared test to support or refute answer
chi, p = stats.chisquare(credit_lines)

print('\n')
print('Unique number of open credit lines in the data ... ' + str(unique_open_credit_lines) + '.')
print('The most frequent number of open credit lines ... ' + str(most_freq_num_open_credit_line) + '.')
print('Results of the Chi-square test:  \nchi-squared test statistic = ' + str(chi) + '\np-value of the test = ' + str(p))


