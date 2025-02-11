import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_USD = yf.download("BTC-USD", start="2021-01-01", end="2021-12-31", interval="1d")
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
short_window = 10
long_window = 50
trade_sig['Short'] = BTC_USD['Close'].rolling(window=short_window, min_periods=1).mean()
trade_sig['Long'] = BTC_USD['Close'].rolling(window=long_window, min_periods=1).mean()

trade_sig['Signal'] = 0.0 # On crée une colonne de signaux vide
trade_sig['Signal'] = np.where(trade_sig['Short'] > trade_sig['Long'], 1.0, 0.0)

'''
Stratégie:

- Si la moyenne mobile courte est supérieure à la moyenne mobile longue, on met un 1
dans la colonne Signal.
- Si la moyenne mobile longue est supérieure à la moyenne mobile courte, on met un 0.

À condition que cela se fasse sur une période égale sur une période de la durée du plus
court intervalle.

Ensuite, si le signal est 1, on achète, si le signal est 0, on vend.
Pour cela, on regarde la différence entre deux lignes et si elle vaut 1 ou -1, une ligne
a croisé l'autre. Si c'est un 0, c'est que les deux lignes ne se sont pas croisées.
'''

trade_sig['Position'] = trade_sig['Signal'].diff()
# print(trade_sig)

fig2, ax2 = plt.subplots(dpi=500)
date_format = DateFormatter("%h %d 20%y")
ax2.xaxis.set_major_formatter(date_format)

ax2.tick_params(axis='x', labelsize=5)
ax2.tick_params(axis='y', labelsize=5)

fig2.autofmt_xdate()

ax2.plot(BTC_USD['Close'], lw=0.5, label='Closing Price') # lw = line width
ax2.plot(trade_sig['Short'], lw=0.5, label='Short Term MA')
ax2.plot(trade_sig['Long'], lw=0.5, label='Long Term MA')

# flèches indiquants les meilleures positions d'achat et de vente
ax2.plot(trade_sig.loc[trade_sig['Position'] == 1.0].index, trade_sig.Short[trade_sig['Position'] == 1.0],
marker=6, ms=4, linestyle='none', color='red')
ax2.plot(trade_sig.loc[trade_sig['Position'] == -1.0].index, trade_sig.Short[trade_sig['Position'] == -1.0],
marker=6, ms=4, linestyle='none', color='green')

ax2.set_title("Bitcoin to USD Exchange Rate", fontsize=10)
ax2.set_ylabel("Price of Bitcoin in USD", fontsize=5)
ax2.grid()
ax2.legend(fontsize=5)
plt.close(fig)
# plt.show()

# backtesting
initial_capital = 10000.0 # USD
backtest = pd.DataFrame(index=BTC_USD.index)
backtest['BTC_Return'] = BTC_USD['Close'] / BTC_USD['Close'].shift(1) # Auj / Hier

# Si le signal est 1, on achète, sinon on ne fait rien
backtest['Alg_Return'] = np.where(trade_sig.Signal == 1, backtest.BTC_Return, 1.0)
backtest['Balance'] = initial_capital * backtest.Alg_Return.cumprod()

fig3, ax3 = plt.subplots(dpi=500)
date_format = DateFormatter("%h %d 20%y")
ax3.xaxis.set_major_formatter(date_format)
ax3.tick_params(axis='x', labelsize=5)
ax3.tick_params(axis='y', labelsize=5)
fig3.autofmt_xdate()

# Buy and Hold : On ne touche plus à rien
ax3.plot(initial_capital * backtest.BTC_Return.cumprod(), lw=0.5, label='Buy and Hold')

# Crossing Averages
ax3.plot(backtest['Balance'], lw=0.5, label='Crossing Averages')

ax3.set_title('Value of Portfolio')
ax3.set_ylabel('USD')
ax3.grid()
ax3.legend()
plt.show()