import streamlit as st
import pandas as pd
import numpy as np


from modules.data_loader import get_data
from modules.risk_metrics import calculate_portfolio_metrics, value_at_risk, max_drawdown
from modules.visualizations import plot_cumulative_returns, plot_drawdown, plot_allocation
from reports.export_report import export_to_excel, export_to_pdf

st.set_page_config(page_title="Portfolio Risk Analyzer", layout="wide")
st.title("📈 Portfolio Risk Analyzer")



st.sidebar.header("Portfolio Input")
tickers_input = st.sidebar.text_area("Enter Ticker Symbols (comma separated)", "AAPL, MSFT, GOOGL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))
weights_input = st.sidebar.text_input("Enter weights (comma separated, must sum to 1)", "0.4,0.3,0.3")

uploaded_file = st.sidebar.file_uploader("or upload CSV (Ticker, Weights)", type=["csv"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    tickers = df['Ticker'].tolist()
    weights = df['Weights'].tolist()
else:
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    weights = [float(w.strip()) for w in weights_input.split(",") if w.strip()]


if not tickers:
    st.warning("Please enter at least one ticker symbol.")
    st.stop()
    
if len(tickers) != len(weights):
    st.error("⚠️ The number of tickers and weights must match.")
    st.stop()


if not np.isclose(sum(weights), 1.0):
    st.error(f"⚠️ Weights must sum to 1. Current sum is {sum(weights):.2f}.")
    st.stop()


data = get_data(tickers, start_date, end_date)

if data.empty:
    st.error("Could not fetch data for the given tickers and date range. Please check the ticker symbols.")
    st.stop()

returns = data.pct_change().dropna()
portfolio_returns, cumulative_returns, avg_return, volatility, sharpe_ratio = calculate_portfolio_metrics(returns, weights)
var_95 = value_at_risk(portfolio_returns)
drawdown, max_dd = max_drawdown(cumulative_returns)


st.subheader("Key Portfolio Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Annualized Return", f"{avg_return:.2%}")
col2.metric("Annualized Volatility (Risk)", f"{volatility:.2%}")
col3.metric("Sharpe Ratio", f"{sharpe_ratio:.2f}")

col4, col5 = st.columns(2)
col4.metric("Max Drawdown", f"{max_dd:.2%}")
col5.metric("Value at Risk (VaR 95%)", f"{var_95:.2%}")


st.subheader("Portfolio Cumulative Returns")
fig_cum_returns = plot_cumulative_returns(cumulative_returns)
st.pyplot(fig_cum_returns)

st.subheader("Asset Allocation")
fig_allocation = plot_allocation(tickers, weights)
st.pyplot(fig_allocation)

st.subheader("Portfolio Drawdown")
fig_drawdown = plot_drawdown(drawdown)
st.pyplot(fig_drawdown)


st.subheader("Export Report")
metrics_dict = {
    "Annual Return": f"{avg_return:.2%}",
    "Volatility": f"{volatility:.2%}",
    "Sharpe Ratio": f"{sharpe_ratio:.2f}",
    "Max Drawdown": f"{max_dd:.2%}",
    "VaR (95%, 1-day)": f"{var_95:.2%}"
}

if st.button("Export to Excel"):
    filepath = export_to_excel(metrics_dict, cumulative_returns)
    st.success(f"Report exported to {filepath}")

if st.button("Export to PDF"):
    filepath = export_to_pdf(metrics_dict)
    st.success(f"Report exported to {filepath}")