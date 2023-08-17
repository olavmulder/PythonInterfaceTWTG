from serial.tools import list_ports
import serial
from crc import *
from utils import *
import crcmod

class USB:
    port:str = None
    mcu = None
    speedUSB:int = None
    timeout:float = None
    vID:int = None
    pID:int = None

    OK  = [TestStandResult.OK, "OK\n"]
    UNKNOWN  = [TestStandResult.UNKNOWN,"UNKNOWN\n"]
    DUT_NOT_ACCESSIBLE = [TestStandResult.DUT_NOT_ACCESSIBLE,"DUT_NOT_ACCISBLE\n"]
    NOT_ALLOWED = [TestStandResult.NOT_ALLOWED, "NOT_ALLOWED\n"]
    FAILURE = [TestStandResult.FAILURE, "FAILURE\n"]
    DATA = [TestStandResult.DATA, "DATA:"]


    def __init__(self, vID_, pID_, sUSB, tOut=1.0):
        self.pID = pID_
        self.vID = vID_
        self.speedUSB = sUSB
        self.timeout = tOut
        if self.init() != TestStandResult.OK:
            raise Exception('Init USB went wrong, no port found')
        

    def init(self):
        self.port:str = None
        device_list = list_ports.comports()
        for device in device_list:
            if (device.vid != None or device.pid != None):
                if ('{:04X}'.format(device.vid) == '{:04X}'.format(self.vID) and \
                    '{:04X}'.format(device.pid) == '{:04X}'.format(self.pID)):

                    self.port = device.device
                    break
        if(self.port == None):
            return TestStandResult.FAILURE
        return TestStandResult.OK

       
    def __OpenPort(self):
        self.mcu = serial.Serial(self.port, self.speedUSB) #, bytesize=serial.EIGHTBITS, timeout=self.timeout)
    
    def __ClosePort(self):
        self.mcu.close()

    #write data to usb
    def __WriteData(self, value):
        bytes = value
        if not (isinstance(value, bytearray)):
            bytes = bytearray()
            for i in range(len(value)):
                bytes += value[i].to_bytes(1, byteorder='big')
        self.mcu.write(bytes)
        return bytes
   
    #read data from usb, returng string
    def __ReadData(self):    
        self.mcu.flush()
        x = self.mcu.readline()
        x = "".join(map(chr, x))
        return x

    #send data, returns TestStandResult 
    def SendDataToMcu(self, value):
        self.__OpenPort()
        self.__WriteData(value)
        retMsg = self.__ReadData()
        #get first byte to determine which command the return value depends on
        retMsgByteArray = bytearray()
        retMsgByteArray.extend(map(ord, retMsg))
        command:int = (retMsgByteArray[0])
        del retMsgByteArray[0]
        retMsg = retMsgByteArray.decode('utf-8')
      
        ret:TestStandResult = None
        if retMsg == self.OK[1]: 
            ret = TestStandResult.OK
        
        elif retMsg == self.UNKNOWN[1]:
            ret = TestStandResult.UNKNOWN
        
        elif retMsg == self.DUT_NOT_ACCESSIBLE[1]:
            ret = TestStandResult.DUT_NOT_ACCESSIBLE
        
        elif retMsg == self.NOT_ALLOWED[1]:
            ret = TestStandResult.NOT_ALLOWED

        elif retMsg == self.FAILURE[1]:
            while ret != TestStandResult.OK:
                ret = self.__WriteData(value)
                retMsg = self.__ReadData()
                if retMsg == self.OK[1]:
                    ret = TestStandResult.OK

        elif retMsg[:5] == self.DATA[1]:
            data = retMsg[5:]
            print("received data: ", data)
            ret = TestStandResult.OK
        else:
            raise Exception("invalid retmsg")

        self.__ClosePort()
        return ret, command
