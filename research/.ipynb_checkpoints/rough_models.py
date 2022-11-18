
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pandas_datareader as pdr
from statsmodels.tsa.api import acf, graphics, pacf
from statsmodels.tsa.ar_model import AutoReg, ar_select_order

df1 = pd.read_csv('master-cci.csv')
df2 = pd.read_csv('master-econ.csv')

sns.set_style("darkgrid")
pd.plotting.register_matplotlib_converters()

sns.mpl.rc("figure", figsize=(26,16))
sns.mpl.rc("font", size=15)

fig, ax = plt.subplots()
ax = df1.plot(ax=ax)

