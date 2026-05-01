import yfinance as yf
import datetime
import os

FILE_NAME = "stock_data.csv"

def fetch_data():
    stock = yf.Ticker("TCS.NS")  # Change stock here
    data = stock.history(period="1d")

    if data.empty:
        print("No data found (market closed or invalid symbol)")
        return

    today = datetime.date.today()

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a") as f:
        if not file_exists:
            f.write("Date,Open,High,Low,Close,Volume\n")

        for index, row in data.iterrows():
            line = f"{today},{row['Open']},{row['High']},{row['Low']},{row['Close']},{row['Volume']}\n"
            f.write(line)

    print("✅ Data written successfully")

if __name__ == "__main__":
    fetch_data()