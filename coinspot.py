'''
Created on 27 Apr. 2018

@author: RohanBhatia
'''

import requests
from bs4 import BeautifulSoup
import configparser
import time

print("---------------------")
print("   Coinspot-scraper  ")
print("---------------------")
print("")
print("Processing....")
print("")

my_config_parser = configparser.SafeConfigParser()
my_config_parser.read('config.ini')
typeOfValue = my_config_parser.get('Coinspot', 'TypeOfValue')
cryproList = my_config_parser.get('Coinspot', 'CryproList')
displayValue = my_config_parser.get('Coinspot', 'DisplayValue')

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
    websiteURLList.append('https://www.coinspot.com.au/sell/ANS')
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
    websiteURLList.append('https://www.coinspot.com.au/sell/BTG')
    websiteURLList.append('https://www.coinspot.com.au/sell/LSK')
    websiteURLList.append('https://www.coinspot.com.au/sell/STEEM')
    websiteURLList.append('https://www.coinspot.com.au/sell/ZEC')
    websiteURLList.append('https://www.coinspot.com.au/sell/BCN')
    websiteURLList.append('https://www.coinspot.com.au/sell/SC')
    websiteURLList.append('https://www.coinspot.com.au/sell/XRB')
    websiteURLList.append('https://www.coinspot.com.au/sell/WAN')
    websiteURLList.append('https://www.coinspot.com.au/sell/PPT')
    websiteURLList.append('https://www.coinspot.com.au/sell/AE')
    websiteURLList.append('https://www.coinspot.com.au/sell/XVG')
    websiteURLList.append('https://www.coinspot.com.au/sell/XRB')
    websiteURLList.append('https://www.coinspot.com.au/sell/DOGE')
    websiteURLList.append('https://www.coinspot.com.au/sell/PIVX')
    websiteURLList.append('https://www.coinspot.com.au/sell/CAN')
    return websiteURLList

displayFormatOne = []
displayFormatOne.append("---------------------")
displayFormatOne.append("Format: Name = Price")
displayFormatOne.append("---------------------")

displayFormatTwo = []
displayFormatTwo.append("---------------------")
displayFormatTwo.append("  Format: Price Only ")
displayFormatTwo.append("---------------------")

for websiteURL in getCoinSpotWebsiteURLS():
    req = requests.get(websiteURL)
    soup = BeautifulSoup(req.content, "lxml")
    if(soup.text != "Not Found"):
        priceStringFull = soup.select('h1.price-title')[0].text.strip()
        priceString = priceStringFull.split("$")
        displayFormatOne.append(priceString[0] + priceString[1])
        displayFormatTwo.append(priceString[2])
    else:
        displayFormatOne.append(soup.text.upper() + " - " + websiteURL)
        displayFormatTwo.append(soup.text.upper() + " - " + websiteURL)

#Function to print the values based on config file
def printPrices(displayValue):
    if(displayValue == "1"):
        for displayFormatValue in displayFormatOne:
            print(displayFormatValue)
    elif(displayValue == "2"):
        for displayFormatValue in displayFormatTwo:
            print(displayFormatValue)
    else:
        for displayFormatValue in displayFormatOne:
            print(displayFormatValue)
        for displayFormatValue in displayFormatTwo:
            print(displayFormatValue)

printPrices(displayValue)
print("")    
input("Press enter to exit...")
