import pandas as pd
from datetime import datetime
import pyRofex
import time

instrumentos = [
    "MERV - XMEV - AL29 - 48hs",
    "MERV - XMEV - AL30 - 48hs",
    "MERV - XMEV - AL35 - 48hs",
    "MERV - XMEV - AE38 - 48hs",
    "MERV - XMEV - AL41 - 48hs",
    "MERV - XMEV - GD29 - 48hs",
    "MERV - XMEV - GD30 - 48hs",
    "MERV - XMEV - GD35 - 48hs",
    "MERV - XMEV - GD38 - 48hs",
    "MERV - XMEV - GD41 - 48hs",
    "MERV - XMEV - GD46 - 48hs",
    "MERV - XMEV - AL29D - 48hs",
    "MERV - XMEV - AL30D - 48hs",
    "MERV - XMEV - AL35D - 48hs",
    "MERV - XMEV - AE38D - 48hs",
    "MERV - XMEV - AL41D - 48hs",
    "MERV - XMEV - GD29D - 48hs",
    "MERV - XMEV - GD30D - 48hs",
    "MERV - XMEV - GD35D - 48hs",
    "MERV - XMEV - GD38D - 48hs",
    "MERV - XMEV - GD41D - 48hs",
    "MERV - XMEV - GD46D - 48hs",
    "MERV - XMEV - AL29 - CI",
    "MERV - XMEV - AL30 - CI",
    "MERV - XMEV - AL35 - CI",
    "MERV - XMEV - AE38 - CI",
    "MERV - XMEV - AL41 - CI",
    "MERV - XMEV - GD29 - CI",
    "MERV - XMEV - GD30 - CI",
    "MERV - XMEV - GD35 - CI",
    "MERV - XMEV - GD38 - CI",
    "MERV - XMEV - GD41 - CI",
    "MERV - XMEV - GD46 - CI",
    "MERV - XMEV - AL29D - CI",
    "MERV - XMEV - AL30D - CI",
    "MERV - XMEV - AL35D - CI",
    "MERV - XMEV - AE38D - CI",
    "MERV - XMEV - AL41D - CI",
    "MERV - XMEV - GD29D - CI",
    "MERV - XMEV - GD30D - CI",
    "MERV - XMEV - GD35D - CI",
    "MERV - XMEV - GD38D - CI",
    "MERV - XMEV - GD41D - CI",
    "MERV - XMEV - GD46D - CI",
    "MERV - XMEV - TO23 - 48hs",
    "MERV - XMEV - TO26 - 48hs",
    "MERV - XMEV - PARP - 48hs",
    "MERV - XMEV - TX26 - 48hs",
    "MERV - XMEV - TX28 - 48hs",
    "MERV - XMEV - TC23 - 48hs"
]


prices = pd.DataFrame(columns=["Last", "Bid", "Ask"], index=instrumentos).fillna(0)
prices.index.name = "Instrumento"

# Initialize the environment

pyRofex.initialize(user="aqui_va_tu_usuario",
                   password="aqui_va_tu_contraseña",
                   account="aqui_va_tu_cuenta",
                   environment=pyRofex.Environment.LIVE)

def market_data_handler(message):
    global prices
    prices.loc[message["instrumentId"]["symbol"]] = [message["marketData"]["LA"]["price"], 
                                                             message["marketData"]["OF"][0]["price"],
                                                             message["marketData"]["BI"][0]["price"]]

# Initialize Websocket Connection with the handlers
pyRofex.init_websocket_connection(market_data_handler=market_data_handler)


# Subscribes to receive market data messages
pyRofex.market_data_subscription(
    tickers=instrumentos,
    entries=[
        pyRofex.MarketDataEntry.LAST,
        pyRofex.MarketDataEntry.BIDS,
        pyRofex.MarketDataEntry.OFFERS
    ]
)

while True:
    print(time.strftime("%D %H:%M:%S", time.localtime()))
    prices.to_pickle("prices.pkl")
    time.sleep(1)
