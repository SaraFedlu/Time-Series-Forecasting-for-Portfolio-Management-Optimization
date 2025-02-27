import yfinance as yf
import pandas as pd

def fetch_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

# Define the date range
start_date = "2015-01-01"
end_date = "2025-01-31"

# Fetch data for TSLA, BND, and SPY
tsla_data = fetch_data("TSLA", start_date, end_date)
bnd_data = fetch_data("BND", start_date, end_date)
spy_data = fetch_data("SPY", start_date, end_date)

# Save to CSV
tsla_data.to_csv("data/TSLA_data.csv", index=False)
bnd_data.to_csv("data/BND_data.csv", index=False)
spy_data.to_csv("data/SPY_data.csv", index=False)

print("Data fetching complete. Files saved as CSV.")