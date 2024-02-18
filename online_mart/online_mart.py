# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:39:01 2024

@author: Miraz
"""

import pandas as pd

orders_data = pd.read_csv('data/ORDERS.csv', encoding='latin1')
orders_data = orders_data.rename(columns={
        'ROWID':'ROW_ID',
        'ORDERID':'ORDER_ID',
        'ORDERDATE':'ORDER_DATE',
        'ORDERPRIOTORITY':'ORDER_PRIORITY',	
        'ORDERQUANTITY':'ORDER_QUANTITY',
        'SALES':'SALES',
        'DISCOUNT':'DISCOUNT',
        'SHIPMODE':'SHIP_MODE',
        'PROFIT':'PROFIT',
        'UNITPRICE':'UNIT_PRICE',
        'SHIPPINGCOSTS':'SHIPPING_COST',
        'CUSTOMERNAME':'CUSTOMER_NAME',
        'PROVINCE':'STATE',
        'REGION':'REGION',
        'CUSTOMERSEGMENT':'CUSTOMER_SEGMENT',	
        'PRODUCTCATEGORY':'PRODUCT_CATEGORY',	
        'PRODUCTSUBCATEGORY':'PRODUCT_SUBCATEGORY',	
        'PRODUCTNAME':'PRODUCT_NAME',
        'PRODUCTCONTAINER':'PRODUCT_CONTAINER',	
        'PRODUCTBASEMARGIN':'PRODUCT_BASE_MARGIN',	
        'SHIPDATE':'SHIP_DATE',	
        'DATASET':'DATASET'
    })

state_mapping = {
        'Nunavut':'NY', 
        'Northwest Territories':'CA', 
        'Prince Edward Island':'IL', 
        'Manitoba':'TX',
        'British Columbia':'AZ', 
        'Nova Scotia':'PA', 
        'Ontario':'FL', 
        'Newfoundland':'OH',
        'Quebec':'NC',
        'New Brunswick':'IN', 
        'Saskachewan':'WA',
        'Yukon':'CO', 
        'Alberta':'OK'
    }


orders_data.info()
orders_data['STATE'] = orders_data['STATE'].replace(state_mapping)

orders_data.drop(columns=['DATASET','ROW_ID', 'REGION'], inplace=True)

orders_data['COST'] = orders_data['UNIT_PRICE'] * orders_data['ORDER_QUANTITY']
orders_data['DISCOUNT'] = orders_data['DISCOUNT'] * 100

orders_data['PRODUCT_BASE_MARGIN'].fillna(0, inplace=True)
orders_data['PRODUCT_BASE_MARGIN'] = orders_data['PRODUCT_BASE_MARGIN'] * 100

orders_data_list = orders_data['PRODUCT_CONTAINER'].str.split(' ', expand=True)
orders_data['PACKAGE_SIZE'] = orders_data_list[0]
orders_data['PACKAGE_TYPE'] = orders_data_list[1]


orders_data.to_csv('data/cleaned_orders.csv', index=False)