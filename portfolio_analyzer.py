''' 
Initialy created under the name Stock Analyzer Library, Version 2.0
https://github.com/StevenMedvetz/stock-analysis/blob/main/stock_analyzer.py
Date: March 13, 2023
Author: Steven Medvetz

Completly Modified in 2024 March and April by Nicolas Payen
add total returns calucaltion (including dividends) toDate and fromDate
add annualized returns calculations
add ablity to work with tickers from various exchanges
add various weighting method including Dynamic Weighting methodology
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
from stock_analyzer import Asset
from plotly.subplots import make_subplots
from dateutil import relativedelta
from datetime import datetime

# Get the current working directory
# Get the current working directory
current_dir = os.getcwd()
# Construct the file path to your JPEG image
image_path = os.path.join(current_dir, "Koi_logo3.png")
logo_img = Image.open("Koi_logo3.png")

pio.renderers.default = "browser"

'''
A portfolio is a group of assets, the user can give / calculate the weights for each ticker
tickers : list of yahoo tickers included in the portfolio
start_date : starting date of the analysis
end_date : end date of the analysis
weight_method : to indicate the method used to calculate the weights  
    Random = random round number 
    EqualWeight = same weight for each tickers, use fractional shares
    CustomWeight = based on the nb shares given by the user in parameter (weights), fixed all along the period, use fractional shares
    CustomDynamicWeight = based on the nb shares given by the user in parameters (weights), but adjusted all along the way to take into account changes in share prices and exchange rates, input used first at the end of the period.
weights : input for the custom weights [ 10, 20, 40, 30] for example
prtfname : name of the portfolio
refcurrency : currency used as reference to calculate returns (EUR or USD)
show_graphs : display automatically graphs 
withIndex is used to know if the portfolio should display the indexes for Benchmark
        if withIndex is false, it is then possible to give indexes in the tickers or create a portfolio of index. 
        To compare this portfolio with indexes uses the portfolio_benchmark_bench
'''
class Portfolio(Asset):
    def __init__(self, prtfname = "Xport", tickers = ["AAPL", "EL.PA"], start_date = None, end_date = datetime.today().strftime('%Y-%m-%d'), weight_method = 'EqualWeight', weights = None, refcurrency = 'EUR', riskfreeticker = '^TNX', withindex=True, show_graphs=True):
        #we create the parent Assets class for the portfolio
        super().__init__(tickers, start_date, end_date, refcurrency, riskfreeticker, withindex, show_graphs, prtfname)
        #let's add the elements specific to the portfolio 
        self.weights = weights
        self.weight_method = weight_method
        self.portfolio_assets_data_df = pd.DataFrame()
        self.generated_weights_df = pd.DataFrame()
        self.weighted_simple_returns_df = pd.DataFrame()
        self.weighted_total_returns_df = pd.DataFrame()
        self.weighted_todate_returns_df = pd.DataFrame()
        self.annualized_weighted_todate_returns_df = pd.DataFrame()
        self.weighted_fromdate_returns_df = pd.DataFrame()
        self.annualized_weighted_fromdate_returns_df = pd.DataFrame()
        self.weighted_fromdate_dividends_df = pd.DataFrame()
        self.annualized_weighted_fromdate_dividends_df = pd.DataFrame()
        
        
        print("-------- The porfolio " + str(prtfname)+ " includes " + str(len(self.tickers)) + " tickers -\n")
        #let's generate the weight if necessary
        if weight_method == "EqualWeight":
            self.generated_weights_df = self.generate_iso_weights()
        elif weight_method == 'Random':
            self.generated_weights_df = self.generate_random_weights()
        elif weight_method == 'CustomDynamicWeight' and weights is not None:
            self.generated_weights_df = self.generate_customQ_weights(weights)
        elif weight_method == 'CustomWeight' and weights is not None:
            self.generated_weights_df = self.generate_custom_weights(weights)
        else:
            print("Weighting method unknown, apply default method instead\n")
            self.generated_weights_df = self.generate_isoQ_weights()
        #let's get the returns data

    # Generate weights that add up to 1 , we assume the portfolio as equal proportion between all tickers during all periods
    def generate_iso_weights(self):
        print("---------------- The porfolio Equal weights calculation -------------------------------------------\n")
        #weights = [1 for _ in range(len(self.tickers))]
        weights = [1] * len(self.tickers)
        if(len(self.tickers)>1):
            total_weight = sum(weights)
            weights = np.array([weight / total_weight for weight in weights])
            weights = weights.astype(float)
        print("Equal weights: ")
        print(weights)  
        return weights

    # Generate random weights that add up to 1 
    def generate_random_weights(self):
        print("---------------- The porfolio Random weights calculation ------------------------------------------\n")
        weights = [random.randint(1, 2*len(self.tickers)) for _ in range(len(self.tickers))]
        if(len(self.tickers)>1):
            total_weight = sum(weights)
            weights = np.array([weight / total_weight for weight in weights])
            weights = weights.astype(float)
        print("Random weights:   \n")
        print(weights)
        return weights

    # Generate weights based on the numbers of shares given when calling the functions, we use the qty of share at the end of the period for the reference weights.
    # The weights are dynamically calculated to take into account the change in share prices during the analysis.
    # for the 'fromtodate analysis', this is very good. it tell us what is the total return if I would have boughts these numbers of shares for these tickers at a given date
    # if the portfolio is equality distributed then it is not a problem.
    def generate_customQ_weights(self, weights, adj=False):
        print("---------------- The porfolio Custom weights calculation (dynamic weighting method) ---------------\n") 
        #lets check the validity of the weights given
        #let's get the number of tickers
        if len(self.tickers)>1:
            if len(self.tickers) != len(weights): 
                print("error: the number of tickers is different than the number of weights \n")
                weights = self.generate_iso_weights()
                return weights
        #lets collect the share price at the start of the analysis
        #The ref share prices for the portfolio weighting is the share price at the beginning of the period (close value that day)
        #let's drop de indexes
        #we remove the benchmark index from the portfolio
        sharesprices_df = pd.DataFrame()
        sharesprices_df = self.assets_data_df.copy()
        if self.withindex:
            sharesprices_df.drop(columns=self.index_symbols, level='Ticker', inplace=True)    
        sharesprices_df['Adj Close'].fillna(0)
        if adj:
            refshareprices = self.apply_fx_rates_todf(sharesprices_df['Adj Close'].fillna(0))
        else:
            refshareprices = self.apply_fx_rates_todf(sharesprices_df['Close'].fillna(0))
        #Let's convert the ref share prices in the reference currency
        #for every ticker I will extract the refshare price (last month value) and use it to calculate the weight, i also need the total of the shares prices for the portfolio
        #self.assets_df.info()
        #let's create first simple weight with the quantity of shares given to us
        #we want the same structure of the returns data frame use for the calculation
        if len(self.tickers)>1:
            self.myportfolio_dynamic_weight_df = refshareprices.copy()
            self.myportfolio_dynamic_weight_df.info()
            temp_df = pd.DataFrame(list(zip(self.tickers, weights)), columns=['Ticker', 'Qty'])
            for index, row in temp_df.iterrows():
                ticker_tmp = row['Ticker']
                qty_tmp = row['Qty']
                #at first all values will be the same for a given ticker
                for ind, col in enumerate(self.myportfolio_dynamic_weight_df.columns):
                    if col == ticker_tmp:
                        self.myportfolio_dynamic_weight_df.loc[:,col] = float(qty_tmp)
            #now that I have the base structure I can calculate my dynamic weights
            weights = self.myportfolio_dynamic_weight_df
            totalholdingvalues = (refshareprices*weights).sum(axis=1)
            totalrefshareprices = refshareprices.sum(axis=1)
            print("totalrefshareprice: ")
            print(totalrefshareprices)
            #we multiple the weight by the ratio share prices / total share prices
            weights = (weights*refshareprices)
            print("weight * share price:")
            print(weights)
            weights = weights.div(totalholdingvalues, axis=0)
            print("(weight * share price)/totalholdingvalues:")
            print(weights)
            weights = weights.dropna()
        else:
            weights = [1]
        print("Custom Dynamic Weights:   \n")
        print (weights)
        return weights

    # Use defined weights that are equivalent to investing a given proporation in each tickers that add up to 1 
    def generate_custom_weights(self, weights):
        print("---------------- The porfolio custom weights calculation ------------------------------------------\n")
        #lets check the validity of the weights given
        #let's get the number of tickers
        if len(self.tickers)>1:
            if len(self.tickers) != len(weights): 
                print("error: the number of tickers is different than the number of weights \n")
                weights = self.generate_iso_weights()
                return weights
            #convert to a list of float
            weights = [float(x) for x in weights]
            #we normalize if it is not done yet
            total_weights = sum(weights)
            weights = [(x/total_weights) for x in weights]
        else:
            weights = [1]
        print("Normalized Custom Weights:   \n")
        print(weights)
        return weights
    
    # calculate weighted simple returns for the portfolio
    def portfolio_simple_returns(self, adj = False, cum = False, log = False):
        print(" ****************** The porfolio simple returns calculation ***************************************\n")
        returns = self.simple_returns(adj, cum)
        if self.withindex:
            #we remove the benchmark index from the portfolio
            returns.drop(columns=self.index_symbols, inplace=True)    
        print('portfolio''s weight simple return')
        print(self.generated_weights_df)
        print('returns')
        print(returns)   
        self.weighted_simple_returns_df = (returns*self.generated_weights_df).sum(axis=1)
        print(self.weighted_simple_returns_df)
        return self.weighted_simple_returns_df 

    # calculate weighted total returns for the portfolio    
    def portfolio_total_returns(self, adj = False, log = False):
        print(" ****************** The porfolio total returns calculation (with Dividends) ***********************\n")
        if self.weighted_total_returns_df.empty: 
            returns = self.total_returns(adj).fillna(0)
            #we remove the benchmark index from the portfolio
            if self.withindex:
                returns.drop(columns=self.index_symbols, inplace=True)
            #let's make sure the tickers are in the same order in both matrix
            if len(self.tickers)>1:
                returns = returns.sort_index(axis=1)
                if self.weight_method == 'Custom' and self.weights is not None:
                    self.generated_weights_df = self.generated_weights_df.sort_index(axis=1)
            print('returns')
            print(returns)
            print('portfolio weights')
            print(self.generated_weights_df)
            print('portfolio''s weight total returns')
            temp_df = returns.mul(self.generated_weights_df).fillna(1)
            print("temp_df")
            print(temp_df)
            self.weighted_total_returns_df = temp_df.sum(axis=1)
            print(self.weighted_total_returns_df)
        return self.weighted_total_returns_df 

    # calculate weighted total returns for the portfolio    
    def portfolio_todate_total_returns(self, adj = False, log = False):
        print(" ****************** The porfolio toDate total returns calculation *********************************\n")
        if self.weighted_todate_returns_df.empty: 
            returns = self.toDate_total_returns(adj).fillna(0)
            #we remove the benchmark index from the portfolio
            if self.withindex:
                returns.drop(columns=self.index_symbols, inplace=True)
            print('portfolio''s weight todate total returns')
            print(self.generated_weights_df)
            print('returns')
            print(returns)
            print('weighted return')
            self.weighted_todate_returns_df = (returns*self.generated_weights_df).sum(axis=1)
            # Calculate the difference between the two dates , we will need the number of days of holding to calculate the annualized total returns
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.start_date, '%Y-%m-%d')
            #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
            self.annualized_weighted_todate_returns_df =  ((1+(self.weighted_todate_returns_df/100))**(365.25/(self.weighted_todate_returns_df.index-date1).days)-1)*100
            print(self.weighted_todate_returns_df)
        return self.weighted_todate_returns_df

    # calculate weighted total returns for the portfolio    
    def portfolio_fromdate_total_returns(self, adj = False, log = False):
        print(" ****************** The porfolio fromDate total returns calculation *******************************\n")
        if self.weighted_fromdate_returns_df.empty:
            returns = self.fromDate_total_returns(adj).fillna(0)
            print(returns)
            #we remove the benchmark index from the portfolio
            if self.withindex:
                returns.drop(columns=self.index_symbols, inplace=True)
            print('portfolio''s weighted fromdate total returns')
            print(self.generated_weights_df)
            print('returns')
            print(returns)
            print('weighted returns')
            self.weighted_fromdate_returns_df = (returns*self.generated_weights_df).sum(axis=1)
            print(self.weighted_fromdate_returns_df)
            # Calculate the difference between the two dates , we will need the number of days of holding to calculate the annualized total returns
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.end_date, '%Y-%m-%d')
            #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
            self.annualized_weighted_fromdate_returns_df =  ((1+(self.weighted_fromdate_returns_df/100))**(365.25/(date1-self.weighted_fromdate_returns_df.index).days)-1)*100
        return self.weighted_fromdate_returns_df

    # calculate weighted total dividends for the portfolio    
    def portfolio_fromdate_dividends(self, adj = False, log = False):
        print(" ****************** The porfolio fromDate Dividends calculation *******************************\n")
        if self.weighted_fromdate_dividends_df.empty:
            dividends = self.calculate_dividend(adj, 'fromdate').fillna(0)
            print(dividends)
            #we remove the benchmark index from the portfolio
            if self.withindex:
                dividends.drop(columns=self.index_symbols, inplace=True)
            print('portfolio''s weighted fromdate dividends')
            print(self.generated_weights_df)
            print('returns')
            print(dividends)
            print('weighted dividends')
            self.weighted_fromdate_dividends_df = (dividends*self.generated_weights_df).sum(axis=1)
            print(self.weighted_fromdate_dividends_df)
            # Calculate the difference between the two dates , we will need the number of days of holding to calculate the annualized total dividends yield
            # Parse the dates from strings into datetime objects
            date1 = datetime.strptime(self.end_date, '%Y-%m-%d')
            #calculate the annualized rate of return at the end of the period https://www.investopedia.com/terms/a/annualized-total-return.asp
            self.annualized_weighted_fromdate_dividends_df =  ((1+(self.weighted_fromdate_dividends_df/100))**(365.25/(date1-self.weighted_fromdate_dividends_df.index).days)-1)*100
        return self.weighted_fromdate_dividends_df

    # draw returns for the portfolio    
    def portfolio_returns_plot(self, adj = False, cum = True, log = False, template = 'plotly_dark'):
        if cum is False:
            returns = self.portfolio_simple_returns(adj, cum).mul(100)
        else:
            returns = self.portfolio_total_returns(adj, cum)
        if log:
            returns = self.log_returns(adj, cum).mul(100)
        returns = returns.rename(self.prtfname)
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = self.prtfname, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio " + str(self.prtfname) + " Total Returns with " + self.weight_method + " from " + str(self.start_date) + "(with Dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        fig = self.brand_graphic(fig)                
        fig.show() 

    # draw returns for the portfolio    
    def portfolio_fromdate_total_returns_plot(self, benchmark = False, adj = False, template = 'plotly_dark'):
        returns = self.portfolio_fromdate_total_returns(adj) 
        returns = returns.rename(self.prtfname)
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = self.prtfname, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio " + str(self.prtfname) + " fromDate Total Returns with " + self.weight_method + " (with Dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        fig = self.brand_graphic(fig)                
        fig.show() 

    #Nicolas - add a function to calculate and draw annualized todate total return on the portfolio
    def portfolio_annualized_fromdate_total_returns_plot(self, adj = False, template = 'plotly_dark', show=True):
        returns = self.portfolio_fromdate_total_returns(adj)
        returns = self.annualized_weighted_fromdate_returns_df[:-3]
        returns = returns.rename(self.prtfname)
        if self.withindex:
            index_returns = self.annualized_fromdate_total_returns_df.drop(columns=self.tickers, inplace=False)
            # Concatenate index returns with ticker returns
            returns_with_index = pd.concat([returns, index_returns], axis=1)
        else:
            returns_with_index = returns
        print("---- annualized fromdate total returns ------\n")
        print(returns_with_index)
        #the last values (less than a year) can show high volatility as short term performance is amplified when we annualized the data. So we may want to skip them when calculating the mean  
        portfolio_mean = self.annualized_weighted_fromdate_returns_df.iloc[:-3].mean()
        portfolio_std = self.annualized_weighted_fromdate_returns_df.iloc[:-3].std()
        print("Portfolio fromdate mean returns:" + str(portfolio_mean))
        print("Portfolio fromdate returns std:" + str(portfolio_std))
        graph_legend = "The mean portfolio fromDate total returns is " + "{:.2f}".format(portfolio_mean) + " % per annum with a std deviation of " + "{:.2f}".format(portfolio_std)
        fig = px.line(returns_with_index, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = graph_legend, orientation="h", font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Annualized fromDate Total Returns for the portfolio " + str(self.prtfname) + " (with dividends) in " + str(self.refcurrency) + " since " + str(self.start_date),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        fig = self.brand_graphic(fig)
        fig.show() 
        return returns
    
    # draw returns for the portfolio    
    def portfolio_todate_total_returns_plot(self, benchmark = False, adj = False, template = 'plotly_dark'):
        returns = self.portfolio_todate_total_returns(adj)
        returns = returns.rename(self.prtfname)
        fig = px.line(returns, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = self.prtfname, font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio toDate Total Returns with " + self.weight_method + " since " + str(self.start_date) + " (including Dividends) in " + str(self.refcurrency),
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        fig = self.brand_graphic(fig)              
        fig.show() 

    #Nicolas - add a function to calculate and draw annualized todate total return on the portfolio
    def portfolio_annualized_todate_total_returns_plot(self, adj = False, template = 'plotly_dark'):
        returns = self.portfolio_todate_total_returns(adj)
        returns = self.annualized_weighted_todate_returns_df
        returns = returns.rename(self.prtfname)
        #we also want to display the indexes as benchmark
        index_returns = self.annualized_todate_total_returns_df.drop(columns=self.tickers, inplace=False)
        # Concatenate index returns with ticker returns
        returns_with_index = pd.concat([returns, index_returns], axis=1)
        print("---- annualized todate total returns ------\n")
        print(returns)
        portfolio_mean = self.annualized_weighted_todate_returns_df.mean()
        portfolio_std = self.annualized_weighted_todate_returns_df.std()
        print("Portfolio mnean returns:" + str(portfolio_mean))
        print("Portfolio returns std:" + str(portfolio_std))
        graph_legend = "The mean portfolio since " + str(self.start_date) + " total returns is " + "{:.2f}".format(portfolio_mean) + " % per annum with a std deviation of " + "{:.2f}".format(portfolio_std)
        fig = px.line(returns_with_index, template = template)
        fig.update_traces(hovertemplate='%{y:.2f}%')
        fig.update_layout(
            showlegend = True,
            legend = dict(title = graph_legend, orientation="h", font = dict(size = 16)),
            title={
                'y':0.95,
                'x':0.5,
                'text': f"Annualized toDate Total Returns for the portfolio " + str(self.prtfname) + " (with Dividends) since " + str(self.start_date) + " in " + str(self.refcurrency),
                'font': {'size': 24},
                
                'xanchor': 'center',
                'yanchor': 'top'},
            hovermode = "x unified",
            xaxis_title = "Date",
            yaxis_title = "% Returns")
        fig = self.brand_graphic(fig)   
        fig.show() 
        return returns

    def portfolio_fromdate_cov_matrix(self, plot = True, cum = False, template = 'plotly_dark'):
        returns = self.portfolio_fromdate_total_returns(self.adj)
        returns = self.annualized_weighted_fromdate_returns_df[:-3]
        returns = returns.rename(self.prtfname)
        if self.withindex:
            index_returns = self.annualized_fromdate_total_returns_df.drop(columns=self.tickers, inplace=False)
            # Concatenate index returns with ticker returns
            returns_with_index = pd.concat([returns, index_returns], axis=1)
        else:
            returns_with_index = self.annualized_fromdate_total_returns_df
        print("---- portfolio covariance matrix for fromDate returns  ------\n")
        print(returns_with_index)
        cov_matrix = returns_with_index.cov()
        if plot:
            fig = px.imshow(cov_matrix, text_auto=True, color_continuous_scale='tempo', template = template, title = "Covariance Matrix for " + self.refcurrency + " returns")
            fig.update_layout(
                legend = dict(title = None),
                title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio " + str(self.prtfname) + " " + str(self.refcurrency) + " returns covariance matrix",
                'xanchor': 'center',
                'yanchor': 'top'}
                )
            fig = self.brand_graphic(fig)
            fig.show()
        return cov_matrix
        
    def portfolio_fromdate_corr_matrix(self, plot = True, cum = False, template = 'plotly_dark'):
        returns = self.portfolio_fromdate_total_returns(self.adj)
        returns = self.annualized_weighted_fromdate_returns_df[:-3]
        returns = returns.rename(self.prtfname)
        if self.withindex:
            index_returns = self.annualized_fromdate_total_returns_df.drop(columns=self.tickers, inplace=False)
            # Concatenate index returns with ticker returns
            returns_with_index = pd.concat([returns, index_returns], axis=1)
        else:
            returns_with_index = self.annualized_fromdate_total_returns_df
        print("---- portfolio correlation matrix for fromDate returns ------\n")
        print(returns_with_index)
        corr_matrix = returns_with_index.corr()
        if plot:
            fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='tempo', template = template, title = "Correlation Matrix for " + self.refcurrency + " returns" )
            fig.update_layout(
                legend = dict(title = None),
                title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio " + str(self.prtfname) + " " + str(self.refcurrency) + " returns correlation matrix",
                'xanchor': 'center',
                'yanchor': 'top'}
                )
            fig = self.brand_graphic(fig)
            fig.show()
        return corr_matrix
    
        #Standard Deviation of Portfolio w/ Optional Crypto Arg
    def portfolio_port_std(self, crypto = False):
        if crypto:
            trading_days = 365.25
        else:
            trading_days  = 252

        cov_matrix = self.cov_matrix()
        port_variance = np.dot(self.weights.T, np.dot(cov_matrix, self.weights))
        port_std = np.sqrt(port_variance) * np.sqrt(trading_days)

        return port_std
    
    def portfolio_risk_return(self, adj = False, crypto = False, template = 'plotly_dark'):
        returns = self.portfolio_simple_returns(adj).mul(100)
        if crypto:
            trading_days = 365.25
        else:
            trading_days  = 252
        summary = returns.describe().T.loc[:,["mean","std"]]
        summary["mean"] = round(summary["mean"]*trading_days,2) # Multiply by number of trading days
        summary["std"]  = round(summary["std"]*np.sqrt(trading_days),2)
        summary.rename(columns = {'mean':'% Return', 'std':'Risk'}, inplace = True) 
        fig = px.scatter(summary, 
                         x = 'Risk', 
                         y = '% Return', 
                         title = "Annual Risk / Return",
                         text = summary.index,
                         template = template)
        fig.update_traces(hovertemplate='Risk: %{x}<br>Return: %{y}')
        fig.update_traces(marker={'size': 15},
                          textposition='top center',
                          hoverlabel=dict(font=dict(size=15) ))
        fig.update_layout(
            legend = dict(title = None),
            title={
            'y':0.9,
            'x':0.5,
            'text': "Portfolio " + str(self.prtfname) + " risks/ returns analysis in " + str(self.refcurrency),
            'font': {'size': 24},
            'xanchor': 'center',
            'yanchor': 'top',},
            xaxis = dict(title = dict(font = dict(size = 20))),
            yaxis = dict(title = dict(font = dict(size = 20)))
            )
        fig = self.brand_graphic(fig)
        fig.show()
    
    def portfolio_pie_plot(self, template = 'plotly_dark'):
        if isinstance(self.generated_weights_df, pd.DataFrame):
            data = pd.DataFrame({"Assets": self.generated_weights_df.columns,"Weights": self.generated_weights_df.mean()})
        elif isinstance(self.generated_weights_df, pd.Series):
            data = pd.DataFrame({"Assets": self.tickers, "Weights": self.generated_weights_df.mean()})
        else:
            data = pd.DataFrame({"Assets": self.tickers, "Weights": self.generated_weights_df})
        fig=go.Figure(go.Pie(labels=data['Assets'],
                                 values=data['Weights'],
                                 name = "",
                                 textinfo = 'label + percent'))
        fig.update_layout(
            template = template,
            title={
                'y':0.95,
                'x':0.5,
                'text': "Portfolio " + str(self.prtfname) + " mean assets allocation due to " + self.weight_method + " weighting method",
                'font': {'size': 24},
                'xanchor': 'center',
                'yanchor': 'top'},
                )
        fig.update_traces(hovertemplate='%{label}: %{percent}')
        fig = self.brand_graphic(fig)
        fig.show()


