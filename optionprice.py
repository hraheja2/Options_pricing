import yfinance as yf 
import numpy as np
stc="AAPL"
data =yf.download(stc,start="2026-01-01", end ="2027-07-01")
print(data)
print(data['Close'].to_numpy(),"values")
close_prices=(np.zeros(len(data['Close'].to_numpy())))
open_prices=(np.zeros(len(data[['Close']].to_numpy())))
print(close_prices.shape,"shape")
close_prices[:]=data['Close'].to_numpy()[:,0]
open_prices[:]=data['Open'].to_numpy()[:,0]
returns=np.zeros(len(close_prices))
for i in range(len(returns)):
	returns[i]=np.log(close_prices[i]/open_prices[i])
print(returns,"returns")
print(close_prices)
mean=0
for i in range(len(data['Close'].to_numpy())):
	mean+=returns[i]
mean=mean/len(data['Close'].to_numpy())
print(mean,'mean')
variance=0
for i in range(len(data['Close'].to_numpy())):
	variance+= (returns[i]-mean)**2
variance=variance/((len(data['Close'].to_numpy()))-1)
print(variance,'variance')
volatility=np.sqrt(variance*252)
print(volatility,'volatliity')
r=0.045
max_price=2*close_prices[-1]
print(max_price,'max_price')
total_exercise_time=1
time_step=1000
price_step=1000
time_dif=total_exercise_time/time_step-1
price_dif=(max_price-close_prices[-1])/price_step
a=1/time_dif
b=1/(2*price_dif)
c=1/(price_dif**2)
v_i=0
vi1=0
vi2=0
K=yf.Ticker(stc).option_chain(yf.Ticker(stc).options[0]).calls['strike'][1]
print(K,'K')
for i in range(0,time_step):
	v_i=vi1
	vi1=max((i+1)*price_dif-K,0)
	for j in range(i,i+1):
		vi2=vi1*(a+(r*(j*price_dif)*b)+((volatility**2)*((j*price_dif)**2)*c))/((a+(r*(j*price_dif)*b)+(0.5*(volatility**2)*((j*price_dif)**2)*c))-r)+v_i*(0.5*(volatility**2)*((j*price_dif)**2)*c)/(a+(r*(j*price_dif)*b)+(0.5*(volatility**2)*((j*price_dif)**2)*c)-r)

print(vi2,"option price")
