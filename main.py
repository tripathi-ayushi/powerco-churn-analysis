from src.data_loader import load_all_data
from src.eda import basic_info, plot_distributions
from src.feature_engineering import add_price_features
from src.modeling import train_random_forest

CLIENT_DATA_PATH = "data/client_data.csv"
PRICE_DATA_PATH = "data/price_data.csv"

def main():
    client_df, price_df = load_all_data(CLIENT_DATA_PATH, PRICE_DATA_PATH)

    # EDA summary
    basic_info(client_df, "Client Data")
    basic_info(price_df, "Price Data")

    # EDA visualizations
    plot_distributions(client_df, "client")
    plot_distributions(price_df, "price")

    # Feature Engineering
    client_df = add_price_features(client_df)
    print("\n🔧 Added price sensitivity features:")
    print(client_df[[
        "price_per_unit_energy_peak",
        "price_per_unit_energy_off_peak",
        "price_spread",
        "price_to_net_margin_ratio",
        "price_sensitivity_score"
    ]].head())

    # Modeling
    feature_cols = [
        "price_per_unit_energy_peak",
        "price_per_unit_energy_off_peak",
        "price_spread",
        "price_to_net_margin_ratio",
        "price_sensitivity_score"
    ]

    train_random_forest(client_df, feature_cols)


if __name__ == "__main__":
    main()
