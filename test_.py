from crc import *
from UserInterface import UserInterface
from Protocol import *
from utils import *
import unittest
from cli import *

class TestCRC(unittest.TestCase):
    #test input cli.py 
    
    #only hex values and int value for 
    def test_Setup_Cli(self):
        strOld = str_n = "0x"
        for i in range(0,1):
            str_n = strOld + str(i)
            self.assertEqual(TestStandResult.OK, Setup(str(str_n), str(str_n), str(str_n)))
    
    #only int values
    def test_Setup_Cli2(self):
        self.assertEqual(TestStandResult.OK, Setup(1,1,1))
    
    #not allowed value 
    def test_Setup_Cli3(self):
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("0xh", str(1)))
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("0x", "0xggg", str(1)))
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("x 0", "-1", str(1)))
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("x 0", "-1", "A"))
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("0x0", "-1", "A"))
        self.assertEqual(TestStandResult.NOT_ALLOWED, Setup("0x0", "0x1", "A"))
        
    
    #right stuff
    def test_Config_Cli(self):
        self.assertEqual(TestStandResult.OK, Setup(0x0483, 0x5740))
        self.assertEqual(TestStandResult.OK, CONFIG_USART(1, 0x10, 1, 1, 1, 1, 1))
        self.assertEqual(TestStandResult.OK, CONFIG_SPI(1,1,1))
        self.assertEqual(TestStandResult.OK, CONFIG_I2C(9999, 0x1000, 1))

        #self.assertEqual(TestStandResult.OK, RECEIVE_USART(1))
        
        #self.assertEqual(TestStandResult.OK, SEND_USART("1", "1"))
        #self.assertEqual(TestStandResult.OK, SEND_USART("1", "hihi"))
        #self.assertEqual(TestStandResult.OK, SEND_USART("1", "4874124"))
    
    #wrong stuff
    def test_Config__Cli2(self):
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_USART(5, 1000, 1, 1, 1, 1, 1))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_USART(1, 1000, 1, 2, 1, 1, 1))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_USART(1, 1000, 1, 1, "a", 1, 1))
        
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_SPI("a", 1, 1, 1, 0))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_SPI(1, 5, 1, 1, 0))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_SPI(1000, 0x1, "g", 1, 0))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_SPI(404049, 1, "g", 1, "b"))

        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_I2C(-1, "0x", 0))
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_I2C(100000, -1, 0))   
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_I2C(100000, -1, 2))    
        self.assertEqual(TestStandResult.NOT_ALLOWED, CONFIG_I2C(100000, -1, "B"))    
    
    
    
    #works also with data corruption on mcu side
    #SendDataOVerProtocol & ReceiveDataOverProtocol!!
    def test_SendDataProtocolDataTypeAndLengthVar(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        arr = 0xff
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.OK, res)

        arr = 0xffffff
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.OK, res)

        arr = 0xffffffff
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.OK, res)

        arr = [0xff]
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.OK, res)

        arr = [0xfffff, 0xf1]
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.NOT_ALLOWED, res)
        
        arr = "hello"
        res = ui.SendDataOverProtocol(SEND.SEND_USART1, arr)
        self.assertEqual(TestStandResult.OK, res)
    
    def test_SendDataProtocol1(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,0xA,0xB]
        self.assertEqual(TestStandResult.OK, ui.SendDataOverProtocol(SEND.SEND_USART1, data))
       
    def test_SendDataProtocol2(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        data = "hello world"
        self.assertEqual(TestStandResult.OK, ui.SendDataOverProtocol(SEND.SEND_USART1, data))
    
    def test_SendDataProtocol3(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        data = [0x01, 0x01, 0x03, 0X04]
        self.assertEqual(TestStandResult.OK, ui.SendDataOverProtocol(SEND.SEND_USART1, data))
    
    def test_SendDataProtocol4(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        data = 0xffff
        data = bytearray((data.to_bytes(2, 'big')))
        self.assertEqual(TestStandResult.OK, ui.SendDataOverProtocol(SEND.SEND_USART1, data))
    
    #receive data
    #def test_ReceiveDataProtocol(self):
    #    vid = 0x0483
    #    pid = 0x5740
    #    ui = UserInterface(vid, pid)
    #    self.assertEqual(TestStandResult.OK, ui.ReceiveDataOverProtocol(RECEIVE.RECEIVE_USART1))
    
    
    #sending of config  
    def test_ConfigUsartSend(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)

        #not allowed values
        self.assertEqual(ui.ConfigUSART(type=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_SPI), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, speed=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, speed=0xffffffffff), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,clkOutput=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,clkLastBit=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,clkPhase=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,clkPolarity=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,overSampling=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,hardwareControl=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,trDir=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,endianness=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,sync=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,stopBits=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,parityBit=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1,dataLenght=-10), TestStandResult.NOT_ALLOWED)
        #allowed values
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, speed=10), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, clkOutput=Clockoutput.Clkout_Disable), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, clkLastBit=LastClockpulse.Lastpulse_No_Output), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, clkPhase=Clockphase.Clkphase_One), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, clkPolarity=Clockpolarity.Clkpol_High), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, overSampling=Oversampling.Over_16), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, hardwareControl=HardwareControl.HWC_CTS), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, trDir=TranferDirection.Trans_None), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, endianness=Endianness.LSB), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, sync=Sync.Asynchronous), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, stopBits=StopBit.Stop_Half), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, parityBit=ParityBit.Par_Even), TestStandResult.OK)
        self.assertEqual(ui.ConfigUSART(type=CONFIG.CONFIG_USART1, dataLenght=DataLength.EIGHT), TestStandResult.OK)

    def test_ConfigI2C(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        #not allowed values
        self.assertEqual(ui.ConfigI2C(speed=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(own_addr=0xffffffffff), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(own_addr2=-10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(dutyCycle=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(role=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(addressing=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(dual=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(generalcall=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(no_stretch=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigI2C(enabled=10), TestStandResult.NOT_ALLOWED)

        self.assertEqual(ui.ConfigI2C(speed=10), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(own_addr=0xfffffff), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(own_addr2=0x100), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(dutyCycle=Dutycycle.Duty_16_9), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(role=Role.Role_Master), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(addressing=I2C_addressing.addr_10), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(dual=I2C_dualaddressing.Dual_Off), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(generalcall=I2C_generalcall.Gen_On), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(no_stretch=I2C_nostretch.NoStretch_Off), TestStandResult.OK)
        self.assertEqual(ui.ConfigI2C(enabled=1), TestStandResult.OK)

    def testConfigSPI(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        self.assertEqual(ui.ConfigSPI(role=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(direction=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(dataLength=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(clkPol=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(clkPhase=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(nss=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(baudpre=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(endianness=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(ti_mode=10), TestStandResult.NOT_ALLOWED)
        self.assertEqual(ui.ConfigSPI(enabled=10), TestStandResult.NOT_ALLOWED)
        
        self.assertEqual(ui.ConfigSPI(role=Role.Role_Master), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(direction=SPI_direction.Dir_One_Line), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(dataLength=SPI_DataLength.SPI_Len_Eight), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(clkPol=Clockpolarity.Clkpol_High), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(clkPhase=Clockphase.Clkphase_One), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(nss=NSS.NSS_HardInput), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(baudpre=Baud_prescaler.Pre_128), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(endianness=Endianness.LSB), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(ti_mode=TI_mode.TI_Off), TestStandResult.OK)
        self.assertEqual(ui.ConfigSPI(enabled=1), TestStandResult.OK)
        
    #protocol.py
    #config test right values
    def testValue(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        self.assertEqual(ui.i2c.GetAmountElements(), 10)
        self.assertEqual(ui.usart[0].GetAmountElements(),14)
        self.assertEqual(ui.usart[1].GetAmountElements(),14)
        self.assertEqual(ui.usart[2].GetAmountElements(),14)
        self.assertEqual(ui.usart[3].GetAmountElements(),14)
        self.assertEqual(ui.spi.GetAmountElements(), 10)
    
    #spi
    def testProtocolSPI(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        #SetDataList
        for i in range(0, ui.spi.GetAmountElements()):
            ui.spi.SetDataList(i,i)
        #GetDataList
        for i in range(0, ui.spi.GetAmountElements()):
            self.assertEqual(i, ui.spi.GetDataListItem(i))
        #SetValue
        val = 1000
        ui.spi.SetValue(val)
        #GetValue
        self.assertEqual(val, ui.spi.GetValue())

        self.assertEqual(ui.spi.GetStringList(),["role: ", "direction: ", "dataLength: ", "clock polarity: ", "clock phase: ", "nss: ", "baud prescaler: ", \
                    "endianness: ", "ti_mode: ", "enabled: "])

    #i2c
    def testProtocolI2C(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        #SetDataList
        for i in range(0, ui.i2c.GetAmountElements()):
            ui.i2c.SetDataList(i,i)
        #GetDataList
        for i in range(0, ui.i2c.GetAmountElements()):
            self.assertEqual(i, ui.i2c.GetDataListItem(i))
        #SetValue
        val = 1000
        ui.i2c.SetValue(val)
        #GetValue
        self.assertEqual(val, ui.i2c.GetValue())

        self.assertEqual(ui.i2c.GetStringList(), ["speed: ", "address: ", "address 2: ", "dutycycle: ", "role: ", "addressing: ", "dual: ", "generalcall: ", \
                    "no_stretch: ", "enabeld: "])
    
    #usart
    def testProtocolUSART(self):
        vid = 0x0483
        pid = 0x5740
        ui = UserInterface(vid, pid)
        #SetDataList
        for i in range(0, ui.usart[0].GetAmountElements()):
            ui.usart[0].SetDataList(i,i)
        #GetDataList
        for i in range(0, ui.usart[0].GetAmountElements()):
            self.assertEqual(i, ui.usart[0].GetDataListItem(i))
        #SetValue
        val = 1000
        ui.usart[0].SetValue(val)
        #GetValue
        self.assertEqual(val, ui.usart[0].GetValue())

        self.assertEqual(ui.usart[0].GetStringList(),["speed: ", "clock output: ","clock last bit: ", "clock phase: ", "clock polarity: ", \
                     "oversampling: ", "endianness: ", "sync: ", "enabled: ", \
                    "transfer direction: ", "hardware_control: ", "stop bit: ", "parity bit: ","data lenght: "] )
#usb.py   
    #wrong usb values
    def testUSBInit(self):
        vid = 0x0000
        pid = 0x0000
        self.assertRaises(Exception, UserInterface,vid, pid)
    
#works
#CRC
      
    def test_encodeData(self):
        for i in range (0,0xff):
            for j in range(0,0xff):
                sendData = Encode(bytearray((i,j)))
                
                retData  = Decode(sendData)
                self.assertEqual(sendData, retData[0], "data has changed")
    
    def test_encodeDataAndCorrupt(self):
        for i in range (0,0xff):
            for j in range(0,0xff):
                sendData = Encode(bytearray((i,j)))
                sendData[0] ^= 1<<1
                retData  = Decode(sendData)
                self.assertEqual(False, retData[0], "data has not changed, but was expected")
    
    def test_singleBitError(self):
        for i in range (0,1):
            for j in range(0,1):
                sendData = Encode(bytearray((i,j)))

                sendDataInt = int.from_bytes(sendData, 'big')

                for k in range (0, 16):
                    val = (sendDataInt ^ (1 <<16+k))
                    bytesData = val.to_bytes(4, 'big')


                    retData = Decode(bytesData)
                    if(retData[0] == False):
                        data = CorrectData(retData[1], retData[2], retData[3])
                        self.assertEqual(sendData, data, "data has changed")
            
    def test_multiBitError(self):
        for i in range (0,1):
            for j in range(0,1):
                sendData = Encode(bytearray((i,j)))
                sendDataInt = int.from_bytes(sendData, 'big')

                for k in range (0, 16):
                    for l in range (1 ,16):
                        if k != l:
                            val = ((sendDataInt ^  (1 <<16+k)) ^  (1<<16+l))
                            bytesData = val.to_bytes(4, 'big')

                            retData = Decode(bytesData)
                            if(retData[0] == False):
                                data = CorrectData(retData[1], retData[2], retData[3])
                                self.assertEqual(sendData, data, "data has changed")
                           
    def test_TrippleBitError(self):
        sendData = Encode(bytearray((0xff,0xff)))
        sendDataInt = int.from_bytes(sendData, 'big')
        val = (sendDataInt ^ (1 <<16))
        val = val ^ (1 << 17)
        val = val ^ (1 << 18)
        bytesData = val.to_bytes(4, 'big')
        retData = Decode(bytesData)
        if(retData[0] == False):
            data = CorrectData(retData[1], retData[2], retData[3])
            self.assertEqual(False, data, "data has changed")
        self.assertEqual(False, data, "data has changed")
    
    #test error in crc checksum
    def test_crc_checksumError(self):
        sendData = Encode(bytearray((0xff, 0xff)))
        sendDataInt = int.from_bytes(sendData, 'big')
        val = (sendDataInt ^ 1)
        bytesData = val.to_bytes(4, 'big')
        retData = Decode(bytesData)

        if(retData[0] == False):
            data = CorrectData(retData[1], retData[2], retData[3])
           
            self.assertEqual(False, data, "data has changed")
    
    def test_crc_wrongDataSize(self):
        sendData = Encode(bytearray((0xff, 0xff, 0xff)))
        self.assertEqual(-1, sendData)
        
        sendData = Encode(bytearray((0xff, 0xff)))
        self.assertNotEqual(-1, sendData)
        
        sendData += 0xff.to_bytes(1, 'big')
        self.assertEqual(-1, Decode(sendData))
