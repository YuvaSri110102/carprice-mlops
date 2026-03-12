import pandas as pd
import logging
import sys
import os

# Add project root to path to allow importing from 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.data.validate import validate_columns
from src.data.preprocess import preprocess_data

logging.basicConfig(level=logging.INFO)

def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from given path
    """
    try:
        logging.info(f"Loading dataset from {path}")
        df = pd.read_csv(path)
        logging.info(f"Dataset loaded successfully with shape {df.shape}")
        validate_columns(df)
        return df

    except Exception as e:
        logging.error("Error loading dataset")
        raise e

if __name__ == "__main__":

    data_path = "data/raw/cardekho_dataset.csv"
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)