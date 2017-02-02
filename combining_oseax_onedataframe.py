""" The purpose of this code is simply to collect all data, for adjusted prices in Norwegian stocks, into a single CSV for further operations. 
To do this, simply execute the whole script. If you would like to collect other data, e.g., the closing price, volume, or otherwise; simply change 'Adj Close' to 'Close', 'Volume', or otherwise.
Good luck."""


import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import lxml
import csv

def compile_data():
    
    with open("oseax_ol.pickle","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv("Norwegian_stocks/{}.csv".format(ticker))
            df.set_index('Date',inplace=True)
            df.rename(columns = {'Adj Close':ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
            
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
            
                if count % 10 == 0:
                    print(count)
        except:
            try:
                pd.read_csv("Norwegian_stocks/'{}.OL'.csv".format(ticker))
                df.set_index('Date',inplace=True)
                df.rename(columns = {'Adj Close':ticker}, inplace=True)
                df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
                    
                if main_df.empty:
                    main_df = df
                else:
                    main_df = main_df.join(df, how='outer')
                    
                    if count % 10 == 0:
                        print(count)
            except:
                print("Failure")
    print(main_df.head())
    main_df.to_csv('OSEAX_joined_adjustedcloses.csv')
    
    
def compile_data2():
    
    with open("oseax_norm.pickle","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv("Norwegian_stocks/{}.csv".format(ticker))
            df.set_index('Date',inplace=True)
            df.rename(columns = {'Adj Close':ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
            
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
            
                if count % 10 == 0:
                    print(count)
        except:
            try:
                pd.read_csv("Norwegian_stocks/'{}.OL'.csv".format(ticker))
                df.set_index('Date',inplace=True)
                df.rename(columns = {'Adj Close':ticker}, inplace=True)
                df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
                    
                if main_df.empty:
                    main_df = df
                else:
                    main_df = main_df.join(df, how='outer')
                    
                    if count % 10 == 0:
                        print(count)
            except:
                print("Failure")
    print(main_df.head())
    main_df.to_csv('OSEAX_joined_adjustedcloses.csv')

    
def compile_data3():
    
    with open("oseaxx_norm.pickle","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv("Norwegian_stocks/{}.csv".format(ticker))
            df.set_index('Date',inplace=True)
            df.rename(columns = {'Adj Close':ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
            
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
            
                if count % 10 == 0:
                    print(count)
        except:
            try:
                pd.read_csv("Norwegian_stocks/'{}.OL'.csv".format(ticker))
                df.set_index('Date',inplace=True)
                df.rename(columns = {'Adj Close':ticker}, inplace=True)
                df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
                    
                if main_df.empty:
                    main_df = df
                else:
                    main_df = main_df.join(df, how='outer')
                    
                    if count % 10 == 0:
                        print(count)
            except:
                print("Failure")
    print(main_df.head())
    main_df.to_csv('OSEAX_joined_adjustedcloses.csv')

def compile_data4():
    
    with open("oseaxx_ol.pickle","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv("Norwegian_stocks/{}.csv".format(ticker))
            df.set_index('Date',inplace=True)
            df.rename(columns = {'Adj Close':ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
            
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
            
                if count % 10 == 0:
                    print(count)
        except:
            try:
                pd.read_csv("Norwegian_stocks/'{}.OL'.csv".format(ticker))
                df.set_index('Date',inplace=True)
                df.rename(columns = {'Adj Close':ticker}, inplace=True)
                df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
                    
                if main_df.empty:
                    main_df = df
                else:
                    main_df = main_df.join(df, how='outer')
                    
                    if count % 10 == 0:
                        print(count)
            except:
                print("Failure")
    print(main_df.head())
    main_df.to_csv('OSEAX_joined_adjustedcloses.csv')
    

def compiler_master():
    try:
        compile_data()
    except:
        try:
            compile_data2()
        except:
            try:
                compile_data3()
            except:
                try:
                    compile_data4()
                except:
                    print("Error")

                    
compiler_master()
