#Major 🔑: Importing and using Python libraries
!pip install pandas
!pip install requests
!pip install stockstats
import requests
import pandas as pandas
from stockstats import StockDataFrame

#Major 🔑: Importing API data
#Daily "https://metapennies.com/api/bitcoin-technical-indicators-daily/YOUR-API-KEY"
getYourApiData = requests.get("https://metapennies.com/api/bitcoin-technical-indicators-weekly/YOUR-API-KEY")
YourApiData = getYourApiData.json()

#Major 🔑: Declaring variables (empty boxes)
open = []
close = []
high = []
low = []
volume = []
amount = []

#Major 🔑: Setting variables with basic loop (fill the empty boxes)
#Learn more (https://www.learnpython.org/en/loops)
for i in YourApiData:
    iprice_open = i['price_open']
    open.append(iprice_open)
    iprice_close = i['price_close']
    close.append(iprice_close)
    iprice_high = i['price_high']
    high.append(iprice_high)
    iprice_low = i['price_low']
    low.append(iprice_low)
    ivolume = i['volume']
    volume.append(ivolume)
    amount.append(ivolume)

YourDataFrame = pandas.DataFrame({
    "open": open,
    "close": close,
    "high": high,
    "low": low,
    "volume": volume,
    "amount": amount,            
})

#Major 🔑: Calculate technical indicators (RSI, Bollinger Bands, MACD)
#YourIndicator['boll'] = YourIndicator.get('boll')
#YourIndicator['macd'] = YourIndicator.get('macd')
YourIndicator = StockDataFrame.retype(YourDataFrame)
YourIndicator['rsi_14'] = YourIndicator.get('rsi_14')

#Major 🔑: Render DataFrame table 
print(YourIndicator)
