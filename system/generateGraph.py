import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def makeGraph(x, y):
    plt.plot(x, y)
    plt.ylabel('Voltage')
    plt.xlabel('Time (s since start)')
    plt.savefig('assets/plot.png')
