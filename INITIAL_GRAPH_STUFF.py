# SAMYUKTA SREEKANTH - R00170779 - SDH2C
# STATISTICS AND PROBABILITY
# INITIAL GRAPHS - HISTOGRAM, LINE PLOT

# Note: close 'x' the current figure to view the other figures after running the program
# Note: I have done in 4 python files for easy reading

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'Assignment.xlsx'
data = pd.read_excel(excel_file)
data_sheet1 = pd.read_excel(excel_file)
data_sheet1.head()

# LINE PLOT
data['Algorithm 1'].plot(kind="line", color = "pink")
data['Algorithm 2'].plot(kind="line", color = "orange")
legend = ['Algorithm 1', 'Algorithm 2']
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.legend(legend)
plt.title('Initial')
plt.show()

# HISTOGRAMS ALG 1 INITIAL
data['Algorithm 1'].plot(kind="hist", color = "pink")
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.title('Initial \n Algorithm 1')
plt.show()

# HISTOGRAM ALG 2 INITIAL
data['Algorithm 2'].plot(kind="hist", color = "orange")
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.title('Initial \n Algorithm 2')
plt.show()

