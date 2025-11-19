import pandas as pd
from app.type_inferer import infer_column_type

def test_infer_int_column():
    series = pd.Series([1, 2, 3])
    assert infer_column_type(series) == "INT"

def test_infer_float_column():
    series = pd.Series([1.1, 2.5, 3.0])
    assert infer_column_type(series) == "FLOAT"

def test_infer_string_column():
    series = pd.Series(["apple", "banana", "cherry"])
    result = infer_column_type(series)
    assert result.startswith("VARCHAR(")

def test_infer_date_column():
    series = pd.to_datetime(pd.Series(["2023-01-01", "2023-02-01"]))
    assert infer_column_type(series) == "DATETIME"