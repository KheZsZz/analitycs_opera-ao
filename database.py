import pandas as pd 

def Load_data(ID_DB:str, ID_SHEET:str):
    df = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/{ ID_DB }/export?format=csv&gid={ ID_SHEET }"
        , encoding="utf-8")
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce", dayfirst=True)
    df = df.dropna(subset=["Data"])
    return df

