import numpy as np
import matplotlib.pyplot as mplot

def graph_sin():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    mplot.plot(x, y)
    mplot.title("Graph of Sin Function")
    mplot.xlabel("X-axis")
    mplot.ylabel("Y-axis")
    mplot.show()

graph_sin()

def tan_graph():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.tan(x)
    mplot.plot(x, y)
    mplot.title("Graph of Tan Function")
    mplot.xlabel("X-axis")
    mplot.ylabel("Y-axis")
    mplot.show()

tan_graph()

def cos_graph():
    x = np.linspace(0, np.pi * 2, 100)
    y = np.cos(x)
    mplot.plot(x, y)
    mplot.title("Graph of Cos Function")
    mplot.xlabel("X-axis")
    mplot.ylabel("Y-axis")
    mplot.show()

cos_graph()





