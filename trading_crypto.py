import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_EUR = yf.download("BTC-EUR", start='2023-01-01', end='2023-01-20', interval='1d')
print(BTC_EUR.head())

BTC_EUR['Short'] = BTC_EUR['Close'].rolling(window=9, min_periods=1).mean()
BTC_EUR['Long'] = BTC_EUR['Close'].rolling(window=30, min_periods=1).mean()

print(BTC_EUR.head())
print(BTC_EUR.tail())

fig, ax = plt.subplots(dpi=100)

ax.plot(BTC_EUR['Close'], lw=0.75, label='Closing Price')

ax.plot(BTC_EUR['Short'], lw=0.75, alpha=0.75, label='7 Day SMA')
ax.plot(BTC_EUR['Long'], lw=0.75, alpha=0.75, label='30 Day SMA')

ax.set_ylabel('Price of Bitcoin(EUR)')
ax.set_title('Bitcoin to EUR Exchange Rate')
ax.grid()
ax.legend()

trade_signals = pd.DataFrame(index=BTC_EUR.index)

short_interval = 1
long_interval = 3

trade_signals['Short'] = BTC_EUR['Close'].rolling(window=short_interval, min_periods=1).mean()
trade_signals['Long'] = BTC_EUR['Close'].rolling(window=long_interval, min_periods=1).mean()

trade_signals['Signal'] = 0.0
trade_signals['Signal'] = np.where(trade_signals['Short'] > trade_signals['Long'], 1.0, 0.0)

trade_signals['Position'] = trade_signals['Signal'].diff()

fig2, ax2 =plt.subplots(dpi=100)

ax2.plot(BTC_EUR['Close'], lw=0.75, label='Closing Price')
ax2.plot(BTC_EUR['Short'], lw=0.75, alpha=0.75, color='orange', label='Short term SMA')
ax2.plot(BTC_EUR['Long'], lw=0.75, alpha=0.75, color='purple', label='Long term SMA')

ax2.plot(trade_signals.loc[trade_signals['Position']==1.0].index, trade_signals.Short[trade_signals['Position'] == 1.0], marker=6, ms=4, linestyle='none', color='green')
ax2.plot(trade_signals.loc[trade_signals['Position']==-1.0].index, trade_signals.Short[trade_signals['Position'] == -1.0], marker=7, ms=4, linestyle='none', color='red')

ax2.set_ylabel('Price of Bitcoin (EUR)')
ax2.set_title('Bitcoin to EuR Exchange Rate')

ax2.grid()  
ax2.legend()

plt.show()
