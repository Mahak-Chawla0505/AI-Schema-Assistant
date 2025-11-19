def infer_column_type(series):
    if series.dropna().apply(lambda x: isinstance(x, int)).all():
        return "INT"
    elif series.dropna().apply(lambda x: isinstance(x, float)).all():
        return "FLOAT"
    elif series.dropna().apply(lambda x: "date" in str(type(x)).lower()).any():
        return "DATETIME"
    else:
        max_len = series.dropna().astype(str).map(len).max()
        return f"VARCHAR({max_len})"