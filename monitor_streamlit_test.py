import streamlit as st
import pandas as pd
from datetime import datetime
import time

def read_data():
    read = True
    while read:
        try:
            data = pd.read_pickle("prices.pkl")
            read = False
        except:
            pass
    return data

def tail(item):
    return item[14:]

prices = read_data()
tickers = st.multiselect("Seleccione instrumentos", 
                         prices.index.tolist(), 
                         prices.index.tolist(), 
                         format_func=tail)
update_bt = st.checkbox("Actualización continua")
refresh_bt = st.empty()
holder = st.empty()
table = st.empty()


def show_table():
    global prices, table,tickers
    holder.text(datetime.now())
    prices = read_data()
    table.table(prices.loc[tickers])

show_table()

    
if update_bt:
    time_step = refresh_bt.slider("Segundos para actualizar", 1, 300)
    while True:
        show_table()
        time.sleep(time_step)
else:
    if refresh_bt.button("Refrescar"):
        show_table()