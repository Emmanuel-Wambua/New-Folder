import sqlite
import yfinance as yf

db = sqlite.connect('stocks_db.db')

cursor = db.cursor

class GetData:
    def __init__(self, ticker):
        self.ticker = ticker

    def gettin_data(self):
        stock = yf.Ticker(self.ticker)
        earnings = stock.history(period="max")
        print(earnings)

finances = GetData("AAPL")
butt = finances.gettin_data()
print(butt)

cursor.execute('''
    CREATE TABLE Stockings(
        Date int NOT NULL,   
        Open int NOT NULL,   
        High int NOT NULL,   
        Low int NOT NULL,   
        Close int NOT NULL,   
        Volume int NOT NULL,   
        Dividends int NOT NULL,   
        Stock Splits int NOT NULL) 
    )
    INSERT INFO Stockings(Date,Open,High,Low,Close,Volume,Dividends,Stocks)
        VALUES(butt)
''')

db.commit()