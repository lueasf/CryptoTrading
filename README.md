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

## Yfinance
- download() est une méthode de yfinance utilisé pour récupérer les données d'une action.

## Pandas
- head() est une méthode de pandas utilisé pour afficher les premières lignes d'un dataframe (tableau de données).
- rolling() est une méthode de pandas utilisé pour calculer les MA.