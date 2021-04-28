from binance.client import Client
from dotenv import load_dotenv
import csv
import talib
from numpy import genfromtxt

load_dotenv()

client = Client('API_KEY', 'SECRET_KEY')
exchange_info = client.get_exchange_info()



# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Dec, 2017")

# csvfile = open('allday_present.csv', 'w', newline='')
# kline_candlestick = csv.writer(csvfile, delimiter=',')

# for i in klines:
#     i[0] = i[0] / 1000
#     kline_candlestick.writerow(i)

my_data = genfromtxt('2020-2021.csv', delimiter=',')

close = my_data[:,4]

real = talib.RSI(close, timeperiod=14)

print(real) 