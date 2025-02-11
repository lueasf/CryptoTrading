import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_USD = yf.download("BTC-USD", start="2020-01-01", end="2020-12-31", interval="1d")
BTC_USD['SMA_9'] = BTC_USD['Close'].rolling(window=9, min_periods=1).mean() # On ajoute une colone au dataframe, avec les MA.
# print(BTC_USD.tail(7))

### Graphique des données
fig, ax = plt.subplots(dpi=500)
date_format = DateFormatter("%h %d 20%y")
ax.xaxis.set_major_formatter(date_format)

ax.tick_params(axis='x', labelsize=5)
ax.tick_params(axis='y', labelsize=5)

fig.autofmt_xdate() # pivote les dates pour une meilleure lisibilité

ax.plot(BTC_USD['Close'], lw=0.5, label='Closing Price') # lw = line width
ax.plot(BTC_USD['SMA_9'], lw=0.5, label='9 Day SMA')
ax.set_title("Bitcoin to USD Exchange Rate", fontsize=10)
ax.set_ylabel("Price of Bitcoin in USD", fontsize=5)
ax.grid()
ax.legend(fontsize=5)
# plt.show()

### Moving Average Crossover Stratégie
trade_sig = pd.DataFrame(index=BTC_USD.index) # On crée un dataframe vide avec les dates de BTC_USD
short_window = 9
long_window = 30
trade_sig['Short'] = BTC_USD['Close'].rolling(window=short_window, min_periods=1).mean()
trade_sig['Long'] = BTC_USD['Close'].rolling(window=long_window, min_periods=1).mean()

trade_sig['Signal'] = 0.0 # On crée une colonne de signaux vide

'''
Stratégie:

- Si la moyenne mobile courte est supérieure à la moyenne mobile longue, on met un 1
dans la colonne Signal.
- Si la moyenne mobile longue est supérieure à la moyenne mobile courte, on met un 0.

À condition que cela se fasse sur une période égale sur une période de la durée du plus
court intervalle.

Ensuite, si le signal est 1, on achète, si le signal est 0, on vend.
'''

# print(trade_sig)
