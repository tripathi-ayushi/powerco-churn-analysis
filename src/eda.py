import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def basic_info(df: pd.DataFrame, name: str):
    print(f"\n📊 Dataset: {name}")
    print("-" * 40)
    print("Shape:", df.shape)
    print("\nColumn Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDescriptive Statistics:")
    print(df.describe(include='all'))

def plot_distributions(df: pd.DataFrame, name: str, save_dir="outputs"):
    numeric_cols = df.select_dtypes(include=['number']).columns
    os.makedirs(save_dir, exist_ok=True)

    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"{name} - Distribution of {col}")
        plt.tight_layout()
        save_path = os.path.join(save_dir, f"{name}_{col}_dist.png")
        plt.savefig(save_path)
        plt.close()
