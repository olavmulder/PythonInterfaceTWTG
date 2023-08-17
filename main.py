from UserInterface import UserInterface
from utils import *
from test_ import *
def main():
    vid = 0x0483
    pid = 0x5740
    ui = UserInterface(vid, pid)
    '''print("return: ", ui.ConfigProtocol(CONFIG.CONFIG_USART1, 9600, dataLength=DataLength.NINE, parityBit=False,\
            stopBit= True, endianness = Endianness.LSB, sync = Sync.Synchronous))
    
    print("return: ", ui.SendDataOverProtocol(SEND.SEND_USART1, [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09]))

    print("return: ", ui.ReceiveDataOverProtocol(RECEIVE.RECEIVE_USART1))
    '''

    ui.ConfigUSART(CONFIG.CONFIG_USART1, 10, clkOutput=Clockoutput.Clkout_Enable, clkLastBit=LastClockpulse.Lastpulse_Output,
        clkPhase=Clockphase.Clkphase_One, clkPolarity=Clockpolarity.Clkpol_High, overSampling=Oversampling.Over_16, hardwareControl=HardwareControl.HWC_RTS, \
        trDir=TranferDirection.Trans_RX, endianness=Endianness.LSB, sync=Sync.Asynchronous, \
            stopBits=StopBit.Stop_Half, parityBit=ParityBit.Par_Odd, dataLenght=DataLength.NINE)
    
    ui.ConfigUSART(CONFIG.CONFIG_USART2, 100, clkOutput=Clockoutput.Clkout_Disable, clkLastBit=LastClockpulse.Lastpulse_Output,
        clkPhase=Clockphase.Clkphase_One, clkPolarity=Clockpolarity.Clkpol_High, overSampling=Oversampling.Over_8, hardwareControl=HardwareControl.HWC_RTS, \
        trDir=TranferDirection.Trans_RX, endianness=Endianness.LSB, sync=Sync.Synchronous, \
            stopBits=StopBit.Stop_Half, parityBit=ParityBit.Par_Odd, dataLenght=DataLength.NINE)
    
    ui.ConfigUSART(CONFIG.CONFIG_USART3, 1000, clkOutput=Clockoutput.Clkout_Disable, clkLastBit=LastClockpulse.Lastpulse_No_Output,
        clkPhase=Clockphase.Clkphase_One, clkPolarity=Clockpolarity.Clkpol_High, overSampling=Oversampling.Over_8, hardwareControl=HardwareControl.HWC_NONE, \
        trDir=TranferDirection.Trans_RX, endianness=Endianness.LSB, sync=Sync.Synchronous, \
            stopBits=StopBit.Stop_Half, parityBit=ParityBit.Par_Even, dataLenght=DataLength.NINE)
    
    ui.ConfigUSART(CONFIG.CONFIG_USART4, 10000, clkOutput=Clockoutput.Clkout_Disable, clkLastBit=LastClockpulse.Lastpulse_No_Output,
        clkPhase=Clockphase.Clkphase_One, clkPolarity=Clockpolarity.Clkpol_High, overSampling=Oversampling.Over_8, hardwareControl=HardwareControl.HWC_NONE, \
        trDir=TranferDirection.Trans_None, endianness=Endianness.MSB, sync=Sync.Synchronous, \
            stopBits=StopBit.Stop_Half, parityBit=ParityBit.Par_Even, dataLenght=DataLength.NINE)
    
    '''print("res: ", ui.ConfigSPI(role=Role.Role_Master, direction=SPI_direction.Dir_Two_Line, dataLength=SPI_DataLength.SPI_Len_Sixteen, clkPol=Clockpolarity.Clkpol_High, \
        clkPhase=Clockphase.Clkphase_One, nss=NSS.NSS_HardInput, baudpre=Baud_prescaler.Pre_128, endianness=Endianness.LSB, ti_mode=TI_mode.TI_Off, enabled=1))
    
    print("res: ", ui.ConfigI2C(speed=115200, own_addr=10, own_addr2=1000, dutyCycle=Dutycycle.Duty_16_9, role=Role.Role_Master,addressing=I2C_addressing.addr_10, dual=I2C_dualaddressing.Dual_Off,\
        generalcall=I2C_generalcall.Gen_Off, no_stretch=I2C_nostretch.NoStretch_On, enabled=0 ))
    '''
    return 0


if __name__ == "__main__":
    unittest.main() 
    #main()