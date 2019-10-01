"""
Template for drawing plots with matplotlib
"""

# if this script generates this error:
# _tkinter.TclError: no display name and no $DISPLAY environment variable
# uncomment these 2 lines
#import matplotlib 
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Concepts:
# - pyplot create Figures, figures create Axes.
# - Artist are the actual rendered stuff (rendered on canvas)
# - All plotting functions except `np.array` as input.

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# multiple subplot example.
# I prefer this way: by calling plot function of axis object.
np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

# on a ssh terminal, usually we can't have interactive plots.
# let's save the image to disk.
fig.savefig("test.png")

# another example of using axis.
# one may use Axis.set() to setup Figure title, label, ... etc
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

# Create two subplots sharing y axis
fig, (ax1, ax2) = plt.subplots(2, sharey=True)

ax1.plot(x1, y1, 'ko-')
ax.set(xlabel='', ylabel='Damped oscillation',
       title='A tale of 2 subplots')
ax2.plot(x2, y2, 'r.-')
ax2.set(xlabel='time (s)', ylabel='Undamped')

plt.show()

# Usually people from Matlab would expect a state-machine-like enviornment (MATLAB-style)
# and most commands are invoke by pyplot. Plots are added to current figure/axes, by default
# But we don't have to always go with this. There is also a OO interface for plotting.

# a template for a plot function
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})


# a list of plotting functions
# ax.annotate - text annotations  Annotate 	ax.texts
# ax.bar - bar charts 	          Rectangle 	ax.patches
# ax.errorbar - error bar plots   Line2D and Rectangle 	ax.lines and ax.patches
# ax.fill - shared area 	      Polygon 	ax.patches
# ax.hist - histograms 	          Rectangle 	ax.patches
# ax.imshow - image data 	      AxesImage 	ax.images
# ax.legend - axes legends 	      Legend 	ax.legends
# ax.plot - xy plots 	          Line2D 	ax.lines
# ax.scatter - scatter charts 	  PolygonCollection 	ax.collections
# ax.text - text 	              Text 	ax.texts

# set canvas size

# gcf() gca(): get current figure/axes
# clf() cla(): clear current figure/axes

# MATLAB-style of drawing multiple subplots
# subplot() takes 3 positional arguemnts: nrows, ncols, index
# `index` begins from 1 and increases left to right, top to bottom, as this
#  _______
# |_1_|_2_|
# |_3_|_4_|
# |_5_|_6_|
#

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
