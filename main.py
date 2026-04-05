from src.import_data import read_df
from src.data_cleaning import cleaning_data
from src.anomaly_detection import *
from src.feature_engineering import *
from src.export_data import final_validation, export_dataset

try:
    # --> import data
    df = read_df()

    print("Shape du DataFrame initial : ", df.shape)

    # --> cleaning data
    df = cleaning_data(df)

    # --> Anomaly detection
    df = detect_amount_outliers(df)
    df = detect_credit_score_outliers(df)
    df = create_final_anomaly_flag(df)

    # --> Feature engineering
    df = extract_temporal_features(df)
    df = validate_montants_eur(df)
    df = categorize_risk(df)

    # --> Validation
    final_validation(df, critical_cols=[
        "transaction_id",
        "client_id",
        "montant",
        "date_transaction"
    ])

    # --> Export
    export_dataset(df)

    print("Shape du DataFrame final : ", df.shape)
    print("le nomber duplicated :",df.duplicated(subset="transaction_id").sum())
    print(df.isnull().sum()[df.isnull().sum() > 0])
    print("\nPipeline exécuté avec succès")

except Exception as e:
    print("[ERREUR] :", e)