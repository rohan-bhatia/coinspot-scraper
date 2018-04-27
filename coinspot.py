'''
Created on 27 Apr. 2018

@author: RohanBhatia
'''

import requests
from bs4 import BeautifulSoup
import time


def getCoinSpotWebsiteURLS():
    websiteURLList = []
    websiteURLList.append('https://www.coinspot.com.au/sell/ADA')
    websiteURLList.append('https://www.coinspot.com.au/sell/BTC')
    websiteURLList.append('https://www.coinspot.com.au/sell/CAN')
    websiteURLList.append('https://www.coinspot.com.au/sell/DENT')
    websiteURLList.append('https://www.coinspot.com.au/sell/DOGE')
    websiteURLList.append('https://www.coinspot.com.au/sell/ETH')
    websiteURLList.append('https://www.coinspot.com.au/sell/FUN')
    websiteURLList.append('https://www.coinspot.com.au/sell/RDD')
    websiteURLList.append('https://www.coinspot.com.au/sell/STR')
    websiteURLList.append('https://www.coinspot.com.au/sell/TRX')
    websiteURLList.append('https://www.coinspot.com.au/sell/XRP')
    websiteURLList.append('https://www.coinspot.com.au/sell/XVG')
    return websiteURLList

priceListForFinalPrint = []

print("---------------------")
print("Format: Name = Price")
print("---------------------")
for websiteURL in getCoinSpotWebsiteURLS():
    req = requests.get(websiteURL)
    soup = BeautifulSoup(req.content, "lxml")
    
    priceStringFull = soup.select('h1.price-title')[0].text.strip()
    priceString = priceStringFull.split("$")
    print(priceString[0] + priceString[1])
    
    priceListForFinalPrint.append(priceString[1])
