# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
#
# style.use('fivethirtyeight')
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#     graph_data = open('example.txt', 'r').read()
#     lines = graph_data.split('\n')
#     xs = []
#     xy = []
#
#     for line in lines:
#         if len(line) > 1:
#             x, y = line.split(',')
#             xs.append(x)
#             xy.append(y)
#     ax1.clear()
#     ax1.plot(xs, ys)
#
# ani = animation.FuncAnimation(fig, animate, interval=1000)

import pandas as pd
import re

infoList = pd.read_json('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=T07TXHIJILP0NJUT')

xAxis = []
yAxis = []

# print(infoList["Time Series (15min)"])

for x, y in infoList["Time Series (15min)"].items():
    # cleaning out bad data
    if not re.search('[a-zA-Z]',x):
        # separate day and time
        # append time data of ticker to xAxis
        tickTime = x.split(" ")
        xAxis.append(tickTime[1])

        for aX, xY in y.items():
            # grab data from close price of ticker
            # append data to yAxis list
            if "close" in aX:
                yAxis.append(xY)

print(xAxis)
print(yAxis)
