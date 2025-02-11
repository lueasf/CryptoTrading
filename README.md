# CryptoTrading

Ce projet à pour but de créer un algorithme de trading de cryptomonnaie en utilisant la méthode de **Simple Moving Averages (SMA)**.

## Installation
```bash
git clone 
cd CryptoTrading
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
python3 app.py
```

## Analyse basique
Simple Moving Averages (SMA) est une méthode d'analyse technique qui permet de lisser les données de prix en créant une série de moyennes de prix. Cela permet de mieux visualiser la tendance générale du prix d'un actif. C'est un peu comme
les "sliding windows".  
> Une fenêtre de 50 jours signifie que pour chaque jour, on prend les 50 jours précédents et on calcule la moyenne.

Moving Average Crossover : C'est une stratégie de trading qui consiste à acheter ou vendre un actif lorsque deux moyennes mobiles se croisent.

# Backtesting
Le backtesting est une méthode qui permet de tester une stratégie ou un modèle sur des données historiques. 
Ici, j'effectue le backtesting avec un portefeuille de 10 000$.
On test avec la stratégie Buy and Hold et la stratégie SMA. 
Au bout de 1 an, B&H atteint 40 000$ et SMA atteint 45 000$ .
On quadruple notre investissement. C'est parce que en 2020, le Bitcoin a explosé.
Si on recommence avec les données de 2021, on se rend compte, que
B&H surpasse Crossing Averages à la fin et les rendements sont moins élevés qu'en 2020.

## Yfinance
- download() est une méthode de yfinance utilisé pour récupérer les données d'une action.

## Pandas
- head() est une méthode de pandas utilisé pour afficher les premières lignes d'un dataframe (tableau de données).
- rolling() est une méthode de pandas utilisé pour calculer les MA.
- diff() est une méthode de pandas utilisé pour calculer la différence entre deux lignes.
- cumsum() est une méthode de pandas utilisé pour calculer la somme cumulée.
- cumprod() est une méthode de pandas utilisé pour calculer le produit cumulé.

# Matlplotlib
- plot() est une méthode de matplotlib utilisé pour afficher un graphique.
```python
ax2.plot(trade_sig.loc[trade_sig['Position'] == 1.0].index, trade_sig.Short[trade_sig['Position'] == 1.0],
marker=6, ms=4, linestyle='none', color='red')
```
Cette ligne permet de placer un marker rouge sur le graphique à chaque fois que la position est à 1.0, indiquant un signal d'achat.

