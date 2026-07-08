import yfinance as yf 
import numpy as np
stc="NVDA"
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
r=0.055
max_price=1.03*np.exp((30*mean))*close_prices[-1]
print(max_price,'max_price')
total_exercise_time=1/12
time_step=1000
price_step=1000
time_dif=(total_exercise_time/(time_step))
price_dif=(max_price)/price_step
v_i=0
vi1=0
vi2=0
K=yf.Ticker(stc).option_chain(yf.Ticker(stc).options[0]).calls['strike'][0]
print(K,'K')
for i in range(0,time_step):
	for j in range(0,price_step):
		v_i=vi1
		vi1=max((i+1)*price_dif-K,0)
		vi2=max((i+2)*price_dif-K,0)
		a=0.5*r*j*time_dif-0.5*(volatility**2)*(j**2)*time_dif
		b=1+(volatility**2)*(j**2)*time_dif+r*time_dif
		c=-0.5*r*j*time_dif-0.5*(volatility**2)*(j**2)*time_dif
		vt2=a*v_i+b*vi1+c*vi2

print(vt2,"option price")