# SAMYUKTA SREEKANTH - R00170779 - SDH2C
# STATISTICS AND PROBABILITY
# INITIAL
# MEASURES OF CENTRALITY , MEASURES OF VARIABILITY

import numpy as np
import xlrd
import statistics

loc = ("Assignment.xlsx")
initial_run_number_values = [];
intital_algorithm1_values = [];
initial_algorithm2_values = [];

wb = xlrd.open_workbook(loc)
sheet0 = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(1)

sheet0.cell_value(0, 0)
sheet1.cell_value(0, 0)

# INITIAL ALGORITHM

# Displaying the data
for i in range(sheet0.nrows):
    print(str(sheet0.cell_value(i, 0)) + "\t\t\t\t" + str(sheet0.cell_value(i, 1)) + "\t\t\t\t" + str(sheet0.cell_value(i, 2)))

for i in range(1, sheet0.nrows):
    intital_algorithm1_values.append(sheet0.cell_value(i, 1))
for i in range(1, sheet0.nrows):
    initial_algorithm2_values.append(sheet0.cell_value(i, 2))

# INITIAL ALGORITHM 1
initial_alg1_mean = statistics.mean(intital_algorithm1_values)
initial_alg1_median = statistics.median(intital_algorithm1_values)
initial_alg1_sd = np.std(intital_algorithm1_values)
initial_alg1_max = np.max(intital_algorithm1_values)
initial_alg1_min = np.min(intital_algorithm1_values)
intital_alg1_range = initial_alg1_max - initial_alg1_min
intital_alg1_q1 = np.quantile(intital_algorithm1_values, 0.25)
intital_alg1_q3 = np.quantile(intital_algorithm1_values, 0.75)
intital_alg1_IQR = intital_alg1_q3 - intital_alg1_q1

print("INITIAL\n-----------\nALGORITHM 1\n-----------")
print("Mean :", round(initial_alg1_mean, 3))
print("Median :", round(initial_alg1_median, 3))
print("Standard Deviation :", round(initial_alg1_sd, 3))
print("Range :", round(intital_alg1_range, 3))
print("Inter quartile Range :", round(intital_alg1_IQR, 3))

# INITIAL ALGORITHM 2
initial_alg2_mean = statistics.mean(initial_algorithm2_values)
initial_alg2_median = statistics.median(initial_algorithm2_values)
initial_alg2_sd = np.std(initial_algorithm2_values)
initial_alg2_max = np.max(initial_algorithm2_values)
initial_alg2_min = np.min(initial_algorithm2_values)
initial_alg2_range = initial_alg2_max - initial_alg2_min
initial_alg2_q1 = np.quantile(initial_algorithm2_values, 0.25)
initial_alg2_q3 = np.quantile(initial_algorithm2_values, 0.75)
initial_alg2_IQR = initial_alg2_q3 - initial_alg2_q1

print("-----------\nALGORITHM 2\n-----------")
print("Mean :", round(initial_alg2_mean,3))
print("Median :", round(initial_alg2_median,3))
print("Standard Deviation :", round(initial_alg2_sd,3))
print("Range :", round(initial_alg2_range,3))
print("Inter quartile Range :", round(initial_alg2_IQR,3))





