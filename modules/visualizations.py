import matplotlib.pyplot as plt

def plot_cumulative_returns(cumulative_returns):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(cumulative_returns, label = "Portfolio")
    ax.set_title("Cumulative Returns Over Time")
    ax.set_ylabel("Cumulative Returns")
    ax.legend()
    return fig
  
def plot_allocation(tickers, weights):
    fig, ax = plt.subplots()
    ax.pie(weights, labels=tickers, autopct='%1.1f%%', startangle=90)
    ax.set_title("Portfolio Allocation")
    return fig

def plot_drawdown(drawdown):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.fill_between(drawdown.index, drawdown.values, color='red', alpha=0.4)
    ax.set_title("Drawdown Over Time")
    ax.set_ylabel("Drawdown")
    return fig

