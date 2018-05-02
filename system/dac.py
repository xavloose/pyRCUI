import math
import Adafruit_MCP4725
import threading
import time

class device():
    def __init__(self):
        self.dac = Adafruit_MCP4725.MCP4725()
        self._voltage = 2
        self._tVoltage = 2
    def setVoltage(self, voltage):
        self._tVoltage = voltage
        threading.Thread(target=self._voltageRampup).start()
        #self.dac.set_voltage(int(round(int(self._voltage)*1.565)))
    def getVoltage(self):
        return self._tVoltage
    def _voltageRampup(self):
        while (self._voltage != self._tVoltage):
            if self._voltage < int(self._tVoltage):
                self._voltage += 10
                if self._voltage > int(self._tVoltage):
                    self._voltage = int(self._tVoltage)
            else:
                self._voltage -= 10
                if self._voltage < int(self._tVoltage):
                    self._voltage = int(self._tVoltage)
            self.dac.set_voltage(int(round(int(self._voltage - 2)*1.565)))
            time.sleep(1)

