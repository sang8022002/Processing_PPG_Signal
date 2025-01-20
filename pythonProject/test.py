import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Clear allq
plt.close('all')
plt.clf()
plt.cla()

# Load CSV file
file_name = "/home/sang/Desktop/Processing_PPG_Signal/Processing_PPG_Signal/pythonProject/IR_RED_LED.csv"
ch = 1
fs = 25
colum_red = "red"
colum_ir = "ir"
ArrayIR = pd.read_csv(file_name,usecols= [colum_ir]).to_numpy()
# print(f"ArrayIR: {ArrayIR}")
ArrayRed = pd.read_csv(file_name,usecols= [colum_red]).to_numpy()
# print(f"ArrayRed: {ArrayRed}")
 
# make a move window find min and max of ArrayIR
def movmin1(A, k):
    x = A.rolling(k, min_periods= 1, center= True).min().to_numpy() # 
    return x
def movmax1(A, k):
    x = A.rolling(k, min_periods= 1, center= True).max().to_numpy()
    return x

ArrayIR = pd.DataFrame(ArrayIR)
ArrayRed = pd.DataFrame(ArrayRed)
#calculate ac/dc ir
max_ir = movmax1(ArrayIR, fs)
print(f"max_ir: {max_ir}")
min_ir = movmin1(ArrayIR, fs)
print(f"min_ir: {min_ir}")
baseline_data_ir = (max_ir + min_ir)/2
print(f"baseline_data_ir: {baseline_data_ir}")
acDivDcIr = (max_ir - min_ir)/baseline_data_ir

#calculate ac/dc red
max_red = movmax1(ArrayRed, fs)
min_red = movmin1(ArrayRed, fs)
baseline_data_red = (max_red + min_red)/2
acDivDcRed = (max_red - min_red)/baseline_data_red

# Plot SPO2 = 110-25*(ac/dc_red)/(ac/dc_ir)
SPO2 = 110 - 25*(acDivDcRed/acDivDcIr)
# plt.figure("SPO2")
plt.xlabel("Samples")
plt.ylabel("SPO2")
plt.plot(SPO2)
plt.show()


