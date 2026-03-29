import pandas as pd

def read_df(file_path="data/bank-transactions.csv") :
    try : 
    
        # --> read data in csv
        df = pd.read_csv(file_path)
        
        print("Dataset loaded successfully")
        return df
    
    except FileNotFoundError as e :
        print("[ERREUR] : ", e)

    except Exception as e :
        print("[ERREUR] : ", e)