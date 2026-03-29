import pandas as pd

def cleaning_data(df):

    df = df.copy()
    
    # --> calculs le nomber de columns avants cleaning
    N_avant = df.shape[0]

    # --> supprimes la doublon par transaction_id
    df = df.drop_duplicates(subset="transaction_id", keep="first")

    # --> modifier le format de date
    df["date_transaction"] = pd.to_datetime(
        df["date_transaction"], errors="coerce"
    )
    df["date_transaction"] = df["date_transaction"].dt.strftime("%Y-%m-%d %H:%M:%S")

    # --> modifier le types de montant
    df["montant"] = df["montant"].astype(str)
    df["montant"] = df["montant"].str.replace(",", ".", regex=False)
    df["montant"] = df["montant"].astype(float)

    # --> modifier le type de solde
    df["solde_avant"] = (
        df["solde_avant"]
        .astype(str)
        .str.replace(" EUR", "", regex=False)
    )
    df["solde_avant"] = pd.to_numeric(df["solde_avant"], errors="coerce")

    # --> transfaires les valeur de devise in upper 
    df["devise"] = df["devise"].str.upper()

    # --> transfaires les valeur de devise in capitalize
    df["segment_client"] = df["segment_client"].str.capitalize()

    # --> supprimes les ecepace in agence
    df["agence"] = df["agence"].str.strip()

    # --> imputer score_credit_client avec mediane
    if "score_credit_client" in df.columns:
        median_score = df["score_credit_client"].median()
        df["score_credit_client"] = df["score_credit_client"].fillna(median_score)

    # --> imputer segment_client avec le mode
    if "segment_client" in df.columns:
        mode_segment = df["segment_client"].mode()[0]
        df["segment_client"] = df["segment_client"].fillna(mode_segment)

    # --> imputer agence avec le mode
    if "agence" in df.columns:
        mode_agence = df["agence"].mode()[0]
        df["agence"] = df["agence"].fillna(mode_agence)


    # --> calculs le nomber de columns apres cleaning
    N_apres = df.shape[0]
    print(f"nomber des columns avants et apres le netwayage : {N_avant - N_apres}")

    return df


