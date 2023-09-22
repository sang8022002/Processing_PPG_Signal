# import heartpy as hp
# import matplotlib.pyplot as plt
# data, timer = hp.load_exampledata(2)
#
# print(timer[0])
# sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')
#
# print('sample rate is: %f Hz' %sample_rate)
# wd, m = hp.process(data, sample_rate, report_time = True)
#
# #plot
# #plt.figure(figsize=(20,4))
# hp.plotter(wd, m)
# plt.show()
#
# #let's zoom in on a bit
# #plt.figure(figsize=(12,4))
# plt.xlim(2000, 3000)
# hp.plotter(wd, m)
# plt.show()
#
# #display measures computed
# for measure in m.keys():
#     print('%s: %f' %(measure, m[measure]))
print("Hello world")
import pandas as pd
df = pd.DataFrame({'B': [0, 1, 2, 3, 4,5,6,7,8]})
x = df.rolling(3,min_periods= 1, center= True).mean()
print(x)
