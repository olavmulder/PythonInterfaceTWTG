from utils import *
from numpy import uint8

class Protocol():
    #needed?
    __value: uint8 = []

    __dataList = []

    def __init__(self):
        self.__dataList = [0 for i in range(self.GetAmountElements())]
        #self.__value = [0 for i in range(6)]

    def SetDataList(self,val, i):
        self.__dataList[i] = val

    def GetDataListItem(self, i):
        return self.__dataList[i]

    def GetDataListAll(self):
        return self.__dataList

    #needed??
    def GetValue(self):
        return self.__value
    #needed??

    def SetValue(self, val):
        self.__value = val

    def ValueString(self):
        strVal =""
        for i  in range(len(self.__dataList)):
            strVal += self.GetStringListElement(i) + str(self.__dataList[i])
            if(i < len(self.__dataList)-1):
                strVal+=", "
        return strVal
    
    
class USART(Protocol):
    __amountElements = 14
    __stringList = ["speed: ", "clock output: ","clock last bit: ", "clock phase: ", "clock polarity: ", \
                     "oversampling: ", "endianness: ", "sync: ", "enabled: ", \
                    "transfer direction: ", "hardware_control: ", "stop bit: ", "parity bit: ","data lenght: "]

    def __init__(self):
        super().__init__()
    def GetAmountElements(self):
        return self.__amountElements

    def GetStringListElement(self, i):
        return self.__stringList[i]
    def GetStringList(self):
        return self.__stringList
    

class I2C(Protocol):
    __stringList = ["speed: ", "address: ", "address 2: ", "dutycycle: ", "role: ", "addressing: ", "dual: ", "generalcall: ", \
                    "no_stretch: ", "enabeld: "]
    __amountElements = 10

    def __init__(self):
        super().__init__()
    
    def GetAmountElements(self):
        return self.__amountElements

    def GetStringListElement(self, i):
        return self.__stringList[i]

    def GetStringList(self):
        return self.__stringList


class SPI(Protocol):
    __amountElements = 10
    __stringList = ["role: ", "direction: ", "dataLength: ", "clock polarity: ", "clock phase: ", "nss: ", "baud prescaler: ", \
                    "endianness: ", "ti_mode: ", "enabled: "]
    
    def __init__(self):
        super().__init__()
    
    def GetAmountElements(self):
        return self.__amountElements

    def GetStringListElement(self, i):
        return self.__stringList[i]

    def GetStringList(self):
        return self.__stringList