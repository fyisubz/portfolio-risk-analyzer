import numpy as np

def calculate_portfolio_metrics(returns, weights):
    portfolio_returns = returns.dot(weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()

    volatility = portfolio_returns.std()*np.sqrt(252)
    avg_return = portfolio_returns.mean()*252
    sharpe_ratio = avg_return/volatility if volatility != 0 else 0

    return portfolio_returns, cumulative_returns, avg_return, volatility, sharpe_ratio

def value_at_risk(portfolio_returns, confidence = 0.05):
    return np.percentile(portfolio_returns, 100 * confidence)

def max_drawdown(cumulative_returns):
    cum_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns-cum_max)/cum_max
    max_dd = drawdown.min()
    return drawdown, max_dd