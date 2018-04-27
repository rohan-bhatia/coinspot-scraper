'''
Created on 27 Apr. 2018

@author: RohanBhatia
'''

import requests
from bs4 import BeautifulSoup
import time

#List of URLs to scrap
def getCoinSpotWebsiteURLS():
    websiteURLList = []
	websiteURLList.append('https://www.coinspot.com.au/sell/BTC')
	websiteURLList.append('https://www.coinspot.com.au/sell/ETH')
	websiteURLList.append('https://www.coinspot.com.au/sell/XRP')
	websiteURLList.append('https://www.coinspot.com.au/sell/BCC')
	websiteURLList.append('https://www.coinspot.com.au/sell/EOS')
	websiteURLList.append('https://www.coinspot.com.au/sell/LTC')
	websiteURLList.append('https://www.coinspot.com.au/sell/STR')
	websiteURLList.append('https://www.coinspot.com.au/sell/ADA')
	websiteURLList.append('https://www.coinspot.com.au/sell/MIOTA')
	websiteURLList.append('https://www.coinspot.com.au/sell/NEO')
	websiteURLList.append('https://www.coinspot.com.au/sell/TRX')
	websiteURLList.append('https://www.coinspot.com.au/sell/XMR')
	websiteURLList.append('https://www.coinspot.com.au/sell/DASH')
	websiteURLList.append('https://www.coinspot.com.au/sell/XEM')
	websiteURLList.append('https://www.coinspot.com.au/sell/USDT')
	websiteURLList.append('https://www.coinspot.com.au/sell/ETC')
	websiteURLList.append('https://www.coinspot.com.au/sell/VEN')
	websiteURLList.append('https://www.coinspot.com.au/sell/OMG')
	websiteURLList.append('https://www.coinspot.com.au/sell/QTUM')
	websiteURLList.append('https://www.coinspot.com.au/sell/ICX')
	websiteURLList.append('https://www.coinspot.com.au/sell/XVG')
	websiteURLList.append('https://www.coinspot.com.au/sell/XRB')
	websiteURLList.append('https://www.coinspot.com.au/sell/DOGE')
	websiteURLList.append('https://www.coinspot.com.au/sell/PIVX')
	websiteURLList.append('https://www.coinspot.com.au/sell/CAN')
    return websiteURLList

print("---------------------")
print("Format: Name = Price")
print("---------------------")
for websiteURL in getCoinSpotWebsiteURLS():
    req = requests.get(websiteURL)
    soup = BeautifulSoup(req.content, "lxml")
    
    priceStringFull = soup.select('h1.price-title')[0].text.strip()
    priceString = priceStringFull.split("$")
    print(priceString[0] + priceString[1])

print("")
print("")	
input("Press enter to exit...")
