''' 
Initialy created under the name Stock Analyzer Library, Version 2.0
https://github.com/StevenMedvetz/stock-analysis/blob/main/stock_analyzer.py
Date: March 13, 2023
Author: Steven Medvetz

Completly Modified in 2024 March and April by Nicolas Payen
add total returns calucaltion (including dividends) toDate and fromDate
add annualized returns calculations
add ablity to work with tickers from various exchanges
add various weighting method 
add various currency support and take into account exchange rate in returns 
add various indexes to easily benchmark the performance of a ticker 
modify Assets and Portfolio class
'''
import numpy as np
import yfinance as yf
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import random
import statistics 
import os
from PIL import Image
from plotly.subplots import make_subplots
from dateutil import relativedelta
from datetime import datetime


# Get the current working directory
#current_dir = "./Desktop/myPythonProjects/Portfoliotools/"
# Get the current working directory
current_dir = os.getcwd()
# Construct the file path to your JPEG image
image_path = os.path.join(current_dir, "Koi_logo3.png")
logo_img = Image.open("Koi_logo3.png")

pio.renderers.default = "browser"

#an Asset is a stock with its associated data for a given perdio
'''
A Asset is a group of assets
tickers : list of yahoo tickers associated with the assets
start_date : starting date of the analysis
end_date : end date of the analysis
refcurrency : currency used as reference to calculate returns (EUR or USD), EUR as default
riskfreeticker : ticker representing the risk-free rate, by default we use '^TNX' the 10 years US Treasury rate
withIndex is used to know if the portfolio should display the indexes for Benchmark
        if withIndex is false, it is then possible to give indexes in the tickers or create a portfolio of index. 
        To compare this portfolio with indexes uses the portfolio_benchmark_bench
show_graphs : display automatically graphs 
'''
class Asset:
    def __init__(self, tickers, start_date, end_date = datetime.today().strftime('%Y-%m-%d'), refcurrency=None, riskfreeticker = None, withindex=True, show_graphs=False, prtfname = None):
        
        self.prtfname = prtfname
        #standard indexes used to benchmark the portfolio
        #^TYX is 30 years US treasury bond ticker
        #^TNX is 10 years US treasury bond ticker
        #^FVX is 5 years US treasury bond ticker
        self.treasury_bonds_tickers = ['^TNX', '^FVX', '^TYX']
        self.index_symbols = ['^GSPC', '^DJI', '^IXIC', '^STOXX', '^RUT', '^N225', '^FCHI', '^AEX']
        #this is the index(es) we will use for benchmark
        # '^HSI', '000001.SS']
        self.tickers = tickers
        self.withindex = withindex
        if withindex:
            self.tickers_and_index = tickers + self.index_symbols 
        else:
            self.tickers_and_index = self.tickers
        self.end_date = end_date 
        
        #if start_date is unknown then we apply by default 5 years duration analysis
        self.start_date = start_date
        if start_date is None: 
            #calculate start of period
            calcdays = ( -5 * 365.25 )
            start_period = datetime.strptime(self.end_date, '%Y-%m-%d') + timedelta(days=calcdays)
            self.start_date = start_period.strftime("%Y-%m-%d") 

        # we adjust the risk free ticker based on the duration of the analysis
        if riskfreeticker is None:
            # Define your two dates
            # Convert the date strings to datetime objects
            date1 = datetime.strptime(self.start_date, '%Y-%m-%d')
            date2 = datetime.strptime(self.end_date, '%Y-%m-%d')
            duration = (date2-date1).days / 365.25
            if duration > 10:
                #30 years bond
                self.riskfreeticker = '^TYX'
            elif duration > 5:
                #10 years bond
                self.riskfreeticker = '^TNX'
            else:
                #5 years bond
                self.riskfreeticker = '^FVX'
        else:
            self.riskfreeticker = riskfreeticker      

        self.refcurrency = refcurrency
        self.adj = False
        #nicolas add this to store the data for all tickers
        self.assets_info_df = pd.DataFrame()
        self.assets_data_df = pd.DataFrame()
        #double tops and bottoms data
        self.double_bottoms_df = pd.DataFrame()
        self.double_tops_df = pd.DataFrame()
        #RSI data
        self.rsi_df = pd.DataFrame()
        #get PE ratio and market_cap
        self.pe_ratio_df = pd.DataFrame()
        self.market_cap_df= pd.DataFrame(columns=['MarketCap'])
        #create a df to store the results of the simple returns calculation
        self.simple_returns_df = pd.DataFrame()
        #create a df to store the results of the cumulated total returns calculation
        self.cumulative_returns_df = pd.DataFrame()
        #create a df to store the results of the toDate total returns calculation / same as cumulated total returns but different calculation method 
        self.todate_total_returns_df = pd.DataFrame()
        #create a df to store the results of the annualized toDate total returns calculation
        self.annualized_todate_total_returns_df = pd.DataFrame()
        #create a df to store the results of the fromDate total returns calculation
        #this data frame has less data as we removed the last quarter (3 rows) to avoid weird data 
        self.fromdate_total_returns_df = pd.DataFrame()
        #create a df to store the results of the annualized fromDate total returns calculation
        self.annualized_fromdate_total_returns_df = pd.DataFrame()
        #create a df to store the results of the annualized fromDate total returns calculation
        self.dividends_yield_df = pd.DataFrame()
        self.dividends_yield_yearly_df = pd.DataFrame()
        self.dividends_yield_fromdate_df = pd.DataFrame()
        self.dividends_yield_todate_df = pd.DataFrame()
        self.annualized_fromdate_dividends_yield_df = pd.DataFrame()
        self.annualized_todate_dividends_yield_df = pd.DataFrame()

        self.riskfreeticker = riskfreeticker

        #------------------------ Start of Currency work ---------------------------
        if refcurrency is None:
            self.currency_adjust_analysis = False
        else:
            self.currency_adjust_analysis = True
        
        #get the list of currency for every tickers
        self.currencies = self.get_tickers_currency(self.tickers_and_index)
        print("currencies")
        print(self.currencies)
        assets_dict = {'TICKER': self.tickers_and_index, 'CURRENCY': self.currencies}
        self.tickers_df = pd.DataFrame(assets_dict)

        #to calculate the cutomweight of a portfolio with various exchange we always need the currrency data
        #so let's get all currency analysis data ready 
        self.fx_df = pd.DataFrame()
        self.currency_df = pd.DataFrame()
        #we need to get the different exchange rates for the various tickers during the period
        self.fx_to_euro_tickers = [['SAR','SAREUR=X'], ['USD','USDEUR=X'], ['GBP','GBPEUR=X'], ['GBp','GBPEUR=X'], ['CHF', 'CHFEUR=X'], ['CNY', 'CNYEUR=X'], ['JPY', 'JPYEUR=X'], ['DKK', 'DKKEUR=X'], ['NOK', 'NOKEUR=X'], ['HKD', 'HKDEUR=X'], ['SGD', 'SGDEUR=X'], ['INR', 'INREUR=X'], ['KRW', 'KRWEUR=X'], ['TWD', 'TWDEUR=X'], ['SEK', 'SEKEUR=X'], ['CAD', 'CADEUR=X'], ['AUD', 'AUDEUR=X'], ['THB', 'THBEUR=X'], ['IDR', 'IDREUR=X']]
        #, ['TRY', 'TRYEUR=X']]
        self.fx_to_usd_tickers = [['SAR','SARUSD=X'],['EUR','EURUSD=X'], ['GBP','GBPUSD=X'], ['GBp','GBPUSD=X'], ['CHF', 'CHFUSD=X'], ['CNY', 'CNYUSD=X'], ['JPY', 'JPYUSD=X'], ['DKK', 'DKKUSD=X'], ['NOK', 'NOKUSD=X'], ['HKD', 'HKDUSD=X'], ['SGD', 'SGDUSD=X'], ['INR', 'INRUSD=X'],  ['KRW', 'KRWUSD=X'], ['TWD', 'TWDUSD=X'], ['SEK', 'SEKUSD=X'], ['CAD', 'CADUSD=X'], ['AUD', 'AUDUSD=X'], ['THB', 'THBUSD=X'], ['IDR', 'IDRUSD=X']]
        #, ['TRY', 'TRYUSD=X']]
        if self.refcurrency == 'EUR':
            self.fx_tickers_df = pd.DataFrame(self.fx_to_euro_tickers, columns=['CURRENCY', 'FX_TICKER'])
        elif self.refcurrency == 'USD':
            self.fx_tickers_df = pd.DataFrame(self.fx_to_usd_tickers, columns=['CURRENCY', 'FX_TICKER'])
        else:
            print("error, unknown reference currency, apply default value (EUR)")
            self.fx_tickers_df = pd.DataFrame(self.fx_to_euro_tickers, columns=['CURRENCY', 'FX_TICKER'])
        #let's collect the FX rate for the reference currency
        self.fx_df = self.get_currency_data()
        #------------------------ End of Currency work ---------------------------
        
        #let's get the yahoo data for the tickers
        self.get_data()

        #let's get all the data 
        self.simple_returns()
        if show_graphs:
            self.returns_plot()

        #Let's gate the market cap information
        self.market_cap_df = self.get_market_caps()

        #let's get all the toDate data 
        self.toDate_total_returns()
        if show_graphs:
            self.todate_total_returns_plot()
            #we create a graph for the annualized return
            self.annualized_todate_total_returns_plot()
            #we create a graph for the risk / return analysis
            self.risk_return_plot(self.annualized_todate_total_returns_df, "Annualized toDate Total Return (mean) / Risk (stdev)")
            #we create a cor matrix
            self.corr_matrix(self.annualized_todate_total_returns_df, "Annualized toDate Total Return Correlation Matrix")
        
        #let's get all the fromDate data 
        self.fromDate_total_returns()
        if show_graphs:
            self.fromdate_total_returns_plot()
            #we create a graph for the annualized return
            self.annualized_fromdate_total_returns_plot()
            #we create a graph for the risk / return analysis
            self.risk_return_plot(self.annualized_fromdate_total_returns_df, "Annualized fromDate Total Return (mean) / Risk (stdev)", True)
            #we create a cor matrix
            self.corr_matrix(self.annualized_fromdate_total_returns_df, "Annualized fromDate Total Return Correlation Matrix")

    #let's get the yahoo finance data for the period and the tickers associated with these assets
    def get_data(self, ticker=None):
        if ticker is not None:
             return yf.download(ticker, start = self.start_date, end = self.end_date, period='1mo', interval='1mo')
        if self.assets_data_df.empty:
            self.assets_data_df = yf.download(self.tickers_and_index, start = self.start_date, end = self.end_date, period='1mo', interval='1mo')
            #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
            self.assets_data_df.index = self.assets_data_df.index.tz_localize(None)
        return self.assets_data_df

    #this function return the currency of each ticker 
    def get_tickers_currency(self, tickers):
        currencies = []
        for tickerSymbol in self.tickers_and_index:
            tickerinfo = yf.Ticker(tickerSymbol)
            if tickerinfo is not None:
                try:
                    currencies.append(tickerinfo.info['currency'])
                except KeyError:
                    print('error: unknow currency field' + str(tickerSymbol))
                    currencies.append(self.refcurrency)
            self.assets_info_df[tickerSymbol] = tickerinfo
        return currencies

    #let's get the yahoo finance data for different exchange rates that we will need to go to the ref currency
    def get_currency_data(self):
        # we get the FX ticker for all the currency we have to support for our tickers
        if self.fx_df.empty:
            currency = []
            fx_ticker = []
            for index, row in self.fx_tickers_df.iterrows():
                currency.append(str(row['CURRENCY']))
                fx_ticker.append(str(row['FX_TICKER']))
            self.fx_df = yf.download(fx_ticker, start = self.start_date, end = self.end_date, period='1mo', interval='1mo')
            #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
            self.fx_df.index = self.fx_df.index.tz_localize(None)
        return self.fx_df
    
    #a function to return the FX for a given currency to the ref currency, we assume the date given is part of the period cover by the analysis 
    def get_fx_rate(self, ticker, date, adj=False):
        if not self.currency_adjust_analysis: 
            return 1
        if self.fx_df.empty:
            self.get_currency_data()
        #get the currency for the ticket
        ticker_currency = self.tickers_df.loc[self.tickers_df['TICKER']==ticker, 'CURRENCY'].values[0]
        if ticker_currency == self.refcurrency: 
            return 1
        elif self.refcurrency == 'EUR' or self.refcurrency == 'USD':
            fx_ticker = self.fx_tickers_df.loc[self.fx_tickers_df['CURRENCY']==ticker_currency,'FX_TICKER'].values[0]
        else:
            return 1
        date.tz_localize(None)
        date = date.strftime('%Y-%m-%d')
        if adj:
            return float(self.fx_df.loc[date, ('Adj Close', fx_ticker)])
        else:
            return float(self.fx_df.loc[date, ('Close', fx_ticker)])

    #a function to return for a given serie of values for a given ticker the modified values for a given currency to the ref currency
    #we assume the date given is dataframe with the tickers in the column, the time series as index, and some share or dividendes values 
    def apply_fx_rates_toserie(self, serie, ticker, adj=False):
        if not self.currency_adjust_analysis:
            return serie
        #print("----------------- Apply FX rate to serie for " + ticker + " --------------------------------------\n")
        #serice contains the data we want to convert, time series as row
        #we have the self.portfolio_df dataframe with for each tickers, its weights, and its currency
        #we have the self.fx_tickers_df dataframe with the mapping betwwen a refcurrency and the currency of a ticker
        #we have the self.fx_df dataframe with all the exchange rates values for each fx_tickers with our time series as index
        if self.fx_df.empty:
            self.fx_df = self.get_currency_data()    
        #now we have to merge all this
        #let's get the currency name for the ticker
        ticker_currency = self.tickers_df.loc[self.tickers_df['TICKER']==ticker, 'CURRENCY'].values[0]
        #if no change of currency required
        if ticker_currency == self.refcurrency: 
            return serie
        elif self.refcurrency in ['EUR', 'USD']:
            #I want to have a serie with the same time series as index
            target_serie = serie.copy()
            #let's get the exchange rates for the currency for the time serie
            fx_ticker = self.fx_tickers_df.loc[self.fx_tickers_df['CURRENCY']==ticker_currency, 'FX_TICKER'].values[0]
            if adj:
                target_serie *= self.fx_df.loc[:, ('Adj Close', fx_ticker)]
            else:
                target_serie *= self.fx_df.loc[:, ('Close', fx_ticker)]
        #if we don't know the currency
        else:
            print('error: unknown currency')
            #we don't change the data
            target_serie = serie
        return target_serie

    #a function to return the modified values for a given currency to the ref currency
    #we assume the date given is dataframe with the tickers in the column, the time series as index, and some share or dividendes values 
    def apply_fx_rates_todf(self, dataframe, adj=False):
        if not self.currency_adjust_analysis:
            return dataframe 
        #print("---------------- Apply FX rate to dataframe -------------------------------------------------------  ") 
        #dataframe includes the data we want to convert, tickers as column, values and time series as index
        #we have the self.portfolio_df dataframe with for each tickers, its weights, and its currency
        #we have the self.fx_tickers_df dataframe with the mapping betwwen a refcurrency and the currency of a ticker
        #we have the self.fx_df dataframe with all the exchange rates values for each fx_tickers with our time series as index
        if self.fx_df.empty:
            self.fx_df = self.get_currency_data()
        #now we have to merge all this
        #I want to have a dataframes with the same time series as index, with ticker as column and with the exchange rate as value
        #if we have only one ticker 
        if isinstance(dataframe,pd.Series):
            dataframe.name = self.tickers[0]
            #convert serie to dataframe
            target_df = pd.DataFrame(dataframe)
        else:
            target_df = dataframe.copy()
        #the first one is the input dataframe
        for column in target_df.columns:
            ticker = column
            ticker_currency = self.tickers_df.loc[self.tickers_df['TICKER']==ticker, 'CURRENCY'].values[0]
            #if no change of currency required
            if ticker_currency == self.refcurrency: 
                target_df.loc[:, column] = target_df.loc[:, column]
            elif self.refcurrency in ['EUR', 'USD']:
                fx_ticker = self.fx_tickers_df.loc[self.fx_tickers_df['CURRENCY']==ticker_currency, 'FX_TICKER'].values[0]
                if adj:
                    target_df[column] *= self.fx_df.loc[:, ('Adj Close', fx_ticker)]
                else:
                    target_df[column] *= self.fx_df.loc[:, ('Close', fx_ticker)]
            #if we don't know the currency
            else:
                print('error: unknown currency')
                #we don't change the data
                target_df.loc[:, column] = target_df.loc[:, column]
        return target_df
    
    #a function to retrieve the market cap for the tickers 
    def get_market_caps(self):
        print(" ****************** Retrieve MarketCap for the tickerDfClose) *************************************\n") 
        if self.market_cap_df.empty:
            #we want the same time serie as index at all our data
            self.market_cap_df = pd.DataFrame(index=self.assets_data_df.index)
            for tickerSymbol in self.tickers:
                tickerData = yf.Ticker(tickerSymbol)
                temp_dict = tickerData.info
                #print("dictionary for " + tickerSymbol)
                #print(temp_dict)  
                #We have now the current market cap, we applied it to last value of the dataframe taking into account the FX at that time
                #ideally we would like to get the marketcap at the given time
                try:
                    # Try to access the data in the dictionary
                    latest_market_cap = float(temp_dict["marketCap"])
                except KeyError:
                    # Handle the case where the key does not exist in the dictionary
                    latest_market_cap = 0
                    print("error: MarketCap does not exist, 0 applied, in the dictionary for " + tickerSymbol)
                latest_market_cap = self.apply_fx_rates_toserie([latest_market_cap], tickerSymbol)
                #we can now calculate a market cap for the other period based on the share price evolution 
                #but this will not take into account the following events: new shares emission, share splits
                df = self.get_data()
                try:
                    if self.adj:
                        latest_share_price = df.iloc[-1, df.columns.get_loc(('Adj Close', tickerSymbol))]
                        self.market_cap_df[tickerSymbol] = (latest_market_cap/ latest_share_price) * df.loc[:, ('Adj Close', tickerSymbol)]                
                    else:
                        latest_share_price = df.iloc[-1, df.columns.get_loc(('Close', tickerSymbol))]
                        self.market_cap_df[tickerSymbol] = (latest_market_cap/ latest_share_price) * df.loc[:, ('Close', tickerSymbol)]
                except KeyError:
                    print("error: MarketCap does not exist, 0 applied, in the dictionary for " + tickerSymbol)
        return self.market_cap_df.fillna(0)

    #we calculate the capital gain without dividendes 
    def simple_returns(self, adj = False, cum = False):
        print(" ****************** Assets Simple Returns calculation (no Dividends) ******************************\n")
        if self.simple_returns_df.empty:
            tickerDf = self.get_data()
            print(tickerDf)
            if not self.currency_adjust_analysis:
                if adj:
                    tickerDfClose = tickerDf['Adj Close']
                else:
                    tickerDfClose = tickerDf['Close']
            else:
                if adj:
                    tickerDfClose = self.apply_fx_rates_todf(tickerDf['Adj Close'])
                else:
                    tickerDfClose = self.apply_fx_rates_todf(tickerDf['Close'])
            #let's calculate the returns
            simple_returns = tickerDfClose.pct_change().fillna(0)
            if cum:
                simple_returns = (1 + simple_returns).cumprod() - 1
            self.simple_returns_df = simple_returns 
        return self.simple_returns_df

    #Nicolas add a function to calculate total return on an asset, we include the gains associated with the dividendes 
    #This is similar than the toDate function, but the toDate function calculate also the annualized data
    def total_returns(self, adj = False):
        print(" ****************** Assets Total Returns calculation (with Dividends) *****************************\n")
        if self.cumulative_returns_df.empty:
            # Fetch and process data for each ticker from Yahoo Finance
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.start_date, '%Y-%m-%d')
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                print("\n ------------- Calculation of total return for: " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1mo', start=self.start_date, end=self.end_date, interval='1mo')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                if not self.currency_adjust_analysis: 
                    tickerDfDividends = tickerDf['Dividends']
                    if adj:
                        tickerDfClose = tickerDf['Adj Close']
                    else:
                        tickerDfClose = tickerDf['Close']
                else:
                    tickerDfDividends = self.apply_fx_rates_toserie(tickerDf['Dividends'], tickerSymbol, adj)
                    if adj:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Adj Close'], tickerSymbol, adj)
                    else:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Close'], tickerSymbol, adj)
                #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
                difference = (tickerDf.index-date1).days
                treasury_counter = 1
                #let's check if it is the US treasury bonds, if so then we get a return rate directly as value from yahoo finance
                if tickerSymbol in self.treasury_bonds_tickers:
                    #calculate the return rate for the treasury bond, we assume analysis is shorter than the risk free ticker given, so we take the bond value
                    #not optimal
                    self.cumulative_returns_df[tickerSymbol] = ((1+tickerDfClose/12).cumprod()-1)*100
                    #we move to the next ticker
                    print("we found " + str(treasury_counter) + " treasury bonds ticker(s) in Total returns")
                    treasury_counter +=1
                    continue
                # Now calculate monthly total returns including dividends between two successive period
                tickerDf['Monthly Total Returns'] = tickerDfClose.pct_change() + tickerDfDividends.div(tickerDfClose.shift(1)).fillna(0) 
                # Convert monthly total returns to return factors (1 + monthly total return). If you don't do this you will get a multiple and not a percentage.
                tickerDf['Return Factor'] = 1 + tickerDf['Monthly Total Returns']
                # Calculate cumulative returns by cumulatively multiplying the return factors and convert to percentages
                tickerDf['Cumulative Returns %'] = (tickerDf['Return Factor'].cumprod() - 1) * 100
                # Add the cumulative returns percentage series to the cumulative returns DataFrame with the ticker as the column name
                self.cumulative_returns_df[tickerSymbol] = tickerDf['Cumulative Returns %']
                print("------------------------------------------------------------------------- \n")
            print("Asset Total Returns calc succcessful\n")
        return self.cumulative_returns_df

    #add function to calculate total annualized return on an asset from a specific date to end date
    def toDate_total_returns(self, adj = False):
        print(" ****************** Assets (annualized) ToDate Total Returns calculation (with Dividends) *********\n")
        if self.todate_total_returns_df.empty:
            # Calculate the difference between the two dates , we will need the number of days of holding to calculate the annualized total returns
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.start_date, '%Y-%m-%d')
            # Fetch and process data for each ticker from Yahoo Finance
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                print("\n ------------- Calculation of toDate total return for: " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1mo', start=self.start_date, end=self.end_date, interval='1mo')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                if not self.currency_adjust_analysis: 
                    tickerDfDividends = tickerDf['Dividends']
                    if adj:
                        tickerDfClose = tickerDf['Adj Close']
                    else:
                        tickerDfClose = tickerDf['Close']
                else:
                    tickerDfDividends = self.apply_fx_rates_toserie(tickerDf['Dividends'], tickerSymbol, adj)
                    if adj:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Adj Close'], tickerSymbol, adj)
                    else:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Close'], tickerSymbol, adj)
                #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
                difference = (tickerDf.index-date1).days
                treasury_counter = 0
                #let's check if it is the US treasury bonds, if so then we get a return rate directly as value from yahoo finance
                if tickerSymbol in self.treasury_bonds_tickers:
                    #calculate the return rate for the treasury bond, we assume analysis is shorter than the risk free ticker given, so we take the first value
                    self.todate_total_returns_df[tickerSymbol] = (tickerDfClose.iloc[0]*(difference/365.25))
                    #we annualized the data based on how old the bond has been hold
                    self.annualized_todate_total_returns_df[tickerSymbol] = ((1+(tickerDfClose.iloc[0]*(difference/365.25)))**(365.25/difference))
                    #we move to the next ticker
                    print("we found " + str(treasury_counter) + " treasury bonds ticker(s) in Asset toDate")
                    treasury_counter +=1
                    continue
                # Now calculate monthly total returns including dividends between the period and the start (used cumsum)
                startshareprice = tickerDfClose.iloc[0]
                tickerDf['ToDate Total Returns'] = ((tickerDfClose-tickerDfClose.iloc[0])/tickerDfClose.iloc[0]) + tickerDfDividends.cumsum().div(tickerDfClose.iloc[0]).fillna(0)
                if not self.currency_adjust_analysis: 
                    print("start adj share price:")
                    print(startshareprice)
                    print("cumulated dividendes:")
                    print(tickerDfDividends.cumsum())
                else:
                    print("start adj share price in :" + str(self.refcurrency))
                    print(startshareprice)
                    print("cumulated dividendes in :" + str(self.refcurrency))
                    print(tickerDfDividends.cumsum())
                # Convert monthly total returns to return factors (1 + monthly total return). If you don't do this you will get a multiple and not a percentage.
                tickerDf['ToDate Total Return Factor'] = 1 + tickerDf['ToDate Total Returns']
                # convert to percentages
                tickerDf['ToDate Total Returns %'] = (tickerDf['ToDate Total Return Factor']-1)* 100
                # Add the cumulative returns percentage series to the cumulative returns DataFrame with the ticker as the column name
                self.todate_total_returns_df[tickerSymbol]=tickerDf['ToDate Total Returns %']
                tickerDf['Annualized ToDate Total Rate of Return%'] =  ((1+(tickerDf['ToDate Total Returns %']/100))**(difference/365.25)-1)*100
                self.annualized_todate_total_returns_df[tickerSymbol] = tickerDf['Annualized ToDate Total Rate of Return%']
                print("------------------------------------------------------------------------- \n")
            #print('Annualized ToDate Total Returns %')
            #pd.set_option('display.max_rows', None)
            #print( self.annualized_todate_total_returns_df)
            #print('Mean Annualized toDate Total Returns %')
            #the last values (less than a year) can show high volatility as short term performance is amplified when we annualized the data. So we may want to skip them when calculating the mean  
            #print( self.annualized_todate_total_returns_df.mean().sort_values(ascending=False))
            #print('Std Deviation Annualized toDate Total Returns %')
            #print(self.annualized_todate_total_returns_df.std().sort_values(ascending=True))
            #pd.reset_option('all', silent=True)
            print("ToDate Total Returns calc succcessful\n")
        return self.todate_total_returns_df    

    #add function to calculate total annualized return on an asset FROM a date TO current date
    def fromDate_total_returns(self, adj = False):
        print(" ****************** Assets (annualized) fromDate Total Returns calculation (with Dividends) ********\n")
        if self.fromdate_total_returns_df.empty:
            # Calculate the difference between the two dates , we will need the number of days of holding to calculate the annualized total returns
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.end_date, '%Y-%m-%d')
            # Fetch and process data for each ticker from Yahoo Finance
            treasury_counter = 1
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                print("\n ------------- Calculation of fromDate total return for: " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1mo', start=self.start_date, end=self.end_date, interval='1mo')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                if not self.currency_adjust_analysis: 
                    tickerDfDividends = tickerDf['Dividends']
                    if adj:
                        tickerDfClose = tickerDf['Adj Close']
                    else:
                        tickerDfClose = tickerDf['Close']
                else:
                    tickerDfDividends = self.apply_fx_rates_toserie(tickerDf['Dividends'], tickerSymbol, adj)
                    if adj:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Adj Close'], tickerSymbol, adj)
                    else:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Close'], tickerSymbol, adj)
                #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
                difference = (date1-tickerDf.index).days
                #let's check if it is the US treasury bonds, if so then we get a return rate directly as value from yahoo finance
                if tickerSymbol in self.treasury_bonds_tickers:
                    #calculate the return rate for the treasury bond, period is one month so we take the rate , we assume analysis are shorter than the risk free ticker given
                    self.fromdate_total_returns_df[tickerSymbol] = (tickerDfClose*(difference/365.25))
                    #we annualized the data based on how old the bond has been hold
                    #want the same size of data as the other tickers so we remove the last 3 ones
                    self.annualized_fromdate_total_returns_df[tickerSymbol] = ((1+tickerDfClose*(difference/365.25))**(365.25/difference)).iloc[:-3]
                    #we move to the next ticker
                    print("we found " + str(treasury_counter) + " treasury bonds ticker(s) in Asset fromDate")
                    treasury_counter +=1
                    continue
                #if it is not the treasury bonds 
                # Now calculate monthly total returns including dividends between a period and the end (used cumsum)
                #we take the average value over the last 3 periods to avoid any strange behavior due to short term volatility
                endshareprice = tickerDfClose.iloc[-3:].mean()
                tickerDf['cumsum_reverse_Dividends'] = tickerDfDividends.loc[::-1].cumsum()[::-1]
                tickerDf['fromDate Total Returns'] = ((tickerDfClose.iloc[-3:].mean()-tickerDfClose)/tickerDfClose) + tickerDf['cumsum_reverse_Dividends'].div(tickerDfClose).fillna(0)
                if not self.currency_adjust_analysis: 
                    print("end adj share price \n")
                    print(endshareprice)
                    print("from date to end date cumulated dividendes: \n")
                    print(tickerDf['cumsum_reverse_Dividends'])
                else:
                    print("end share price in " + str(self.refcurrency))
                    print(endshareprice)
                    print("from date to end date cumulated dividendes in" + str(self.refcurrency))
                    print(tickerDf['cumsum_reverse_Dividends'])
                # Convert monthly total returns to return factors (1 + monthly total return). If you don't do this you will get a multiple and not a percentage.
                tickerDf['fromDate Total Return Factor'] = 1 + tickerDf['fromDate Total Returns']
                # convert to percentages
                tickerDf['fromDate Total Returns %'] = (tickerDf['fromDate Total Return Factor']-1)* 100
                # Add the cumulative returns percentage series to the cumulative returns DataFrame with the ticker as the column name
                print('fromDate Total Returns % \n')
                print(tickerDf['fromDate Total Returns %'])
                self.fromdate_total_returns_df[tickerSymbol]=tickerDf['fromDate Total Returns %']
                tickerDf['Annualized fromDate Total Rate of Return%'] =  ((1+(tickerDf['fromDate Total Returns %']/100))**(365.25/difference)-1)*100
                #if difference is very small (few days) then we may have strange results, so we skip the last 3 items for the annulized returns
                self.annualized_fromdate_total_returns_df[tickerSymbol] = tickerDf['Annualized fromDate Total Rate of Return%'].iloc[:-3]
                print("------------------------------------------------------------------------- \n")
            #print('Annualized fromDate Total Returns %')
            #pd.set_option('display.max_rows', None)
            #print( self.annualized_fromdate_total_returns_df)
            #print('Mean Annualized fromDate Total Returns %')
            #the last values (less than a year) can show high volatility as short term performance is amplified when we annualized the data. So we may want to skip them when calculating the mean  
            #print( self.annualized_fromdate_total_returns_df.mean().sort_values(ascending=False))
            #print('Std Deviation Annualized fromDate Total Returns %')
            #print(self.annualized_fromdate_total_returns_df.std().sort_values(ascending=True))
            #pd.reset_option('all')
            print("fromDate Total Returns calc succcessful\n")
        return self.fromdate_total_returns_df

    #Nicolas add a function to calculate the dividendes yield of an asset over time 
    #period can be either 'yearly' = past 12 months dividends yield, 'fromdate' : dividends yield from a given date till now, 'todate' : dividends yield from a given time to the index 
    def calculate_dividends(self, adj = False, period="default"):
        print(" ****************** Dividends analysis - calculate dividends yields *****************************\n")
        if self.dividends_yield_yearly_df.empty:
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.end_date, '%Y-%m-%d')
            date2 = datetime.strptime(self.start_date, '%Y-%m-%d')
            # Fetch and process data for each ticker from Yahoo Finance
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                #print("\n ------------- Dividendes for : " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1mo', start=self.start_date, end=self.end_date, interval='1mo')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                if tickerSymbol == "SU.PA":
                    print(tickerDf['Dividends'])
                if not self.currency_adjust_analysis: 
                    tickerDfDividends = tickerDf['Dividends']
                    if adj:
                        tickerDfClose = tickerDf['Adj Close']
                    else:
                        tickerDfClose = tickerDf['Close']
                else:
                    tickerDfDividends = self.apply_fx_rates_toserie(tickerDf['Dividends'], tickerSymbol, adj)
                    if adj:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Adj Close'], tickerSymbol, adj)
                    else:
                        tickerDfClose = self.apply_fx_rates_toserie(tickerDf['Close'], tickerSymbol, adj)
                if tickerSymbol == "SU.PA":
                    print(tickerDfDividends)
                # Now calculate the various dividends 
                #rolling yearly dividends 
                tickerDf['Dividends Yield %'] = tickerDfDividends.rolling(window=12, min_periods=1).sum().div(tickerDfClose.shift(1)).fillna(0) * 100
                self.dividends_yield_yearly_df[tickerSymbol] = tickerDf['Dividends Yield %']
               
                #todate : dividendes yield from start date to index
                tickerDf['Dividends Yield todate %'] = tickerDfDividends.cumsum().div(tickerDfClose.iloc[0]).fillna(0) * 100
                self.dividends_yield_todate_df[tickerSymbol] = tickerDf['Dividends Yield todate %']
                difference = (tickerDf.index-date2).days
                tickerDf['Annualized toDate Dividends Yield %'] =  ((1+(tickerDf['Dividends Yield todate %']/100))**(365.25/difference)-1)*100
                self.annualized_todate_dividends_yield_df[tickerSymbol] = tickerDf['Annualized toDate Dividends Yield %'].iloc[:-3]

                #fromdate : dividends yield from index to end date
                tickerDf['cumsum_reverse_Dividends'] = tickerDfDividends.loc[::-1].cumsum()[::-1]
                tickerDf['Dividends Yield fromdate %'] =  tickerDf['cumsum_reverse_Dividends'].div(tickerDfClose.shift(1)).fillna(0) * 100
                self.dividends_yield_fromdate_df[tickerSymbol] = tickerDf['Dividends Yield fromdate %']
                #calculate the annualized dividends yield at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
                #if difference is very small (few days) then we may have strange results, so we skip the last 3 items for the annulized returns
                difference = (date1-tickerDf.index).days
                tickerDf['Annualized fromDate Dividends Yield %'] =  ((1+(tickerDf['Dividends Yield fromdate %']/100))**(365.25/difference)-1)*100
                self.annualized_fromdate_dividends_yield_df[tickerSymbol] = tickerDf['Annualized fromDate Dividends Yield %'].iloc[:-3]
                #print("------------------------------------------------------------------------- \n")
            print("Dividends Yields calculation succcessful\n")
        pd.set_option('display.max_rows', None)    
        if period == "todate":
            print("todate dividends")
            print(self.dividends_yield_todate_df)
            return self.dividends_yield_todate_df
        elif period == "fromdate":
            print("fromdate dividends")
            print(self.dividends_yield_fromdate_df)
            return self.dividends_yield_fromdate_df
        elif period == "yearly":
            print("yearly dividends")
            print(self.dividends_yield_yearly_df)
            return self.dividends_yield_yearly_df
        else:
            print("default yearly dividends")
            print(self.dividends_yield_yearly_df)
            return self.dividends_yield_yearly_df
    
    #function to calculate the RSI for a given ticker
    def calculate_rsi(self, window=14, data_df = None):
        if data_df is None:
            df = self.get_data()
        else:
            df = data_df
        # Calculate price changes
        delta = df['Close'].diff(1)
        # Separate positive and negative price changes
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        # Calculate RS
        rs = gain / loss
        # Calculate RSI
        rsi = 100 - (100 / (1 + rs))
        print("Rsi")
        print(rsi)
        return rsi

    #function to calculate the RSI for all tickers
    def calculate_all_rsi(self, window=14):
        if self.rsi_df is None or self.rsi_df.empty:
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                #print("\n -------------  Calculation of RSIs for " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1mo', start=self.start_date, end=self.end_date, interval='1mo')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                delta = tickerDf['Close'].diff(1)
                # Calculate price changes
                # Separate positive and negative price changes
                gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
                # Calculate RS
                rs = gain / loss
                # Calculate RSI
                rsi = 100 - (100 / (1 + rs))
                self.rsi_df[tickerSymbol] = rsi
            print("Rsi")
            print(self.rsi_df)
            return self.rsi_df
        else:
            return self.rsi_df

    # Detect double bottoms in a time series of prices.
    def detect_double_bottoms_tops(self, window=6, threshold=0.05):
        if self.double_bottoms_df is None or self.double_bottoms_df.empty:
            for tickerSymbol in self.tickers_and_index:
                # Get historical data for tickers
                tickerData = yf.Ticker(tickerSymbol)
                #print("\n ------------- Search of Double Bottoms for " + tickerSymbol + " -----------------------\n")
                tickerDf = tickerData.history(period='1d', start=self.start_date, end=self.end_date, interval='1d')
                #we need to align date, stocks listed in different exchange have diffenent time zone. so we remove the time and time zone from the index
                tickerDf.index = tickerDf.index.tz_localize(None)
                if not self.adj:
                    prices = tickerDf['Close']
                else:
                    prices = tickerDf['Adj Close']
                # Compute local minima
                local_minima = (prices == prices.rolling(window=window, min_periods=1, center=True).min())
                # Compute local maxima
                local_maxima = (prices == prices.rolling(window=window, min_periods=1, center=True).max())
                # Find consecutive local minima
                consecutive_minima = local_minima & local_minima.shift(-1)
                consecutive_maxima = local_maxima & local_maxima.shift(-1)
                # Identify double bottoms and top (two consecutive local minima with a price increase between them)
                self.double_bottoms_df[tickerSymbol] = consecutive_minima & (prices.pct_change() > threshold)
                self.double_tops_df[tickerSymbol] = consecutive_maxima & (prices.pct_change() > threshold)
            print("Double Bottoms")
            print(self.double_bottoms_df)
            print("Double Tops")
            print(self.double_tops_df)
            # Extract True values from double bottoms DataFrame
            true_double_bottoms = self.double_bottoms_df[self.double_bottoms_df]
            # Extract True values from double tops DataFrame
            true_double_tops = self.double_tops_df[self.double_tops_df]
            print("Double Bottoms True only")
            print(true_double_bottoms.dropna())
            print("Double Tops True only")
            print(true_double_tops.dropna())
        return self.double_bottoms_df


    def std(self, adj = False, crypto = False):
        returns = self.simple_returns(adj).mul(100)
        if crypto:
            trading_days = 365.25
        else:
            trading_days  = 252
        std = returns.describe().T.loc["std"]
        std = std*np.sqrt(trading_days)
        return std
   
    def mean_return(self, adj = False, crypto = False, template = 'plotly_dark'):
        returns = self.simple_returns(adj).mul(100)
        if crypto:
            trading_days = 365.25
        else:
            trading_days  = 252
        mean = returns.describe().T.loc["mean"]
        mean = mean*trading_days # Multiply by number of trading days 
        return mean
    
    def returns_plot(self, adj = False, cum = False, log = False, template = 'plotly_dark'):
        returns = self.simple_returns(adj, cum).mul(100)
        if log:
            returns = self.log_returns(adj, cum).mul(100)
        try:
            returns = returns.to_frame()
        except:
            pass
        
        returns = returns.rename(columns={'Close': 'Returns'})
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Daily Returns",
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        # Add the logo image
        fig = self.brand_graphic(fig) 
        fig.show() 
        return returns

    #Nicolas - add a function to calculate and draw annualized todate total return on the portfolio
    def annualized_todate_total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.toDate_total_returns(adj)
        returns = self.annualized_todate_total_returns_df.iloc[1:,:]
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Annualized ToDate Total Returns since " + str(self.start_date) + " for " + str(self.prtfname) + "'s Assets (with dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        # Add the logo image
        fig = self.brand_graphic(fig)     
        fig.show() 
        return returns

    #Nicolas - add a function to calculate and draw annualized todate total return on the portfolio
    def annualized_fromdate_total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.fromDate_total_returns(adj)
        returns = self.annualized_fromdate_total_returns_df.iloc[1:,:]
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Annualized fromDate Total Returns for " + str(self.prtfname) + "'s Assets (with dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")  
        print("add image located at : " + image_path)
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show() 
        return returns

    #Nicolas - add a function to calculate and draw todate total return on the portfolio
    def todate_total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.toDate_total_returns(adj)
        returns = returns.rename(columns={'Close': 'Returns'})
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"ToDate Total Returns for " + str(self.prtfname) + "'s Asset (with dividends) since " + str(self.start_date) + " in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show()
        return returns

    #Nicolas - add a function to calculate and draw fromdate total return on the portfolio
    def fromdate_total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.fromDate_total_returns(adj)
        returns = returns.rename(columns={'Close': 'Returns'})
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f" fromDate Total Returns for " + str(self.prtfname) + "'s Asset (with dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show() 
        return returns

    #Nicolas - add a function to calculate total return on the portfolio
    def total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.total_returns(adj)
        returns = returns.rename(columns={'Close': 'Returns'})
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Total Returns since " + str(self.start_date) + " for " + str(self.prtfname) + "'s Asset (including dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        # Add the logo image
        fig = self.brand_graphic(fig)     
        fig.show() 
        return returns

    def fromdate_totalreturn_risk_return_plot(self):
        #we create a graph for the risk / return analysis
        self.risk_return_plot(self.annualized_fromdate_total_returns_df, "Annualized fromDate Total Return (mean) / Risk (stdev) for " + str(self.prtfname) + "'s Assets", True)
   
    def fromdate_risk_dividends_plot(self):
        #we create a graph for the risk / return analysis
        self.risk_return_plot(self.annualized_fromdate_dividends_yield_df, "Annualized fromDate Dividends Yield (mean) / Risk (stdev) for " + str(self.prtfname) + "'s Assets", True)

    def fromdate_total_return_corr_matrix(self):
        #we create a cor matrix
        self.corr_matrix(self.annualized_fromdate_total_returns_df, "Annualized fromDate Total Return Correlation Matrix for " + str(self.prtfname) + "'s Assets")

    def todate_totalreturn_risk_return_plot(self):
        #we create a graph for the risk / return analysis
        self.risk_return_plot(self.annualized_todate_total_returns_df, "Annualized toDate Total Return (mean) / Risk (stdev) for " + str(self.prtfname) + "'s Assets")
        
    def todate_total_return_corr_matrix(self):  
        #we create a cor matrix
        self.corr_matrix(self.annualized_todate_total_returns_df, "Annualized toDate Total Return Correlation Matrix for " + str(self.prtfname) + "'s Assets")

    #function to create a plot graph that shows the replationship between returns (y) and risks (x)  
    def risk_return_plot(self, data, graph_title="Risk (stdev) / Return (mean)", annualized_fromdate = False, template = 'plotly_dark'):
        summary = pd.DataFrame()
        if annualized_fromdate: 
            #we skip the last 3 periodes to remove high volatility
            summary['% Returns'] = data.iloc[:-3].mean()
        else:
            summary['% Returns'] = data.mean()
        summary['Risks'] = data.std()
        print(summary)
        # Add a new column to indicate whether each data point is from a ticker or an index
        summary['Type'] = summary.index.map(lambda x: 'Ticker' if x in self.tickers else 'Index')
        print("summary plot")
        print(summary)
        fig = px.scatter(summary, 
                         x = 'Risks', 
                         y = '% Returns', 
                         color='Type',
                         title = graph_title,
                         text = summary.index,
                         template = template
                         )
        fig.update_traces(hovertemplate='Risk: %{x}<br>Return: %{y}')
        fig.update_traces(marker={'size': 15},
                          textposition='top center',
                          hoverlabel=dict(font=dict(size=15) ))
        fig.update_layout(
            legend = dict(title = None),
            title={
            'y':0.9,
            'x':0.5,
            'font': {'size': 24},
            'xanchor': 'center',
            'yanchor': 'top',},
            xaxis = dict(title = dict(font = dict(size = 20))),
            yaxis = dict(title = dict(font = dict(size = 20)))
            )
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show()

    #function to create a plot graph that shows the replationship between returns (y) and risks (x)  
    #Nicolas - add a function to calculate total return on the portfolio
    def marketcap_plot(self, template = 'plotly_dark'):
        if self.market_cap_df is None or self.market_cap_df.empty:
            self.market_cap_df = self.get_market_caps()
        market_cap = self.market_cap_df.sort_values(by=self.market_cap_df.index[-1], axis=1, ascending=False)
        print("---- marketcap plot ------\n")
        fig = px.line(market_cap, template = template)
        fig.update_traces(hovertemplate='%{y}')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = None, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"MarketCap evolution for " + str(self.prtfname) + "'s Assets since " + str(self.start_date) + " in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x",
            xaxis_title = "Date",
            yaxis_title = "MarketCap") 
        # Add the logo image
        fig = self.brand_graphic(fig)   
        fig.show() 

    #function to create a plot graph that shows the correlation between the returns   
    def corr_matrix(self, data, graph_title="Correlation Matrix", plot = True, cum = False, template = 'plotly_dark'):
        if data is None:
            if cum:
                returns = self.simple_returns(cum)
            else:
                returns = self.simple_returns()
        else:
            returns = data
        if len(returns.columns) > 1:
            print('Correlation matrix creation')
            corr_matrix = returns.corr()
            print(corr_matrix)
            if plot:
                fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='tempo', template = template, title = graph_title)
                fig.update_layout(
                    legend = dict(title = None),
                    title={
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'}
                    )
                # Add the logo image
                fig = self.brand_graphic(fig)
                fig.show()
                return corr_matrix
            else:
                return returns
        
    def close_plot(self, adj = False, normalize = False, template = 'plotly_dark'):
        df = self.get_data()
        if adj:
            df["CLose"] = df["Adj Close"]
            title = f"{self.tickers} Adjusted Closing Price"
        else:
            title = f"{self.tickers} Closing Price"      
        if normalize:
            df["Close"] = df["Close"].div(df["Close"].iloc[0]) #Normalizes data
            fig = px.line(df["Close"], 
                          x = df.index,
                          y = df["Close"],
                          title = "Normalized " + title,      
                          template = template) # Plotting Normalized closing data
            fig.update_traces(hovertemplate='Price: $%{y}')
            fig.update_layout(
                legend = dict(title = None, font = dict(size = 16)),
                title={
                'y':0.9,
                'x':0.5,
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
                hovermode = "x unified",
                xaxis_title = "Date",
                yaxis_title = "Normalized " + title + " (USD)"
                )
            # Add the logo image
            fig = self.brand_graphic(fig)
            fig.show()
        else:
            
            fig = px.line(df["Close"], 
                          x = df.index,
                          y = df["Close"],
                          title = title,
                          template = template) # Plotting Normalized closing data
            fig.update_traces(hovertemplate='Price: $%{y}')
            fig.update_layout(
                legend = dict(title = None, font = dict(size = 16)),
                title={
                'y':0.9,
                'x':0.5,
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
                hovermode = "x unified",
                xaxis_title = "Date",
                yaxis_title = "Closing Price (USD)"
                )
            # Add the logo image
            fig = self.brand_graphic(fig)
            fig.show()    
        
        
    def candlestick(self, sma1 = 0, sma2 = 0, rsi_p= 14, template = 'plotly_dark'):
        df = self.get_data(self.tickers[0])
        if df is None or df.empty:
            return
        #calculate RSI
        rsi_df = self.calculate_rsi(rsi_p,df)

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02, row_heights=[0.7, 0.3])
        fig.add_trace(go.Candlestick(x=df.index,
                                      open=df['Open'],
                                      high=df['High'],
                                      low=df['Low'],
                                      close=df['Close'],
                                      name='candlestick'),
                                     
                      row=1, col=1)
        fig.update_traces(increasing_line_width = 1.5,
                          decreasing_line_width = 1.5
                         )
        if sma1 > 0:
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'].rolling(window=sma1).mean(),
                                      name=f'{sma1}-months moving average', line=dict(color='lightblue', width = 1)),
                          row=1, col=1)
        if sma2 > 0:
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'].rolling(window=sma2).mean(),
                                      name=f'{sma2}-months moving average', line=dict(color='red', width = 1)),
                          row=1, col=1)
        
        fig.add_trace(go.Bar(x=df.index,
                             y=df['Volume'],
                             name='volume'),
                      row=2, col=1)
        
        # RSI trace
        fig.add_trace(go.Scatter(x=rsi_df.index, y=rsi_df, name='RSI', line=dict(color='orange', width=1)), row=1, col=1)
    
        # Add horizontal lines at RSI levels 70 and 30
        fig.add_shape(type="line", xref="paper", yref="y", x0=rsi_df.index[0], x1=rsi_df.index[-1], y0=70, y1=70, name="overbought", line=dict(color="red", width=1, dash="dash"), row=1, col=1)
        fig.add_shape(type="line", xref="paper", yref="y", x0=rsi_df.index[0], x1=rsi_df.index[-1], y0=30, y1=30, name="oversold", line=dict(color="green", width=1, dash="dash"), row=1, col=1)
    
        fig.update_layout(
                          title={
                          'text': f'{self.tickers[0]} Candlestick Chart with Volume',
                          'y':0.9,
                          'x':0.5,
                          'font': {'size': 24},
                          'xanchor': 'center',
                          'yanchor': 'top',},
                          xaxis_rangeslider_visible=False,
                          xaxis_title='Date',
                          yaxis_title='Price',
                          hovermode = "x unified",
                          bargap=0,
                          bargroupgap=0,
                          template = template)
        fig.update_xaxes(title_text='', row=1, col=1, showgrid=False)
        fig.update_xaxes(title='Date', row=2, col=1)
        fig.update_yaxes(title='Volume',row=2,col=1)
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show()

    #trace the RSI analysis for all tickers 
    def momentum_rsi_plot(self, windows=14, template = 'plotly_dark'):
        df = self.calculate_all_rsi(windows)
        if df is None or df.empty:
            return
        
        Rsi_start = windows+1

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02, row_heights=[0.6, 0.4])
        
        fig.add_trace(go.Candlestick(x=df.columns,
                                      open=df.iloc[-3],
                                      high=df.iloc[-3:].max(),
                                      low=df.iloc[-3:].min(),
                                      close=df.iloc[-1],
                                      name='>RSI last 3 periods'),
                        row=1, col=1)

        fig.add_trace(go.Candlestick(x=df.columns,
                                      open=df.fillna(0).iloc[Rsi_start],
                                      high=df.fillna(0).iloc[Rsi_start:-1].max(),
                                      low=df.fillna(0).iloc[Rsi_start:-1].min(),
                                      close=df.fillna(0).iloc[-1],
                                      name='RSI all periods'),
                        row=2, col=1)

        # Add horizontal lines at RSI levels 70 and 30
        fig.add_shape(type="line", xref="paper", yref="y", x0=df.columns[0], x1=df.columns[-1], y0=70, y1=70, name="overbought", line=dict(color="red", width=1, dash="dash"), row=1, col=1)
        fig.add_shape(type="line", xref="paper", yref="y", x0=df.columns[0], x1=df.columns[-1], y0=30, y1=30, name="oversold", line=dict(color="green", width=1, dash="dash"), row=1, col=1)

        # Add horizontal lines at RSI levels 70 and 30
        fig.add_shape(type="line", xref="paper", yref="y", x0=df.columns[0], x1=df.columns[-1], y0=70, y1=70, name="overbought", line=dict(color="red", width=1, dash="dash"), row=2, col=1)
        fig.add_shape(type="line", xref="paper", yref="y", x0=df.columns[0], x1=df.columns[-1], y0=30, y1=30, name="oversold", line=dict(color="green", width=1, dash="dash"), row=2, col=1)
    
        fig.update_layout(
                          title={
                          'text': 'Momentum analysis : Relative Strength Index (RSI)',
                          'y':0.9,
                          'x':0.5,
                          'font': {'size': 24},
                          'xanchor': 'center',
                          'yanchor': 'top',},
                          xaxis1_rangeslider_visible=False,
                          xaxis2_rangeslider_visible=False,
                          yaxis1_title ='RSI last 3 periods',
                          yaxis2_title ='RSI all periods',
                          hovermode = "x unified",
                          bargap=0,
                          bargroupgap=0,
                          template = template)
        # Add the logo image
        fig = self.brand_graphic(fig)
        fig.show()

    def brand_graphic(self, fig):
        fig.add_layout_image(
                        source=logo_img,  # URL or local file path to your logo
                        xref="paper",  # Set the x reference to paper coordinates
                        yref="paper",  # Set the y reference to paper coordinates
                        x=0,  # Position of the logo from the left side (0 to 1)
                        y=1,  # Position of the logo from the top (0 to 1)
                        sizex=0.10,  # Size of the logo relative to the plot
                        sizey=0.10,
                        xanchor="left",  # Anchor point of the logo (left side)
                        yanchor="top",   # Anchor point of the logo (top side)
                        opacity=1,
                        visible = True,
                        layer="above")
        return fig
