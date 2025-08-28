import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data
def get_data(tickers, start_date, end_date, interval="1d"):
    """
    Downloads and formats historical stock data from Yahoo Finance.
    """
    if isinstance(tickers, str):
        tickers = [tickers]

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    if data.empty:
        return pd.DataFrame()

    if len(tickers) > 1:
        if isinstance(data.columns, pd.MultiIndex):
            data = data["Adj Close"]
        else:
            data = data[[col for col in data.columns if "Close" in col]]
    else:
        if "Adj Close" in data.columns:
            data = data[["Adj Close"]]
        elif "Close" in data.columns:
            data = data[["Close"]]
        data.columns = tickers

    return data