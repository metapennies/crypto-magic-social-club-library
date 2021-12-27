#Major 🔑: Importing and using Python libraries
!pip install plotly
import requests
import plotly.express

#Major 🔑: Importing API data
#Bitcoin Weather Free "https://metapennies.com/api/bitcoin-weather-free/YOUR-API-KEY"
getYourApiData = requests.get("https://metapennies.com/api/bitcoin-weather/YOUR-API-KEY")
YourApiData = getYourApiData.json()

#Major 🔑: Slicing JSON data
#Last date API data (most current date)
YourApiDataCurrent = YourApiData[-1]

#Major 🔑: Simple If Statements & MACD technical analysis points system
#Weekly Points Logic: If MACD Line > 0 then 30 Points | If MACD Line <= 0 then 0 Points
if YourApiDataCurrent['weekly_macd_line_zero'] == '> zero':
    weekly_macd_line_zero_points = 30
else: weekly_macd_line_zero_points = 0

if YourApiDataCurrent['weekly_histogram_zero']  == '> zero':
    weekly_histogram_zero_points = 30
else: weekly_histogram_zero_points = 0
   
if YourApiDataCurrent['weekly_macd_line_slope'] == 'slope +':
    weekly_macd_line_slope_points = 20
else: weekly_macd_line_slope_points = 0

if YourApiDataCurrent['weekly_histogram_slope'] == 'slope +':
    weekly_histogram_slope_points = 20
else: weekly_histogram_slope_points = 0

#Major 🔑: Easy Math (add the weekly points)
weekly_points = weekly_macd_line_zero_points + weekly_histogram_zero_points + weekly_macd_line_slope_points + weekly_histogram_slope_points

#Major 🔑: Simple If Statements (daily)
#Daily Points Logic: If MACD Line > 0 then 30 Points | If MACD Line <= 0 then 0 Points
if YourApiDataCurrent['daily_macd_line_zero']  == '> zero':
    daily_macd_line_zero_points = 30
else: daily_macd_line_zero_points = 0
    
if YourApiDataCurrent['daily_histogram_zero']  == '> zero':
    daily_histogram_zero_points = 30
else: daily_histogram_zero_points = 0

if YourApiDataCurrent['daily_signal_line_slope'] == 'slope +':
    daily_signal_line_slope_points = 20
else: daily_signal_line_slope_points = 0

if YourApiDataCurrent['daily_histogram_slope'] == 'slope +':
    daily_histogram_slope_points = 20
else: daily_histogram_slope_points = 0

#Major 🔑: Easy Math (add the daily points from above)
daily_points = daily_macd_line_zero_points + daily_histogram_zero_points + daily_signal_line_slope_points + daily_histogram_slope_points

#Major 🔑: Easy Math (weighted average of weekly and daily points) 
#Change the Weightings Yourself and Test Results Visually
temperature = (weekly_points * 0.72) + (daily_points * 0.28)

#Major 🔑: Slicing JSON data
#Most Recent 500 Days
NumberofDays = len(YourApiData)
YourApiData = YourApiData[NumberofDays - 500:NumberofDays]

#Major 🔑: Declaring variables (empty boxes)
date = []
price_close = []
weather_color = []

#Major 🔑: Setting variables using a simple loop (fill the empty boxes)
#Learn More (https://www.learnpython.org/en/Loops)
for i in YourApiData:
    idate = i['date']
    date.append(idate)
    iprice_close = i['price_close']
    price_close.append(iprice_close)
    #Major 🔑: Simple If Statement Challenge: Change the colors and run your Bitcoin analysis
    if i['temperature'] > 50:
        iweather_color = "gold"
    else: iweather_color = "lightblue"
    weather_color.append(iweather_color)

#Major 🔑: Setting variables and creating charts using Plotly
xaxis_data = date
yaxis_data = price_close
yaxis_data_min = min(yaxis_data) 
yaxis_data_max = max(yaxis_data)    

yourChart = plotly.express.bar(x=xaxis_data, y=yaxis_data)
yourChart.update_layout(yaxis_range=[yaxis_data_min,yaxis_data_max], plot_bgcolor='white')
yourChart.update_traces(
    marker_color=weather_color
)

#Major 🔑: Render text, variables and charts
print('Bitcoin Weather')
print(temperature)
print('Bitcoin Weather Chart')
yourChart.show()
