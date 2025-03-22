import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """Load a CSV file from the given path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    print(f"Loaded {os.path.basename(file_path)} with shape {df.shape}")
    return df


def load_all_data(client_path: str, price_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load both client and price datasets."""
    client_df = load_data(client_path)
    price_df = load_data(price_path)
    return client_df, price_df
