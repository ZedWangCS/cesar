import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from model.data_processing import load_data, clean_data

def train():
    # load and clean data
    df = load_data()
    df = clean_data(df)
    print(f"Training on {len(df)} rows")

    X = df[["surface_reelle_bati", "nombre_pieces_principales","code_departement"]]
    y = df["valeur_fonciere"]

    # using random forest for regression
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)

    # save the model
    model_path = Path(__file__).parent / "model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train()