import time
import Adafruit_ADS1x15
import threading
import numpy
from . import generateGraph as graph

filename = "20180403_actual_voltage.txt"

class device():
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1
        self.adc.start_adc(0, gain=self.GAIN)
        self.thread = threading.Thread(target=self._get_data)
        self.thread.daemon = True
        self.thread.start()

    def getVoltage(self):
        y = numpy.loadtxt(fname="data/" + filename, dtype=float, usecols=0)
        graph.makeGraph(range(0, len(y)), y)
        return self._voltage
    def _get_data(self):
        while True:
            self._voltage = self.adc.get_last_result()/10.0
            self.f = open("data/" + filename, "a+")
            self.f.write('%s\n' % str(self._voltage))
            self.f.close()
            time.sleep(1)
