import pandas as pd

def add_price_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Avoid division by zero
    df["price_per_unit_energy_peak"] = df["forecast_price_energy_peak"] / df["forecast_cons_12m"].replace(0, 1)
    df["price_per_unit_energy_off_peak"] = df["forecast_price_energy_off_peak"] / df["forecast_cons_12m"].replace(0, 1)
    
    # Spread and ratio features
    df["price_spread"] = df["forecast_price_energy_peak"] - df["forecast_price_energy_off_peak"]
    df["price_to_net_margin_ratio"] = (
        (df["forecast_price_energy_peak"] + df["forecast_price_energy_off_peak"]) / df["net_margin"].replace(0, 1)
    )

    # Composite price sensitivity score (engineered intuition)
    df["price_sensitivity_score"] = df["price_spread"] * df["price_per_unit_energy_peak"]

    return df
