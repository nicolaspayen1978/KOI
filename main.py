'''
KOI v1.0.1
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

#import stock_analyzer.py 
import stock_analyzer as sa
#import portfolio_analyzer.py 
import portfolio_analyzer as pa
#import portfolio_benchmark.py 
import portfolios_benchmark as pb



#install package for date manipulation
from datetime import datetime, timedelta

#other impots
import random

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

#in case you want to overwrite the list of tickers manually, do not mix tickers from different stock exchanges
#*************************************** 4GS PORTFOLIO *************************************************************
# ******************************
# Section: 4Gs Climate Tech Portfolio
# ******************************
# This section defines the 4Gs portfolio that I manage focusing on climate technology,
# [tickers, nb_shares] which can be updated as needed to reflect changes in the portfolio.
FourGs_Green = [['SU.PA', 271], ['AI.PA', 175], ['TOM.OL', 600], ['VOW.DE', 60], ['VWSB.DE', 225], ['ORSTED.CO', 151], ['NEX.PA', 25], ['TSLA', 269], ['WM', 90], ['NEE', 245], ['BEPC', 420], ['DQ', 162], ['ENPH', 25], ['601012.SS', 9120], ['0175.HK', 4000], ['2208.HK', 9200], ['002594.SZ', 200], ['LTOD.IL', 75], ['6752.T', 1000], ['GEV', 110], ['NEP', 1597]]

#*************************************** GREEN - CLIMATE TECH *************************************************************
# ******************************
# Section: Climate Tech Portfolio Definitions
# ******************************
# This section defines portfolios that focus on different themes in climate technology,
# such as solar, wind, and storage. Each portfolio is represented as a list of stock
# tickers, which can be updated as needed to reflect changes in the market.
# these lists are created and maintained by Nicolas Payen. They may not be up-to-date
# some Tickers that generate errors when retrieving data from Yahoo Finance have been removed (mainly ticker with .L)
ClimateTech_SOLAR = ['AGX']
ClimateTech_SOLAR += ['NXT', 'CPV.XA', 'RELIANCE.NS', '601012.SS', '300274.SZ', 'FSLR', '600438.SS', '688223.SS', 'ENPH', '002459.SZ', '688599.SS', 'SOLARINDS.BO', 'SEDG', '009830.KS', '3800.HK']
ClimateTech_SOLAR += ['BSIF.L', 'NESF.L', '600732.SS', '300763.SZ', '002056.SZ', '000591.SZ', '300118.SZ', '688390.SS', 'ARRY', 'SHLS', '002518.SZ', 'RUN', '300393.SZ', 'DQ', 'S92.DE', 'JKS']
ClimateTech_SOLAR += ['000880.KS', 'CSIQ', 'NOVA', 'RECSI.OL', 'SOLT.ST', 'MBTN.SW', 'AMPS', 'MAXN', 'SOL', 'FTCI', 'SOLR.V', 'ASTI', '13X.SG']
ClimateTech_SOLAR += ['RIGD.IL', 'ZODIAC.NS']
##remove due to issue with currency 'SOLAR.BK', '1785.TWO', '688717.SS'

ClimateTech_WIND = ['UKW.L', 'TPIC', 'NRDXF', 'TKA.DE', '001289.SZ', '601016.SS', '2727.HK','NDX1.DE', '300772.SZ', 'VIS18348-USD', 'SMNEY', '2208.HK', 'VWSB.DE', 'GE', 'ENR.DE', 'GEV']
#remove due to issue with currency and yahoo finance  'GWIND.IS'

ClimateTech_STORAGE = ['GRID.L', 'GSF.L', 'IKA.L', '688006.SS', '6409.TW', 'STEM', 'PLL', 'AMY.V', 'BES.V', 'NRGV', 'CBAT', 'QS', 'GWH', 'ENVX', 'FREY', 'SLDP', 'AMPX', 'ENR', 'NVNXF', 'NNOMF', 'ILIKF']
ClimateTech_STORAGE += ['688390.SS', '300014.SZ', '002074.SZ', '688567.SS', '300207.SZ', '3931.HK', '096770.KS', 'BYDDY', '006400.KS', 'FLUX', '6752.T', 'FLNC', '051910.KS', 'TSLA', '373220.KS', '300750.SZ']

ClimateTech_GRID = ['AGX', 'PWR', 'HUNGF', 'AGR', 'POWERGRID.NS', 'NGG', '600517.SS', 'AEP', 'XEL', 'PRY.MI', 'PLPC', 'POWL', '298040.KS', 'POWERINDIA.NS', 'ABBNY', 'KEC.NS', 'JYOTISTRUC.NS', 'LT.NS', 'NKT.CO', 'SMNEY', 'GE', 'SU.PA', 'GEV']

ClimateTech_EMOBILITY = ['UBER', 'TSLA', 'BYDDY', 'VOW.DE', 'LI', 'RIVN', 'NIO', 'XPEV', 'POAHY', '0175.HK', 'LCID', 'BOSCHLTD.BO', 'PSNY', '002056.SZ', 'QS', '688667.SS', 'KNDI', 'SLDP', 'GOEV', 'HYLN', 'GP', 'ILIKF', 'IDEX']
ClimateTech_EMOBILITY += ['IKA.L', 'FUV', 'AYRO', '9863.HK', 'BMW.DE', 'MBG.DE']
#remove due to issue with yahoo finance 'RIDE',


ClimateTech_EVCHARGING = ['PODP.L', '6409.TW', 'BLNK', 'SHLS', '688390.SS', 'ZAP.OL', 'BOSCHLTD.NS', 'TSLA', 'ADSE', 'NAAS', 'WKHS', 'CHPT', 'EVGO', 'WBX', 'DCFC'] 
#remove due to issue 'CRGE'

#ClimateTech ELECTRIFICATION & COMMODITY
ClimateTech_ELEC = ['ABBNY', 'ELHA.AT', '6409.TW', 'LIGHT.AS', '0QWC.IL', 'PLL', 'ZIJMF', 'AMY.V', 'MN.V', 'GLNCY', 'RCIIND.BO', 'KOD.L', 'SGML', 'VLX.L', 'ELBM', 'BHP', 'TECK', 'PRY.MI', 'CETY', 'NOVA', 'BHP1.F']
ClimateTech_ELEC += ['002460.SZ', '9696.HK', 'SQM', '1COV.DE', 'POWL', '298040.KS', '329180.KS', '6503.T', '6501.T', '688187.SS', '2727.HK', 'DQ', 'ETN', 'NGLOY', 'SCCO', 'ELK.OL', 'NKT.CO', 'ALB', 'WCH.DE']
ClimateTech_ELEC += ['LR.PA', 'NDA.DE', 'GE', 'SU.PA', 'E7V0.F', 'SOLAR-B.CO', 'GEV']

#Climate Tech ISOLATION & HEAT PUMP
ClimateTech_HEAT = ['ORA', 'SPXC', 'SKFOF', '000786.SZ', 'SOLB.BR', 'AKE.PA', 'BAS.DE', '3300.HK', 'KYOCY', 'AGCO', 'NIBE-B.ST', 'IR', 'JCI', '6367.T', 'BOSCHLTD.NS', '373220.KS', 'SGO.PA', 'ROCK-B.CO', 'ROCK-A.CO']

'AQNU'
#Climate Tech CLEAN INFRA COMPANY
ClimateTech_INFRA = ['BEP-PA', 'AMPS', 'NEP', 'AQN', 'ORA', 'CWEN-A', 'AGR', 'RNW', 'CEG', 'ADANIGREEN.NS', 'BEPC', 'CWEN', 'JLEN.L', 'FSFL.L', 'NESF.L', 'TRIG.L', 'BSIF.L', 'GRID.L', 'NEE', 'AMRC', 'AES', '0586.HK']
ClimateTech_INFRA += ['001289.SZ', 'SCATC.OL', 'ENEL.MI', 'ANA.MC', 'AY', 'BYW.DE', 'NEOEN.PA', 'NSOL.OL', 'VLTSA.PA', '000591.SZ', '6838.T', 'ECV.DE', 'IBDRY', 'RWE.DE', '300140.SZ', '601016.SS', 'ENGI.PA', 'RIGD.IL']
ClimateTech_INFRA += ['EVGRF', 'WM', 'ORSTED.CO', 'BEPC.TO', 'NHY.OL', 'EDPR.LS', 'ORIT.L']
#problem with currency 'PEN.PR', '2082.SR', 'AYDEM.IS'

#Climate Tech POWER UTILITIES
ClimateTech_POWER = ['OEWA.F', 'FOJCF', '600900.SS', '015760.KS', 'WEC', 'ED', 'PCG', 'XEL', 'NGG', 'AEP', 'SRE', 'D', 'SO', 'NEE-PR', 'DUK', '0MC5.IL']
#remove due to issue 'AESC'

#Climate Tech NUCLEAR
ClimateTech_NUCL = ['FOJCF', 'UEC', '0611.HK', '601611.SS', 'PALAF', 'SMR', '015760.KS', '000881.SZ', 'UCLE', 'NLR', '601985.SS', 'CCJ', 'UUUU', 'DNN']

#Climate Tech WASTE
ClimateTech_WASTE = ['WM', 'SY9.F', 'NORVA.ST', '300190.SZ', '0K8W.IL', '9221.T', 'AWHCL.BO', '6564.T', '9336.T', '5857.T', '9247.T', 'CLG.AX', 'CWY.AX', 'RWI.AS', 'VEOEY', 'RSG', 'GFL', 'SRCL', 'MEG', 'CWST', 'CLH', 'WCN']

#Climate Tech CLEAN FUEL
ClimateTech_CleanFUEL = ['HLGN', 'ORA', 'GRN.TO', 'PYR.TO', 'PHE.L', 'VSL.L', 'EQT.L']

#Climate Tech GREEN HYDROGEN
ClimateTech_HTWO = ['HLGN', 'BLDP', 'VSL.L', 'CPH2.L', 'CWR.L', 'AFC.L', 'HGEN.L', 'ATOM.L', 'FCEL', 'NEL.OL', 'ITM.L', 'PLUG', 'CMI', 'SMNEY', 'TKA.DE', 'GREENH.CO', 'H2O.DE', 'BE', 'APD', 'AI.PA'] 

#Climate Tech WATER
ClimateTech_WATER = ['VLTO', '0270.HK', '300070.SZ', 'BJWTF', 'XYL', 'VEOEY', 'AWK', '6370.T', '0807.HK']

#*************************************** AI *************************************************************
# ******************************
# Section: AI, Automation, Robotic
# ******************************
#automation and robotic 
Automation_Robotic = ['6201.T', 'MBLY', 'ABBNY', 'MSBHF', 'EMR', 'DNZOF', 'ROK', 'FANUY', '300124.SZ', '6506.T', 'OMRNY', 'SEKEY', 'KWHIY', '000150.KS', 'PDYN', 'CDNS', 'FICO']
# 'RWLK', 
#Artifical Intelligence (AI)
Artifical_Intelligence = ['AI', 'ANET', 'ADBE', 'ASML', 'UPST', 'SYM', 'ISRG', 'SNOW', 'AME', 'MRVL', 'ANSS', 'EQIX', 'IBM', 'AMZN', 'GOOG', 'MSFT', 'SOI.PA', 'SMCI', 'AMD', 'INTC', 'NVDA']

#*************************************** HEALTHCARE *************************************************************
#healthcare - Health Tech
HealthTech = ['A', 'ABBV', 'ABT', 'ACCD', 'AGTI', 'AKYA', 'ALC', 'ALGN', 'AMGN', 'ANGO', 'ANIK', 'ATEC', 'ATR', 'ATRI','AXNX', 'AZN', 'AZTA', 'BAX', 'BDX', 'BIO', 'BIO-B']
HealthTech += ['BLCO', 'BMY', 'BRKR', 'BSX', 'BTSG', 'CERT', 'CGON', 'CI', 'CMAX', 'CNMD', 'COO', 'CPSI', 'DGX', 'DH', 'DHR', 'DOCS', 'DXCM', 'EMBC', 'EVH', 'EW']
HealthTech += ['GDRX', 'GEHC', 'GILD', 'GKOS', 'GMED', 'HAE', 'HCA', 'HCAT', 'HQY', 'HSTM', 'ICUI', 'IDXX', 'INSP', 'IQV', 'IRTC', 'ISRG', 'ITGR', 'JNJ', 'LIVN', 'LLY']
HealthTech += ['MASI', 'MDRX', 'MDT', 'MMSI', 'MRK', 'MTD', 'MYGN', 'NARI', 'NRC', 'NVST', 'OMCL', 'OSUR', 'PEN', 'PGNY', 'PHR', 'PINC', 'PODD', 'PRVA', 'QDEL']
HealthTech += ['RCM', 'REGN', 'RGEN', 'RMD', 'RVTY', 'SDGR', 'SHC', 'SLP', 'SNN', 'SPOK', 'STE', 'STVN', 'SWAV', 'SYK', 'TDOC', 'TFX', 'THC', 'TMO', 'TXG']
HealthTech += ['UTMD', 'VEEV', 'VRTX', 'WAT', 'WRBY', 'WST', 'XRAY', 'ZBH'] 

#healthcare - Health Infra
HealthInfra = [ 'IART', 'LH', 'HR', 'DOC', 'LTC', 'CHCT', 'UHT', 'GMRE', 'NHI', 'CTRE', 'SBRA', 'OHI', 'PEAK', 'VTR', 'WELL', 'GMRE-PA' ]

#healthcare - Health Care
HealthCare = [ 'ALHC', 'CAH', 'CNC', 'COR', 'CRL', 'CVS', 'ELV', 'GH', 'GSK', 'HSIC', 'HUM', 'ICLR', 'MCK', 'MOH', 'NEUE', 'OMI', 'OSCR', 'PDCO', 'PFE', 'SNY', 'UNH', 'ZYXI'] 

#healthcare molecule
HealthDrug = ['ACOR', 'ALKS', 'AMPH', 'AMRX', 'BHC', 'BIIB', 'COLL', 'CTLT', 'DCPH', 'DVAX', 'ELAN', 'EVO', 'HCM', 'HLN', 'ILMN', 'INDV', 'IRWD', 'ITCI', 'KMDA']
HealthDrug += ['LFCR', 'MEDP', 'MRNA', 'NBIX', 'NEOG', 'NTRA', 'NVO', 'NVS', 'PBH', 'PCRX', 'PETQ', 'PRGO', 'QGEN', 'RDY', 'TAK', 'TARO', 'TEVA', 'TWST', 'VTRS', 'ZTS'] 

#*************************************** OTHER *************************************************************
#tickerSymbols = ['ENPH', 'TSLA', 'FSLR', 'NEE', 'SHEL', 'XOM', 'CVX', 'BP']
#US Magnificient 7 or 8 ;-)
MAG_SEVEN = ['GOOG', 'TSLA', 'AAPL', 'META', 'MSFT', 'NFLX', 'NVDA', 'AMZN']
# EU Magnificient 7 or 8 ;-) Granolas
GRANOLAS= ['GSK', 'ROG.SW', 'ASML', 'NSRGY', 'NVS', 'NVO', 'OR.PA', 'MC.PA', 'AZN', 'SAP', 'SNY']

#*************************************** FOSSIL FUEL *************************************************************
#Coal
COAL = ['GLNCY', 'GMETCOAL.BO', '3315.T', 'AMR', 'SXC', 'SOL.AX', 'CRN.AX', 'SMR.AX', 'YAL.AX', 'NHC.AX', 'NC', 'NRP', 'CEIX', 'ARLP', 'BTU', 'HCC', 'METC', 'ARCH']
#O&G
OIL_GAS = ['WFRD', 'SAVE.L', 'IPO.TO', 'OKE', 'CTRA', 'EQNR', 'KEYUF', 'ATGFF', 'FRHLF', 'PMGYF', 'AETUF', 'PEYUF', 'TRMLF', 'BIREF', 'ZPTAF', 'CWEGF', 'ATHOF', 'GENGF']
OIL_GAS += ['JRNGF', 'TNEYF', 'MEGEF', 'SPGYF', 'CRLFF', 'CNNEF', 'CRNCY', 'TUWOY', 'AOIFF', 'TUWLF', 'PMOIF', 'EE', 'GLNCY', 'NHC.AX', 'SPM.MI', 'BOIL.L','SOI', 'PUMP']
OIL_GAS += ['WTTR', 'PARR', 'SBOW', 'TALO', 'PCCYF', 'EC', 'TRP', 'CHRD', 'SUN', 'SM', 'ATO', 'BKR', 'VET', 'HPK', 'DVN', 'VAL', 'SLB', 'PTEN', 'CVI', 'PBF', 'MGY']
OIL_GAS += ['NTPC.NS', 'IMO', '096770.KS', 'FANG', 'STOHF', 'EQT', 'FTI', 'VLO', '2222.SR', 'SNPMF', 'IMPP', 'CPE', 'PBR-A', 'MPC', 'OXY', 'E', 'CVX', 'XOM', 'SHEL', 'BP', 'TTE']

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

#Create the tool to benchmark and analyze portfolios, choose the currency of reference
print('***************************************************************************************************************************************')
myPortfolioBenchmarkBench = pb.Portfolio_benchmark_bench(start_period, end_period, 'EUR')

#add a portfolio
myPortfolioBenchmarkBench.add_portfolio('4Gs Green', FourGs_Green, 'CustomDynamicWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Solar', ClimateTech_SOLAR, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Wind', ClimateTech_WIND, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Storage', ClimateTech_STORAGE, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Grid', ClimateTech_GRID, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech eMobility', ClimateTech_EMOBILITY, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech EVcharging', ClimateTech_EVCHARGING, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Elec', ClimateTech_ELEC, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Heat', ClimateTech_HEAT, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Infra', ClimateTech_INFRA, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Power', ClimateTech_POWER, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Nuclear', ClimateTech_NUCL, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Waste', ClimateTech_WASTE, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech Fuel', ClimateTech_CleanFUEL, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech H2', ClimateTech_HTWO, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('ClimateTech H2', ClimateTech_WATER, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Coal', COAL, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Oil & Gas', OIL_GAS, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Health Tech', HealthTech, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Health Infra', HealthInfra, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Health Care', HealthCare, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Health Drugs', HealthDrug, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Generational', Generational, 'EqualWeight')
#myPortfolioBenchmarkBench.add_portfolio('Gratification', Gratification, 'EqualWeight')

#myPortfolioBenchmarkBench.add_portfolio('Automation', Automation_Robotic, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('AI', Artifical_Intelligence, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('Magnificient 7 (US*)', MAG_SEVEN, 'EqualWeight')
myPortfolioBenchmarkBench.add_portfolio('Granolas (EU*)', GRANOLAS, 'EqualWeight')

#display chart
#myPortfolioBenchmarkBench.display_portfolio_charts('4Gs Green')
#myPortfolioBenchmarkBench.display_portfolio_charts('Generational')
#myPortfolioBenchmarkBench.display_portfolio_charts('Gratification')
#myPortfolioBenchmarkBench.display_portfolio_charts('AI')
#myPortfolioBenchmarkBench.display_portfolio_charts('Automation')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Solar')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Storage')
#myPortfolioBenchmarkBench.display_portfolio_charts('ClimateTech Grid')
#myPortfolioBenchmarkBench.display_portfolio_charts('Magnificient 7 (US*)')
#myPortfolioBenchmarkBench.display_portfolio_charts('Granolas (EU*)')
myPortfolioBenchmarkBench.compute_fromdate_sharpe_ratios()
#benchmark portfolio
myPortfolioBenchmarkBench.portfolio_risks_fromdate_totalreturns_plot()


