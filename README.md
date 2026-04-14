# Algorithmic Trading Strategy Backtester

## Overview
This project implements a simple algorithmic trading strategy using Python.  
It analyzes historical stock data and generates trading signals using a moving average crossover strategy.

## Strategy
The strategy uses two moving averages:

- **MA10 (10-day moving average)** – short term trend
- **MA30 (30-day moving average)** – long term trend

Trading rules:

- **BUY** when MA10 > MA30
- **SELL** when MA10 < MA30

## Tools Used
- Python
- Pandas
- Matplotlib
- yfinance

## Output
The program:
- Downloads historical stock price data
- Calculates moving averages
- Generates buy/sell signals
- Plots the stock price with moving averages

## Author
Meenakshy Ajay  
BCA Student interested in Financial Data Analysis and Quantitative Finance
