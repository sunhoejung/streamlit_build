# -*- coding:utf-8 -*-

import streamlit as st
from streamlit_option_menu import option_menu
from stock.yfinance import run_stock
from estate.estate import real_estate
from call_data import call_data

def main():
    estate_data = call_data()
    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['부동산 정보', '미국 주식 정보'], 
                               icons=['file-bar-graph', 'bar-chart'], menu_icon="cast", default_index=1)
    if selected == "부동산 정보":
        real_estate(estate_data)
    elif selected == "미국 주식 정보":
         run_stock()
    else:
        print("error..")
        
if __name__ == "__main__":
    main()