from ctypes import *
from . import adc, dac

class Platform:
    def __init__ (self):
        self.vADC = adc.device();
        self.vDAC = dac.device();
        self.oVoltage = "2000 V"
        self.dt5770 = CDLL('caen_module/dt5770.so')
        self.dt5770.get_info.restype = c_char_p
        #self.dt5770.print_info()
        self.c_s = c_char_p(self.dt5770.get_info()).value.decode('utf-8')
    def start(self):
        return True
    def connection_info(self):
        return {'manufacture': 'CAEN', 'model': 'DT770'}
    def get_sn(self):
        return self.c_s
    def get_oVoltage(self):
        return self.oVoltage
    def get_tVoltage(self):
        return self.vDAC.getVoltage()
    def get_aVoltage(self):
        return self.vADC.getVoltage()
    def set_tVoltage(self, newVoltage):
        self.vDAC.setVoltage(newVoltage)
