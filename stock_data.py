"""
Created on Thu Dec 28 15:43:38 2017

@author: Joseph
"""
from bs4 import BeautifulSoup
import requests
import csv
def stock_get(nyse_codes, csv_file):
	"""
	This function takes New York stock exchange tickers (i.e. 'AAPL' for Apple) and the csv file location where to store this data.
	The result is a csv file with company code, price, previous open, market volume, and market value. All of this data is from bloomberg.com
	At the moment it pauses for 3 seconds after each request so that you don't get flagged. Change as necessary. Perhaps will move to Scrapy.
	"""
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
	return 0

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
	return final_delta_values

def kNN_comparison(test_point, rest_of_data, k):
	"""
	This function takes a test date open value which you want to predict if the stock will increase or not. The 'test_point' is
	the percent change in stock on a previous day. The aptly named 'rest_of_data' will include the percent change on a previous day,
	and then a '0' or '1' if that stock decreased or increased on a given date. This given date should not be the same date as the 'test_point',
	the goal is to see if changes in stocks on previous days can have lasting effects on stocks in the future.

	"""
	[training_set, test_set] = prep_data(rest_of_data)
	euclidean_distance(test_point, training_set)
	return 0
def prep_data(csv_file, split_value, ):
	"""
	This function places the data into two lists, training set and test set.
	"""
	return 0
def euclidean_distance(test_point, data_set):				 
	distances = []
	for i in range(len(data_set)):
		distances.append((test_point[i] - data_set[i])^(1/2))
	return distances
	
					  
				
					  
					  
			
	

