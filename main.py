# Show slider time series
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
#
# # Load your excel file
# df = pd.read_excel('sampleData1.xlsx')
#
# # Convert timestamps to datetime objects
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#
# # Plot initial graph (sensor 1)
# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.25)
# l, = plt.plot(df['Timestamp'], df['Sensor 1'], lw=2)
#
# # Create slider
# axcolor = 'lightgoldenrodyellow'
# axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
# spos = Slider(axpos, 'Sensor', 1, 26, valinit=1, valstep=1)
#
# def update(val):
#     sensor = 'Sensor ' + str(int(spos.val))
#     y = df[sensor]
#     l.set_ydata(y)
#     fig.canvas.draw_idle()
#
# spos.on_changed(update)
#
# plt.show()

###################################################
# Show All sensors in 1 graph
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load your excel file
# df = pd.read_excel('sampleData1.xlsx')
#
# # Convert timestamps to datetime objects
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # Ensure column names are strings and have no leading/trailing spaces
# df.columns = df.columns.astype(str)
# df.columns = df.columns.str.strip()
#
# # Plot sensor readings over time
# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# for i in range(1, 27):
#     plt.plot(df['Timestamp'], df['Sensor ' + str(i)], label='Sensor ' + str(i))
#
# plt.title('Sensor Readings Over Time')
# plt.xlabel('Timestamp')
# plt.ylabel('Sensor Reading')
# plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))  # Adjust the legend position and size as needed
# plt.show()

#######################################################
#Show moving average
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
# # Load your excel file
# df = pd.read_excel('sampleData1.xlsx')
# # Convert timestamps to datetime objects
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # Calculate the moving average for each sensor
# window_size = 10  # Adjust as needed
# for i in range(1, 27):
#     df['Sensor ' + str(i) + '_MA'] = df['Sensor ' + str(i)].rolling(window=window_size).mean()
# # Plot initial graph (sensor 1 and its moving average)
# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.25)
# l, = plt.plot(df['Timestamp'], df['Sensor 1'], label='Original')
# l_ma, = plt.plot(df['Timestamp'], df['Sensor 1_MA'], label='Moving Average')
# # Create slider
# axcolor = 'lightgoldenrodyellow'
# axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
# spos = Slider(axpos, 'Sensor', 1, 26, valinit=1, valstep=1)
# def update(val):
#     sensor = 'Sensor ' + str(int(spos.val))
#     y = df[sensor]
#     y_ma = df[sensor + '_MA']
#     l.set_ydata(y)
#     l_ma.set_ydata(y_ma)
#     fig.canvas.draw_idle()
# spos.on_changed(update)
# plt.legend()
# plt.show()

############################################################
# Save all of the line graphs
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
#
# # Load your excel file
# df = pd.read_excel('sampleData1.xlsx')
#
# # Convert timestamps to datetime objects
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#
# # Calculate the moving average for each sensor
# window_size = 10  # Adjust as needed
# for i in range(1, 27):
#     df['Sensor ' + str(i) + '_MA'] = df['Sensor ' + str(i)].rolling(window=window_size).mean()
#
# # Plot and save graph for each sensor
# for i in range(1, 27):
#     fig, ax = plt.subplots()
#     plt.plot(df['Timestamp'], df['Sensor ' + str(i)], label='Original')
#     plt.plot(df['Timestamp'], df['Sensor ' + str(i) + '_MA'], label='Moving Average')
#     plt.title('Sensor ' + str(i))
#     plt.xlabel('Timestamp')
#     plt.ylabel('Sensor Reading')
#     plt.legend()
#     plt.savefig('Sensor_' + str(i) + '.png')  # Save the figure as PNG
#     plt.close(fig)  # Close the figure

############################################################
# # Decompose the time series graph
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
# from statsmodels.tsa.seasonal import seasonal_decompose
#
# # Load your excel file
# df = pd.read_excel('sampleData1.xlsx')
#
# # Convert timestamps to datetime objects and set it as index
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# df = df.set_index('Timestamp')
#
# # Infer the frequency of the data
# freq = pd.infer_freq(df.index)
#
# # Calculate the moving average for each sensor
# window_size = 10  # Adjust as needed
# for i in range(1, 27):
#     df['Sensor ' + str(i) + '_MA'] = df['Sensor ' + str(i)].rolling(window=window_size).mean()
#
# # Decompose the time series of Sensor 1
# result = seasonal_decompose(df['Sensor 1'], model='additive')
#
# # Plot initial graph (sensor 1 and its moving average)
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
# plt.subplots_adjust(bottom=0.25)
# result.observed.plot(ax=ax1, legend=False)
# result.trend.plot(ax=ax2, legend=False)
# result.seasonal.plot(ax=ax3, legend=False)
# result.resid.plot(ax=ax4, legend=False)
#
# ax1.set_ylabel('Observed')
# ax2.set_ylabel('Trend')
# ax3.set_ylabel('Seasonal')
# ax4.set_ylabel('Residual')
#
# # Create slider
# axcolor = 'lightgoldenrodyellow'
# axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
# spos = Slider(axpos, 'Sensor', 1, 26, valinit=1, valstep=1)
#
# def update(val):
#     sensor = 'Sensor ' + str(int(spos.val))
#     result = seasonal_decompose(df[sensor], model='additive')
#     ax1.clear()
#     ax2.clear()
#     ax3.clear()
#     ax4.clear()
#     result.observed.plot(ax=ax1, legend=False)
#     result.trend.plot(ax=ax2, legend=False)
#     result.seasonal.plot(ax=ax3, legend=False)
#     result.resid.plot(ax=ax4, legend=False)
#     fig.canvas.draw_idle()
#
# spos.on_changed(update)
#
# plt.show()
