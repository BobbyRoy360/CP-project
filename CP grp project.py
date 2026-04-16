import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path = r"C:\Users\HP\Desktop\pm25_data.csv"   # change this
data = pd.read_csv(file_path)
print("Columns:", data.columns)
if 'Datetime' in data.columns:
    data['Date'] = pd.to_datetime(data['Datetime'])
elif 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])
else:
    raise Exception("No Date column found")

if 'PM2.5' not in data.columns:
    raise Exception("PM2.5 column not found")

data = data[['Date', 'PM2.5']]
data = data.dropna()
data = data.sort_values('Date')
print("Max:", data['PM2.5'].max())
print("Min:", data['PM2.5'].min())
print("Mean:", data['PM2.5'].mean())
print("Std Dev:", data['PM2.5'].std())
plt.figure()
plt.plot(data['Date'], data['PM2.5'])
plt.xlabel('Date')
plt.ylabel('PM2.5 (µg/m³)')
plt.title('PM2.5 Variation Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
data['MA7'] = data['PM2.5'].rolling(wndow=7).mean()
plt.figure()
plt.plot(data['Date'], data['PM2.5'], label='Original')
plt.plot(data['Date'], data['MA7'], label='7-day Avg')
plt.legend()
plt.title('Smoothed Trend')
plt.show()
plt.figure()
plt.hist(data['PM2.5'], bins=25)
plt.xlabel('PM2.5')
plt.ylabel('Frequency')
plt.title('Distribution')
plt.show()
pm_values = data['PM2.5'].values
fft = np.fft.fft(pm_values)
freq = np.fft.fftfreq(len(pm_values))
plt.figure()
plt.plot(freq, np.abs(fft))
plt.title('Fourier Transform (Frequency Analysis)')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()