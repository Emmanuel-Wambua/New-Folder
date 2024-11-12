import yfinance as yf

content=[]

aapl = yf.Ticker("AAPL")

earnings = aapl.history(period="1mo")

content.append(earnings)

for info in content:
    data = {
        "Date":info["Date"],
        "Low":info["Low"],
        "High":info["High"],
        "Volume":info["Volume"],
    }

    print(info["Low"])
    print(info["High"])
    print(info["Volume"])