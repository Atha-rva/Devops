import requests

API_KEY = "TVPF92WQHCHKLELW"  # Get a API Key  Step - 1

# API URL 

# Server URL 

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"   # Server URL 



# Query will Change EveryTime 

# query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"     # Query Can be Change 


# print(url+query)


def get_stock_market_data(symbol , is_time_series):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"     # Query Can be Change 
    print(url+query)
    response = requests.get(url=url+query)
    # print(response.json())

    for key,value in response.json().items():
        if key == "Meta Data":
            if is_time_series:
                print(key,value)
            else: 
                if key == "Time Series (Daily)":
                    continue



is_time_series = True
symbol = input("Enter the Company stock market Symbol  Eg :- IBM , AMZN")
get_stock_market_data(symbol , is_time_series)