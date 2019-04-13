# -*- coding:utf-8 -*-
import tushare
import pandas 
import datetime
import os
import time

def StockPriceInraday(ticker,folder):
	#Step 1: Get the data online
	indraday = tushare.get_hist_data(ticker,ktype = '5')

	#Step 2: If the file exists,append
	file = folder+"/"+ticker+".csv"
	if os.path.exists(file):
		history = pandas.read_csv(file,index_col = 0)
		indraday.append(history)
	#Step 3: Inverse based on index
	indraday.sort_index(inplace = True)
	indraday.index.name = "timestamp"
	#Step 4: Save.
	indraday.to_csv(file)
	print("indraday for ["+ticker+"] got.")

#Step 5:Get the tickers online
tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()

#Step 6: save the ticket list
data_today = datetime.datetime.today().strftime("%Y%m%d")
File = "../data/ticket-list-CN/Ticket-list_" + data_today + ".csv"
tickersRawData.to_csv((File),encoding='utf_8_sig')
print("tickers saved.")

#Step 7:Get the stock price (indraday) for all
for i,ticker in enumerate(tickers):
	try:
		print("Indraday",i,len(tickers))
		StockPriceInraday(ticker,folder = "../data/Indraday-CN")
	except:
		pass
print("Indraday for all stock got")

