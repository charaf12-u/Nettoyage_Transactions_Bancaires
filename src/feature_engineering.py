import pandas as pd

def extract_temporal_features(df):

    df["year"] = df["date_transaction"].dt.year.astype(int)
    df["month"] = df["date_transaction"].dt.month.astype(int)
    df["quarter"] = df["date_transaction"].dt.quarter.astype(int)
    df["weekday"] = df["date_transaction"].dt.dayofweek.astype(int)


    return df


def validate_montants_eur(df):
    df["montant_eur_verifie"] = df["montant"] / df["taux_change_eur"]
    df["montant_eur_diff"]    = df["montant_eur"] - df["montant_eur_verifie"]
    df["montant_eur_flag"]    = df["montant_eur_diff"].abs() > 0.01
    return df


def categorize_risk(df):

    def risk(x):
        if x >= 700:
            return "Low"
        elif x >= 580:
            return "Medium"
        else:
            return "High"

    df["categorie_risque"] = df["score_credit_client"].apply(risk)

    return df