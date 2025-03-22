from src.data_loader import load_all_data
from src.eda import basic_info, plot_distributions

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

if __name__ == "__main__":
    main()
