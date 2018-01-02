"""
Created on Thu Dec 28 15:43:38 2017

@author: Joseph
"""
from bs4 import BeautifulSoup
import requests
import csv
def stock_get(nyse_codes, csv_file)
	stock_data_file = open(csv_file,'a', newline='')
	stock_data_writer = csv.writer(stock_data_file)
	for code in nyse_codes:    
		page = 'https://www.bloomberg.com/quote/' + code + ':US'

		#query1 = urllib3.urlopen(page)
		query1 = requests.get(page)
		url_data = query1.text
		parsed_text = BeautifulSoup(url_data, 'html.parser')
		location_of_final_close = parsed_text.find('span', attrs={'class':'priceText__1853e8a5'})
		final_close = location_of_final_close.text.split()
		databox = []
		databox.append(code)
		databox.append(final_close)
		for i in range(6):
			databox.append(parsed_text.findAll('div',{'class':'value__b93f12ea'})[i].string)
		stock_data_writer.writerow()
	stock_data_file.close()

