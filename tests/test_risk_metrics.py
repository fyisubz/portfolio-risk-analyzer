import pandas as pd
import numpy as np
from modules.risk_metrics import calculate_portfolio_metrics

def test_calculate_metrics():
    np.random.seed(0)
    data = pd.DataFrame(np.random.randn(100, 2)/100, columns=["A", "B"])
    weights = [0.5, 0.5]
    pr, cr, ar, vol, sr = calculate_portfolio_metrics(data, weights)
    assert isinstance(ar, float)
    assert isinstance(vol, float)