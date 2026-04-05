import pandas as pd

def cleaning_data(df):

    df = df.copy()

    # --> delet doubles
    df = df.drop_duplicates(subset="transaction_id", keep="first")

    # --> type date
    df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")
    df = df.dropna(subset=["date_transaction"])

    # --> modifier montant
    df["montant"] = (
        df["montant"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    # --> modifier solde
    df["solde_avant"] = (
        df["solde_avant"]
        .astype(str)
        .str.replace(" EUR", "", regex=False)
    )
    df["solde_avant"] = pd.to_numeric(df["solde_avant"], errors="coerce")

    # --> modifier taux_interet
    df["taux_interet"] = df["taux_interet"].fillna(0)

    # --> type string
    string_cols = ["transaction_id","client_id", "devise","segment_client","agence","categorie",
                   "produit","type_operation","statut"]
    StringType(df , string_cols)

    df["devise"] = df["devise"].str.upper()
    df["segment_client"] = df["segment_client"].str.capitalize()
    df["statut"] = df["statut"].str.capitalize()
    df["type_operation"] = df["type_operation"].str.capitalize()


    # --> missing values
    if "score_credit_client" in df.columns:
        df["score_credit_client"] = df["score_credit_client"].fillna(
            df["score_credit_client"].median()
        )

    if "segment_client" in df.columns:
        df["segment_client"] = df["segment_client"].fillna(
            df["segment_client"].mode()[0]
        )

    if "agence" in df.columns:
        df["agence"] = df["agence"].fillna(
            df["agence"].mode()[0]
        )

    print("Cleaning terminé")
    return df


def StringType(df , columns) :
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower().astype("string")
    