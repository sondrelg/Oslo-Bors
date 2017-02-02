""" This is an automated script for downloading Norwegian stock data for the stocks listed on Oslo Børs and Oslo Axess.
The stock tickers are extracted from the URL's below:

Oslo Børs: http://www.netfonds.no/quotes/kurs.php
Oslo Axess: http://www.netfonds.no/quotes/kurs.php?exchange=OAX

Please note that because Norwegian securities tend to require an .OL-suffix when using yahoo finance (which we are), there is a need to run the process
with and without an ".OL"-suffix for both exchanges.

Given that you have the required packages installed, you should be able to run the entire script in one go.
The relevant CSV-files will be created in a folder called Norwegian_Stocks in your working directory.
"""

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

def save_oslobors_tickers_ol():
    try:
        ol = ".OL"
        resp = requests.get('http://www.netfonds.no/quotes/kurs.php')   
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class':'mbox'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            tickers.append(ticker+ol)          
        with open("oseax_ol.pickle","wb") as f:
            pickle.dump(tickers,f)
        print(tickers)
        return tickers
    except:
        pass


def get_data_from_yahoo1(reload_oseax=False):
    if reload_oseax:
        tickers = save_oslobors_tickers_ol()
    else:
        with open("oseax_ol.pickle","rb") as f:                                
            tickers = pickle.load(f)
    if not os.path.exists('Norwegian_stocks'):
        os.makedirs('Norwegian_stocks')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,2,1)
    for ticker in tickers:
#        for i in tickers:
            try:
                if not os.path.exists('Norwegian_stocks/{}.csv'.format(ticker)):
                    df = web.DataReader(ticker, 'yahoo',start,end)
                    df.to_csv('Norwegian_stocks/{}.csv'.format(ticker))
                    print("Downloaded "+ticker)
                else:
                    print('Already have {}'.format(ticker))
            except:
                print("     Requires normal ticker")
    print(ticker)

    
def save_oslobors_tickers_norm():
    try:
        resp = requests.get('http://www.netfonds.no/quotes/kurs.php')   ## ACTIVATE THIS FOR OSLO BØRS                         ## 1
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class':'mbox'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            tickers.append(ticker)             
        with open("oseax_norm.pickle","wb") as f:
            pickle.dump(tickers,f)
        print(tickers)
        return tickers
    except:
        pass


def get_data_from_yahoo2(reload_oseax=False):
    if reload_oseax:
        tickers = save_oslobors_tickers_norm()
    else:
        with open("oseax_norm.pickle","rb") as f:                                
            tickers = pickle.load(f)
    if not os.path.exists('Norwegian_stocks'):
        os.makedirs('Norwegian_stocks')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,2,1)
    for ticker in tickers:
#        for i in tickers:
            try:
                if not os.path.exists('Norwegian_stocks/{}.csv'.format(ticker)):
                    df = web.DataReader(ticker, 'yahoo',start,end)
                    df.to_csv('Norwegian_stocks/{}.csv'.format(ticker))
                    print("Downloaded "+ticker)
                else:
                    print('Already have {}'.format(ticker))
            except:
                print("     Requires OL-suffix")
    print(ticker)

    
    

def save_osloaxess_tickers_ol():
    try:
        ol = ".OL"
        resp = requests.get('http://www.netfonds.no/quotes/kurs.php?exchange=OAX') 
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class':'mbox'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            tickers.append(ticker+ol)         
        with open("oseaxx_ol.pickle","wb") as f:
            pickle.dump(tickers,f)
        print(tickers)
        return tickers
    except:
        pass


def get_data_from_yahoo3(reload_oseax=False):
    if reload_oseax:
        tickers = save_osloaxess_tickers_ol()
    else:
        with open("oseaxx_ol.pickle","rb") as f:                                
            tickers = pickle.load(f)
    if not os.path.exists('Norwegian_stocks'):
        os.makedirs('Norwegian_stocks')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,2,1)
    for ticker in tickers:
#        for i in tickers:
            try:
                if not os.path.exists('Norwegian_stocks/{}.csv'.format(ticker)):
                    df = web.DataReader(ticker, 'yahoo',start,end)
                    df.to_csv('Norwegian_stocks/{}.csv'.format(ticker))
                    print("Downloaded "+ticker)
                else:
                    print('Already have {}'.format(ticker))
            except:
                print("     Requires normal ticker")
    print(ticker)
    

def save_osloaxess_tickers_norm():
    try:
        resp = requests.get('http://www.netfonds.no/quotes/kurs.php?exchange=OAX')            
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class':'mbox'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            tickers.append(ticker)        
        with open("oseaxx_norm.pickle","wb") as f:
            pickle.dump(tickers,f)
        print(tickers)
        return tickers
    except:
        pass


def get_data_from_yahoo4(reload_oseax=False):
    if reload_oseax:
        tickers = save_osloaxess_tickers_norm()
    else:
        with open("oseaxx_norm.pickle","rb") as f:                                
            tickers = pickle.load(f)
    if not os.path.exists('Norwegian_stocks'):
        os.makedirs('Norwegian_stocks')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,2,1)
    for ticker in tickers:
#        for i in tickers:
            try:
                if not os.path.exists('Norwegian_stocks/{}.csv'.format(ticker)):
                    df = web.DataReader(ticker, 'yahoo',start,end)
                    df.to_csv('Norwegian_stocks/{}.csv'.format(ticker))
                    print("Downloaded "+ticker)
                else:
                    print('Already have {}'.format(ticker))
            except:
                print("     Requires OL-suffix")
    print(ticker)
    
""" Below are the four functions. You may run the whole script, and these should run sequentially. The process may take up to 10 minutes in total. """
    
#Normal tickers - Oslo Børs
save_oslobors_tickers_norm()
get_data_from_yahoo2()

#OL-suffixed toclers - Oslo Børs
save_oslobors_tickers_ol()
get_data_from_yahoo1()

#Normal tickers - Oslo Axess
save_osloaxess_tickers_norm()
get_data_from_yahoo4()
    
#OL-suffixed tickers - Oslo Axess
save_osloaxess_tickers_ol()
get_data_from_yahoo3()





    
    