import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Clear allq
plt.close('all')
plt.clf()
plt.cla()

# Load CSV file
file_name = "IR_RED_LED.csv"
ch = 1
fs = 25
colum_red = "red"
colum_ir = "ir"
A3 = pd.read_csv(file_name,usecols= [colum_ir]).to_numpy()
ArrayRed = pd.read_csv(file_name,usecols= [colum_red]).to_numpy()

# A3 = pd.read_csv(file_name)
A1 = A3.copy()
A2 = pd.DataFrame(A1)
ArrayRed1 = ArrayRed.copy()
ArrayRed2 = pd.DataFrame(ArrayRed1)


# Remove NaN and Zero values
x = np.arange(1, len(A1[:, 0]) + 1)
x1 = np.arange(1, len(ArrayRed1[:, 0]) + 1)
plt.figure(90)

for i in range(1, ch + 1):
    plt.subplot(ch, 1, i)
    plt.plot(x / fs, A1[:, i - 1])
plt.show()

nan_idx = np.isnan(A1)
A1[nan_idx] = 1e-16

zero_idx = (A1 == 0)
A1[zero_idx] = 1e-16
#calculate red
nan_idx = np.isnan(ArrayRed1)
ArrayRed1[nan_idx] = 1e-16

zero_idx = (ArrayRed1 == 0)
ArrayRed1[zero_idx] = 1e-16
#################################

def movmean1(A, k):
    x = A.rolling(k,min_periods= 1, center= True).mean().to_numpy()
    return x
def movmedian1(A, k):
    x = A.rolling(k, min_periods= 1, center= True).median().to_numpy()
    return x
#calculate ac/dc red
baseline_data_red = movmean1(ArrayRed2, fs)
acDivDcRed = ArrayRed1/baseline_data_red

##############################################

baseline_data = movmean1(A2, fs)
#clean_data = A1[:, 0] - baseline_data
acDivDcIr = A1/baseline_data
plt.figure(20)
for i in range(1, ch + 2):
    if i != (ch + 1):
        plt.subplot(ch+1, 1, i)
        plt.plot(x/fs, acDivDcIr)
        # plt.plot(x/fs, )
    else:
        plt.subplot(ch+1, 1, i)
        plt.plot(x/fs, acDivDcRed)
plt.show()
R = acDivDcRed/acDivDcIr
spo2 = 110-25*R

plt.figure("spo2")
plt.plot(x/fs, spo2)
plt.show()

clean_data = A1 - baseline_data
window_size = int(fs / 10)
clean_data = pd.DataFrame(clean_data )
median_data = movmedian1(clean_data,window_size )

plt.figure(9000)

for i in range(1, ch + 1):
    plt.subplot(ch, 1, i)
    plt.plot(x / fs, A1[:, i - 1])
    plt.plot(x / fs, baseline_data)
plt.show() #code heare

plt.figure(9001)


for i in range(1, ch + 1):
    plt.subplot(ch, 1, i)
    plt.plot(x / fs, median_data)
plt.show()

# Find peaks
from scipy.signal import find_peaks
df = pd.DataFrame(median_data)

# Trích xuất cột 'median_data' thành mảng NumPy 1 chiều
print(df.columns)
print(median_data)
median_data4 = median_data.flatten()
ampl, __ = find_peaks(median_data4, distance=int(0.7 * fs))

duong_bao = []

plt.figure(9002)
for i in range(1, ch + 1):
    plt.subplot(ch, 1, i)
    plt.plot(x, median_data)
    for value in ampl:
        plt.plot(value, median_data[value], "r*")
        duong_bao.append([value, median_data[value]])
# Vẽ đường bao
duong_bao_x = [point[0] for point in duong_bao]
duong_bao_y = [point[1] for point in duong_bao]
plt.plot(duong_bao_x, duong_bao_y, 'b-', label='Đường bao')

# Thêm tiêu đề và nhãn cho đồ thị
plt.title('Đường bao của các điểm đỏ')
plt.xlabel('Giá trị x')
plt.ylabel('Giá trị trung vị')
plt.grid(True)
plt.legend()
plt.show()



# Calculate FHR = 60*fs/RR
RR = ampl[1:] - ampl[:-1]
FHR = 60 * fs / RR
print(FHR)
plt.figure(9003)

for i in range(1, ch + 2):
    if i != (ch + 1):
        plt.subplot(ch + 1, 1, i)
        plt.plot(x, median_data)
        for value in ampl:
            plt.plot(value, median_data[value], "x")
    else:
        plt.subplot(ch + 1, 1, i)
        plt.plot(ampl[:-1], FHR)
        plt.ylim([30, 120])
plt.show()
# clean_data0 = clean_data
median_data = pd.DataFrame(median_data )
baseline_data1 = movmean1(median_data, fs)
median_data = np.array(median_data)
baseline_data1 = np.array(baseline_data1)
median_data1 = - median_data + baseline_data1
median_data1 = median_data1.flatten()
plt.figure(9004)
for i in range(1, ch + 2):
    if i != (ch + 1):
        plt.subplot(ch+1, 1, i)
        plt.plot(x/fs, median_data)
        plt.plot(x/fs, baseline_data1)
    else:
        plt.subplot(ch+1, 1, i)
        plt.plot(x/fs, median_data1)
plt.show()
ampl1, __ = find_peaks(median_data1, distance=int(0.7 * fs))

plt.figure(9005)

for i in range(1, ch + 1):
    plt.subplot(ch, 1, i)
    plt.plot(x, median_data1)
    for value in ampl1:
        plt.plot(value, median_data1[value], "r*")
plt.show()





