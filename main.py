''''
KOI v1.0.2
Credits to the original stock_analyzer.py from StevenMedvetz version 2.0. It was a starting point for the Asset Class and Portfolio Class
Credits to James Eagle for the total return calculation
Rest of the code is from Nicolas Payen
how to install package
pip3 install pandas --upgrade --no-cache-dir
'''
# Install the yfinance and pandas package with pip if you don't have it.
import yfinance as yf
import pandas as pd
import numpy as np
import sys
#install package for graph
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#install package for date manipulation
from datetime import datetime, timedelta
#other impots
import random

#import stock_analyzer.py 
import stock_analyzer as sa
#import portfolio_analyzer.py 
import portfolio_analyzer as pa
#import portfolio_benchmark.py 
import portfolios_benchmark as pb
#import equity_research_tickers.py 
import equity_research_tickers as ert
#import equity_research_tickers.py 
import fourGs_portfolio as fourGs


#env set-up
#i send the output to the webbrowser
pio.renderers.default = "browser"
#I want to see all data in the console
np.set_printoptions(threshold=np.inf)
# Permanently changes the pandas settings
pd.reset_option("all")
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', None)

myPortfolioData = []
tickerSymbols = []
tickerWeights = None

#function for the user to pick a stock
def pick_stock():
    ticker_input = input('What is the ticker of the stock you would like to analyze\n? TSLA is the ticker for TESLA\n')
    ticker = yf.Ticker(str(ticker_input))
    info = None
    try:
        info = ticker.info
        return ticker_input.upper()
    except ValueError:
        raise NameError("You did not input a correct stock ticker! AAPL is the ticker for APPlE INC. Try again.")
        self.pick_stock()  

#function for the user to enter the duration of the analysis
def pick_duration():
	date_input = 20
	date_input = input('How many years do you want this analyze to cover\n?')
	years = 20
	try:
		years = int(date_input)
		return years
	except ValueError:
		raise NameError("You did not enter a valid number of years. Try again.")
		self.pick_duration()

#ask the user to pick the duration
years_input = pick_duration()
#calculate end of period
print("Current time: ", datetime.now())
end_period = datetime.now().strftime("%Y-%m-%d")
print("end date is: " + end_period)
#calculate start of period
calcdays = ( -1 * int(years_input) * 365 )
start_period = datetime.now() + timedelta(days=calcdays)
start_period = start_period.strftime("%Y-%m-%d")
print("start date is: " + start_period)

'''
print('***************************************************************************************************************************************')
#We ask the user about the stock ticker he wants to work with here. Just grab them of Yahoo Finance
if tickerSymbols is None: 
	tickerinput = pick_stock()
	tickerSymbols = []
	tickerSymbols.append(tickerinput)
	YN = "Yes"
	while YN == 'Yes' or YN == 'Y' or YN == 'yes':
		YN = input('Do you want to compare it with another stock (Y/N)\n?')
		if YN == 'Yes' or YN == 'Y' or YN == 'yes':
			tickerinput = pick_stock()
			tickerSymbols.append(tickerinput)

if tickerWeights is None:
	if len(tickerSymbols)>1:
		tickerWeights = [ 1 for x in range(len(tickerSymbols))]
	else:
		tickerWeights = [ 1 ]

#Let's create a list of Assets 


print('***************************************************************************************************************************************')
myAsset = sa.Asset(tickerSymbols, start_period, end_period, None, '^TNX', False)
print("Total return on myAsset\n")
myAsset.returns_plot()
myAsset.candlestick()
#myAsset.total_returns_plot()
myAsset.todate_total_returns_plot()
myAsset.annualized_todate_total_returns_plot()
myAsset.fromdate_total_returns_plot()
myAsset.annualized_fromdate_total_returns_plot()

#Let's create a portfolio that includes a list of Assets 
print("Portfolio work and graphs\n")
myPortfolio = pa.Portfolio('test portfolio', tickerSymbols, start_period, end_period, 'Random', None, 'EUR', True)
myPortfolio.portfolio_returns_plot()
myPortfolio.portfolio_todate_total_returns_plot()
myPortfolio.portfolio_fromdate_total_returns_plot()
myPortfolio.portfolio_annualized_todate_total_returns_plot()
myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
myPortfolio.portfolio_pie_plot()

myPortfolio = pa.Portfolio('test portfolio', tickerSymbols, start_period, end_period, 'EqualWeight', None, 'EUR', False)
myPortfolio.total_returns_plot()
myPortfolio.candlestick()
myPortfolio.todate_total_returns_plot()
myPortfolio.annualized_todate_total_returns_plot()
myPortfolio.fromdate_total_returns_plot()
myPortfolio.annualized_fromdate_total_returns_plot()
myPortfolio.todate_totalreturn_risk_return_plot()
myPortfolio.fromdate_totalreturn_risk_return_plot()
myPortfolio.portfolio_returns_plot()
myPortfolio.portfolio_todate_total_returns_plot()
myPortfolio.portfolio_fromdate_total_returns_plot()
myPortfolio.portfolio_annualized_todate_total_returns_plot()
myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
myPortfolio.portfolio_pie_plot()
myPortfolio.marketcap_plot()

myPortfolio = pa.Portfolio('test portfolio', tickerSymbols, start_period, end_period, 'CustomWeight', tickerWeights, 'EUR', True)
myPortfolio.portfolio_returns_plot()
myPortfolio.portfolio_todate_total_returns_plot()
myPortfolio.portfolio_fromdate_total_returns_plot()
myPortfolio.portfolio_annualized_todate_total_returns_plot()
myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
myPortfolio.portfolio_pie_plot()

myPortfolio = pa.Portfolio('test portfolio', tickerSymbols, start_period, end_period, 'CustomDynamicWeight', tickerWeights, 'EUR', True)
myPortfolio.total_returns_plot()
myPortfolio.todate_total_returns_plot()
myPortfolio.annualized_todate_total_returns_plot()
myPortfolio.fromdate_total_returns_plot()
myPortfolio.annualized_fromdate_total_returns_plot()
myPortfolio.portfolio_returns_plot()
myPortfolio.portfolio_todate_total_returns_plot()
myPortfolio.portfolio_fromdate_total_returns_plot()
myPortfolio.portfolio_annualized_todate_total_returns_plot()
myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
myPortfolio.portfolio_pie_plot()
myPortfolio.marketcap_plot()
myPortfolio.portfolio_corr_matrix()
myPortfolio.portfolio_cov_matrix()
'''

# ************************************************************
# Add portfolio(s) to the benchmarking tool
# ************************************************************
#Create the tool to benchmark and analyze portfolios, choose the currency of reference
print('***************************************************************************************************************************************')
myPortfolioBenchmarkBench = pb.Portfolio_benchmark_bench(start_period, end_period, 'EUR')

#I add portfolio(s) to the benchmark bench
#myPortfolioBenchmarkBench.add_portfolio('4Gs', fourGs.FourGs, 'CustomDynamicWeight')

#myPortfolioBenchmarkBench.add_portfolio('4Gs Dynamic', fourGs.FourGs_Dynamic, 'CustomDynamicWeight')
#myPortfolioBenchmarkBench.add_portfolio('4Gs Base', fourGs.FourGs_Base, 'CustomDynamicWeight')
myPortfolioBenchmarkBench.add_portfolio('4Gs Green', fourGs.FourGs_Green, 'CustomDynamicWeight')
#myPortfolioBenchmarkBench.add_portfolio('4Gs Grey', fourGs.FourGs_Grey, 'CustomDynamicWeight')
#myPortfolioBenchmarkBench.add_portfolio('4Gs GenGrat', fourGs.FourGs_GenGrat, 'CustomDynamicWeight')
#myPortfolioBenchmarkBench.add_portfolio('4Gs Yield', fourGs.FourGs_Yield, 'CustomDynamicWeight')

myPortfolioBenchmarkBench.add_portfolio('4Gs PipelineP1', fourGs.FourGs_PipelineP1, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Solar', ert.ClimateTech_SOLAR, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Wind', ert.ClimateTech_WIND, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Storage', ert.ClimateTech_STORAGE, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Grid', ert.ClimateTech_GRID, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech eMobility', ert.ClimateTech_EMOBILITY, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech EVcharging', ert.ClimateTech_EVCHARGING, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Elec', ert.ClimateTech_ELEC, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Heat', ert.ClimateTech_HEAT, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Infra', ert.ClimateTech_INFRA, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Power', ert.ClimateTech_POWER, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Nuclear', ert.ClimateTech_NUCL, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Waste', ert.ClimateTech_WASTE, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Fuel', ert.ClimateTech_CleanFUEL, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech H2', ert.ClimateTech_HTWO, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('ClimateTech Water', ert.ClimateTech_WATER, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Magnificient 7 (US*)', ert.MAG_SEVEN, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Granolas (EU*)', ert.GRANOLAS, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Automation', ert.Automation_Robotic, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('AI', ert.Artificial_Intelligence, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Health Tech', ert.HealthTech, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Health Infra', ert.HealthInfra, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Health Care', ert.HealthCare, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Health Drugs', ert.HealthDrug, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Coal', ert.COAL, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Oil & Gas', ert.OIL_GAS, 'EqualWeight')

# ************************************************************
# Display detailed graphis for given portfolio(s)
# ************************************************************
#myPortfolioBenchmarkBench.display_portfolio_charts('4Gs')
#myPortfolioBenchmarkBench.display_portfolio_charts('4Gs PipelineP1')

#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Solar')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Wind')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Storage')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Grid')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech eMobility')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech EVcharging')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Elec')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Heat')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Infra')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Power')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Nuclear')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Waste')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Fuel')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech H2')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Water')

#myPortfolioBenchmarkBench.display_portfolio_charts('Magnificient 7 (US*)')
#myPortfolioBenchmarkBench.display_portfolio_charts('Granolas (EU*)')

#myPortfolioBenchmarkBench.display_portfolio_charts('Automation')
#myPortfolioBenchmarkBench.display_portfolio_charts('AI')

# ************************************************************
# Commpare portfolio(s) performances
# ************************************************************
myPortfolioBenchmarkBench.compute_fromdate_sharpe_ratios()
#benchmark portfolio
myPortfolioBenchmarkBench.portfolio_risks_fromdate_totalreturns_plot()


