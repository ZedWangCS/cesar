import pandas as pd
from pathlib import Path

"""def load_data() -> pd.DataFrame:
    #load data from csv files
    data_dir = Path(__file__).parent.parent / "data"
    csv_files = list(data_dir.glob("*.csv"))
    df = pd.concat([pd.read_csv(f,low_memory= False) for f in csv_files])
    return df
"""


def load_data() -> pd.DataFrame:
    data_dir = Path(__file__).parent.parent / "data"
    csv_files = list(data_dir.glob("*.csv"))
    df = pd.concat([pd.read_csv(f, low_memory=False) for f in csv_files])
    print("Columns:", df.columns.tolist())
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # keep only 4 columns: surface number of rooms price and department code
    df = df[["surface_reelle_bati", "nombre_pieces_principales", "valeur_fonciere","code_departement", "type_local"]].copy()

    

    

    # convert columns to numeric and handle errors to coerce them to NaN
    df = df[df["type_local"].isin(["Appartement", "Maison"])] # keep only apartments and houses
    df["valeur_fonciere"] = pd.to_numeric(df["valeur_fonciere"].astype(str).str.replace(",", "."), errors="coerce")
    df["surface_reelle_bati"] = pd.to_numeric(df["surface_reelle_bati"], errors="coerce")
    df["nombre_pieces_principales"] = pd.to_numeric(df["nombre_pieces_principales"], errors="coerce")
    df["code_departement"] = pd.to_numeric(df["code_departement"], errors="coerce") #in fact this column is not numeric but we will keep it as numeric for simplicity
    
    df = df.drop(columns=["type_local"])
    
    # drop missing values
    df = df.dropna()
    
    # filter out the abnormal values
    df = df[df["valeur_fonciere"] > 0]
    df = df[df["surface_reelle_bati"] > 0]
    df = df[df["nombre_pieces_principales"] > 0]
    
    
    return df

if __name__ == "__main__":
    df = load_data()
    print(f"Raw data: {len(df)} rows")
    df = clean_data(df)
    print(f"Clean data: {len(df)} rows")
    print(df.describe())