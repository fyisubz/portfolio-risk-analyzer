from modules.data_loader import get_data
import pandas as pd

def test_get_data():
    df = get_data(["AAPL"], "2020-01-01", "2020-01-10")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty