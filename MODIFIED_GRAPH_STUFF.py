# SAMYUKTA SREEKANTH - R00170779 - SDH2C
# STATISTICS AND PROBABILITY
# MODIFIED GRAPHS - HISTOGRAM, LINE PLOT

import matplotlib.pyplot as plt

import pandas as pd
# SAMYUKTA SREEKANTH - R00170779 - SDH2C
# STATISTICS AND PROBABILITY 2020
# MODIFIED GRAPHS - HISTOGRAM, LINE PLOT

# Note: close 'x' the current figure to view the other figures after running the program

excel_file = 'Assignment.xlsx'
data = pd.read_excel(excel_file, "Modified")

# LINE PLOT MODIFIED
data['Algorithm 1'].plot(kind="line", color = "violet")
data['Algorithm 2'].plot(kind="line", color = "gold")
legend = ['Algorithm 1', 'Algorithm 2']
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.legend(legend)
plt.title('Modified')
plt.show()

# HISTOGRAMS ALG 1 MOD
data['Algorithm 1'].plot(kind="hist", color = "violet")
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.title('Modified \n Algorithm 1')
plt.show()

# HISTOGRAM ALG 2 MOD
data['Algorithm 2'].plot(kind="hist", color = "gold")
plt.xlabel("Runtime(s)")
plt.ylabel("Run Number / Frequency")
plt.title('Modified \n Algorithm 2')
plt.show()