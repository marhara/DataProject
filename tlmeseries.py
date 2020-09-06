import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')


def plot_plt(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(20, 10), dpi=dpi)
    plt.plot(x, y, 'g^')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    
    plt.show()



plot_plt(df, x=df.index, y=df.value, title="My Tille")
