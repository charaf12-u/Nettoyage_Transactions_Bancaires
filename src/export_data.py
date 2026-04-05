def final_validation(df, critical_cols):

    print("\nValeurs manquantes critiques:")
    print(df[critical_cols].isnull().sum())

    print("\nTypes:")
    print(df.dtypes)

    print("\nRésumé:")
    print(df.describe())


def export_dataset(df):
    df.to_csv("output/financecore_clean.csv", index=False)
    print("Export OK")

    