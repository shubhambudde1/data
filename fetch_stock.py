import yfinance as yf
import datetime

def fetch_data():
    stock = yf.Ticker("TCS.NS")  # Change stock symbol
    data = stock.history(period="1d")

    today = datetime.date.today()
    
    with open("stock_data.csv", "a") as f:
        for index, row in data.iterrows():
            f.write(f"{today},{row['Open']},{row['High']},{row['Low']},{row['Close']},{row['Volume']}\n")

if __name__ == "__main__":
    fetch_data()