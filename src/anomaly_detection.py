from scipy import stats
import numpy as np

def detect_amount_outliers(df, column="montant"):

    if column not in df.columns:
        return df

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df["is_anomaly_amount"] = ((df[column] < lower) | (df[column] > upper)).astype(int)

    print(f"Montants aberrants : {df['is_anomaly_amount'].sum()}")
    return df


def detect_credit_score_outliers(df, column="score_credit_client", method="IQR"):

    if column not in df.columns:
        return df

    df["is_anomaly_score"] = 0

    
    df.loc[(df[column] < 0) | (df[column] > 850), "is_anomaly_score"] = 1

    if method == "IQR":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df.loc[(df[column] < lower) | (df[column] > upper), "is_anomaly_score"] = 1

    elif method == "Z":
        z = np.abs(stats.zscore(df[column].dropna()))
        df.loc[df[column].notna(), "is_anomaly_score"] = (z > 3).astype(int)

    print(f"Scores aberrants : {df['is_anomaly_score'].sum()}")
    return df


def create_final_anomaly_flag(df):

    anomaly_cols = ["is_anomaly_amount", "is_anomaly_score"]

    df["is_anomaly"] = df[anomaly_cols].max(axis=1)

    print(f"Total anomalies : {df['is_anomaly'].sum()}")
    return df