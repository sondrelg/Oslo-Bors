import datetime as dt
import pandas_datareader as web
import matplotlib as style
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
plt.style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2017,2,1)
security = 'OSEBX.OL'
#security2 = 'STRONG.OL'

df = web.DataReader(security, 'yahoo', start, end)
#df1 = web.DataReader(security2, 'yahoo', start, end)

df['50ma'] = df['Close'].rolling(window=50, min_periods = 0).mean()
df['100ma'] = df['Close'].rolling(window=100, min_periods = 0).mean()
df['200ma'] = df['Close'].rolling(window=200, min_periods = 0).mean()

#Make sure to drop 50 obs for NA. Min periods means we don't have NA obs from MA.
df.dropna(inplace=True)

plt.plot(df['Adj Close'])
plt.plot(df['50ma'])
plt.plot(df['100ma'])
plt.plot(df['200ma'])