import numpy as np
import talib
import datetime
import requesters.xg.XigniteGlobalHistorical as xgh



stdate = datetime.datetime.strptime("2020-09-01", "%Y-%m-%d")
eddate = datetime.datetime.strptime("2021-03-15", "%Y-%m-%d")
resp = xgh.getGlobalHistoricalQuotesRange(id="SPY", idtype="Symbol", startdate=stdate, enddate=eddate)

prices = resp['HistoricalQuotes']

highs = np.array([i['High'] for i in prices])
lows = np.array([i['Low'] for i in prices])
closes = np.array([i['Close'] for i in prices])
print(highs)
print(lows)
print(closes)

print(talib.DX(high=highs, low=lows, close=closes, timeperiod=len(closes)))
print(talib.HT_DCPERIOD(closes))



