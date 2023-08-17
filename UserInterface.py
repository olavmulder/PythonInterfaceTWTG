#!/bin/python3

from crc import *
from USB import USB
from Protocol import *
from utils import *
from numpy import uint32


class UserInterface:
    
    usb_obj = None 
    spi = None
    i2c = None
    usart = None

    def __init__(self, vid, pid, speedUSB = 9600):
        VID = vid
        PID = pid
        self.usb_obj = USB(VID, PID,speedUSB)
        self.spi = SPI()
        self.i2c = I2C()
        self.usart = [USART()]* 4 

    '''def MakeDataProtocolConfig(self, value):

        if(len(value) != 6):
            return -1
        for i in range(0, len(value)):
            if value[i].bit_length() > 8:
                return -1

        arr =[]
        a =  bytearray(((value[0] << 8)+ value[1]).to_bytes(2, 'big'))
        b =  bytearray(((value[2] << 8)+ value[3]).to_bytes(2, 'big'))
        c =  bytearray(((value[4] << 8)+ value[5]).to_bytes(2, 'big'))
        
        arr.append( int.from_bytes(Encode(a), 'big' ))
        arr.append( int.from_bytes(Encode(b), 'big' ))
        arr.append( int.from_bytes(Encode(c), 'big' ))


        arr2 = []
        for i in range (3):
            arr2.append((arr[i] & 0xff000000) >> 24)
            arr2.append((arr[i] & 0xff0000)   >> 16)
            arr2.append((arr[i] & 0xff00)     >> 8)
            arr2.append((arr[i] & 0xff))
        return arr2
    '''
    def ConfigUSART(self, type:CONFIG, speed:uint32=None, clkOutput:Clockoutput=None, clkLastBit:LastClockpulse=None, \
                    clkPhase:Clockphase=None, clkPolarity:Clockpolarity=None, overSampling:Oversampling=None, \
                    hardwareControl:HardwareControl=None, trDir:TranferDirection=None, enable:bool=True, \
                    endianness:Endianness=None,sync:Sync=None, stopBits:StopBit=None, \
                    parityBit:ParityBit=None, dataLenght:DataLength=None):
                    if(type != None):
                        if ( type != CONFIG.CONFIG_USART1 and
                            type != CONFIG.CONFIG_USART2 and
                            type != CONFIG.CONFIG_USART3 and 
                            type != CONFIG.CONFIG_USART4
                        ):
                                ret = TestStandResult.NOT_ALLOWED
                                print("config value is not allowed")
                                return ret
                        else:
                            type:CONFIG = CONFIG(type)
                    #number = type.value-1
                    if(speed != None):
                        if(speed <= 0 or speed > 0xffffffff):
                            ret = TestStandResult.NOT_ALLOWED
                            print("speed cant be lower than 0 or higher than 0xffff_ffff")
                            return ret
                    #set values
                        else:
                            self.usart[type.value-1].SetDataList(speed,0)
                    if(enable != None):
                        if(enable < 0 or enable > 1):
                            ret = TestStandResult.NOT_ALLOWED
                            print(ret, "enable cant be anything else than 0 or 1")
                            return ret
                        else:
                            self.usart[type.value-1].SetDataList(enable, 8)  

                    if(clkOutput != None):
                        if not isinstance(clkOutput, Clockoutput):
                            print(TestStandResult.NOT_ALLOWED.name,"value for clkOutput")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(clkOutput,1)
                    if(clkLastBit != None):
                        if not isinstance(clkLastBit, LastClockpulse):
                            print(TestStandResult.NOT_ALLOWED.name,"value for clock last bit")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(clkLastBit,2)
                    if(clkPhase != None):
                        if not isinstance(clkPhase, Clockphase):
                            print(TestStandResult.NOT_ALLOWED.name,"value for clock phase")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(clkPhase,3)
                    if(clkPolarity != None):
                        if not isinstance(clkPolarity, Clockpolarity):
                            print(TestStandResult.NOT_ALLOWED.name,"value for clock polarity")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(clkPolarity,4)
                    if(overSampling != None):
                        if not isinstance(overSampling, Oversampling):
                            print(TestStandResult.NOT_ALLOWED.name,"value for overSampling")

                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(overSampling,5)
                    if(endianness != None):
                        if not isinstance(endianness, Endianness):
                            print(TestStandResult.NOT_ALLOWED.name,"value for endianness")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(endianness,6)
                    if(sync != None):
                        if not isinstance(sync, Sync):
                            print(TestStandResult.NOT_ALLOWED.name,"value for sync")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(sync,7)

                    if(trDir != None): 
                        if not isinstance(trDir, TranferDirection):
                            print(TestStandResult.NOT_ALLOWED.name,"value for transfer direction")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(trDir,9)               
                    if(hardwareControl != None):
                        #if(hardwareControl.value < 0 and hardwareControl.value > 3):
                        if not isinstance(hardwareControl, HardwareControl):
                            print(TestStandResult.NOT_ALLOWED.name,"value for hardware control")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(hardwareControl,10)                  
                    if(stopBits != None):
                        if not isinstance(stopBits, StopBit):
                            print(TestStandResult.NOT_ALLOWED.name,"value for stop bit")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(stopBits,11)
                    if(parityBit != None):
                        if not isinstance(parityBit, ParityBit):
                            print(TestStandResult.NOT_ALLOWED.name,"value for parity bit")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(parityBit,12)                 
                    if(dataLenght != None):
                        if not isinstance(dataLenght, DataLength):
                            print(TestStandResult.NOT_ALLOWED.name,"value for data length")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.usart[type.value-1].SetDataList(dataLenght,13)
                    
                    #make data ready to send
                    configList = self.usart[type.value-1].GetDataListAll()

                    arr = []
                    s = configList[0]
                    if(s == None):
                        s = 0
                    arr.append(type.value)
                    arr.append( (s & 0xff0000) >> 16)
                    arr.append( (s & 0xff00) >> 8)
                    arr.append(s & 0xff)
                    
                    arrData = 0
                    for i in range(1,9):
                        if isinstance(configList[i], Enum):
                            lData = configList[i].value
                        else:
                            if(configList[i] == None):
                                lData = 0
                            else: 
                                lData = configList[i]
                        arrData = arrData + ((lData & 0x1) << (7-(i-1)))
                    arr.append(arrData)

                    dum = [6, 4, 2, 0]
                    j =  0
                    arrData = 0
                    for i in range(9,13):
                        if isinstance(configList[i], Enum):
                            lData = configList[i].value
                        else:
                            if(configList[i] == None):
                                lData = 0
                            else:
                                lData = configList[i]
                        arrData = arrData + ((lData & 0x3 ) << dum[j])
                        j+=1

                    arr.append(arrData)
                    if(isinstance(configList[13], DataLength)):
                        arr.append(configList[13].value)
                    else:
                        arr.append(0)

                    ##add crc to data
                    a = bytearray(((arr[0] << 8) + arr[1]).to_bytes(2, 'big'))
                    b = bytearray(((arr[2] << 8) + arr[3]).to_bytes(2, 'big'))
                    c = bytearray(((arr[4] << 8) + arr[5]).to_bytes(2, 'big'))
                    d = bytearray((arr[6]).to_bytes(2, 'big'))

                    crcArr = []
                    crcArr.append( int.from_bytes(Encode(a), 'big'))
                    crcArr.append( int.from_bytes(Encode(b), 'big'))
                    crcArr.append( int.from_bytes(Encode(c), 'big'))
                    crcArr.append( int.from_bytes(Encode(d), 'big'))
                    
                    crcArrByte = []
                    for i in range (4):
                        crcArrByte.append((crcArr[i] & 0xff000000) >> 24)
                        crcArrByte.append((crcArr[i] & 0xff0000) >> 16)
                        crcArrByte.append((crcArr[i] & 0xff00) >> 8)
                        crcArrByte.append(crcArr[i] & 0xff)
                   
                    
                    retArr = self.usb_obj.SendDataToMcu(crcArrByte)
                    res:TestStandResult = retArr[0]
                    command = retArr[1]
                    commandName = HandleCommand(command)
                    if(res == TestStandResult.OK):
                        print(self.usart[type.value-1].ValueString())
                    print(res.name, "for", commandName.name)
                    return res
                            
    def ConfigSPI(self,  role:Role=None, direction:SPI_direction=None, dataLength:SPI_DataLength=None, clkPol:Clockpolarity=None,\
                clkPhase:Clockphase=None, nss:NSS=None, baudpre:Baud_prescaler=None, endianness:Endianness=None,
                ti_mode:TI_mode=None, enabled=None):
                #set values
                if(role != None):
                    if not isinstance(role, Role):
                        print(TestStandResult.NOT_ALLOWED.name,"value for role")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(role,0)
                
                if(direction != None):
                    if not isinstance(direction, SPI_direction):
                        print(TestStandResult.NOT_ALLOWED.name,"value for direction")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(direction,1)
               
                if(dataLength != None): 
                    if not isinstance(dataLength, SPI_DataLength):
                        print(TestStandResult.NOT_ALLOWED.name,"value for dataLength")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(dataLength,2)

                if(clkPol != None):
                    if not isinstance(clkPol, Clockpolarity):
                        print(TestStandResult.NOT_ALLOWED.name,"value for clock polarity")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(clkPol,3)
               
                if(clkPhase != None):
                    if not isinstance(clkPhase, Clockphase):
                        print(TestStandResult.NOT_ALLOWED.name,"value for clock phase")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(clkPhase,4)

                if(nss != None):
                    if not isinstance(nss, NSS):
                        print(TestStandResult.NOT_ALLOWED.name,"value for nss")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(nss,5)
                if(baudpre != None):
                    if not isinstance(baudpre, Baud_prescaler):
                        print(TestStandResult.NOT_ALLOWED.name,"value for baud prescaler")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(baudpre,6)
                
                if(endianness != None):
                    if not isinstance(endianness, Endianness):
                        print(TestStandResult.NOT_ALLOWED.name,"value for endianness")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(endianness,7)
                if(ti_mode != None):
                    if not isinstance(ti_mode, TI_mode):
                        print(TestStandResult.NOT_ALLOWED.name,"value for ti mode")
                        return TestStandResult.NOT_ALLOWED
                    else:
                        self.spi.SetDataList(ti_mode, 8)
                if(enabled != None):
                    if enabled < 0 or enabled > 1:
                        print(TestStandResult.NOT_ALLOWED.name,"value for enabled")
                        return TestStandResult.NOT_ALLOWED
                    self.spi.SetDataList(enabled, 9)

                #make data ready to send
                configList = self.spi.GetDataListAll()
                #print(configList)
                arr = []
                arr.append(CONFIG.CONFIG_SPI.value)
                #print(arr)
                arrData = 0
                maxBitVal = [0x01,0x03,0x01,0x01,0x01,0x03]
                bitShift =  [0x07,0x05,0x04,0x03,0x02,0x00]
                lData = 0
                j=0
                for i in range(len(maxBitVal)):
                    if isinstance(configList[j], Enum):
                        lData = configList[j].value
                    else:
                        if(configList[i] == None):
                            lData = 0
                        else:
                            lData = configList[j]
                    arrData = arrData + ((lData & maxBitVal[i]) << (bitShift[i]))
                    j+=1
                arr.append(arrData)

                arrData = 0
                maxBitVal = [0x07,0x01,0x01,0x01]
                bitShift =  [0x03,0x02,0x01,0x00]
                for i in range(len(maxBitVal)):
                    if isinstance(configList[j], Enum):
                        lData = configList[j].value
                    else:
                        if(configList[i] == None):
                            lData = 0
                        else:
                            lData = configList[j]
                    arrData = arrData + ((lData & maxBitVal[i] ) << bitShift[i])
                    j+=1
                print("{0:b}".format(arrData))
                
                arr.append(arrData)

                ##add crc to data
                a = bytearray(((arr[0] << 8) + arr[1]).to_bytes(2, 'big'))
                b = bytearray((arr[2]).to_bytes(2, 'big'))
            
                crcArr = []
                crcArr.append( int.from_bytes(Encode(a), 'big'))
                crcArr.append( int.from_bytes(Encode(b), 'big'))
                
                crcArrByte = []
                for i in range (len(crcArr)):
                    crcArrByte.append((crcArr[i] & 0xff000000) >> 24)
                    crcArrByte.append((crcArr[i] & 0xff0000) >> 16)
                    crcArrByte.append((crcArr[i] & 0xff00) >> 8)
                    crcArrByte.append(crcArr[i] & 0xff)

                retArr = self.usb_obj.SendDataToMcu(crcArrByte)
                res:TestStandResult = retArr[0]
                command = retArr[1]
                commandName = HandleCommand(command)
                if(res == TestStandResult.OK):
                    print(self.spi.ValueString())
                print(res.name, "for", commandName.name)
                return res
    def ConfigI2C(self, speed=None,own_addr=None, own_addr2=None, dutyCycle:Dutycycle=None, role:Role=None, \
                    addressing:I2C_addressing=None, dual:I2C_dualaddressing=None, \
                    generalcall:I2C_generalcall=None, no_stretch:I2C_nostretch=None, \
                    enabled=None):

                    if(speed != None):
                        if(speed <= 0 or speed > 0xffff_ffff):
                            print(TestStandResult.NOT_ALLOWED.name,"value for speed")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(speed, 0)
                    
                    if own_addr != None:
                        if(own_addr < 0 or own_addr > 0xffff_ffff):
                            print(TestStandResult.NOT_ALLOWED.name,"value for own addr")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(own_addr, 1)
                    
                    if own_addr2 != None:
                        if(own_addr2 < 0 or own_addr2 > 0xffff_ffff):
                            print(TestStandResult.NOT_ALLOWED.name,"value for own addr 2")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(own_addr2, 2)

                    if dutyCycle != None:
                        if(dutyCycle != Dutycycle.Duty_16_9 and dutyCycle != Dutycycle.Duty_2):
                            print(TestStandResult.NOT_ALLOWED.name,"value for duty cycle", dutyCycle)
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(dutyCycle,3)
                    
                    if role != None:
                        if(role != Role.Role_Master and role != Role.Role_Slave):
                            print(TestStandResult.NOT_ALLOWED.name,"value for role")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(role, 4)
                        
                    if addressing != None:
                        if(addressing != I2C_addressing.addr_10 and addressing != I2C_addressing.addr_7):
                            print(TestStandResult.NOT_ALLOWED.name,"value for addressing")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(addressing, 5)

                    if dual != None:
                        if(dual != I2C_dualaddressing.Dual_On and dual != I2C_dualaddressing.Dual_Off):
                            print(TestStandResult.NOT_ALLOWED.name,"value for dual addressing")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(dual, 6)
                    
                    if generalcall != None:
                        if(generalcall != I2C_generalcall.Gen_Off and generalcall != I2C_generalcall.Gen_On):
                            print(TestStandResult.NOT_ALLOWED.name,"value for generalcall")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(generalcall, 7)
                    
                    if no_stretch != None:
                        if(no_stretch != I2C_nostretch.NoStretch_Off and no_stretch != I2C_nostretch.NoStretch_On):
                            print(TestStandResult.NOT_ALLOWED.name,"value for no stretch")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(no_stretch, 8)
                    
                    if enabled != None: 
                        if enabled < 0 or enabled > 1:
                            print(TestStandResult.NOT_ALLOWED.name,"value for enabled")
                            return TestStandResult.NOT_ALLOWED
                        else:
                            self.i2c.SetDataList(enabled,9)
                    
                          #make data ready to send
                    configList = self.i2c.GetDataListAll()
                    #print(configList)
                    arr = []

                    j=0
                    arr.append(CONFIG.CONFIG_I2C.value)
                    for i in range (0,3):
                        s = configList[j]
                        if(s == None):
                            s =0
                        arr.append( (s & 0xff000000) >> 24)
                        arr.append( (s & 0xff0000) >> 16)
                        arr.append( (s & 0xff00) >> 8)
                        arr.append(s & 0xff)
                        j+=1

                    arrData = 0
                    for i in range(0,7):
                        if isinstance(configList[j], Enum):
                            lData = configList[j].value
                        else:
                            if configList[j] == None:
                                lData = 0
                            else:
                                lData = configList[j]
                        arrData = arrData + ((lData & 0x01) << (6-i))
                        j+=1
                    arr.append(arrData)

                    ##add crc to data
                    crcArr = []
                    for i in range(0, len(arr), 2):
                        a =bytearray(((arr[i] << 8) + arr[i+1]).to_bytes(2, 'big'))
                        crcArr.append(int.from_bytes(Encode(a), 'big'))
                   
                    
                    crcArrByte = []
                    for i in range( len(crcArr)):
                        crcArrByte.append((crcArr[i] & 0xff000000) >> 24)
                        crcArrByte.append((crcArr[i] & 0xff0000) >> 16)
                        crcArrByte.append((crcArr[i] & 0xff00) >> 8)
                        crcArrByte.append(crcArr[i] & 0xff)
            
                    retArr = self.usb_obj.SendDataToMcu(crcArrByte)
                    res:TestStandResult = retArr[0]
                    command = retArr[1]
                    commandName = HandleCommand(command)
                    if(res == TestStandResult.OK):
                        print(self.i2c.ValueString())
                    print(res.name, "for", commandName.name)
                    return res

    #input array of bytes or 1 int value
    def SendDataOverProtocol(self, type:SEND, data):
        a = bytearray((type.value << 8 ).to_bytes(2, 'big'))
        arr = Encode(a)
        temp = None
        if not (isinstance(data, bytearray)):
            try:
                l = len(data)
                for i in range(0, l):
                    if data[i].bit_length() > 8:
                        ret = TestStandResult.NOT_ALLOWED
                        print(ret.name)
                        return ret
                    if i == 0:
                        temp = (data[i]).to_bytes(1, 'big')
                    else:
                        temp += (data[i]).to_bytes(1, 'big')

            except:
                temp = self.__ConvertToByteArray(data)
        else:
            temp = data
        length = len(temp)
        if length % 2 != 0:
            length +=1
            dum = 0
            temp += dum.to_bytes(1, 'big')
        #encode data
        for i in range(0,length, 2):
            arr += Encode(bytearray((temp[i], temp[i+1])))
        retArr = self.usb_obj.SendDataToMcu(arr)
        res:TestStandResult = retArr[0]
        command = retArr[1]
        commandName = HandleCommand(command)
        print(commandName.name, res.name)
        return res
    
    def __ConvertToByteArray(self, data):
        if isinstance(data, str):
            return str.encode(data)
        elif isinstance(data, int):
            return [ data & 0xff000000 >> 24, data & 0xff0000 >> 16, data & 0xff00 >> 8, data & 0xff]
    
    def ReceiveDataOverProtocol(self, type:RECEIVE):
        a = bytearray((type.value <<8 ).to_bytes(2, 'big'))
        a = Encode(a)
        retArr = self.usb_obj.SendDataToMcu(a)
        res:TestStandResult = retArr[0]
        command = retArr[1]
        commandName = HandleCommand(command)
        print(commandName.name, res.name)
        return res
