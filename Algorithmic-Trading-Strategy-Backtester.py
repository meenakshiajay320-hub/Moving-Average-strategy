import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#download stock data
data=yf.download("RELIANCE.NS", start="2025-01-01", end="2026-01-01")

#calc moving average
#MA10=short term trend
#MA30=longer trend
data["MA10"]=data["Close"].rolling(window=10).mean()
data["MA30"]=data["Close"].rolling(window=30).mean()

#create signal
data["Signal"]=0

#buy signal
data.loc[data["MA10"]>data["MA30"],"Signal"]=1

#sell signal
data.loc[data["MA10"]<data["MA30"],"Signal"]=-1

#show last 5 rows
print(data.tail())

#plot price and MA
plt.figure(figsize=(10,5))

plt.plot(data["Close"],label="Price")
plt.plot(data["MA10"],label="10 Day average")
plt.plot(data["MA30"],label="30 Day average")

plt.title("Moving Average Trading Strategy")
plt.legend()

plt.show()

