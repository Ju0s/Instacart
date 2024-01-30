# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

@st.cache_data
def load_orders_data():
    # orders data
    #original_file_path = './data/orders.csv'
    #new_file_path = './data/orders_random.csv'
    #df = pd.read_csv(original_file_path).dropna()
    
    # 난수 발생기에 seed 값 설정
    #seed_value = 100
    #np.random.seed(seed_value)

    # 무작위 행 추출
    #num_rows_to_extract = 100
    #orders_random = df.sample(num_rows_to_extract)
    #orders_random.to_csv(new_file_path)

    orders_random = pd.read_csv('./data/orders_random.csv')
    return orders_random

#def load_order_products_prior_data():
    # order_products_prior data
    #csv_file_path = './data/order_products__prior.csv'
    #order_products_prior = pd.read_csv(csv_file_path).dropna()

    #seed_value = 101
    #np.random.seed(seed_value)

    #num_rows_to_extract = 100
    #order_products_prior_random = order_products_prior.sample(num_rows_to_extract)

    #return order_products_prior_random

#def load_products_data():
    # products data
    #csv_file_path = './data/products.csv'
    #products = pd.read_csv(csv_file_path).dropna()

    #seed_value = 102
    #np.random.seed(seed_value)

    #num_rows_to_extract = 100
    #products_random = products.sample(num_rows_to_extract)

    #return products_random

def main():
    orders = load_orders_data()
    #order_products_prior = load_order_products_prior_data()
    #products = load_products_data()

    # 일별 주문량
    st.title("Daily Orders")
    daily_order_count = orders.groupby('order_dow').size().reset_index(name='count')
    fig1 = px.bar(daily_order_count, x='order_dow', y='count', labels={'order_dow': 'Day of Week', 'count': 'Number of Orders'},
                title='Daily Order Count', color_discrete_sequence=['skyblue'])
    
    st.plotly_chart(fig1)

if __name__ == "__main__":
    main()