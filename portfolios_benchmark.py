''' 
Created in April 2024 by Nicolas Payen to be able to benchmark several portfolios
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

import os
from PIL import Image
#import stock_analyzer.py 
import stock_analyzer as sa
#import portfolio_analyzer.py 
import portfolio_analyzer as pa


#install package for date manipulation
from datetime import datetime, timedelta

#other impots
import random

# Get the current working directory
#current_dir = "./Desktop/myPythonProjects/Portfoliotools/"
# Get the current working directory
current_dir = os.getcwd()
# Construct the file path to your JPEG image
image_path = os.path.join(current_dir, "Koi_logo3.png")
logo_img = Image.open("Koi_logo3.png")

pio.renderers.default = "browser"

'''
A portfolio benchmark bench is a tool to compare the performances of various portfolio 
Date format should be %Y-%m-%d
'''
class Portfolio_benchmark_bench():
	def __init__(self, start_date = None, end_date = datetime.today().strftime('%Y-%m-%d'), refcurrency = 'EUR', riskfreeticker = None):

		self.index_symbols = ['^GSPC', '^DJI', '^IXIC', '^STOXX', '^RUT', '^N225', '^FCHI', '^AEX']
		self.refcurrency = refcurrency
		self.start_date = start_date
		self.end_date = end_date
		self.portfolios_dict = {}
		self.portfolio_risksadjusted_fromdate_totalreturns = pd.DataFrame()

		#if start_date is unknown then we apply by default 5 years duration analysis
		if start_date is None:
			#calculate start of period
			calcdays = ( -5 * 365.25 )
			start_period = datetime.strptime(self.end_date, '%Y-%m-%d') + timedelta(days=calcdays)
			self.start_date = start_period.strftime("%Y-%m-%d") 

		#let's gather the datan for the riskfreeticker
		# we adjust the risk free ticker based on the duration of the analysis
		if riskfreeticker is None:
        	# Define your two dates
            # Convert the date strings to datetime object
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

		self.portfolios_dict[self.riskfreeticker] = pa.Portfolio(self.riskfreeticker, [self.riskfreeticker], self.start_date, self.end_date, 'EqualWeight', None, self.refcurrency, self.riskfreeticker, False, False)

		for index in self.index_symbols:
			#we create the intem in our portfolio for each of the indexes we use as benchmark, we give one Index at a time, so we put withIndex at False
			self.portfolios_dict[index] = pa.Portfolio(index, [index], self.start_date, self.end_date, 'EqualWeight', None, self.refcurrency, self.riskfreeticker, False, False)

	#function to add a portfolio to the bench
	def add_portfolio(self, prtfname, tickers_weights, weight_method = 'EqualWeight'):
		if prtfname in self.portfolios_dict:
				print("error : portfolio " + prtfname + " already exist")
				return None
		if weight_method == 'Custom' or weight_method == 'CustomDynamicWeight':
			myPortfolioDf = pd.DataFrame(tickers_weights, columns=['TICKET', 'QTY'])
			tickerSymbols = []
			tickerWeights = []
			for index, row in myPortfolioDf.iterrows():
				tickerSymbols.append(str(row['TICKET']))
				tickerWeights.append(str(row['QTY']))
		else:
			tickerSymbols = tickers_weights
			tickerWeights = None
		self.portfolios_dict[prtfname] = pa.Portfolio(prtfname, tickerSymbols, self.start_date, self.end_date, weight_method, tickerWeights, self.refcurrency, self.riskfreeticker, True, False) 
		return 

	#function to retrieve a given portfolio 
	def get_portfolio(self, prtfname):
		if prtfname in self.portfolios_dict:
			return self.portfolios_dict[prtfname]
		else:
			print("error : portfolio " + prtfname + " does not exist")
			return None

	#function to delete a portfolio from the bench
	def delete_portfolio(self, prtfname = " "):
		if prtfname not in self.portfolios_dict:
			print("error : portfolio " + prtfname + " does not exist")
			return None
		else:
			del self.portfolios_dict[prtfname]
		return 

	#function to run the various computation and display results
	def display_portfolio_charts(self, prtfname = 'all', showassetsgraphs=True, light = False):
		if prtfname != 'all':
			myPortfolio = self.get_portfolio(prtfname)
			if showassetsgraphs:
				#myPortfolio.total_returns_plot()
				#myPortfolio.todate_total_returns_plot()
				#myPortfolio.annualized_todate_total_returns_plot()
				#myPortfolio.todate_totalreturn_risk_return_plot()
				#myPortfolio.todate_total_return_corr_matrix()
				#myPortfolio.todate_total_returns_plot()
				#show candelstick with 2 months moving average and 16 month moving average
				myPortfolio.candlestick(2, 8, 14)
				myPortfolio.detect_double_bottoms_tops()
				myPortfolio.calculate_dividends(False, 'fromdate')
				myPortfolio.calculate_dividends(False, 'todate')
				myPortfolio.calculate_dividends(False, 'yearly')			
				myPortfolio.momentum_rsi_plot(14)
				myPortfolio.annualized_fromdate_total_returns_plot()
				myPortfolio.fromdate_totalreturn_risk_return_plot()
				myPortfolio.fromdate_total_return_corr_matrix()
				myPortfolio.fromdate_risk_dividends_plot()
			#myPortfolio.portfolio_returns_plot()
			#myPortfolio.portfolio_todate_total_returns_plot()
			#myPortfolio.portfolio_annualized_todate_total_returns_plot()
			myPortfolio.portfolio_fromdate_total_returns_plot()
			myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
			myPortfolio.marketcap_plot()
			myPortfolio.portfolio_pie_plot()
			myPortfolio.portfolio_fromdate_corr_matrix()
			myPortfolio.portfolio_fromdate_cov_matrix()
			if myPortfolio is None:
				print("error : portfolio " + prtfname + "is not in the portfolios'' dictionary")
				return
		else:
			for key, myPortfolio in self.portfolios_dict.items():
				if key not in self.index_symbols and key != self.riskfreeticker:
					if showassetsgraphs:
#							myPortfolio.total_returns_plot()
#							myPortfolio.todate_total_returns_plot()
#							myPortfolio.annualized_todate_total_returns_plot()
#							myPortfolio.todate_totalreturn_risk_return_plot()
#							myPortfolio.todate_total_return_corr_matrix()
							myPortfolio.candlestick(2, 8, 14)
							myPortfolio.calculate_dividends(False, 'fromdate')
							myPortfolio.calculate_dividends(False, 'todate')
							myPortfolio.calculate_dividends(False, 'yearly')
							myPortfolio.detect_double_bottoms_tops()
							myPortfolio.calculate_all_rsi()
							myPortfolio.fromdate_total_returns_plot()
							myPortfolio.annualized_fromdate_total_returns_plot()
							myPortfolio.fromdate_totalreturn_risk_return_plot()
							myPortfolio.fromdate_total_return_corr_matrix()
							myPortfolio.fromdate_risk_dividends_plot()
#					myPortfolio.portfolio_returns_plot()
#					myPortfolio.portfolio_todate_total_returns_plot()
#					myPortfolio.portfolio_annualized_todate_total_returns_plot()
					myPortfolio.portfolio_fromdate_total_returns_plot()
					myPortfolio.portfolio_annualized_fromdate_total_returns_plot()
					myPortfolio.marketcap_plot()
					myPortfolio.portfolio_pie_plot()
					myPortfolio.portfolio_fromdate_corr_matrix()
					myPortfolio.portfolio_fromdate_cov_matrix()
			return


	#function to run the various computation and display results
	def compute_fromdate_sharpe_ratios(self, showgraphs=True, template = 'plotly_dark'):
		portfolio_returns = pd.DataFrame()
		summary = pd.DataFrame()
		risk_free_portfolio = self.portfolios_dict[self.riskfreeticker]
		risk_free_portfolio.portfolio_fromdate_total_returns()
		risk_free_returns = risk_free_portfolio.annualized_weighted_fromdate_returns_df
		#for each_portfolio we want to get the returns 
		for key, myPortfolio in self.portfolios_dict.items():
			#let's calculate the fromdate total returns for the porfolio
			myPortfolio.portfolio_fromdate_total_returns()
			portfolio_returns = myPortfolio.annualized_weighted_fromdate_returns_df
			#we skip the last 3 periodes to remove high volatility due to short period
			summary.loc[key, 'Excess Returns %'] = (portfolio_returns-risk_free_returns).iloc[:-3].mean()
			summary.loc[key, 'Risks'] = (portfolio_returns-risk_free_returns).std()
			summary.loc[key, 'Sharpe Ratio'] = (summary.loc[key, 'Excess Returns %'] / summary.loc[key, 'Risks'])
			# Add a new column to indicate whether each data point is from a ticker or an index
			if key in self.index_symbols:
				summary.loc[key, 'Type'] = 'Index'
			elif key == self.riskfreeticker:
				summary.loc[key, 'Type'] = 'RiskFree'
			else:
				summary.loc[key, 'Type'] = 'Portfolio'
		print("Benchmark of various portfolios and indexes for Annualized fromDate Excess Returns (with Dividends) in " + str(self.refcurrency) + " since " + str(self.start_date) + " using " + str(self.riskfreeticker) + " for risk-free returns")
		print(summary)
		self.portfolio_risksadjusted_fromdate_totalreturns = summary	

		if showgraphs: 
			fig = px.scatter(summary,
							x = 'Risks', 
	                        y = 'Excess Returns %', 
	                        color='Type',
	                        title = 'Risks/Excess Returns analysis between Portfolios for Annualized fromDate total return since ' + str(self.start_date),
	                        text = summary.index,
	                        template = template
	                        )

			fig.update_traces(hovertemplate='Risk: %{x}<br>Excesss Return %: %{y}<br>')
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
	            			yaxis = dict(title = dict(font = dict(size = 20))))
			fig = self.brand_port_graphic(fig)
			fig.show()

	#function to run show the risk / return plot vs different portfolio
	def portfolio_risks_fromdate_totalreturns_plot(self, showgraphs = True, 	template = 'plotly_dark'):
		portfolio_returns = pd.DataFrame()
		summary = pd.DataFrame()
		#for each_portfolio we want to get the returns 
		for key, myPortfolio in self.portfolios_dict.items():
			#let's calculate the fromdate total returns for the porfolio
			myPortfolio.portfolio_fromdate_total_returns()
			portfolio_returns = myPortfolio.annualized_weighted_fromdate_returns_df
			#we skip the last 3 periodes to remove high volatility due to short period
			summary.loc[key, '% Returns'] = portfolio_returns.iloc[:-3].mean()
			summary.loc[key, 'Risks'] = portfolio_returns.std()
			# Add a new column to indicate whether each data point is from a ticker or an index
			if key in self.index_symbols:
				summary.loc[key, 'Type'] = 'Index'
			elif key == self.riskfreeticker:
				summary.loc[key, 'Type'] = 'RiskFree'
			else:
				summary.loc[key, 'Type'] = 'Portfolio'
		print("Benchmark of various portfolios and indexes for Annualized fromDate Total Returns (with Dividends) in " + str(self.refcurrency) + " since " + str(self.start_date))
		print(summary)
		self.portfolio_risks_fromdate_totalreturns = summary	
		fig = px.scatter(summary,
						x = 'Risks', 
                        y = '% Returns', 
                        color='Type',
                        title = 'Risks/Returns analysis between Portfolios for Annualized fromDate total return since ' + str(self.start_date),
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
            			yaxis = dict(title = dict(font = dict(size = 20))))
		fig = self.brand_port_graphic(fig)
		fig.show()

	#function to run show the risk / dividends plot vs different portfolio
	def portfolio_risks_fromdate_dividends_plot(self, showgraphs = True, 	template = 'plotly_dark'):
		portfolio_dividends = pd.DataFrame()
		summary = pd.DataFrame()
		#for each_portfolio we want to get the dividends 
		for key, myPortfolio in self.portfolios_dict.items():
			#let's calculate the fromdate dividends for the porfolio
			myPortfolio.portfolio_fromdate_total_dividends()
			portfolio_dividends = myPortfolio.annualized_weighted_fromdate_dividends_df
			#we skip the last 3 periodes to remove high volatility due to short period
			summary.loc[key, '% Returns'] = portfolio_dividends.iloc[:-3].mean()
			summary.loc[key, 'Risks'] = portfolio_dividends.std()
			# Add a new column to indicate whether each data point is from a ticker or an index
			if key in self.index_symbols:
				summary.loc[key, 'Type'] = 'Index'
			elif key == self.riskfreeticker:
				summary.loc[key, 'Type'] = 'RiskFree'
			else:
				summary.loc[key, 'Type'] = 'Portfolio'
		print("Benchmark of various portfolios and indexes for Annualized fromDate Dividends in " + str(self.refcurrency) + " since " + str(self.start_date))
		print(summary)
		self.portfolio_risks_fromdate_dividends = summary	
		fig = px.scatter(summary,
						x = 'Risks', 
                        y = '% Dividends', 
                        color='Type',
                        title = 'Risks/Returns analysis between Portfolios for Annualized fromDate Dividends since ' + str(self.start_date),
                        text = summary.index,
                        template = template
                        )
		fig.update_traces(hovertemplate='Risk: %{x}<br>Dividends: %{y}')
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
            			yaxis = dict(title = dict(font = dict(size = 20))))
		fig = self.brand_port_graphic(fig)
		fig.show()

	#function to run show the risk / return plot vs different portfolio
	def portfolio_risks_todate_totalreturns_plot(self, showgraphs = True, 	template = 'plotly_dark'):
		portfolio_returns = pd.DataFrame()
		summary = pd.DataFrame()
		#for each_portfolio we want to get the returns 
		for key, myPortfolio in self.portfolios_dict.items():
			#let's calculate the fromdate total returns for the porfolio
			myPortfolio.portfolio_todate_total_returns()
			portfolio_returns = myPortfolio.annualized_weighted_todate_returns_df
			#we skip the last 3 periodes to remove high volatility due to short period
			summary.loc[key, '% Returns'] = portfolio_returns.mean()
			summary.loc[key, 'Risks'] = portfolio_returns.std()
			# Add a new column to indicate whether each data point is from a ticker or an index
			if key in self.index_symbols:
				summary.loc[key, 'Type'] = 'Index'
			elif key == self.riskfreeticker:
				summary.loc[key, 'Type'] = 'RiskFree'
			else:
				summary.loc[key, 'Type'] = 'Portfolio'
		print("Benchmark of various portfolios and indexes for Annualized toDate Total Returns (with Dividends) in " + str(self.refcurrency) + " since " + str(self.start_date))
		print(summary)	
		fig = px.scatter(summary,
						x = 'Risks', 
                        y = '% Returns', 
                        color='Type',
                        title = 'Risks/Returns analysis between Portfolios for Annualized toDate total return since ' + str(self.start_date),
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
            			yaxis = dict(title = dict(font = dict(size = 20))))
		fig = self.brand_port_graphic(fig)
		fig.show()

	def brand_port_graphic(self, fig):
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

	    