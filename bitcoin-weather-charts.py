#Major 🔑: Importing and using Python libraries
!pip install plotly
import requests
import plotly.express
import plotly.graph_objects as go

#Major 🔑: Importing API data
#Bitcoin Weather Free "https://metapennies.com/api/bitcoin-weather-free/YOUR-API-KEY"
getYourApiData = requests.get("https://metapennies.com/api/bitcoin-weather/YOUR-API-KEY")
YourApiData = getYourApiData.json()

#Major 🔑: Slicing data
#Most recent date API data
YourApiDataToday = YourApiData[-1]
temperature = YourApiDataToday['temperature']

#Major 🔑: Slicing data
#Most recent 500 days
NumberofDays = len(YourApiData)
YourApiData = YourApiData[NumberofDays - 500:NumberofDays]

#Major 🔑: Declaring variables (empty boxes)
date = []
price_close = []
weather_color = []
weekly_macd_line = []
weekly_histogram = []
weekly_signal_line = []
daily_macd_line = []
daily_histogram = []
daily_signal_line = []

#Major 🔑: Setting variables with basic loop (fill the empty boxes)
#Learn more (https://www.learnpython.org/en/loops)
for i in YourApiData:
    idate = i['date']
    date.append(idate)
    iprice_close = i['price_close']
    price_close.append(iprice_close)
    iweather_color=  i['weather_color']
    weather_color.append(iweather_color)
    iweekly_macd_line =  i['weekly_macd_line']
    weekly_macd_line.append(iweekly_macd_line)
    iweekly_histogram = i['weekly_histogram']
    weekly_histogram.append(iweekly_histogram)
    iweekly_signal_line = i['weekly_signal_line']
    weekly_signal_line.append(iweekly_signal_line)
    idaily_macd_line=  i['daily_macd_line']
    daily_macd_line.append(idaily_macd_line)
    idaily_histogram = i['daily_histogram']
    daily_histogram.append(idaily_histogram)
    idaily_signal_line = i['daily_signal_line']
    daily_signal_line.append(idaily_signal_line)

#Major 🔑: Create charts using Plotly
#Chart Bitcoin Weather 🌧️☀️
chartWeather = plotly.express.bar(x=date, y=price_close)
chartWeather.update_layout(plot_bgcolor='white')
chartWeather.update_traces(marker_color=weather_color)

#Chart weekly MACD indicators
chartWeekly = plotly.express.line(x=date, y=weekly_macd_line)
chartWeekly.update_traces(line_color="black")
chartWeekly.add_trace(go.Scatter(x=date, y=weekly_signal_line, fill='tozeroy', line=dict(color="red"), name="signal" ))
chartWeekly.add_trace(go.Bar(x=date, y=weekly_histogram, marker_color="blue", name="histogram"))
chartWeekly.update_layout(plot_bgcolor='white')

#Chart daily MACD indicators
chartDaily = plotly.express.line(x=date, y=daily_macd_line)
chartDaily.update_traces(line_color="black")
chartDaily.add_trace(go.Scatter(x=date, y=daily_signal_line, fill='tozeroy', line=dict(color="red"), name="signal"))
chartDaily.add_trace(go.Bar(x=date, y=daily_histogram, marker_color="blue", name="histogram"))
chartDaily.update_layout(plot_bgcolor='white')

#Major 🔑: Render text, variables and charts 
print('Bitcoin Weather')
print(temperature)
print('Weather Charts')
chartWeather.show()
chartWeekly.show()
chartDaily.show()
