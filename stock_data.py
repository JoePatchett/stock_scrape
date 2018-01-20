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
		for i in range(5):
			databox.append(parsed_text.findAll('div',{'class':'value__b93f12ea'})[i].string)
		stock_data_writer.writerow()
	stock_data_file.close()
	
def calculate_daily_differences(csv_file_day1, csv_file_day2):
	"""
	This function takes the stock data from one day, subtracts each value and appends the day 1, day 2, and delta value
	into a list. The structure is organized as follows: [[Company 1, [day 1 value, day 2 value, delta], [], []...], [Company 2,...]]
	"""
	day1_values = []
	day2_values = []
	final_delta_values = []
	with open(csv_file_day1, newline = '') as day1:
	day_1_reader = csv.reader(day1, delimiter = ',')
	for row in day_1_reader:
		day1_values.append(row[:4])
	with open(csv_file_day2, newline = '') as day2:
	day_2_reader = csv.reader(day2, delimiter = ',')
	for row in day_2_reader:
		day2_values.append(row[:4])
	delta_values = []
	for i range(len(day_1_values)):
		temp_list = []
		for j in day_1_values[i]:
			temp_delta = day_2_values[i][j]-day_1_values[i][j]
			temp_list.append([day_1_values[i][j], day_2_values[i][j], temp_delta)
		final_delta_values.append(temp_list)
def kNN_comparison(test_point, rest_of_data):
	"""
	This machine learning algorithm takes in whatever stock data cal
	"""
					  
					  
			
	

