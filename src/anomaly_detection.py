from scipy import stats
import numpy as np

def detect_amount_outliers(df, column="montant"):
    
    # --> 
    if column not in df.columns:
        print(f"column {column} non trouve in df")
        return df

    # --> calcul quantile 
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # --> calculs les points de data anormalis
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # --> df par montant anormaliz
    df["is_anomaly"] = ((df[column] < lower_bound) | (df[column] > upper_bound)).astype(int)

    print(f"Nomber des montans anormaliz : {df['is_anomaly'].sum()}")

    return df



def detect_credit_score_outliers(df, column="score_credit_client", method="IQR"):
    

    if column not in df.columns:
        print(f"Colonne {column} introuvable")
        return df

    # --> crees un columns is_anomaly_score
    df["is_anomaly_score"] = 0

    # Détecter scores négatifs ou supérieurs à 850
    df.loc[(df[column] < 0) | (df[column] > 850), "is_anomaly_score"] = 1

    # --> pour la method IQR
    if method == "IQR":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df.loc[(df[column] < lower) | (df[column] > upper), "is_anomaly_score"] = 1

    # --> pour la method Z
    elif method == "Z":
        z_scores = np.abs(stats.zscore(df[column].dropna()))
        # index à mettre à jour dans le df
        df.loc[df[column].notna(), "is_anomaly_score"] = (z_scores > 3).astype(int)

    print(f"Scores aberrants détectés : {df['is_anomaly_score'].sum()} anomalies")

    return df

def create_final_anomaly_flag(df, anomaly_columns=None):
    

    if anomaly_columns is None:
        anomaly_columns = [col for col in df.columns if col.startswith("is_anomaly")]

    if not anomaly_columns:
        print("Aucune colonne d'anomalie trouvée")
        return df

    df["is_anomaly"] = df[anomaly_columns].max(axis=1)

    print(f"Flag final is_anomaly créé: {df['is_anomaly'].sum()} anomalies détectées")
    return df