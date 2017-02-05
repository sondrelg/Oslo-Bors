import datetime as dt
import pandas_datareader as web
import matplotlib as style
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
plt.style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2017,2,1)
security = 'PRS.OL'

df = web.DataReader(security, 'yahoo', start, end)
df.to_csv(security+'.csv')
df = pd.read_csv(security+'.csv', parse_dates = True, index_col = 'Date')

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan=1, sharex = ax1)
df_ohlc = df['Adj Close'].resample('7D').ohlc()
df_volume = df['Volume'].resample('7D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
candlestick_ohlc(ax1, df_ohlc.values, width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

